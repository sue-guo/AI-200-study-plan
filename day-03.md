# Day 3: Azure authentication, DefaultAzureCredential, Managed Identity, and Service Principal

Date: 2026-05-30

## Today's Goal

After today, you should be able to:

- Explain why Azure authentication is needed in AI-200 projects
- Describe what `DefaultAzureCredential` does
- Understand the difference between local development auth and cloud auth
- Know when to use Managed Identity
- Know when to use a Service Principal
- Connect Day 2 configuration habits with secure Azure access patterns

## Why This Matters For AI-200

Most AI-200 solutions do not stop at calling a model. They also need to:

- Read secrets or settings securely
- Access Azure OpenAI, Cosmos DB, Storage, Key Vault, or Service Bus
- Work both on a local machine and after deployment to Azure
- Avoid hard-coding passwords, keys, or connection strings

Authentication is the bridge between your code and Azure services. In the exam, questions often ask which identity method fits a given environment.

## Official Learning Resources

- Azure identity overview: https://learn.microsoft.com/en-us/azure/developer/python/sdk/authentication/overview
- DefaultAzureCredential: https://learn.microsoft.com/en-us/python/api/azure-identity/azure.identity.defaultazurecredential
- Azure managed identities overview: https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/overview
- Create a Microsoft Entra app and service principal: https://learn.microsoft.com/en-us/entra/identity-platform/howto-create-service-principal-portal
- Azure SDK authentication guidance: https://learn.microsoft.com/en-us/azure/developer/python/sdk/authentication/

## Hands-On Practice

### 1. Review how Day 2 configuration supports auth

Before adding Azure access, make sure you can explain:

- `endpoint` and `region` are normal configuration
- API keys and client secrets are sensitive
- local `.env` is for development only

That pattern will carry over into Azure SDK work.

### 2. Learn the credential chain

Study `DefaultAzureCredential` as the default way to authenticate Azure SDK clients in most Python apps.

What it tries depends on where the code runs, but the common idea is:

- local developer login
- environment-based credentials
- managed identity in Azure

This lets the same code work locally and in Azure with minimal change.

### 3. Create today's folder

```powershell
mkdir ai200-day03
cd ai200-day03
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
```

### 4. Install packages

```powershell
pip install azure-identity azure-keyvault-secrets python-dotenv
pip freeze > requirements.txt
```

### 5. Create `check_auth.py`

```python
from azure.identity import DefaultAzureCredential

credential = DefaultAzureCredential()
print(type(credential).__name__)
```

Run it:

```powershell
python check_auth.py
```

The point here is not to call Azure yet. It is to get comfortable with the credential object your later code will reuse.

### 6. Inspect environment-based auth

Read about these environment variables:

- `AZURE_CLIENT_ID`
- `AZURE_TENANT_ID`
- `AZURE_CLIENT_SECRET`

These are commonly used for service principal auth during development, CI/CD, or automation.

### 7. Compare with Managed Identity

Managed Identity is the best fit when code is already running in Azure and should access other Azure services without storing secrets.

Good fit examples:

- Azure Container Apps calling Key Vault
- Azure Functions reading from Cosmos DB
- App Service accessing Azure OpenAI

Exam clue: if the app is already in Azure and you do not want credentials in config, Managed Identity is usually the answer.

### 8. Compare with Service Principal

A Service Principal is an app identity in Microsoft Entra ID.

Use it when:

- local dev or automation needs Azure access
- you need non-interactive auth
- Managed Identity is not available

It usually involves a client ID, tenant ID, and client secret or certificate.

## Key Concepts

### `DefaultAzureCredential`

This is the Azure SDK credential most people start with.

It reduces branching in your code because one credential object can work across:

- local dev
- CI/CD
- deployed Azure resources

### Managed Identity

Managed Identity is a cloud-hosted identity assigned to an Azure resource.

Use it to avoid secret management when your app is running in Azure.

### Service Principal

A Service Principal is an application identity in Microsoft Entra ID.

Use it for automation or when you need a credentialed app identity outside the managed identity flow.

### Exam Pattern

Look for the environment first:

- local laptop -> likely developer login or service principal
- Azure-hosted app -> likely managed identity
- automated pipeline -> often service principal

## Today's Notes

- [ ] `DefaultAzureCredential` is the default Azure SDK auth choice for many Python apps.
- [ ] Managed Identity is best when code runs in Azure and should avoid secrets.
- [ ] Service Principal is useful for automation and non-interactive access.
- [ ] Environment variables can hold non-secret config or auth-related settings like client IDs.
- [ ] Local development auth and Azure-hosted auth are often different, but the app code can stay similar.
- [ ] The exam often tests which identity method matches the hosting environment.

## Completion Criteria

- [ ] You can explain what `DefaultAzureCredential` is for
- [ ] You can explain when to use Managed Identity
- [ ] You can explain when to use a Service Principal
- [ ] You created and ran `check_auth.py`
- [ ] You can connect Day 2 config patterns to Day 3 authentication patterns
- [ ] You can identify the likely auth choice from a simple AI-200 scenario

## Quick Review Questions

1. Why is `DefaultAzureCredential` useful?
```
It lets Azure SDK code use one credential type across local development and Azure hosting
```
2. When should you prefer Managed Identity?
```
When the app is already running in Azure and should avoid storing secrets
```
3. When is a Service Principal a good choice?
```
For automation, CI/CD, or non-interactive app authentication
```
4. What kind of information is `AZURE_CLIENT_SECRET`?
```
Sensitive credential data that should not be hard-coded or committed
```
5. In a deployment question, what clue points to Managed Identity?
```
The app is running in Azure and needs access to another Azure service without storing secrets
```
