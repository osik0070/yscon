from openai import OpenAI

# 1. 엘엠스튜디오(LM Studio) 서버 주소 연결하기
# 엘엠스튜디오는 항상 내 컴퓨터의 1234번 방(포트)을 사용합니다.
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

print("👉 엘엠스튜디오 AI에게 질문을 보내는 중입니다. 잠시만 기다려주세요...\n")

# 2. AI에게 보낼 질문 작성하기
completion = client.chat.completions.create(
  model="gemma2", # 이름은 크게 상관없습니다. 엘엠스튜디오에 현재 켜져 있는 모델이 자동으로 사용됩니다.
  messages=[
    {"role": "system", "content": "너는 친절하고 똑똑한 한국어 AI 비서야. 항상 한국어로 대답해줘."},
    {"role": "user", "content": "안녕! 너는 누구야? 1인 기업을 준비하는 초보자에게 따뜻하게 한마디 인사해줘."}
  ],
  temperature=0.7,
)

# 3. AI의 답변 출력하기
print("================[ AI의 답변 ]================\n")
print(completion.choices[0].message.content)
print("\n=============================================")
