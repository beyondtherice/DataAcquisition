from dotenv import load_dotenv
import os

load_dotenv()
# environment variables

monkey = os.getenv("CLIENT_ID")

print(monkey)
