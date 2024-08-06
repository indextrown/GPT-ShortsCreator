from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

prompt_templete_v1 = """
최신 연예 뉴스 기사가 주어집니다.
뉴스 기사를 참고해서 유투브 쇼츠 대본을 작성해주세요.
각 단락마다 영상에 소개될 이미지나 영상 클립을 묘사해주세요. 
10대 소녀가 친구에게 말하는 듯한 말투로 작성해주세요.

반드시 아래 포맷으로 작성해주세요.
[제목] <제목 텍스트>\n\n
[클립] <영상에서 보여줄 이미지나 영상에 대한 묘사\n
[대본] 나레이션 방식의 대본>\n
[클립] <영상에서 보여줄 이미지나 영상에 대한 묘사\n
[대본] 나레이션 방식의 대본\n
...
---
뉴스기사: {article}
---
""".strip()

article = """
오는 9월 결혼 예정인 EXID 출신 하니와 정신의학과 전문의 양재웅 커플의 결혼 연기설이 제기됐다.
이는 양재웅이 운영하는 병원에서 최근 발생한 사고의 여파로 보인다.
하니의 소속사 측 관계자는 "결혼 연기와 관련된 내용은 확인 불가하다"는 입장을 고수하고 있는 상태다.
하니, 양재웅은 4년간의 열애 끝에 지난 6월 9월에 결혼한다는 소식을 전한 바 있다.
하니는 "삶을 함께 하고 싶은 사람을 만났다"라고 밝혔고 양재웅은 한 방송 프로그램에 하니가 먼저 프러포즈를 했다며 행복한 예비신랑으로서의 모습을 보여주기도 했다.
10살 차이인 하니와 양재웅은 2022년 6월 교제를 인정하고 공개 연애를 이어왔다.
하니는 2011년 그룹 EXID로 데뷔했으며 이후 배우로 전향해 드라마 '아직 낫서른', '사랑이라 말해요' 등에 출연했다. 양재웅은 '하트시그널' 시리즈를 비롯해 다양한 방송에 출연하며 얼굴을 알렸다.
② '과잉 경호 논란' 변우석, 근황 공개…의리파 행보
'과잉 경호' 논란으로 곤욕을 치른 배우 변우석이 약 한 달 만에 SNS 활동을 재개하고 근황을 공개했다.
변우석은 자신의 개인 계정을 통해 별다른 멘트 없이 여러 장의 사진을 올렸다. 공개된 사진은 변우석이 최근 촬영한 각종 광고의 비하인드 컷으로 알려졌다.
또 배우 진구와 드라마 '감사합니다' 팀에 커피차를 보내고 모델 출신 배우 주우재와 함께 지인의 결혼식에 참석하는 등 의리 넘치는 행보도 이어오고 있다.
③ (여자)아이들, 월드투어 시작…꿈의 무대 KSPO 돔 입성
대세 걸그룹 (여자)아이들이  2024 월드투어의 성대한 막을 올렸다.
(여자)아이들은 8월 3일과 4일 양일간 서울 송파구 KSPO DOME에서 '2024 여자아이들 월드 투어 아이돌 인 서울'을 성공적으로 개최, 세 번째 월드투어에 돌입했다.
서울 공연을 시작으로 홍콩, 도쿄, 타이페이, 방콕, 마카오, 멜버른, 시드니까지 전 세계 총 14개 도시에서 팬들과 뜨겁게 호흡할 예정이다. 여자 아이들이 K팝의 저력으로 또 한 번 전 세계를 놀라게 하길 기대한다.
출처 : OBS경인TV(https://www.obsnews.co.kr)
"""

prompt = prompt_templete_v1.format(article = article)
# print(prompt)

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  # model="gpt-3.5-turbo-0125",
  messages=[
    {"role": "system", "content": "당신은 유용한 도우미입니다."},
    {"role": "user", "content": prompt}
  ]
)
print(response.choices[0].message.content)
