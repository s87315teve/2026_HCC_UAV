import ollama

# 此程式碼示範如何使用Ollama的套件以及OpenAI相容格式來進行聊天互動。
# 請確保 Ollama 已經在本地或指定的伺服器上運行，並且已經安裝了對應的模型（如 gemma3:270m）。
# 使用者可以輸入訊息，AI 會根據歷史對話進行回應，直到使用者輸入 "quit" 結束對話。

#----------------------DEMO 1: 此為使用Ollama library的範例程式碼---------------------------

client = ollama.Client(host="http://localhost:11434")
MODEL = "gemma3:270m"  # 或 qwen2.5, mistral 等

print("Chat started. Type 'quit' to exit.\n")

history = []

while True:
    user_input = input("You (Please input you message here): ").strip()
    
    if user_input.lower() == "quit":
        print("Bye!")
        break
    
    if not user_input:
        continue

    history.append({"role": "user", "content": user_input})

    response = client.chat(
        model=MODEL,
        messages=history,
        options={"temperature": 0.7}
    )

    reply = response["message"]["content"]
    history.append({"role": "assistant", "content": reply})

    print(f"AI: {reply}\n")


# ------------------------------------------------------------------


#----------------------DEMO 2: 此為使用OpenAI相容格式的範例程式碼---------------------------

# from openai import OpenAI

# client = OpenAI(
#     base_url="http://localhost:11434/v1",  # Ollama 的 OpenAI 相容端點
#     api_key="",  # 如果沒有特別設定api_key的話可以隨便寫
# )

# MODEL = "gemma3:270m"

# print("Chat started. Type 'quit' to exit.\n")

# history = []

# while True:
#     user_input = input("You (Please input your message here): ").strip()

#     if user_input.lower() == "quit":
#         print("Bye!")
#         break

#     if not user_input:
#         continue

#     history.append({"role": "user", "content": user_input})

#     response = client.chat.completions.create(
#         model=MODEL,
#         messages=history,
#         temperature=0.7,
#     )

#     reply = response.choices[0].message.content
#     history.append({"role": "assistant", "content": reply})

#     print(f"AI: {reply}\n")
