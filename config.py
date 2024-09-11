import os
from dotenv import load_dotenv

load_dotenv()  # Carrega as variáveis de ambiente do arquivo .env

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
