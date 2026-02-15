# Configuration et connexion à Elasticsearch
from elasticsearch import Elasticsearch
from datetime import datetime, timedelta
import json
import subprocess
import os
import warnings
import dotenv
from urllib3.exceptions import InsecureRequestWarning
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

warnings.simplefilter("ignore", InsecureRequestWarning)
# Configuration
ES_HOST = "https://localhost:9200"
ES_USER = "elastic"
ES_PASSWORD = os.getenv("ELASTIC_PASSWORD")  

# Connexion
es = Elasticsearch(
    [ES_HOST],
    basic_auth=(ES_USER, ES_PASSWORD),
    verify_certs=False
)

# Vérification de la connexion
health = es.cluster.health()
print(f"Cluster Elasticsearch: {health['status']} ({health['number_of_nodes']} nœuds)")
