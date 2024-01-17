from decouple import config
import api_gpt
import c_empleado
import pandas as pd
import random


def get_empleado(path):
    empleados = []
    for _ ,row in pd.read_excel(path).iterrows():
        empleado = c_empleado.Empleado( row['Nombre'], row['Apellidos']
                                       , row['Cargo'], row['Edad']
                                       )
        empleados.append(empleado)

    # incio de sesion
    user = random.choice(empleados)
    return user


def config_prompt(user):
    prompt = f'''Como {user.rol}, participarás en un juego interactivo que te permitirá 
    aprender a seleccionar el equipo de protección personal adecuado para diferentes actividades de riesgo.
    Tu personaje es un trabajador de {user.age} años de una empresa de distribución eléctrica.En cada turno, se te 
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
    path = './empleados.xlsx'
    user = get_empleado(path)
    prompt = config_prompt(user)

    OPEN_AI_KEY = config('OPEN_AI_KEY')
    chat_history = []
    temperature = .2
    preguntas = 2
    
    print(f'Hola {user.rol} {user.name} {user.lname}')

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