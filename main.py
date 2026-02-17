import os
from dotenv import load_dotenv
from google import genai

from prompt import hello_world_prompt
from schemas import HelloWorldResponse

# .env から API キー読み込み
load_dotenv()

# クライアント作成
client = genai.Client()

# モデル指定
model_id = "gemini-2.5-flash-lite"


def main():
    # プロンプト生成
    prompt = hello_world_prompt("Python")

    # Gemini呼び出し（Structured Output）
    response = client.models.generate_content(
        model=model_id,
        contents=prompt,
        config={
            "response_mime_type": "application/json",
            "response_schema": HelloWorldResponse.model_json_schema(),
        }
    )

    # Pydanticで検証
    parsed = HelloWorldResponse.model_validate_json(response.text)

    print("=== Pydantic Parsed Result ===")
    print(parsed)
    print("\n=== Code ===")
    print(parsed.code)

if __name__ == "__main__":
    main()