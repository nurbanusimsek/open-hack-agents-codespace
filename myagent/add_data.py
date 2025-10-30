import os
from dotenv import load_dotenv

# Azure SDK imports
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.agents.models import FilePurpose

# Load environment variables (expects PROJECT_CONNECTION_STRING in .env)
load_dotenv(override=True)