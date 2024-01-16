from decouple import config
import api_gpt


def config_prompt():
    prompt = '''Como ingeniero de seguridad industrial, participarás en un juego interactivo que te permitirá 
    aprender a seleccionar el equipo de protección personal adecuado para diferentes actividades de riesgo.
    Tu personaje es un trabajador de 45 años de una empresa de distribución eléctrica.En cada turno, se te 
    presentará una actividad de riesgo y se te proporcionarán tres alternativas de equipos de protección personal. 
    Deberás seleccionar la alternativa correcta basándote en tu conocimiento y experiencia. Además, el juego variará 
    en dificultad. De forma aleatoria, se seleccionará un nivel de dificultad entre capacitado, experto y veterano. 
    Esto afectará a la complejidad de las actividades de riesgo y las opciones de equipos de protección personal.
    Después de cada elección, recibirás retroalimentación y una explicación sobre por qué la alternativa seleccionada es correcta o incorrecta. Además, se te recordará tu puntaje acumulado.
    La estructura de cada turno será la siguiente:

    - Puntaje: <Puntaje>
    - Dificultad: <Dificultad>
    - Pregunta: <Pregunta o caso>
    - Alternativa: <Alternativas>

    Tras seleccionar una alternativa inmediatamente empieza otro turno.¡Empecemos con la primera pregunta!
'''

    return prompt


def get_alternativa():
    a = '0'
    while a != '1' and a != '2' and a != '3' and a != 'exit':
        a = input(' ')
    return a

#####################################################################################################
def main():
    OPEN_AI_KEY = config('OPEN_AI_KEY')
    chat_history = []
    temperature = .2
    prompt = config_prompt()
    preguntas = 2

    while preguntas > 0:
        if prompt == 'exit':
            break
        else:
            response , chat_history = api_gpt.show_get_respuesta_GPT(chat_history, prompt, temperature, OPEN_AI_KEY)  
        preguntas -= 1
        prompt = get_alternativa()
        if preguntas == 0:
            prompt = '''Motivame a seguir aprendiendo y recuerdame mi puntaje:
                        La estructura será la siguiente:
                        Tu puntaje: <Puntaje>
                        <Mensaje motivador>'''
            temperature = .7 # para que se ponga creativo
            response , chat_history = api_gpt.show_get_respuesta_GPT(chat_history, prompt, temperature, OPEN_AI_KEY) 
        
    
if __name__ == "__main__":
    main()