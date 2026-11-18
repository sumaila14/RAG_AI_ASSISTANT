import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)

response = client.embeddings.create(
    model=os.getenv("EMBED_MODEL"),
    input=["I am a good boy" , "python is a good language"]
)

print(len(response.data[0].embedding))
print(len(response.data[1].embedding))
