from dotenv import load_dotenv
import os

load_dotenv(".env")

HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
RELOAD = os.getenv("RELOAD")