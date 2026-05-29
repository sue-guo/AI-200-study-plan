# AI-200 Study Todo List

Goal: Microsoft Certified: Azure AI Cloud Developer Associate / Exam AI-200

Daily rhythm:
- [ ] Study Microsoft Learn or official docs for 45-60 minutes
- [ ] Complete hands-on practice for 45-60 minutes
- [ ] Write down 5-10 key points or common traps
- [ ] Review practice questions or yesterday's weak points

## Week 1: Python and Azure AI Foundations

- [x] Day 1: Read the AI-200 exam guide; install Python, Azure CLI, VS Code; understand Azure SDK authentication basics
- [ ] Day 2: Review Python async, HTTP APIs, environment variables, and configuration management
- [ ] Day 3: Learn Azure authentication: DefaultAzureCredential, Managed Identity, and Service Principal
- [ ] Day 4: Learn Azure OpenAI / Microsoft Foundry basics: model deployment, chat completion, and embeddings
- [ ] Day 5: Build a Python CLI that sends a question to a model and returns an answer
- [ ] Day 6: Add config loading, logging, exception handling, and retry logic to the CLI
- [ ] Day 7: Review the week; draw the flow for authentication, SDK usage, and model calls

## Week 2: Containers and Azure Deployment

- [ ] Day 8: Learn Docker basics: Dockerfile, image, container, environment variables, and ports
- [ ] Day 9: Containerize the AI CLI or convert it into a simple API first, then containerize it
- [ ] Day 10: Use Azure Container Registry to build, push, and pull container images
- [ ] Day 11: Deploy the container to Azure Container Apps; configure environment variables and revisions
- [ ] Day 12: Learn KEDA and event-driven scaling for HTTP, queues, and events
- [ ] Day 13: Learn AKS basics: manifest, deployment, service, config map, and secret
- [ ] Day 14: Review the week; compare Container Apps and AKS, and summarize likely exam scenarios

## Week 3: AI Data Services and RAG

- [ ] Day 15: Learn RAG concepts: chunking, embeddings, vector search, and metadata filters
- [ ] Day 16: Practice Cosmos DB for NoSQL SDK CRUD, partition keys, RU, and consistency
- [ ] Day 17: Store embeddings in Cosmos DB and run vector similarity search; review indexing policy basics
- [ ] Day 18: Practice PostgreSQL with pgvector: table design, vector type, indexes, and similarity queries
- [ ] Day 19: Optimize PostgreSQL vector workloads: connection pooling, index choice, and query latency
- [ ] Day 20: Learn Azure Managed Redis: cache operations, expiration, invalidation, and vector indexing
- [ ] Day 21: Build a small RAG flow: ingest document, create embeddings, retrieve chunks, and generate answer

## Week 4: Events, Messaging, and Azure Functions

- [ ] Day 22: Learn Azure Functions triggers: HTTP trigger, timer trigger, and queue trigger
- [ ] Day 23: Practice Functions bindings, app configuration, and deployment
- [ ] Day 24: Learn Service Bus: queues, topics, subscriptions, dead-letter queues, and message locks
- [ ] Day 25: Learn Event Grid: custom events, filters, retry behavior, and event-driven workflows
- [ ] Day 26: Design an async AI workflow: request enters queue, worker processes it, result is stored
- [ ] Day 27: Convert the RAG app to use async processing through Service Bus or Queue-triggered Functions
- [ ] Day 28: Review the week; compare Service Bus, Event Grid, Storage Queue, and Functions scenarios

## Week 5: Security, Monitoring, and Troubleshooting

- [ ] Day 29: Learn Key Vault: secrets, keys, certificates, rotation, and SDK retrieval
- [ ] Day 30: Learn App Configuration: centralized configuration, feature flags, and Key Vault references
- [ ] Day 31: Use Managed Identity so the app can access Key Vault, Cosmos DB, or Storage without passwords
- [ ] Day 32: Learn OpenTelemetry: traces, spans, and distributed tracing
- [ ] Day 33: Learn Azure Monitor and Application Insights: logs, metrics, alerts, and failures
- [ ] Day 34: Practice KQL queries for errors, latency, request volume, and failure rate
- [ ] Day 35: Troubleshoot common failures: container startup failure, permission failure, connection failure, and timeout

## Week 6: Integrated Project and Exam Review

- [ ] Day 36: Integrate the project: RAG API, container deployment, Key Vault, and App Configuration
- [ ] Day 37: Add Service Bus async processing and retry handling
- [ ] Day 38: Add Application Insights, OpenTelemetry traces, and useful KQL queries
- [ ] Day 39: Review all official AI-200 skill areas and identify weak topics
- [ ] Day 40: Take a practice test or self-assessment; create an error log
- [ ] Day 41: Review missed questions; focus on containers, RAG, messaging, security, and monitoring
- [ ] Day 42: Final review: error log, architecture diagrams, service selection table, and key command patterns

## Final Project Checklist

Build an AI document Q&A service with:
- [ ] Python FastAPI
- [ ] Azure OpenAI or Microsoft Foundry model calls
- [ ] Cosmos DB or PostgreSQL with pgvector for embeddings
- [ ] Redis cache
- [ ] Service Bus for async tasks
- [ ] Azure Container Apps deployment
- [ ] Key Vault for secrets
- [ ] App Configuration for settings
- [ ] Application Insights and OpenTelemetry monitoring
- [ ] KQL queries for troubleshooting

## Daily Completion Questions

- [ ] Can I explain when to use today's Azure service?
- [ ] Did I write code, deploy, or configure something hands-on?
- [ ] Can I answer why this service is better than the alternatives in an exam scenario?
