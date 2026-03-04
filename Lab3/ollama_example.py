import ollama



client = ollama.Client(host="http://localhost:11434")
MODEL = "gemma3:270m"  # 或 qwen2.5, mistral 等

# client = ollama.Client(host="http://192.168.0.183:11434"). ##如果其他電腦可以執行更厲害的模型的話，可以指定外部IP
# MODEL = "gemma3:12b"  # 或 qwen2.5, mistral 等

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
