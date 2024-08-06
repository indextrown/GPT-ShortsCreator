
# GPT-ShortsCreator

GPT-ShortsCreator는 OpenAI의 GPT 모델을 사용하여 짧은 콘텐츠를 생성하는 프로젝트입니다.

## 프로젝트 설명

이 프로젝트는 OpenAI의 GPT-3.5-turbo 모델을 활용하여 유치원생의 눈높이에 맞춘 친절한 답변을 생성하는 프로그램입니다. 주로 교육용 콘텐츠나 짧은 문장을 생성하는 데 사용됩니다.

## 설치 및 설정

### 필수 사항

- Python 3.9 이상
- OpenAI API 키

### 설치 방법

1. 저장소 클론

   ```sh
   git clone https://github.com/indextrown/GPT-ShortsCreator.git
   cd GPT-ShortsCreator
   ```

2. 가상 환경 설정

   ```sh
   python -m venv .venv
   source .venv/bin/activate  # Windows에서는 .venv\Scripts\activate
   ```

3. 필요한 패키지 설치

   ```sh
   pip install -r requirements.txt
   ```

4. 환경 변수 설정

   프로젝트 루트 디렉토리에 `.env` 파일을 생성하고, 다음과 같이 OpenAI API 키를 추가합니다.

   ```env
   OPENAI_API_KEY=your_api_key_here
   ```

## 사용 방법

`Gpt.py` 파일을 실행하여 GPT 모델을 사용할 수 있습니다. 다음은 예제 코드입니다.

```python
from openai import OpenAI
from dotenv import load_dotenv
import os

# .env 파일의 환경 변수 로드
load_dotenv()

# 환경 변수에서 API 키 가져오기
api_key = os.getenv("OPENAI_API_KEY")

# OpenAI 클라이언트 초기화
client = OpenAI(api_key=api_key)

# 내용을 API에 요청
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "당신은 친절한 유치원 선생님입니다. 항상 5살 유치원생의 눈높이에 맞춰서 5살이 알아듣기 쉽게 아주 쉬운 단어를 사용하고 친절하게 답변을 해주세요."},
    {"role": "user", "content": "안녕하세요~ 선생님 ~ 챗 GPT가 뭐에요?"}
  ]
)

print(completion.choices[0].message["content"])
```

## 기여 방법

1. 이 저장소를 포크합니다.
2. 새 브랜치를 생성합니다. (`git checkout -b feature/your-feature-name`)
3. 변경 사항을 커밋합니다. (`git commit -m 'Add some feature'`)
4. 브랜치에 푸시합니다. (`git push origin feature/your-feature-name`)
5. 풀 리퀘스트를 생성합니다.

## 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다. 자세한 내용은 `LICENSE` 파일을 참고하세요.
