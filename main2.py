from tkinter import *
import main

import openai



def Get_Response(msg):
 api=(main.APi_Key)
 response = openai.ChatCompletion.create(

 model = "gpt-4",

 messages = [{'role':'user','content':msg}]

)

 return response['choices'][0]['message']['content']

window = Tk()

window.title('MY AI')

window.config(bg='cyan')

chat_log = Text(window,height=20,width=50,state=DISABLED)

chat_log.pack(padx=10,pady=5)

promt = Entry(window,width=40)

promt.pack(padx=10,pady=10)

def SendMSG():

 usermsg = promt.get()

 chat_log.config(state=NORMAL)

 chat_log.insert(END,f'You: {usermsg}\n')

#ChatGPT Response

 AIanswer = Get_Response(usermsg)

 chat_log.insert(END,f'AI:{AIanswer}')

 chat_log.config(state=DISABLED)

send = Button(window,text='Send',command=SendMSG)

send.pack(padx=10,pady=10)

window.mainloop()