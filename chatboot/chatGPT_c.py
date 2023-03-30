import openai
import gradio as gr
import requests
from urllib.parse import quote
from bs4 import BeautifulSoup
import spacy
import random

# 设置 OpenAI API key
openai.api_key = "YOUR_API_KEY"

# 加载 spaCy 模型
nlp = spacy.load("en_core_web_sm")

# 定义处理图片的块
def process_image(image):
    if image is not None:
        img = Image.open(BytesIO(image)).resize((300, 300))
        img_buffer = BytesIO()
        img.save(img_buffer, format="JPEG")
        img_data = b64encode(img_buffer.getvalue()).decode("ascii")
        return f"![image](data:image/jpg;base64,{img_data})"
    else:
        return ""

# 定义处理代码的块
def process_code(code):
    # 提取代码块
    soup = BeautifulSoup(code, "html.parser")
    code = soup.find("pre", {"class": "prettyprint"})
    if code is None:
        return None
    # 解码 HTML 实体
    code = code.text.replace("&lt;", "<").replace("&gt;", ">")
    # 限制代码长度以避免超出 OpenAI API 的限制
    code = code[:2048]
    return code.strip()

# 定义生成答案的块
def generate_answer(question, image, code):
    # 如果有上传的图片，将其包含在 prompt 中
    prompt = f"Answer the following question: {question}"
    prompt += "\n\n" + process_image(image)
    # 如果有代码输入，将其包含在 prompt 中
    if code is not None:
        prompt += f"\n\nCode:\n{code}"
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

# 定义显示代码的块
def display_code(code):
    # 如果没有代码输入，则返回空字符串
    if code is None:
        return ""
    # 格式化代码
    pretty_code = requests.post(
        "https://google-code-prettify.appspot.com/run_prettify",
        data={"lang": "python", "skin": "sunburst", "style": "default", "code": code},
    ).text
    # 将代码包含在 pre 标签中，并使用 Gradio 的 HTML 输出组件进行显示
    return f"<pre class='prettyprint'>{pretty_code}</pre>"

# 定义生成文案的块
def generate_copy(question, image, code):
    # 调用 ChatGPT 生成答案
    answer = generate_answer(question, image, code)
    # 将答案
    doc = nlp(f"{question} {answer}")
    # 提取主题关键词
    topics = [token.text for token in doc.noun_chunks]
    # 使用主题关键词生成标题
    title = "How to " + " ".join(topics)
    # 使用主题关键词和答案生成正文
    paragraphs = []
    for sentence in doc.sents:
        if not sentence.text.startswith(question):
            paragraphs.append(sentence.text)
    body = "\n\n".join(paragraphs)
    # 将图片和代码加入正文中
    body = process_image(image) + "\n\n" + body + "\n\n" + display_code(code)
    # 将标题和正文组合起来，并返回结果
    result = f"# {title}\n\n{body}"
    return result

def text_copy_generator(question: gr.inputs.Textbox(), image: gr.inputs.Image(), code: gr.inputs.Textbox()):
    return generate_copy(question, image, process_code(code))
gr.Interface(fn=text_copy_generator, inputs=[gr.inputs.Textbox(label="Question"), gr.inputs.Image(label="Image"), gr.inputs.Textbox(label="Code")], outputs="text").launch()