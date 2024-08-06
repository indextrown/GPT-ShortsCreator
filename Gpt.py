from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()
client = OpenAI()

# 내용을 API에 요청
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "당신은 친절한 유치원 선생님입니다. 항상 5실 유치원생의 눈높이에 맞춰서 5살이 알아듣기 쉽게 아주 쉬운 단어를 사용하고 친절하게 답변을 해주세요."},
    {"role": "user", "content": "안녕하세요~ 선생님 ~ 챗 GPT가 뭐에요?"}
  ]
)

print(completion.choices[0].message)


## temperature topp 모두 랜덤성과 연관된 파라미터
## 정리하자면 둘다 숫자 낮아지면 더 예측가능하고 일관됨 <-> 높아지면 창의적이고 예측불가

## temperature(0~2) 기본값: 1
# 온도값이 낮을 수록 생성된 내용이 더 일관됨 <->높아질수록 창의적

## Top P(0~1) 기본값: 1
# 모델이 고려하는 단어 확률을 누적해 특정 임계값에 도달할 때까지의 단어들만 고려한다
# 예시: hot(35%) warm (25%) 이면 누적확률이 60%에 도달하기 위해 필요한 단어들만을 고려한다

## token기준 https://platform.openai.com/tokenizer
# 1토큰: 영어: 약4글자(단어의 0.75단어) 
# 한국어가 분리함: 같은내용임에도 불구하고 토큰 수가 많이 늘어남

## 토큰당 가격
# 예시 131토큰이 있을 때 