# Chat App Python

Este es un proyecto final desarrollado para la materia "Programación 1" de la universidad. Se trata de una simple app de chat desarrollada en Python utilizando la biblioteca Tkinter para la interfaz gráfica y Pyrebase para la integración con Firebase Realtime Database.

## Descripción

La aplicación de chat permite a los usuarios crear y unirse a salas de chat utilizando códigos de sala generados aleatoriamente. Cada sala de chat almacena los mensajes en una base de datos en tiempo real de Firebase, lo que permite una comunicación en tiempo real entre los usuarios.

## Características

- Crear y unirse a salas de chat utilizando códigos de sala únicos.
- Enviar y recibir mensajes en tiempo real.
- Interfaz gráfica simple y fácil de usar utilizando Tkinter.

## Requisitos de Instalación

Antes de ejecutar la aplicación, asegúrese de tener instalado Python 3 y las siguientes bibliotecas:

``` pip install tk pyrebase ```


## Configuración

Antes de ejecutar la aplicación, debe configurar la conexión con su base de datos de Firebase. Para ello, siga estos pasos:

1. Cree un proyecto en [Firebase Console](https://console.firebase.google.com/).
2. Agregue una aplicación web a su proyecto y copie la configuración de Firebase.
3. Pegue la configuración de Firebase en el código en la sección `firebase = pyrebase.initialize_app({...})`.

## Ejecución

Para ejecutar la aplicación, simplemente ejecute el archivo `main.py`:

``` python main.py ```


## Capturas de Pantalla

![image](https://github.com/dalvinsegura/chat-app-final-project-programming/assets/64456007/8ba5accc-2078-4475-92d7-625a10d578e7)

![image](https://github.com/dalvinsegura/chat-app-final-project-programming/assets/64456007/69755c4e-4dfc-4e54-9027-55e9a649ef47)

![image](https://github.com/dalvinsegura/chat-app-final-project-programming/assets/64456007/f97b3eef-de1c-4649-8feb-2bba303c85fc)


## Contribuir

Si desea contribuir a este proyecto, siéntase libre de crear una solicitud de extracción. Cualquier contribución es bienvenida y apreciada.

## Licencia

Este proyecto está licenciado bajo la [Licencia MIT](LICENSE).
