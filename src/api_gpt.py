from openai import OpenAI


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
  stream=False
)
  full_r_content = chat_completion.choices[0].message.content
  mensaje = []
  # print while writing
  #for chunk in chat_completion:
  #  c_msg = chunk.choices[0].delta
  #  mensaje.append(c_msg)
  #  full_r_content = ''.join([(m.content)for m in mensaje])
  #  print(full_r_content)
  #  print('\033[H\033]J', end='') # clean screen 
  #  print(chat_completion)
  print(chat_history)
  print(full_r_content)
  # aniadimos la respuesta al historial
  chat_history.append({'role': 'assistant', 'content': full_r_content})

  return full_r_content , chat_history