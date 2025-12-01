```mermaid
graph TD;
    A[Клиент/Браузер/Postman] -->|REST API| B[API]
    B --> C[CalcController]
    C --> D[LocalCalcService]
    C --> E[CloudCalcService]
    C --> F[SensitivityService]
    C --> G[CompareService]
    D --> H[CalcResponse]
    E --> H
    F --> H
    G --> H
    H --> I[Models]
    I -->|Docker Container| J[Docker Container]
