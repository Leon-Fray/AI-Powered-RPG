import openai
import gradio

openai.api_key = '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'

def read_prewritten_prompt(file_path):
    with open(file_path, 'r') as file:
        return file.read()
prewritten_prompt = read_prewritten_prompt('prompt.txt')

messages = [{"role": "system", "content": prewritten_prompt}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "The Quest for Reunion: Danielle's Adventure")

demo.launch(share=True)