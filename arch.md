project/
├── app/
│   ├── api/                # Маршруты API
│   │   ├── v1/
│   │   │   ├── endpoints/
│   │   │   │   ├── users.py
│   │   │   │   ├── documents.py
│   │   │   │   └── auth.py
│   │   │   └── __init__.py
│   │   └── __init__.py
│   ├── core/               # Основные настройки
│   │   ├── config.py       # Настройки приложения (ENV)
│   │   ├── security.py     # JWT/Tokens
│   │   └── tasks.py        # Фоновые задачи (Celery)
│   ├── db/                 # База данных
│   │   ├── models/         # Модели ORM
│   │   │   ├── user.py
│   │   │   └── document.py
│   │   ├── schemas/        # Pydantic-схемы
│   │   │   ├── user.py
│   │   │   └── document.py
│   │   ├── session.py      # Подключение к БД
│   │   └── init_db.py      # Первоначальная инициализация
│   ├── services/           # Логика приложения
│   │   ├── auth_service.py # Аутентификация
│   │   ├── user_service.py # Логика пользователей
│   │   └── document_service.py
│   ├── main.py             # Точка входа в приложение
├── docker-compose.yml      # Настройки Docker
├── Dockerfile              # Образ приложения
├── .env                    # Переменные окружения
└── README.md               # Документация
