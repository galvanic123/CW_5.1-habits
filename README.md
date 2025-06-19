# Данный проект является трекером полезных привычек
## Использование
В проекте доступно несколько вариантов использования. Инструкции к ним вы можете прочитать далее

## Использование с помощью docker-compose (локально)

### Клонируйте репозиторий
git clone https://github.com/galvanic123/CW_5.1-habits.git
 
Поскольку проект использует Docker, необходимо установить Docker
Откройте скопированный проект.
Переименуйте файл '.env.smple' в '.env' и внесите необходимые данные переменных окружения.
Запустите проект командой: docker-compose up -d --build
Для остановки всех контейнеров и их удаления используйте команду docker-compose down
## Использование на удалённом сервере с docker-compose
### Настройка сервера
Откройте терминал и выполните команду для обновления списка пакетов на сервере: sudo apt update
Затем выполните команду для обновления всех установленных пакетов до их последних версий: sudo apt upgrade
Установите Docker
Проверьте состояние файрвола с помощью команды: sudo ufw status и если фаервол отключен, активируйте его: sudo ufw enable
Откройте необходимые порты: sudo ufw allow 80/tcp sudo ufw allow 443/tcp sudo ufw allow 22/tcp
## Установка Git
Откройте терминал на сервере и выполните команду: sudo apt update sudo apt install git
Клонируйте репозиторий:
git clone https://github.com/galvanic123/CW_5.1-habits.git
 
## Запуск
Перейдите в директорию, где находится файл docker-compose.yml: cd /your/path/hht
Создайте файл .env и внесите необходимые переменные окружения на примере '.env.smple': nano .env
Запустите проект командой: docker-compose up -d
## Использование проекта с автоматическим деплоем
### Настройка сервера
Откройте терминал и выполните команду для обновления списка пакетов на сервере: sudo apt update
Затем выполните команду для обновления всех установленных пакетов до их последних версий: sudo apt upgrade
Установите Docker
Проверьте состояние файрвола с помощью команды: sudo ufw status и если фаервол отключен, активируйте его: sudo ufw enable
Откройте необходимые порты: sudo ufw allow 80/tcp sudo ufw allow 443/tcp sudo ufw allow 22/tcp
## Деплой
В проекте настроен файл GitHub Actions workflow(.github/workflows/ci.yaml). Благодаря этому при каждом push проекта запускается линтер flake8, запускаются тесты и проект деплоится на удалённый сервер после успешного прохождения тестов. Для корректной работы необходимо настроить секреты в вашем репозитории в GitHub.

Создайте секреты: CELERY_BROKER_URL, CELERY_BROKER_URL_FOR_TEST, CELERY_RESULT_BACKEND, CELERY_RESULT_BACKEND_FOR_TEST, DATABASE_HOST, DEPLOY_DIR, DOCKER_HUB_ACCESS_TOKEN, DOCKER_HUB_USERNAME, POSTGRES_DB, POSTGRES_PASSWORD, POSTGRES_USER, SECRET_KEY, SERVER_IP, SSH_KEY, SSH_USER, TG_TOKEN
В сервисах 'web', 'celery', 'celery-beat' в строке image укажите свой DOCKER_HUB_USERNAME