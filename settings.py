from dotenv import load_dotenv, find_dotenv
import os

dotenv_file = find_dotenv()

load_dotenv(dotenv_file)

HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
RELOAD = os.getenv("RELOAD")

X_TOKEN = os.getenv("X_TOKEN")
X_KEY = os.getenv("X_KEY")

DB_SGDB = os.getenv("DB_SGDB")
DB_NAME = os.getenv("DB_NAME")

# Ajusta STR_DATABASE conforme gerenciador escolhido
if DB_SGDB == 'sqlite': # SQLite
  STR_DATABASE = f"sqlite:///{DB_NAME}.db"
else: # SQLite
  STR_DATABASE = f"sqlite:///apiDatabase.db"