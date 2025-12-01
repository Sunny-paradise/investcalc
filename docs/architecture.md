```mermaid
graph TD;
    A[Клиент / браузер] --> B[REST API InvertCalc]
    B --> C[Сервис расчетов]
    C --> D[Модуль генерации отчетов]
    C --> E[Хранилище данных ПК]
    B --> F[Контейнер Docker]
