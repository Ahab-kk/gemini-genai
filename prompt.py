def hello_world_prompt(language: str) -> str:
    return f"""
あなたは優秀なエンジニアです。

{language}でHello Worldを書く方法を教えてください。

必ず以下のJSON形式で出力してください:

{{
  "language": "{language}",
  "code": "実行可能なコード",
  "explanation": "初心者向けの説明"
}}
"""
