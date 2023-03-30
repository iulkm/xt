import openai

openai.api_key = "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"  # 你的 API 密钥

prompt = "Hello, world!"
model = "gpt-3.5-turbo-0301"  # 你想使用的 GPT 模型 ID
#gpt-3.5-turbo
completions = openai.Completion.create(engine=model, prompt=prompt, max_tokens=5)

if completions.choices[0].text.strip() == "Hello":
    print("OpenAI API 验证成功！")
else:
    print("OpenAI API 验证失败。")

