# -*- coding: utf-8 -*-
"""legal_chatbot.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/16O7uTWSN60NKh3kBAibCmPmsjmyyJnXX
"""

!pip install gradio
!pip install transformers

import json
import gradio as gr
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM

tk=AutoTokenizer.from_pretrained("gpt2")
mdl=AutoModelForCausalLM.from_pretrained("gpt2")

conv=[]

def chat(prompt):
    if prompt.lower() in ["stop","quit"]:
        with open("chat_history.json","w") as file:
            json.dump(conv,file,indent=4)
        return "DONE. Bye!"
    if prompt.lower()=="oldconv":
        hist="\n".join(conv)
        return hist
    legal=gen_adv(prompt)
    temp=f"User: {prompt}\nLawyer: {legal}"
    conv.append(temp)
    return legal

def gen_adv(query):
    bot=pipeline("text-generation", model=mdl, tokenizer=tk)
    gen=bot(query, max_length=100, num_return_sequences=1)
    gen_text=gen[0]['generated_text']
    if "Lawyer:" in gen_text:
        legal=gen_text.split("Lawyer:")[1].strip()
    else:
        legal=gen_text.strip()
    return legal

def interact(user_input):
    response=chat(user_input)
    return response

interface= gr.Interface(fn=interact, inputs="text", outputs="text", title="AI Chatbot")
interface.launch()

