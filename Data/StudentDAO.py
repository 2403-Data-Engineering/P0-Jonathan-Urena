import os
from dotenv import load_dotenv

load_dotenv()

number = os.getenv("TEST")
print(number)