<div align="left">
<img src="https://img.shields.io/github/languages/code-size/dvdkitay/goip-send-sms" />
<img src="https://img.shields.io/github/languages/top/dvdkitay/goip-send-sms" />
<div>


## Описание программы

Скрипт для удобной массовой отправки смс через шлюз GOIP

## Настройка конфигурации

Замените параметры конфигцрации в файле `lib/config.py`

```
SERVER_GOIP = "127.0.0.1" # Это сервер на котором работает goip
USERNAME = "admin" # Это ваше имя для входа на SMS-сервер
PASSWORD = "admin" # Это Ваш пароль для входа в SMS-сервер
```

## Запуск программы

```
python3 app.py --provider <SMS_PROVIDER> --goip <GOIP_NAME> --file <FILE_TEL_NUMBER> --text <SMS_TEXT>
```

SMS_PROVIDER - Указывает, какой провайдер в списке поставщиков SMS-сервера будет использоваться для отправки SMS. Ссылочный номер используется для ссылки на поставщика. Пожалуйста, не используйте определенное имя поставщика. Пожалуйста, убедитесь, что указанный провайдер назначен канал (каналы) GoIP.

GOIP_NAME -  Это идентификатор GoIP, определенный для каждого канала GoIP. Если этот параметр не указан, SMS Server выберет GSM канал у провайдера, указанного для отправки SMS.

FILE_TEL_NUMBER - Файл с списокм телефонных номеров (Заполните файл, чтобы каждый номер был с новой строки)

SMS_TEXT - Смс текст, который необходимо отправить всем получателям

## Пример запуска 

```
python3 app.py --provider 1 --goip goip1 --file tel.txt --text Привет, это тест!
```