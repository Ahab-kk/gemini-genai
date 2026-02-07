import os
from dotenv import load_dotenv
from google import genai

# .env から API キー読み込み
load_dotenv()
# 環境変数 GEMINI_API_KEY

# クライアント作成
client = genai.Client()

# モデル指定
model_id = "gemini-2.5-flash-lite"  # 最新のGeminiモデルを使用

# プロンプト作成
prompt = "PythonでHello Worldを書く方法を教えて"

# コンテンツ生成
response = client.models.generate_content(
    model=model_id,
    contents=prompt
)

# 出力
print(response.text)
