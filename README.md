# Телеграм бот для поиска видеоигр

1. lesson6/app - сервис с REST API
1. lesson6/bot - основной бот, принимает запросы на поиск и созраняет в postgres реакции пользователя на результат (нравится/не нравится)
1. lesson6/search - поиск игр по запросу в chromadb, запросы получает в очередь rabbitmq, ответ также через очередь передает на сортировку, масшатбирование через docker-compose
1. lesson6/sort - запросы получает в очередь rabbitmq, сортирует в соответствии с предпочтениями пользователя (user-based коллаборативеая фильтрация с домножением расстояния между эмбеддингами на константу при наличии игры в рекомендациях для пользователя), результат передаёт в очередь для отправки пользователю
1. lesson6/notifier - дополнительный бот, получает отсортированный результат поиска через очередь rabbitmq, добавляет к каждому ответу кнопки нравится/не нравится и отправляет пользователю по chatid