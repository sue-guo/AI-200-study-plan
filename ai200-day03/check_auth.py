from azure.identity import DefaultAzureCredential

credential = DefaultAzureCredential()
print(type(credential).__name__)
