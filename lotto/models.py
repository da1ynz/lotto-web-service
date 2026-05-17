from django.db import models


class Draw(models.Model):
    round_number = models.IntegerField(unique=True)
    winning_numbers = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.round_number}회차 당첨번호: {self.winning_numbers}"


class Ticket(models.Model):
    MODE_CHOICES = [
        ('AUTO', '자동'),
        ('MANUAL', '수동'),
    ]

    name = models.CharField(max_length=50)
    numbers = models.CharField(max_length=50)
    mode = models.CharField(max_length=10, choices=MODE_CHOICES)
    round_number = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.numbers}"