import sys
from azure.identity import DefaultAzureCredential

print("Python version:", sys.version)
print("DefaultAzureCredential object created successfully")

credential = DefaultAzureCredential()
print(type(credential).__name__)