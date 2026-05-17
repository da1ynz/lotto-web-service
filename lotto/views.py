import random
from django.shortcuts import render, redirect
from .models import Ticket
from .models import Draw
from django.contrib.admin.views.decorators import staff_member_required


def buy_ticket(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        mode = request.POST.get('mode')
        round_number = 1

        if mode == 'AUTO':
            numbers = random.sample(range(1, 46), 6)
            numbers.sort()
        else:
            numbers = [
                int(request.POST.get('num1')),
                int(request.POST.get('num2')),
                int(request.POST.get('num3')),
                int(request.POST.get('num4')),
                int(request.POST.get('num5')),
                int(request.POST.get('num6')),
            ]
            numbers.sort()

        number_text = ','.join(map(str, numbers))

        Ticket.objects.create(
            name=name,
            numbers=number_text,
            mode=mode,
            round_number=round_number
        )

        return redirect('ticket_list')

    return render(request, 'lotto/buy.html')


def ticket_list(request):
    tickets = Ticket.objects.all().order_by('-created_at')
    return render(request, 'lotto/ticket_list.html', {'tickets': tickets})

def check_result(request):
    results = []

    if request.method == 'POST':
        name = request.POST.get('name')
        tickets = Ticket.objects.filter(name=name).order_by('-created_at')

        for ticket in tickets:
            try:
                draw = Draw.objects.get(round_number=ticket.round_number)

                ticket_numbers = set(map(int, ticket.numbers.split(',')))
                winning_numbers = set(map(int, draw.winning_numbers.split(',')))

                match_count = len(ticket_numbers & winning_numbers)

                if match_count == 6:
                    rank = '1등'
                elif match_count == 5:
                    rank = '2등'
                elif match_count == 4:
                    rank = '3등'
                elif match_count == 3:
                    rank = '4등'
                else:
                    rank = '낙첨'

                results.append({
                    'ticket': ticket,
                    'winning_numbers': draw.winning_numbers,
                    'match_count': match_count,
                    'rank': rank,
                })

            except Draw.DoesNotExist:
                results.append({
                    'ticket': ticket,
                    'winning_numbers': '아직 추첨 전',
                    'match_count': '-',
                    'rank': '추첨 전',
                })

    return render(request, 'lotto/check_result.html', {'results': results})

@staff_member_required
def admin_draw(request):
    message = None
    draw = None

    if request.method == 'POST':
        last_draw = Draw.objects.order_by('-round_number').first()

        if last_draw:
            next_round = last_draw.round_number + 1
        else:
            next_round = 1

        numbers = random.sample(range(1, 46), 6)
        numbers.sort()
        number_text = ','.join(map(str, numbers))

        draw = Draw.objects.create(
            round_number=next_round,
            winning_numbers=number_text
        )

        message = f'{next_round}회차 추첨이 완료되었습니다.'

    return render(request, 'lotto/admin_draw.html', {
        'message': message,
        'draw': draw,
    })

@staff_member_required
def admin_results(request):
    tickets = Ticket.objects.all().order_by('-created_at')
    results = []

    for ticket in tickets:
        try:
            draw = Draw.objects.get(round_number=ticket.round_number)

            ticket_numbers = set(map(int, ticket.numbers.split(',')))
            winning_numbers = set(map(int, draw.winning_numbers.split(',')))

            match_count = len(ticket_numbers & winning_numbers)

            if match_count == 6:
                rank = '1등'
            elif match_count == 5:
                rank = '2등'
            elif match_count == 4:
                rank = '3등'
            elif match_count == 3:
                rank = '4등'
            else:
                rank = '낙첨'

            results.append({
                'ticket': ticket,
                'winning_numbers': draw.winning_numbers,
                'match_count': match_count,
                'rank': rank,
            })

        except Draw.DoesNotExist:
            results.append({
                'ticket': ticket,
                'winning_numbers': '아직 추첨 전',
                'match_count': '-',
                'rank': '추첨 전',
            })

    return render(request, 'lotto/admin_results.html', {'results': results})