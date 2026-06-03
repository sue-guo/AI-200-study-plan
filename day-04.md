# Day 4: Azure OpenAI / Microsoft Foundry basics, model deployment, chat completion, and embeddings

Date: 2026-05-31

## Today's Goal

After today, you should be able to:

- Explain what Azure OpenAI and Microsoft Foundry are used for
- Understand the difference between a model, a deployment, and an endpoint
- Know how chat completion fits into an AI app
- Know what embeddings are and why they matter for search and RAG
- Recognize the main Azure AI building blocks you will use later in the course

## Why This Matters For AI-200

AI-200 is not only about infrastructure. It also tests whether you understand how to connect an app to AI capabilities in Azure.

In practice, an AI app usually needs to:

- send prompts to a deployed chat model
- receive structured responses
- create embeddings for search or retrieval
- keep model access secure and configurable
- choose the right Azure AI service for the scenario

Today is the bridge between authentication and actual model usage.

## Official Learning Resources

- Azure OpenAI overview: https://learn.microsoft.com/en-us/azure/ai-services/openai/overview
- Azure OpenAI quickstarts: https://learn.microsoft.com/en-us/azure/ai-services/openai/
- Azure AI Foundry overview: https://learn.microsoft.com/en-us/azure/ai-studio/what-is-ai-studio
- Chat completions concept: https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/chatgpt
- Embeddings concept: https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/embeddings

## Hands-On Practice

### 1. Learn the core terms

Make sure these words feel distinct:

- model: the underlying AI model capability
- deployment: a named, usable instance of a model in Azure
- endpoint: the URL your app calls
- API key or identity: the way your app authenticates

Exam trap: the deployment name is not always the same as the model name.

### 2. Study chat completion

Chat completion is the standard pattern for multi-turn conversation with a model.

You usually send:

- system instructions
- user messages
- optional assistant history

You usually get back:

- generated text
- sometimes structured output
- token usage information

Think of it as the conversational API shape behind many AI assistant apps.

### 3. Study embeddings

Embeddings turn text into vectors that capture semantic meaning.

Use embeddings when you need to:

- compare document chunks
- perform similarity search
- support retrieval-augmented generation
- store and search meaning, not just keywords

Exam clue: if the task is about finding semantically similar text, embeddings are usually involved.

### 4. Review model deployment flow

A simple flow usually looks like this:

1. Create or choose an Azure AI resource
2. Deploy a model with a deployment name
3. Capture the endpoint and auth method
4. Call the deployment from your app
5. Handle response parsing, retries, and logging

### 5. Create today's folder

```powershell
mkdir ai200-day04
cd ai200-day04
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
```

### 6. Install packages

```powershell
pip install openai azure-identity python-dotenv
pip freeze > requirements.txt
```

### 7. Create a small reference file

Create `notes.md` or `model_notes.txt` and write:

- endpoint
- deployment name
- model name
- auth method
- chat completion
- embeddings

This is just to build the vocabulary you will use tomorrow.

## Key Concepts

### Azure OpenAI

Azure OpenAI gives you access to OpenAI models through Azure infrastructure, identity, and governance.

It is commonly used when you need:

- enterprise controls
- Azure integration
- managed access patterns
- deployment inside a larger Azure solution

### Microsoft Foundry

Microsoft Foundry is the broader platform experience for building and managing AI solutions on Azure.

For AI-200, think of it as part of the Azure AI ecosystem you may use to deploy, manage, and connect AI capabilities.

### Chat Completion

Chat completion is the API style for conversation-based model interaction.

It is the main pattern for:

- copilots
- assistant-like experiences
- prompt-and-response workflows

### Embeddings

Embeddings are vector representations of text.

They are the foundation for:

- semantic search
- chunk retrieval
- vector databases
- RAG systems

## Today's Notes

- [ ] A model is not the same as a deployment.
- [ ] The endpoint is the address my app calls.
- [ ] Chat completion is the core interaction pattern for assistant-style apps.
- [ ] Embeddings are used for similarity and retrieval, not just generation.
- [ ] Azure AI apps usually combine auth, deployment, config, and model calls.
- [ ] The exam may ask me to identify the right AI building block for a scenario.

## Completion Criteria

- [ ] You can explain model vs deployment vs endpoint
- [ ] You can explain what chat completion is for
- [ ] You can explain what embeddings are for
- [ ] You reviewed the official Azure OpenAI / Foundry docs
- [ ] You created the Day 4 working folder
- [ ] You can describe the high-level flow for calling a deployed model

## Quick Review Questions

1. What is the difference between a model and a deployment?
```
A model is the AI capability itself; a deployment is the named Azure instance your app calls
```
2. Why do chat completion APIs matter?
```
They are the common way to build assistant-style, multi-turn AI experiences
```
3. What are embeddings used for?
```
Semantic search, similarity matching, and retrieval
```
4. What is the endpoint in an Azure AI app?
```
The URL your code sends requests to
```
5. Why does Azure matter for AI model access?
```
It gives you managed identity, deployment control, and integration with the rest of Azure
```
