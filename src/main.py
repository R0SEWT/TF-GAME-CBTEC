from decouple import config
import api_gpt


def config_prompt():
    prompt = '''Haremos una dinámica, realiza un juego para aprender a elegir el equipo de protección
        personal adecuado para la actividad de riesgo. El jugador es un trabajador de una empresa de 
        distribucion electrica de 45 años. Para cada actividad de riesgo brinda tres alternativas de 
        conjugación,donde al menos una es correcta, brindame las(s) alternativas correctas. De forma 
        aleatoria selecciona un nivel de dificultad (0,1,2) . Realiza una pregunta a la vez. Continua 
        hasta que te diga "stop". Empieza por la primera pregunta.
Dificultad: <Dificultad>
Pregunta:<Pregunta>
Alternativa:<Alternativas>
Alternativa correcta: <Alternativa correcta>
'''
    p_rol = 'Toma el rol de un ingeniero de seguridad industrial. '
    return prompt, p_rol


#####################################################################################################
def main():
    API_OPEN_AI_KEY = config('API_OPEN_AI_KEY')
    chat_history = []
    temperature = .2

    while True:
        prompt = input('Digita Prompt: ')
        if prompt == 'exit':
            break
        else:
            response , chat_history = api_gpt.show_get_respuesta_GPT(chat_history, prompt, temperature, API_OPEN_AI_KEY)


    #prompt, p_rol = config_prompt()
            
    ## inicializar el juego
    #respuesta = api_gpt.get_respuesta_GPT(prompt, p_rol, .3, API_OPEN_AI_KEY)
    #print(respuesta)
    # guardar respuestas
    # salir del juego
    # comunicar resultados

if __name__ == "__main__":
    main()