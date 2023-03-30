import openai
import gradio as gr
from selenium import webdriver
import multiprocessing

# 设置OpenAI API Key
openai.api_key = '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'
#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

# 使用OpenAI API生成聊天回复
def generate_response(prompt, model, max_tokens, temperature, frequency_penalty, presence_penalty):
    response = openai.Completion.create(
        # engine=engine,
        model=model,
        prompt=prompt,
        max_tokens=max_tokens,
        n=1,
        stop=None,
        temperature=temperature,
        top_p=0.9,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty,
    )

    message = response.choices[0].text.strip()
    return message


# 可选的引擎列表
engine_list = {
    "Davinci": "text-davinci-003",
    "Curie": "text-curie-001",
    "Babbage": "text-babbage-001",
    "Ada": "text-ada-001"
}


#自动打开
def open_page(url):
    option = webdriver.ChromeOptions()
    option.add_experimental_option("detach", True)
    driver = webdriver.Chrome(chrome_options=option)
    driver.maximize_window()
    driver.get(url)


# 使用 Gradio 搭建聊天界面
with gr.Blocks("Chat with OpenAI") as demo:
    with gr.Row():
        with gr.Column(scale=3):
            # 添加输入块
            input_text = gr.Textbox(placeholder="输入", lines=5)
            # 添加输出块
            output_text = gr.Textbox(placeholder="输出", lines=16)
            # 添加按钮块
            button = gr.Button("发送")
        with gr.Column(scale=1):
            # 选择引擎
            model = gr.Dropdown(choices=list(engine_list.values()), label="选择语言模型", value='text-davinci-003')
            max_tokens = gr.Slider(0, 2048, step=50, label="相应长度", value=100)
            temperature = gr.Slider(0.0, 1.0, step=0.1, label="多样性调节", value=0.5)
            frequency_penalty = gr.Slider(0.0, 1.0, step=0.1, label="重复性调节", value=0.5)
            presence_penalty = gr.Slider(0.0, 1.0, step=0.1, label="创新性调节", value=0.5)
            gr.Examples(
                [["制订一个周计划"], ["写一个关于小狗的故事"], ["chatGPT是什么"]],
                input_text,
                None,
                None,
                cache_examples=False,
                label="例子",
            )
        # 添加按钮块
        button.click(generate_response,
                     [input_text, model, max_tokens, temperature, frequency_penalty, presence_penalty], output_text)

demo.launch(share=True)
# def run_app():
#     demo.launch(share=True)


# def open_pages():
#     # time.sleep(1)
#     open_page('http://127.0.0.1:7860')


# # 创造两个进程
# if __name__ == '__main__':
#     try:
#         p1 = multiprocessing.Process(target=run_app)
#         p2 = multiprocessing.Process(target=open_pages)
#         p1.start()
#         p2.start()
#         p1.join()
#     except Exception as e:
#         print("程序异常:", e)
