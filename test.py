import openai

openai.api_key = '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'

def read_prewritten_prompt(file_path):
    with open(file_path, 'r') as file:
        return file.read()
prewritten_prompt = read_prewritten_prompt('prompt.txt')
messages = []
# system_msg = input("What type of chatbot would you like to create?\n")
messages.append({"role": "system", "content": prewritten_prompt})

print("Enter Start Game!")
while input != "quit()":
    message = input()
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")