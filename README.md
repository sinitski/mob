# Webhook Sender - Flet Android App

Приложение для отправки данных на Telegram webhook с Android.

## Возможности

- 📝 Текстовое поле для ввода числа
- 💬 Опциональное поле для комментария
- 🚀 Отправка POST запроса на вебхук
- 📱 Поддержка lock screen widget (планируется)
- 🔄 Автоматическая сборка APK через GitHub Actions

## Локальная сборка

### Требования

- Python 3.8+
- Java JDK 11+
- Android SDK

### Установка зависимостей

```bash
pip install -r requirements.txt
pip install buildozer
pip install cython
```

### Запуск на компьютере

```bash
flet run main.py
```

### Сборка APK

```bash
# Сборка debug версии
buildozer android debug

# Результат будет в папке bin/
```

## Автоматическая сборка через GitHub Actions

1. Отправьте код в GitHub репозиторий
2. GitHub Actions автоматически создаст APK
3. Скачайте APK из artifacts в Actions tab

### Создание релиза

```bash
git tag v1.0.0
git push origin v1.0.0
```

APK будет автоматически загружена как Release asset.

## Структура проекта

```
.
├── main.py                    # Основное приложение
├── requirements.txt           # Python зависимости
├── README.md                 # Этот файл
├── android/                  # Android-специфичные файлы
└── .github/workflows/        # GitHub Actions workflows
    └── build-apk.yml        # Workflow для сборки APK
```

## API Payload

Приложение отправляет JSON в следующем формате:

```json
{
  "update_id": 1234567890,
  "message": {
    "message_id": 1,
    "from": {
      "id": 789161700,
      "is_bot": false,
      "first_name": "Eugene",
      "username": "eugn3"
    },
    "chat": {
      "id": 789161700,
      "type": "private"
    },
    "date": 1234567890,
    "text": "50 такси"
  }
}
```

## Lock Screen Widget

Для добавления lock screen widget на Android (Crouton 11.2):
- После установки приложения, длинное нажатие на lock screen
- Выбрать "Widgets"
- Найти "Webhook Sender"
- Добавить на экран

Код для поддержки widgets добавлен в приложение.

## Установка на Android

1. Включить "Unknown sources" в настройках
2. Скачать APK
3. Открыть файл и установить
4. Запустить приложение

## Troubleshooting

**Ошибка сборки APK:**
- Убедитесь, что установлен Android SDK
- Установите необходимые tools: `sdkmanager "build-tools;31.0.0" "platforms;android-31"`

**Приложение не отправляет:**
- Проверьте интернет соединение
- Проверьте URL вебхука в коде
- Проверьте логи в GitHub Actions

## Лицензия

MIT
