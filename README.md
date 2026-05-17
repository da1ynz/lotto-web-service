# 6/45 Lotto Web Service

Django와 Docker를 사용하여 구현한 6/45 로또 웹 서비스 프로젝트입니다.  
일반 사용자는 로또를 구매하고 당첨 결과를 확인할 수 있으며, 관리자는 판매 내역 확인 및 추첨 기능을 사용할 수 있습니다.

---

# 프로젝트 개요

본 프로젝트는 Django 웹 프레임워크와 PostgreSQL 데이터베이스를 기반으로 구현되었으며, Docker Compose를 사용하여 multi-container 환경으로 구성하였습니다.

사용자는 자동 또는 수동 방식으로 로또를 구매할 수 있으며, 추첨 결과와 비교하여 당첨 여부를 확인할 수 있습니다.  
관리자는 로또 추첨 기능과 전체 판매 및 당첨 내역 확인 기능을 사용할 수 있습니다.

---

# 주요 기능

## 일반 사용자 기능

### 1. 로또 구매 기능

- 자동 번호 구매
- 수동 번호 구매
- 구매 정보 DB 저장

### 2. 구매 내역 확인 기능

- 사용자가 구매한 복권 목록 확인 가능

### 3. 당첨 확인 기능

- 구매 번호와 당첨 번호 비교
- 맞은 개수 계산
- 등수 출력

---

## 관리자 기능

### 1. 판매 내역 확인

- 전체 구매 복권 목록 확인 가능

### 2. 로또 추첨 기능

- 1~45 사이 랜덤 번호 6개 생성
- 회차별 당첨 번호 저장

### 3. 당첨 내역 확인 기능

- 전체 사용자의 당첨 결과 확인 가능

### 4. Django Admin 기능

- Ticket 및 Draw 데이터 관리 가능

---

# 기술 스택

## Backend

- Python 3
- Django

## Database

- PostgreSQL

## Container

- Docker
- Docker Compose

---

# 프로젝트 구조

```text
lotto_project/
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── lotto/
│   ├── migrations/
│   ├── templates/
│   │   └── lotto/
│   │       ├── buy.html
│   │       ├── ticket_list.html
│   │       ├── check_result.html
│   │       ├── admin_draw.html
│   │       └── admin_results.html
│   ├── admin.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── manage.py
└── README.md