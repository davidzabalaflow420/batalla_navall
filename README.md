BattleShip

BattleShip es un juego de estrategia naval en el que el objetivo es hundir los barcos del oponente antes de que este hunda los tuyos. Este programa está desarrollado en Python con la librería Kivy para crear una interfaz gráfica de usuario (GUI).
Cómo ejecutar el programa

Asegúrate de tener Python y la librería Kivy instalada en tu sistema. Puedes instalar Kivy con el siguiente comando:

pip install kivy

Descarga o clona el repositorio del proyecto.
Navega hasta la carpeta raíz del proyecto en tu terminal.
Ejecuta el archivo Main.pycon el siguiente comando:

python Main.py
Esto iniciará la aplicación y mostrará la pantalla del menú principal.
Estructura del proyecto
El proyecto sigue una estructura de Model-View-Controller (MVC), donde:

Modelo : Contiene la lógica del juego, como la colocación de barcos y el manejo de los ataques.

LogicT.py: Maneja la lógica de la inteligencia artificial (IA) y del jugador.
LogicJ.py: Maneja la lógica general del juego.


Ver : Contiene los componentes visuales de la interfaz de usuario.

Menu.py: Implemente la pantalla del menú principal.
Tablero.py: Implementa los tableros del juego para el jugador y la máquina.


Controlador : Maneja la interacción con la base de datos.

BD.py: Contiene las funciones para conectarse y realizar operaciones en la base de datos.


Main.py: Es el punto de entrada de la aplicación, donde se inicia el bucle principal de Kivy.

Cómo está creado
El programa está desarrollado utilizando el framework Kivy para Python, que permite crear aplicaciones de escritorio multiplataforma con una interfaz gráfica de usuario. La lógica del juego se divide en diferentes clases y módulos para una mejor organización y mantenibilidad del código.
La aplicación comienza con la pantalla del menú principal ( MenuScreen), donde el usuario puede elegir entre jugar, ver información sobre los desarrolladores, ver las estadísticas del juego o salir. Al seleccionar "Jugar", se muestra la pantalla del juego con los tableros del jugador y de la máquina.
La clase LogicJuegomaneja la lógica principal del juego, incluyendo la colocación de barcos y el manejo de los turnos de ataque. La clase LogicIAimplementa la inteligencia artificial que controla los ataques de la máquina, mientras que la clase LogicJugadormaneja la lógica del lado del jugador.
El programa utiliza la librería kivy.uixpara crear los componentes visuales de la interfaz, como botones, etiquetas y cuadrículas de tableros. Además, se utilizan ventanas emergentes para mostrar mensajes y notificaciones al usuario.
La conexión con la base de datos se realiza a través de la clase BDen el módulo controller.BD. Esta clase establece la conexión con la base de datos PostgreSQL alojada en Neon.tech y proporciona métodos para realizar operaciones como insertar y obtener estadísticas del juego.
