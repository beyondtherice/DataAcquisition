from dotenv import load_dotenv
load_dotenv()

import os

# environment variables

monkey = os.environ.get("CLIENT_ID")

print(monkey)
