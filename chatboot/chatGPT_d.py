import openai
import gradio as gr
from PIL import Image
from io import BytesIO
from base64 import b64encode

# 设置 OpenAI API key
openai.api_key = "YOUR_API_KEY"

# 定义处理图片的块
def process_image(image):
    if image is not None:
        with Image.open(BytesIO(image)) as img:
            img = img.resize((300, 300))
            img_buffer = BytesIO()
            img.save(img_buffer, format="JPEG")
            img_data = b64encode(img_buffer.getvalue()).decode("ascii")
        return f"![image](data:image/jpg;base64,{img_data})"
    else:
        return ""

# 定义生成答案的块
def generate_answer(question, image):
    # 如果有上传的图片，将其包含在 prompt 中
    prompt = f"Answer the following question: {question}"
    prompt += "\n\n" + process_image(image)

    # 调用 OpenAI API
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
        top_p=0.9,
        frequency_penalty=0.5,
        presence_penalty=0.0,
    )

    # 解析响应并返回结果
    result = response.choices[0].text.strip()
    return result

# 定义 Gradio 输入组件
question_input = gr.inputs.Textbox(label="请输入您的问题：")
image_input = gr.inputs.Image(label="请上传您的图片：", source="upload")

# 定义 Gradio 输出组件
answer_output = gr.outputs.Textbox(label="答案将会在这里显示。")

# 创建 Gradio 应用程序
app = gr.Interface(
    fn=generate_answer,
    inputs=[question_input, image_input],
    outputs=answer_output,
    title="OpenAI GPT-3 App",
    description="输入一个问题,OpenAI GPT-3 将会生成一个答案，并可选包含一张图片。",
    theme="compact",
    blocks=[
        gr.Block(
            process_image,
            name="处理图片",
            inputs=[image_input],
            outputs=[],
            block_type="filter",
        ),
        gr.Block(
            generate_answer,
            name="生成答案",
            inputs=[question_input, gr.inputs.Input("处理图片")],
            outputs=[answer_output],
            block_type="compute",
        ),
    ],
)

# 运行 Gradio 应用程序
app.launch()

