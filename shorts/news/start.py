from openai import OpenAI
from dotenv import load_dotenv

# chatgpt
load_dotenv()
client = OpenAI()

# 프롬포트 텍스트 가져오기
with open("prompt.text") as file:
    file = file.read().strip()

# 프롬포트 문자열에 들어갈 뉴스기사
with open("contents.text") as contents:
    contents = contents.read()

# article에 contents를 삽입한 프롬포트 문자열 생성하기
prompt = file.format(article = contents)
print(prompt)

