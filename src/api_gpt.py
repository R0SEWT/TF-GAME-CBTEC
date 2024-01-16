from openai import OpenAI
import os

def get_respuesta_GPT(prompt, OPENAI_API_KEY): 
  client = OpenAI(api_key=OPENAI_API_KEY)
  chat_completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    max_tokens=2048,
    messages=[
      {"role": "user", "content": prompt}
  ]
)
  respuesta = chat_completion.choices[0].message.content
  return respuesta


def get_respuesta_GPT(prompt, p_rol, temp, OPENAI_API_KEY): 
  client = OpenAI(api_key=OPENAI_API_KEY)
  chat_completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    temperature=temp,
    max_tokens=255,
    messages=[
      {"role": "system", "content": p_rol},
      {"role": "user", "content": prompt}
  ]
)
  respuesta = chat_completion.choices
  return respuesta


def show_get_respuesta_GPT(chat_history, prompt, temp, OPENAI_API_KEY): 
  # aniadimos el prompt al historial
  chat_history.append({'role': 'user', 'content': prompt})
  # nos conectamos con gpt3.5 y le pedimos la respuesta en modo stream
  client = OpenAI(api_key=OPENAI_API_KEY)
  chat_completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    temperature=temp,
    max_tokens=255,
    messages=chat_history
  ,
  stream=True
)
  mensaje = []
  # print while writing
  for chunk in chat_completion:
    c_msg = chunk.choices[0].delta.content
    mensaje.append(c_msg)
    full_r_content = ''.join(str(i) for i in mensaje if i is not None) 
    #print('\033[H\033]J', end='') # clean screen no me funciona xd
    #print(chr(27) + "[2J")
    print(full_r_content)
    print("\033[H\033[J", end="")

  #print(chat_history)
  print(full_r_content)
  # aniadimos la respuesta al historial
  chat_history.append({'role': 'assistant', 'content': full_r_content})

  return full_r_content , chat_history


def check_esc(text):
   esc = 'Alternativa Correcta:'
   return text.endswith(esc)

# buged
def show_get_r_GPT(chat_history, prompt, temp, OPENAI_API_KEY): 
  # aniadimos el prompt al historial
  chat_history.append({'role': 'user', 'content': prompt})
  # nos conectamos con gpt3.5 y le pedimos la respuesta en modo stream
  client = OpenAI(api_key=OPENAI_API_KEY)
  chat_completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    temperature=temp,
    max_tokens=255,
    messages=chat_history
  ,
  stream=True
)
  mensaje = []
  # print while writing
  
  save_alternativa = False

  for chunk in chat_completion:
    c_msg = chunk.choices[0].delta.content
    mensaje.append(c_msg)
    if save_alternativa:
      alternativa = ''.join(str(i) for i in mensaje if i is not None) 
      print(alternativa)
    else:
      full_r_content = ''.join(str(i) for i in mensaje if i is not None)
      print(full_r_content)
      print("\033[H\033[J", end="")
   
    if check_esc(full_r_content):
      save_alternativa = True

  #print(chat_history)
  print(full_r_content)
  # aniadimos la respuesta al historial
  full_r_content += alternativa
  chat_history.append({'role': 'assistant', 'content': full_r_content})

  return full_r_content , chat_history