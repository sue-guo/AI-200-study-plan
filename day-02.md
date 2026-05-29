# Day 2: Python async, HTTP API, environment variables, and configuration

Date: 2026-05-29

## Today's Goal

After today, you should be able to:

- Explain why async code matters for AI and cloud apps
- Read and write simple `async` / `await` Python code
- Understand the shape of a small HTTP API
- Load local settings from environment variables or a `.env` file
- Keep secrets out of source code
- Prepare a clean configuration pattern for later Azure SDK, Azure OpenAI, Cosmos DB, Redis, and Service Bus work

## Why This Matters For AI-200

AI-200 is not only about calling a model. In real Azure AI applications, your code usually needs to:

- Receive HTTP requests from users or another service
- Call model endpoints, databases, queues, and storage over the network
- Use configuration values that differ between local, test, and production environments
- Avoid hard-coding secrets, keys, endpoints, or connection strings
- Handle slow external services without blocking the whole app

That is why today's basics are important before we move into Azure authentication and model calls.

## Official Learning Resources

- Python async and await: https://docs.python.org/3/library/asyncio-task.html
- FastAPI first steps: https://fastapi.tiangolo.com/tutorial/first-steps/
- FastAPI async docs: https://fastapi.tiangolo.com/async/
- Python environment variables: https://docs.python.org/3/library/os.html#os.environ
- python-dotenv: https://pypi.org/project/python-dotenv/
- Pydantic settings management: https://docs.pydantic.dev/latest/concepts/pydantic_settings/

## Hands-On Practice

### 1. Create today's folder

```powershell
mkdir ai200-day02
cd ai200-day02
python -m venv .venv # creates an isolated environment for this project
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
```

### 2. Install packages

```powershell
# uvicorn = Web Server
pip install fastapi uvicorn httpx python-dotenv pydantic-settings
pip freeze > requirements.txt # a list of all installed packages in the format package==version
```

### 3. Create a local `.env` file

Copy `.env.example` to `.env`:

```powershell
Copy-Item .env.example .env
```

Then edit `.env` if you want to change the values.

Important: `.env` is for local-only settings. Do not commit real secrets.

### 4. Run the async demo

```powershell
python async_demo.py
```

What to notice:

- The tasks start together.
- The total runtime is close to the longest individual wait, not the sum of all waits.
- This is useful when an app waits for model APIs, databases, queues, or storage.

### 5. Start the API

```powershell
uvicorn main:app --reload --port 8000
```

Open:

- http://127.0.0.1:8000/health
- http://127.0.0.1:8000/config
- http://127.0.0.1:8000/docs

### 6. Call the API with the HTTP client

Keep the API running in one terminal. Open another terminal:

```powershell
cd ai200-day02
.\.venv\Scripts\Activate.ps1
python http_client.py
```

## Key Concepts

### `async` / `await`

Use async code when your program spends time waiting for network, disk, database, model, or queue operations.

Common AI app examples:

- Wait for an Azure OpenAI response
- Read document chunks from a database
- Send an ingestion job to a queue
- Retrieve a secret from Key Vault
- Write telemetry to Application Insights

Do not expect async to make CPU-heavy work magically faster. It mainly helps with waiting.

### HTTP API

An HTTP API exposes operations through URLs and methods:

- `GET /health`: check whether the app is alive
- `GET /config`: inspect non-secret configuration
- `POST /chat`: later, send a prompt to a model
- `POST /documents`: later, upload or ingest a document

For AI-200, be ready to understand where an API runs: local machine, container, Azure Container Apps, AKS, or Azure Functions.

### Environment Variables

Environment variables let the same code run in different places:

- Local: `.env`
- Container: container environment variables
- Azure Container Apps: app settings / secrets
- Azure Functions: application settings
- Production Azure resources: often combined with managed identity and Key Vault

Exam trap: do not store production secrets directly in source code or Docker images.

### Configuration Management

Good config code should:

- Load settings from the environment
- Provide reasonable local defaults when safe
- Fail clearly when required settings are missing
- Separate secret and non-secret values
- Make it easy to move from local `.env` to Azure App Configuration or Key Vault later

## Today's Notes

- [ ] `async` / `await` helps Python handle network waiting efficiently.
- [ ] Async is useful for I/O-bound work, not mainly for CPU-bound work.
- [ ] HTTP APIs use routes such as `/health`, `/config`, and later `/chat`.
- [ ] `.env` is for local development; production should use platform-managed settings or secret stores.
- [ ] Secrets should not be committed to source control.
- [ ] Config values often differ between local, test, staging, and production.
- [ ] Azure Container Apps, Functions, and App Service all support environment/app settings.
- [ ] Later, Key Vault should hold secrets and App Configuration can hold centralized non-secret configuration.
- [ ] A health endpoint is useful for containers, load balancers, and monitoring.
- [ ] Pydantic settings gives a typed way to load and validate configuration.

## Completion Criteria

- [ ] `ai200-day02` folder created
- [ ] Virtual environment created
- [ ] Packages installed and `requirements.txt` generated
- [ ] `.env.example` reviewed and copied to `.env`
- [ ] `async_demo.py` runs successfully
- [ ] FastAPI app starts with `uvicorn`
- [ ] `/health`, `/config`, and `/docs` open successfully
- [ ] `http_client.py` can call the local API
- [ ] You can explain why secrets should not be hard-coded
- [ ] You can explain when async is useful in an Azure AI application

## Quick Review Questions

1. Why is async useful when calling a model endpoint?
```
Handle many API calls efficiently while waiting
```
2. What is the difference between a secret and normal configuration?
```
Normal configuration: Non-sensitive settings, can have
- app name
- log level
- feature flags
- API base URLs

Secret configuration: Sensitive data that must be protected, like 
- API keys
- password
- database credentials
```
3. Why should a containerized app read settings from environment variables?
```
In container systems, the same image is deployed to multiple environments, [Useful] no code changes needed if using environment variables, [Security] no secrets inside the image, [Easy deployment automation] CI/CD pipelines just inject environment variables.
```
4. Why should `.env` usually be excluded from source control?
```
Avoid data leaks
```
5. What would `/health` be used for in Azure Container Apps?
```
In cloud services like Azure Container Apps, /health is a health check endpoint. it tells cloud system app is alive
```

