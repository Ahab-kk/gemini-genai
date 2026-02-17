import os
from dotenv import load_dotenv
from google import genai
from pydantic import BaseModel

# .env から API キー読み込み
load_dotenv()
# 環境変数 GEMINI_API_KEY

class HelloWorldResponse(BaseModel):
    language: str
    code: str
    explanation: str

# クライアント作成
client = genai.Client()

# モデル指定
model_id = "gemini-2.5-flash-lite"

# プロンプト作成
prompt = """
PythonでHello Worldを書く方法を教えて。
必ず以下のJSON形式で返してください:
{
  "language": "...",
  "code": "...",
  "explanation": "..."
}
"""

# コンテンツ生成
response = client.models.generate_content(
    model=model_id,
    contents=prompt,
    config={
        "response_mime_type": "application/json",
        "response_schema": HelloWorldResponse.model_json_schema(),
    }
)

# 出力
print(response.text)

# JSONをPydanticでパース
parsed = HelloWorldResponse.model_validate_json(response.text)

print(parsed)
print(parsed.code)