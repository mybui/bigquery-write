import os

# port
PORT = os.environ.get("PORT", 8080)

# logging config (default remote)
LOG = os.environ.get("LOG", "remote")

ELQ_USER = os.environ.get("ELQ_USER")
ELQ_PASSWORD = os.environ.get("ELQ_PASSWORD")
ELQ_BASE_URL = os.environ.get("ELQ_BASE_URL")

GOOGLE_APPLICATION_CREDENTIALS = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
GOOGLE_CLOUD_PROJECT = os.environ.get('GOOGLE_CLOUD_PROJECT')
GOOGLE_CLOUD_DATASET = os.environ.get('GOOGLE_CLOUD_DATASET')