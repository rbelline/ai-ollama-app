import ollama

respone = ollama.list()
#print(respone)

res = ollama.chat(
    model="llama3.2",
    messages=[
        {"role":"user", "content": "why is the sky blue?"}
    ]
)
print(res["message"]["content"])