import openai
import gradio as gr

openai.api_key = "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"

def chat(inputs):
    model_engine = "text-davinci-002"
    completions = openai.Completion.create(
        #要使用的模型的 ID
        engine=model_engine,
        #生成结果的提示文本，即你想要得到的内容描述
        prompt=inputs,
        # max_tokens=1024,
        # n=1,
        # stop=None,
        #控制结果的随机性，如果希望结果更有创意可以尝试 0.9，或者希望有固定结果可以尝试 0.0
        temperature=0.5,
        # 生成结果时的最大 tokens 数
        max_tokens=1024,
        #一个可用于代替 temperature 的参数，对应机器学习中 nucleus sampling，如果设置 0.1 意味着只考虑构成前 10% 概率质量的 tokens
        # temperature=0.5,
        top_p=1.0,
        #制字符的重复度(-2.0 ~ 2.0 之间的数字)
        frequency_penalty=2.0,
        #控制主题的重复度(-2.0 ~ 2.0 之间的数字)
        presence_penalty=2.0,
    )

    message = completions.choices[0].text
    return message

with gr.Blocks() as demo:
    t1 = gr.Textbox(label="提示55665", )
    t4 = gr.TextArea()
    t3 = gr.Button()
    t3.click(chat,t1,t4)
demo.launch(share=True)
