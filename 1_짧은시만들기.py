from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

response = client.chat.completions.create(
  model="gpt-3.5-turbo-0125",
  response_format={ "type": "json_object" },
  messages=[
    {"role": "system", "content": "You are a helpful assistant designed to output JSON with 'poem' key."},
    {"role": "user", "content": "겨울에 대한 짧은 시를 써줘."}
  ]
)
print(response.choices[0].message.content)


