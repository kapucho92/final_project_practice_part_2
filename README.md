# Автоматизация теста к API
- Тест проверяет, как система отрабатывает следующий сценарий:
1. Осуществляется запрос на создание заказа.
2. Номер трека заказа сохраняется в переменную.
3. Осуществляется запрос на получения заказа по треку заказа.
4. Проверяется, что код ответа равен 200.
- Для запуска тестов должны быть установлены пакеты pytest и requests
- Запуск всех тестов выполняется командой pytest