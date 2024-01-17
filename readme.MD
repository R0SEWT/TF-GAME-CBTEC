# Juego de Selección de Equipos de Protección Personal

Este proyecto es un juego interactivo basado en texto que te permite aprender sobre la selección de equipos de protección personal para diferentes actividades de riesgo. El juego simula la experiencia de un trabajador de una empresa de distribución eléctrica enfrentándose a diversas situaciones laborales.

## Ingeniering Prompting
Este proyecto es el resultado del trabajo final del curso de Ingeniering. Para concientrizar sobre el adecuado uso de EPP para diferentes actividades de riesgo.

## Requisitos

Asegúrate de tener instaladas las siguientes bibliotecas en tu entorno de Python:

```bash
pip install python-decouple
pip install pandas
```

## Configuración

Antes de ejecutar el juego, necesitas configurar tu clave de API de OpenAI. Crea un archivo `.env` en el mismo directorio que tu script y agrega la siguiente línea:

```plaintext
OPEN_AI_KEY=tu_clave_de_api
```

Reemplaza `tu_clave_de_api` con tu clave de API de OpenAI.

## Cómo jugar

1. Ejecuta el script `main.py`.
2. Selecciona un empleado aleatorio de la lista de empleados cargada desde el archivo `empleados.xlsx`.
3. Se te presentará un escenario y tres alternativas de equipos de protección personal.
4. Elige la alternativa correcta basándote en tu conocimiento y experiencia.
5. Recibirás retroalimentación y una explicación después de cada elección.
6. El juego variará en dificultad de manera aleatoria entre capacitado, experto y veterano.
7. Después de cada turno, se mostrará tu puntaje acumulado y un mensaje motivador.
8. ¡Disfruta del juego y aprende sobre la selección de equipos de protección personal!

## Estructura del Código

- `c_empleado.py`: Contiene la clase `Empleado` para representar a los empleados.
- `api_gpt.py`: Proporciona funciones para interactuar con OpenAI GPT-3 para obtener respuestas.
- `main.py`: El punto de entrada principal para ejecutar el juego.

## Archivos de Datos

- `empleados.xlsx`: Archivo Excel que contiene la información de los empleados.

¡Diviértete aprendiendo sobre la seguridad laboral y la selección de equipos de protección personal!