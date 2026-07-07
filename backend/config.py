import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'futuremap-secret-key-2024')
    DEBUG = True
    CORS_ORIGINS = "*"
