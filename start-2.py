import ollama

respone = ollama.list()
#print(respone)

#res = ollama.chat(
#    model="llama3.2",
#    messages=[
#        {"role":"user", 
#         "content": "why is the sky blue?",
#        },
#    ],
#    stream=True,
#)
#for chunk in res:
#    print(chunk["message"]["content"], end="", flush=True)
#print(res["message"]["content"])

#res = ollama.generate(
#    model="llama3.2",
#    prompt="why is the sky blue?",
#)

#show
#print(ollama.show("llama3.2"))

#create a new model with modelfile
#modelfile = """
#FROM llama3.2
#SYSTEM you are a very smart assistant who knows everything about datalogic spa products. You are very succint and informative. All the information are in this page https://www.datalogic.com/ita/prodotti-hp-255.html
#PARAMETER temperature 0.1
#"""
#
#ollama.create(model="dat", modelfile=modelfile)
#
#res = ollama.generate(model="dat",
#                      prompt="tell me about top 3 datalogic product categories")
#
#print(res["response"])

#delete model
#ollama.delete("dat")

