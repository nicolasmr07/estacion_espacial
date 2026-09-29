Guía de sustentación — Sistema de gestión de la Estación Espacial
Esta guía explica, punto por punto, el proyecto editable/ tal como quedó construido. No se cambia ni se mejora nada del código: solo se explica.

PARTE 1 — Visión general del proyecto
¿Qué hace el programa? Es un programa de consola (se usa escribiendo en el teclado, sin ventanas) que permite administrar las misiones de una estación espacial: registrar misiones nuevas, mostrarlas, buscarlas, cambiarles el estado, iniciarlas, finalizarlas y ver un resumen de cuántas hay en cada estado.

¿Qué problema resuelve? Sin este programa, alguien tendría que llevar el control de las misiones "a mano" (en papel o de memoria). El programa guarda las misiones en una lista dentro de la memoria del computador mientras el programa está corriendo, y ofrece un menú para interactuar con esa lista de forma ordenada.

¿Qué representa cada parte del sistema?

Una misión (Mision y sus hijas) representa una tarea espacial concreta: explorar un planeta, investigar un área científica o rescatar una tripulación.
La estación espacial (EstacionEspacial) representa el lugar que administra todas las misiones: las guarda, las busca, cambia su estado.
El menú (Menu) representa la persona que usa el teclado: pregunta opciones, lee lo que el usuario escribe y le pide a la estación que haga cosas.
Los validadores (validar_texto) representan reglas: "esto que escribiste, ¿tiene sentido o no?".
¿Cómo está dividido el proyecto? En tres carpetas de código (modelos, servicios, utils), un archivo de texto (Biblioteca.txt) y un archivo que arranca todo (main.py).

¿Por qué existen modelos, servicios y utils? Porque cada carpeta agrupa código que cumple un papel distinto dentro del programa (esto se explica a fondo en la Parte 2), y agruparlo así hace más fácil encontrar dónde está cada cosa.

¿Qué responsabilidad tiene cada carpeta?

modelos/: define qué es cada cosa (una misión, una estación, un estado). Son las "cosas" del mundo del programa.
servicios/: es el punto de acceso que usa main.py para llegar al menú.
utils/: contiene herramientas de apoyo que no son "cosas" del dominio del problema, sino ayudas técnicas (el menú de consola, las validaciones).
¿Cómo se comunican las carpetas entre sí? Mediante import. Un archivo de una carpeta escribe, por ejemplo, from modelos.estado_mision import EstadoMision, y así puede usar código que vive en otra carpeta.

¿Cuál es el punto de entrada del programa? main.py. Es el único archivo pensado para ejecutarse directamente.

¿Qué archivo se ejecuta primero? main.py. Cuando se ejecuta python main.py, Python lee ese archivo de arriba hacia abajo.

¿Cuál es el recorrido general? main.py → servicios/gestion_misiones.py → utils/menu.py (clase Menu) → modelos/estacion_espacial.py (clase EstacionEspacial) → clases de modelos/mision*.py (las misiones en sí).

Mapa conceptual (relaciones reales del código):

main.py
   │  (importa Menu)
   ▼
servicios/gestion_misiones.py
   │  (re-exporta Menu, que está definida en utils/menu.py)
   ▼
utils/menu.py  →  clase Menu
   │  (crea y usa)
   ▼
modelos/estacion_espacial.py  →  clase EstacionEspacial
   │  (guarda y usa objetos)
   ▼
modelos/mision.py  →  clase Mision (abstracta)
   │  (es la clase padre de)
   ▼
modelos/mision_exploracion.py  →  MisionExploracion
modelos/mision_investigacion.py → MisionInvestigacion
modelos/mision_rescate.py      → MisionRescate

(en paralelo, todas estas piezas usan)
modelos/estado_mision.py → EstadoMision (Enum)
utils/validaciones.py    → validar_texto() (función suelta, actualmente sin uso desde el menú)
PARTE 2 — Explicación de cada carpeta
modelos/
"Modelo" aquí significa: una representación en código de algo que existe en el problema real (una misión, una estación, un estado). Las clases que están aquí son las que definen de qué está hecho el sistema: sus datos y su comportamiento básico. Están aquí porque son el "sustantivo" del programa (la misión, la estación), no una acción de interfaz ni una herramienta genérica.

Contiene: estado_mision.py, mision.py, mision_exploracion.py, mision_investigacion.py, mision_rescate.py, estacion_espacial.py.

servicios/
"Servicio" significa: una capa que ofrece una función concreta al resto del programa, sin ser ella misma un dato del dominio. Aquí solo hay un archivo, gestion_misiones.py, que no define lógica propia: simplemente importa la clase Menu (definida realmente en utils/menu.py) y la deja disponible bajo el nombre servicios.gestion_misiones.Menu, para que main.py pueda acceder al menú "a través del servicio de gestión de misiones" en lugar de importar directamente desde utils. Es, literalmente, una puerta de acceso.

utils/
"Utils" (de utilities, utilidades) agrupa herramientas de apoyo que no son "cosas" del problema (no son una misión ni una estación), sino piezas técnicas que varias partes del programa podrían necesitar:

menu.py: contiene la clase Menu, que maneja toda la interacción por consola (imprimir opciones, leer lo que el usuario escribe, decidir qué hacer). No es un dato del dominio (no es una misión), es la interfaz de usuario.
validaciones.py: contiene validar_texto(), una función de apoyo que cualquier parte del programa podría usar para comprobar que un texto solo tenga letras y espacios.
mensajes.py: existe como parte de la estructura obligatoria del proyecto, pero no contiene código ejecutable: solo un comentario explicando por qué no se extrajeron los mensajes de print() a este archivo (hacerlo habría significado modificar la lógica original de los métodos, algo que estaba prohibido en el ejercicio). Esto es importante para la sustentación: si te preguntan "¿qué hace mensajes.py?", la respuesta correcta es "actualmente no contiene código, solo un comentario explicativo, porque no había manera de extraer los mensajes sin modificar los métodos originales".
Estos tres archivos están separados de modelos/ y servicios/ porque ninguno representa una "cosa" del problema (como sí lo hacen Mision o EstacionEspacial) ni es la puerta de entrada del servicio: son apoyos que usan otras partes del programa.

PARTE 3 — Explicación de cada archivo
modelos/estado_mision.py
Existe para: definir los únicos cuatro estados posibles de una misión.
Responsabilidad: ser el "diccionario cerrado" de estados válidos.
Importa: from enum import Enum.
Por qué ese import: porque Enum es la herramienta de Python para crear un conjunto fijo y nombrado de valores constantes.
Clases: EstadoMision.
Funciones sueltas: ninguna.
Métodos: ninguno propio (los Enum no necesitan métodos para funcionar como constantes).
Quién lo usa: modelos/mision.py, modelos/estacion_espacial.py.
Qué necesita: solo la librería estándar enum.
Entra: nada (es un archivo de definición, no recibe datos).
Sale: los cuatro valores PLANIFICADA, PREPARACION, EJECUCION, FINALIZADA, disponibles para quien los importe.
Participación: es la base de todo el manejo de estados del proyecto.
modelos/mision.py
Existe para: definir qué tienen en común TODAS las misiones, sin importar su tipo.
Responsabilidad: guardar código, nombre y estado; obligar a que toda misión concreta implemente iniciar() y finalizar().
Importa: from abc import ABC, abstractmethod y from modelos.estado_mision import EstadoMision.
Por qué esos imports: ABC/abstractmethod para declarar que Mision es una clase abstracta (no se puede usar directamente, solo a través de sus hijas); EstadoMision porque el atributo estado guarda uno de esos cuatro valores.
Clases: Mision.
Funciones sueltas: ninguna.
Métodos: __init__, get_codigo, get_nombre, get_estado, set_estado, set_codigo, set_nombre, iniciar (abstracto), finalizar (abstracto).
Quién lo usa: mision_exploracion.py, mision_investigacion.py, mision_rescate.py (heredan de Mision).
Qué necesita: estado_mision.py.
Entra: codigo y nombre (texto) al crear una misión.
Sale: objetos "misión" con comportamiento común ya definido.
Participación: es el "molde" común de toda misión del proyecto.
modelos/mision_exploracion.py
Existe para: representar una misión de exploración planetaria.
Responsabilidad: guardar el planeta a explorar y decidir qué pasa al iniciar/finalizar ese tipo específico de misión.
Importa: Mision (para heredar) y EstadoMision (para comparar y asignar estados).
Por qué esos imports: necesita ser hija de Mision y necesita comparar self.get_estado() contra los valores del Enum.
Clases: MisionExploracion.
Métodos: __init__, iniciar, finalizar.
Quién lo usa: utils/menu.py (crea objetos MisionExploracion cuando el usuario elige el tipo "exploracion").
Qué necesita: mision.py, estado_mision.py.
Entra: codigo, nombre, planeta.
Sale: un objeto listo para agregarse a la estación.
Participación: es uno de los tres "tipos concretos" de misión que el usuario puede crear desde el menú.
modelos/mision_investigacion.py
Igual estructura que el anterior, pero representa una misión de investigación científica, recibe area en vez de planeta, y su iniciar() tiene un paso intermedio (PREPARACION) antes de EJECUCION.

modelos/mision_rescate.py
Igual estructura, representa un rescate de tripulación, recibe tripulacion, y su iniciar() pasa directo de PLANIFICADA a EJECUCION (sin paso intermedio).

modelos/estacion_espacial.py
Existe para: administrar la colección completa de misiones.
Responsabilidad: guardar, agregar, mostrar, buscar, cambiar estado y resumir las misiones.
Importa: from modelos.estado_mision import EstadoMision.
Por qué: cambiar_estado() y mostrar_resumen() necesitan comparar y asignar valores del Enum.
Clases: EstacionEspacial.
Métodos: __init__, agregar_mision, mostrar_misiones, buscar_por_codigo, buscar_por_nombre, cambiar_estado, mostrar_resumen.
Quién lo usa: utils/menu.py (la clase Menu crea un objeto EstacionEspacial y llama a todos estos métodos).
Qué necesita: estado_mision.py. También recibe objetos que ya son instancias de Mision (o sus hijas), pero no necesita importar esas clases porque nunca las crea, solo las guarda y les llama métodos que ya tienen (get_codigo, get_estado, iniciar, etc.).
Entra: objetos "misión" completos, códigos (texto) para buscar.
Sale: texto impreso en consola, o el objeto misión encontrado (o None), o simplemente confirmaciones.
Participación: es el "almacén" central del programa.
servicios/gestion_misiones.py
Existe para: cumplir con la carpeta obligatoria servicios/ y ofrecer un punto de acceso a Menu.
Responsabilidad: reexportar Menu.
Importa: from utils.menu import Menu.
Por qué: porque la clase Menu en realidad está definida en utils/menu.py; este archivo solo la "trae" a este módulo.
Clases propias: ninguna (usa la de utils/menu.py).
Quién lo usa: main.py.
Qué necesita: utils/menu.py.
Entra/Sale: no procesa datos, solo conecta módulos.
Participación: es un "puente" de importación.
utils/menu.py
Existe para: ser la interfaz de consola completa del programa.
Responsabilidad: mostrar el menú, leer la opción del usuario, pedir los datos necesarios, y llamar al método correcto de EstacionEspacial o de una misión concreta.
Importa: time, EstacionEspacial, MisionExploracion, MisionInvestigacion, MisionRescate.
Por qué: time para la animación de puntos al salir; las clases de misión para poder crear objetos nuevos según lo que el usuario escoja; EstacionEspacial para tener dónde guardarlos.
Clases: Menu.
Métodos: __init__, ejecutar.
Quién lo usa: servicios/gestion_misiones.py (y, a través de él, main.py).
Qué necesita: modelos/estacion_espacial.py, modelos/mision_exploracion.py, modelos/mision_investigacion.py, modelos/mision_rescate.py.
Entra: todo lo que el usuario escribe por teclado (input()).
Sale: todo lo que se imprime en pantalla (print()).
Participación: es el "controlador" que conecta al usuario humano con el resto del sistema.
utils/validaciones.py
Existe para: ofrecer una validación de texto reutilizable.
Responsabilidad: decir si un texto contiene solo palabras alfabéticas.
Importa: nada.
Clases: ninguna.
Funciones: validar_texto(texto).
Quién lo usa: actualmente ningún otro archivo la llama (quedó conservada tal como estaba en el archivo original de Rusia, pero en el menú fusionado la validación de nombre se sigue haciendo de forma directa con .isalpha(), tal como estaba en el archivo de EEUU). Es válido mencionar esto como observación en la sustentación.
Entra: un texto.
Sale: True o False.
utils/mensajes.py
No contiene clases, funciones ni variables: solo un comentario que explica por qué se dejó vacío (ver Parte 2). Ningún otro archivo lo importa.

Biblioteca.txt
No es código Python, es un archivo de texto plano. Se explica en la Parte 22.

main.py
Existe para: ser el punto de arranque del programa.
Responsabilidad: crear el menú y ponerlo a funcionar.
Importa: from servicios.gestion_misiones import Menu.
Clases/funciones propias: ninguna.
Quién lo usa: nadie (es el archivo final, el que el usuario ejecuta).
Qué necesita: servicios/gestion_misiones.py.
Entra: nada al importarse; al ejecutarse como programa principal, arranca el bucle de consola.
Sale: el programa completo corriendo.
Participación: es la primera y última pieza del recorrido: abre el programa y, cuando Menu.ejecutar() termina (opción 0), el programa se cierra aquí.
PARTE 4 — Explicación de cada import
from abc import ABC, abstractmethod (en modelos/mision.py)
abc: es un módulo de la librería estándar de Python cuyo nombre significa Abstract Base Classes (clases base abstractas).
ABC: es una clase especial que, cuando otra clase hereda de ella (como class Mision(ABC):), convierte a esa clase en "abstracta": no se puede crear un objeto directamente de Mision.
abstractmethod: es un decorador (una etiqueta que se pone justo encima de un método con @) que marca un método como obligatorio de reescribir en cualquier clase hija.
Por qué aparecen aquí: porque el proyecto quiere impedir que alguien cree una misión "genérica" sin tipo (Mision("1", "x") directamente); toda misión debe ser de un tipo concreto (exploración, investigación o rescate), cada una con su propia forma de iniciar y finalizar.
Qué pasaría si se eliminaran: Mision dejaría de ser abstracta, se podría instanciar directamente (Mision("1","x")), y ya no habría obligación de que las clases hijas definan iniciar()/finalizar(); si una hija no los definiera, heredaría métodos vacíos que no hacen nada útil, en vez de que Python avise del error al intentar crear el objeto.
Qué depende de ellos: la clase Mision completa, y por herencia, MisionExploracion, MisionInvestigacion y MisionRescate.
from enum import Enum (en modelos/estado_mision.py)
enum: módulo estándar de Python para crear conjuntos fijos de constantes con nombre.
Enum: la clase base que se hereda para crear esos conjuntos.
Por qué aparece aquí: para que el estado de una misión solo pueda ser uno de cuatro valores exactos, y no cualquier texto escrito a mano.
Qué pasaría si se eliminara: EstadoMision no podría existir tal como está escrita, y el proyecto tendría que volver a usar textos sueltos como "Planificada" (como hacía el archivo de Rusia), perdiendo la protección contra errores de escritura (por ejemplo, escribir "Planificad" por error, que un Enum no permite).
Qué depende de él: modelos/mision.py (atributo estado), modelos/mision_exploracion.py, mision_investigacion.py, mision_rescate.py (comparan y asignan estados), modelos/estacion_espacial.py (en cambiar_estado y mostrar_resumen).
import time (en utils/menu.py)
time: módulo estándar de Python para trabajar con tiempo (pausas, medir duración, fechas, etc.).
Por qué aparece aquí: se usa time.sleep(1), que detiene la ejecución del programa durante 1 segundo, para crear el efecto visual de "Saliendo del sistema..." con puntos apareciendo uno por uno.
Qué pasaría si se eliminara: el programa seguiría funcionando igual en todo lo demás, pero al elegir la opción 0 no habría pausa ni animación: el mensaje de salida aparecería completo de inmediato.
Qué depende de él: únicamente el bloque case 0: dentro de Menu.ejecutar().
Imports entre archivos propios del proyecto
Como from modelos.mision import Mision, from modelos.estado_mision import EstadoMision, from modelos.estacion_espacial import EstacionEspacial, from utils.menu import Menu, etc. Estos no traen código de la librería estándar, sino que conectan los propios archivos del proyecto entre sí, tal como se explicó en la Parte 3.

PARTE 5 — Explicación de todas las clases
EstadoMision
Representa el estado en el que se encuentra una misión.
Existe para evitar estados escritos "a mano" y con errores.
Hereda de Enum.
Hereda de Enum porque esa es la clase de Python diseñada para crear conjuntos cerrados de constantes.
class EstadoMision(Enum): — class crea una clase nueva; EstadoMision es el nombre que le damos; (Enum) indica que hereda el comportamiento de Enum.
Mision
Representa cualquier misión, sin importar su tipo específico.
Existe para reunir en un solo lugar lo que TODA misión necesita (código, nombre, estado) y obligar a definir iniciar/finalizar.
Hereda de ABC.
Hereda de ABC para volverse abstracta: no se puede crear un objeto Mision directamente, solo a través de sus hijas.
class Mision(ABC): — Mision es la clase; (ABC) es la clase padre.
MisionExploracion(Mision)
Representa una misión de exploración a un planeta.
Existe para dar el comportamiento específico de este tipo de misión.
Hereda de Mision.
Hereda de Mision porque una exploración es un tipo de misión: tiene código, nombre y estado igual que cualquier otra, pero además tiene su propio atributo (planeta) y su propia forma de iniciar/finalizar.
class MisionExploracion(Mision):
class: palabra reservada de Python para declarar una clase nueva.
MisionExploracion: el nombre de la clase hija.
(Mision): indica que Mision es la clase padre (también llamada superclase). MisionExploracion es la clase hija (también llamada subclase).
Una clase hija recibe automáticamente todos los métodos y atributos "heredables" de la clase padre (en este caso: get_codigo, get_nombre, get_estado, set_estado, set_codigo, set_nombre, y el propio mecanismo del __init__ de Mision, al que se llama con super().__init__(...)).
MisionExploracion se relaciona con Mision heredando su estructura básica y sobrescribiendo (dando una nueva versión de) iniciar() y finalizar().
MisionInvestigacion(Mision) y MisionRescate(Mision)
Misma explicación que MisionExploracion, cambiando el atributo propio (area y tripulacion respectivamente) y la lógica interna de iniciar()/finalizar().

EstacionEspacial
Representa el lugar que administra todas las misiones.
Existe para centralizar el almacenamiento y las operaciones sobre el conjunto de misiones.
No hereda de ninguna clase escrita por nosotros (no tiene paréntesis con un nombre dentro).
class EstacionEspacial: — no tiene nada entre paréntesis porque no necesita heredar comportamiento de ninguna otra clase del proyecto: es independiente. (Técnicamente, en Python toda clase hereda de object de forma automática e invisible, pero eso no cambia su comportamiento aquí; por eso no se escribe nada.)
Menu
Representa la interacción por consola con el usuario.
Existe para separar "hablar con el usuario" de "administrar las misiones" (esa parte la delega a EstacionEspacial).
No hereda de ninguna clase propia del proyecto, igual que EstacionEspacial.
PARTE 6 — Atributos
Mision.__codigo, Mision.__nombre, Mision.__estado
Representan: el código identificador, el nombre y el estado actual de cualquier misión.
Dónde se crean: dentro de Mision.__init__.
Qué valor pueden contener: __codigo y __nombre contienen texto (str); __estado contiene siempre uno de los cuatro valores de EstadoMision.
Cuándo reciben su valor: en el momento en que se crea el objeto (por ejemplo, MisionExploracion("1", "Marte Uno", "Marte")), __codigo y __nombre reciben lo que se pasó; __estado siempre arranca en EstadoMision.PLANIFICADA sin que nadie lo pida explícitamente.
Quién los modifica: set_estado() modifica __estado; set_codigo() y set_nombre() modifican __codigo/__nombre (si el nuevo valor pasa la validación).
Quién los utiliza: get_codigo(), get_nombre(), get_estado(), y por dentro, todos los métodos iniciar()/finalizar() de las subclases (a través de esos métodos get_).
Qué ocurriría si no existieran: no habría forma de identificar una misión (__codigo), de mostrar su nombre (__nombre), ni de saber en qué fase está (__estado); el programa no podría hacer casi nada de lo que hace.
Por qué llevan doble guion bajo (__): esto activa el encapsulamiento en Python (llamado name mangling): el atributo queda "escondido" bajo un nombre interno distinto (_Mision__codigo), de modo que no se puede acceder a él directamente desde fuera de la clase escribiendo mision.__codigo; hay que usar mision.get_codigo(). Esto obliga a pasar siempre por los métodos definidos, que pueden incluir validaciones.
Código real
self.__codigo = codigo.strip()
Explicación
self es el objeto que se está construyendo en ese momento (ver Parte 9).
self.__codigo es el atributo que va a vivir dentro de ese objeto.
codigo (sin self.) es el parámetro que llegó al método, es decir, el valor que alguien pasó al crear la misión.
.strip() es un método de los textos en Python que elimina espacios en blanco sobrantes al principio y al final del texto.
= guarda, del lado derecho hacia el lado izquierdo, el resultado en el atributo.
Aparecen "dos nombres iguales" (codigo y codigo) porque uno es el parámetro (una variable temporal que solo existe mientras se ejecuta el método) y el otro es el atributo (self.__codigo, que sí queda guardado en el objeto para siempre). Que se llamen parecido es solo una convención de quien escribió el código, para que sea fácil de leer; Python los trata como cosas completamente distintas porque uno tiene self. (y además el prefijo __) y el otro no.
planeta (en MisionExploracion), area (en MisionInvestigacion), tripulacion (en MisionRescate)
Representan: el dato específico que solo tiene sentido para ese tipo de misión.
Dónde se crean: en el __init__ de cada subclase respectiva.
Qué valor pueden contener: texto libre, lo que el usuario haya escrito.
Cuándo reciben su valor: al crear el objeto.
Quién los modifica: nadie después de la creación (no existe un set_planeta(), por ejemplo); se usan tal como se recibieron.
Quién los usa: los propios métodos iniciar()/finalizar() de esa misma clase, para armar el mensaje impreso.
Qué ocurriría si no existieran: los mensajes de iniciar()/ finalizar() no podrían decir en qué planeta, área o con qué tripulación se trabaja.
Nótese que estos atributos no llevan doble guion bajo (no son self.__planeta), así que si se quisiera, se podría acceder desde fuera con objeto.planeta directamente; no están tan protegidos como __codigo.
EstacionEspacial.misiones
Representa: la colección completa de misiones registradas.
Dónde se crea: en EstacionEspacial.__init__, como una lista vacía [].
Qué valor puede contener: una lista de objetos Mision (en la práctica, objetos de sus hijas concretas).
Cuándo recibe valores: cada vez que se llama a agregar_mision() y la validación pasa, se le añade un elemento con .append().
Quién lo modifica: agregar_mision().
Quién lo utiliza: mostrar_misiones(), buscar_por_codigo(), buscar_por_nombre(), mostrar_resumen(), y también utils/menu.py (que puede recorrerla, aunque en la versión actual el menú usa buscar_por_codigo() en vez de recorrerla directamente).
Qué ocurriría si no existiera: no habría dónde guardar las misiones; cada una desaparecería apenas terminara de crearse.
Menu.estacion
Representa: la estación espacial que administra ese menú en particular.
Dónde se crea: en Menu.__init__.
Valor: siempre un objeto EstacionEspacial recién creado.
Quién lo usa: prácticamente todo Menu.ejecutar(), para delegarle el trabajo real (self.estacion.agregar_mision(...), etc.).
PARTE 7 — Constructores __init__
¿Qué es __init__? Es un método especial de Python (reconocible porque su nombre empieza y termina en doble guion bajo) que se ejecuta automáticamente cada vez que se crea un objeto nuevo de esa clase. Su trabajo es dejar el objeto "listo para usarse", normalmente guardando los datos iniciales en sus atributos.

¿Cuándo se ejecuta? En el mismo instante en que se escribe, por ejemplo, MisionExploracion("1", "Marte Uno", "Marte"). No hay que llamarlo a mano.

¿Quién lo ejecuta? Python lo ejecuta internamente al procesar la instrucción de creación del objeto.

¿Qué significa self? Es el propio objeto que se está creando en ese momento (ver Parte 9 para más detalle).

Mision.__init__(self, codigo, nombre)
Parámetros que recibe: codigo, nombre (además de self, que Python pasa solo).
Atributos que crea: __codigo, __nombre, __estado.
Valores que guarda: codigo.strip(), nombre.strip(), y siempre EstadoMision.PLANIFICADA como estado inicial.
MisionExploracion.__init__(self, codigo, nombre, planeta)
Parámetros: codigo, nombre, planeta.
Primero ejecuta super().__init__(codigo, nombre): esto llama al __init__ de la clase padre (Mision), para que se hagan las mismas tareas comunes (guardar código, nombre, poner estado en PLANIFICADA).
Después guarda self.planeta = planeta, el atributo propio de esta subclase.
MisionInvestigacion.__init__ y MisionRescate.__init__ funcionan igual, cambiando el último parámetro (area, tripulacion) y el atributo que guardan.

EstacionEspacial.__init__(self)
No recibe parámetros propios (solo self).
Crea el atributo self.misiones = [], una lista vacía.
Menu.__init__(self)
No recibe parámetros propios.
Crea self.estacion = EstacionEspacial(): es decir, dentro del __init__ de Menu se crea un objeto de otra clase (EstacionEspacial), lo cual dispara automáticamente el __init__ de EstacionEspacial también.
Ejemplo real paso a paso
mision = MisionExploracion("007", "Amanecer Rojo", "Marte")
Python ve que se está pidiendo crear un objeto de MisionExploracion.
Reserva espacio en memoria para un objeto nuevo; ese futuro objeto será self dentro del __init__.
Ejecuta MisionExploracion.__init__(self, "007", "Amanecer Rojo", "Marte").
Dentro, super().__init__("007", "Amanecer Rojo") ejecuta Mision.__init__: guarda self.__codigo = "007", self.__nombre = "Amanecer Rojo", self.__estado = EstadoMision.PLANIFICADA.
De vuelta en MisionExploracion.__init__, se guarda self.planeta = "Marte".
El __init__ termina (no tiene return explícito, y no necesita tenerlo).
La variable mision, fuera de la clase, queda apuntando a ese objeto ya completamente armado, con sus 4 atributos listos: __codigo="007", __nombre="Amanecer Rojo", __estado=EstadoMision.PLANIFICADA, planeta="Marte".
PARTE 8 — Métodos (uno por uno)
Mision.get_codigo(self)
Devuelve el código de la misión.
Lo llama cualquier código externo que necesite leer el código (por ejemplo, EstacionEspacial.mostrar_misiones).
Se ejecuta cada vez que se escribe objeto.get_codigo().
Parámetros: solo self.
self = el objeto sobre el que se llama.
Usa internamente: self.__codigo.
No modifica ningún atributo.
No llama a otros métodos.
Devuelve: el texto guardado en __codigo.
Al ejecutarse: simplemente entrega el valor, sin efectos secundarios.
Si no se ejecutara: nadie fuera de la clase podría leer el código (recordemos que __codigo está "escondido" por el doble guion bajo).
El resultado se usa, por ejemplo, dentro de EstacionEspacial.agregar_mision para comparar códigos y evitar duplicados.
def get_codigo(self):
    return self.__codigo
def declara un método/función.
get_codigo(self): nombre del método; recibe self porque necesita saber de qué objeto en particular debe leer el código.
return entrega el valor a quien llamó al método, terminando la ejecución del método en ese punto.
Mision.get_nombre(self) / get_estado(self)
Misma lógica que get_codigo, pero devolviendo __nombre o __estado respectivamente. get_estado() devuelve un valor de tipo EstadoMision (no un texto plano), por eso en otros lugares se ve mision.get_estado().value para obtener el texto legible (por ejemplo, "Planificada").

Mision.set_estado(self, estado)
Cambia el estado de la misión.
Lo llaman los métodos iniciar()/finalizar() de cada subclase, y EstacionEspacial.cambiar_estado().
Se ejecuta cuando la misión avanza de fase.
Parámetro: estado, se espera que sea un valor de EstadoMision.
estado: EstadoMision es una anotación de tipo: es solo información para quien lee el código (y para herramientas), Python no obliga a respetarla en tiempo de ejecución.
Usa: nada más que el parámetro recibido.
Modifica: self.__estado.
No llama a otros métodos.
No devuelve nada (devuelve None implícitamente).
Al ejecutarse: el estado queda actualizado.
Si no se ejecutara: la misión se quedaría congelada en su estado anterior para siempre.
El nuevo valor se lee después con get_estado().
Mision.set_codigo(self, codigo)
Cambia el código de la misión, solo si es válido.
Lo llamaría cualquier código que quiera corregir un código ya asignado (en el menú actual no se usa, pero queda disponible en la clase).
Parámetro: codigo (texto).
Usa: codigo.isdigit() (comprueba si el texto son solo dígitos).
Modifica: self.__codigo, solo dentro del if.
No llama a otros métodos.
No devuelve nada; si la validación falla, imprime un mensaje de error.
Si el dato es correcto: se guarda el nuevo código.
Si es incorrecto: se imprime "El código debe contener únicamente números." y el código anterior no cambia.
Mision.set_nombre(self, nombre)
Cambia el nombre, solo si contiene únicamente letras y espacios.
Usa un bucle for para revisar palabra por palabra (se explica en la Parte 17) y una bandera valido (booleano) que empieza en True y pasa a False en cuanto encuentra una palabra no alfabética.
Si valido sigue True y hay al menos una palabra, guarda el nuevo nombre; si no, imprime el mensaje de error y deja el nombre anterior.
Mision.iniciar(self) / Mision.finalizar(self) (abstractos)
No tienen cuerpo real (pass), son solo una "promesa" de que toda subclase concreta debe definir su propia versión.
Nunca se ejecutan directamente desde Mision, porque no se puede crear un objeto Mision puro.
Se explican a fondo en la Parte 12 (Clases abstractas).
MisionExploracion.iniciar(self)
Cambia el estado de una exploración de PLANIFICADA a EJECUCION e imprime un mensaje.
Lo llama quien tenga un objeto MisionExploracion y quiera iniciarlo (en este proyecto, Menu.ejecutar(), opción 6).
Parámetros: solo self.
Usa: self.get_estado(), self.set_estado(), self.planeta, self.get_nombre().
Modifica: __estado (indirectamente, a través de set_estado).
Condición: si el estado actual es PLANIFICADA, cambia a EJECUCION y muestra "🚀 Exploración iniciada en {planeta}: {nombre}"; si no, muestra una advertencia y no cambia nada.
No devuelve nada.
Si no se ejecutara nunca, la misión se quedaría siempre en PLANIFICADA.
def iniciar(self):
    if self.get_estado() == EstadoMision.PLANIFICADA:
        self.set_estado(EstadoMision.EJECUCION)
        print(f"🚀 Exploración iniciada en {self.planeta}: {self.get_nombre()}")
    else:
        print("⚠️ No se puede iniciar esta misión.")
if self.get_estado() == EstadoMision.PLANIFICADA: pregunta: "¿el estado actual es exactamente PLANIFICADA?".
Si es verdad, entra al bloque: cambia el estado y lo anuncia.
f"..." es un f-string: un texto que permite insertar valores de variables directamente con {}.
else: cubre cualquier otro caso (ya está en ejecución, ya terminó, etc.): no se puede volver a iniciar, así que solo avisa.
MisionExploracion.finalizar(self)
Misma lógica que iniciar(), pero revisa que el estado sea EJECUCION para pasar a FINALIZADA.

MisionInvestigacion.iniciar(self)
A diferencia de exploración, tiene dos pasos: si está PLANIFICADA pasa a PREPARACION; si ya estaba en PREPARACION, pasa a EJECUCION.
Esto significa que hay que llamar iniciar() dos veces seguidas para que una investigación llegue realmente a ejecutarse.
Si el estado es cualquier otro, muestra advertencia.
MisionInvestigacion.finalizar(self)
Igual patrón que MisionExploracion.finalizar, pero con los mensajes propios de investigación.

MisionRescate.iniciar(self) / finalizar(self)
Mismo patrón simple que MisionExploracion (un solo paso de PLANIFICADA→EJECUCION y de EJECUCION→FINALIZADA), con sus mensajes propios de rescate.

EstacionEspacial.agregar_mision(self, mision)
Registra una misión nueva, evitando códigos repetidos.
La llama Menu.ejecutar() (opción 1), después de crear el objeto misión.
Parámetro: mision, un objeto de alguna subclase de Mision.
Usa: any(...), una función de Python que revisa si al menos una condición dentro de una lista de comprobaciones es verdadera; aquí, recorre self.misiones comparando cada código existente con el código de la misión nueva.
Modifica: self.misiones (le agrega un elemento con .append()), solo si no hay duplicado.
Llama a: get_codigo() de cada misión guardada y de la nueva.
No devuelve nada; imprime un mensaje de éxito o de advertencia.
Si el código ya existe: imprime "⚠️ Ya existe una misión con ese código." y no agrega la misión.
Si no existe: la agrega y avisa "✅ Misión agregada correctamente."
def agregar_mision(self, mision):
    if any(m.get_codigo() == mision.get_codigo() for m in self.misiones):
        print("⚠️ Ya existe una misión con ese código.")
    else:
        self.misiones.append(mision)
        print("✅ Misión agregada correctamente.")
any(m.get_codigo() == mision.get_codigo() for m in self.misiones) es una expresión generadora: recorre cada m (cada misión ya guardada) y produce True/False según si su código coincide con el de la misión nueva; any(...) devuelve True en cuanto encuentra una sola coincidencia.
Si hay coincidencia, se rechaza el registro.
Si no, self.misiones.append(mision) agrega el objeto al final de la lista.
EstacionEspacial.mostrar_misiones(self)
Imprime todas las misiones registradas, numeradas.
La llama Menu.ejecutar() (opción 2).
Sin parámetros propios.
Usa: enumerate(self.misiones, start=1), que recorre la lista entregando, en cada vuelta, tanto la posición (empezando en 1) como el objeto misión.
No modifica nada, solo lee e imprime.
Si la lista está vacía: imprime "No hay misiones registradas."
Si tiene elementos: imprime una línea por cada una con código, nombre y get_estado().value (el texto legible del Enum, como "Planificada").
EstacionEspacial.buscar_por_codigo(self, codigo)
Busca y devuelve la misión cuyo código coincide exactamente.
La llama Menu.ejecutar() (opciones 3, 4, 6 y 7) y también cambiar_estado() (dentro de la misma clase).
Parámetro: codigo (texto a buscar).
Usa un bucle for que revisa una por una las misiones guardadas.
break corta el bucle apenas encuentra la coincidencia (no sigue revisando el resto, ya no hace falta).
Devuelve: el objeto misión encontrado, o None si no se encontró ninguna coincidencia (la variable encontrada nunca cambió de None).
Quien recibe el resultado siempre debe comprobar si es None antes de usarlo (y así se hace en todos los lugares donde se llama).
EstacionEspacial.buscar_por_nombre(self, nombre)
Igual estructura que buscar_por_codigo, pero compara mision.get_nombre().lower() == nombre.lower(): .lower() convierte todo a minúsculas antes de comparar, para que la búsqueda no distinga entre mayúsculas y minúsculas (por ejemplo, "Marte Uno" y "marte uno" se consideran iguales).

EstacionEspacial.cambiar_estado(self, codigo)
Permite escoger, desde un submenú, el nuevo estado de una misión ya registrada.
La llama Menu.ejecutar() (opción 4).
Parámetro: codigo, para localizar la misión con buscar_por_codigo.
Si no la encuentra, avisa y termina el método ahí mismo con return (sin seguir mostrando el submenú).
Si la encuentra, imprime 4 opciones de estado y lee la elección con input().
Usa match int(opcion): (una estructura de selección múltiple parecida a un switch de otros lenguajes) para decidir qué constante de EstadoMision asignar según el número elegido.
Modifica el estado de la misión encontrada a través de set_estado().
Si la opción no es un número o no está entre 1 y 4, avisa "Opción inválida." o "Debe ingresar un número." según el caso, sin cambiar nada.
EstacionEspacial.mostrar_resumen(self)
Cuenta cuántas misiones hay en cada estado y el total.
La llama Menu.ejecutar() (opción 5).
Usa 5 variables contadoras (total, planificadas, preparacion, ejecucion, finalizadas), todas inicializadas en 0.
Recorre self.misiones con un for, sumando 1 a total en cada vuelta, y usando if/elif para saber a cuál contador sumarle 1 según el estado de esa misión.
No modifica ninguna misión, solo lee sus estados.
Al final, imprime los 5 números en un bloque con separadores de texto.
Menu.ejecutar(self)
Es el corazón del programa: muestra el menú en un bucle infinito hasta que el usuario elige salir.
La llama main.py (a través del objeto menu creado ahí).
Sin parámetros propios.
Usa while True: (bucle infinito, ver Parte 17), input() para leer al usuario, y match int(opcion): para decidir qué hacer según el número elegido.
Según la opción, llama a métodos de self.estacion (la EstacionEspacial) o a iniciar()/finalizar() de una misión concreta encontrada con buscar_por_codigo().
El bucle termina únicamente con la instrucción break dentro de case 0:.
No devuelve nada (no tiene sentido devolver algo de un bucle de interfaz de usuario que corre indefinidamente).
PARTE 9 — self
¿Qué es self? Es el nombre (por convención, no una palabra reservada obligatoria, pero todo el mundo lo usa así) que recibe, dentro de un método, el objeto concreto sobre el que se está llamando ese método. Cuando se escribe mision.iniciar(), Python automáticamente pasa mision como el primer argumento del método iniciar, y ese argumento se recibe con el nombre self.

¿Por qué aparece en los métodos? Porque un método necesita saber de cuál objeto específico debe leer o modificar los atributos. Sin self, el método no tendría forma de distinguir, por ejemplo, entre la misión "Marte Uno" y la misión "Bio Lab": ambas comparten el mismo código (iniciar()), pero cada una tiene sus propios datos guardados en su propio self.

¿Por qué aparece antes de los atributos (self.algo)? Porque así se le dice a Python: "este algo no es una variable suelta y temporal, es un dato que pertenece a este objeto y debe seguir existiendo después de que el método termine".

Diferencia entre self.nombre y nombre:

nombre (sin self.) es, casi siempre, un parámetro o una variable local: existe solo mientras se ejecuta ese método y luego desaparece.
self.nombre (o self.__nombre, con encapsulamiento) es un atributo: vive dentro del objeto y sigue existiendo mientras el objeto exista.
¿Qué pasaría si se eliminara self? El método dejaría de tener forma de saber sobre qué objeto trabajar. De hecho, Python daría un error, porque cuando se llama mision.iniciar(), Python siempre intenta pasar el objeto como primer argumento; si el método está definido como def iniciar(): (sin parámetro para recibirlo), ocurre un error de tipo "se pasó un argumento de más".

Ejemplo real:

mision1 = MisionExploracion("1", "Marte Uno", "Marte")
mision2 = MisionExploracion("2", "Luna Base", "Luna")
mision1.iniciar()
Aquí, dentro de iniciar(), self es mision1, así que self.get_nombre() devuelve "Marte Uno" y self.planeta es "Marte". Si en cambio se llamara mision2.iniciar(), self sería mision2, y los mismos self.get_nombre()/self.planeta devolverían "Luna Base"/"Luna". El código del método iniciar() es exactamente el mismo en ambos casos; lo único que cambia es a qué objeto apunta self.

PARTE 10 — Herencia
Esquema real de herencia del proyecto
Mision (clase abstracta, hereda de ABC)
├── MisionExploracion
├── MisionInvestigacion
└── MisionRescate
(EstadoMision hereda de Enum, pero no forma parte de esta jerarquía de misiones; EstacionEspacial y Menu no heredan de ninguna clase propia del proyecto.)

Mision (padre) → MisionExploracion, MisionInvestigacion, MisionRescate (hijas)
Qué heredan: los métodos get_codigo, get_nombre, get_estado, set_estado, set_codigo, set_nombre, y el mecanismo del __init__ (que llaman con super().__init__(...)).
Qué atributos pueden usar: pueden leer y modificar __codigo, __nombre, __estado únicamente a través de los métodos heredados (get_..., set_...), no accediendo directamente por el doble guion bajo, debido al encapsulamiento.
Qué métodos sobrescriben: iniciar() y finalizar(). En Mision estos métodos son abstractos (sin lógica real); cada hija da su propia versión completa.
Por qué está construido así: porque las tres clases comparten comportamiento común (código, nombre, estado) pero se comportan distinto al iniciar y finalizar, y cada una necesita un dato extra propio (planeta, área, tripulación). La herencia evita repetir tres veces el código de get_codigo, get_nombre, etc.
EstadoMision (hija) ← Enum (padre)
Hereda de Enum el comportamiento que permite que EstadoMision.PLANIFICADA sea una constante única, comparable con ==, y con un atributo .value que da su texto asociado ("Planificada").
PARTE 11 — Polimorfismo
¿El proyecto usa polimorfismo? Sí.

¿Dónde ocurre, exactamente? En EstacionEspacial.mostrar_misiones():

for i, m in enumerate(self.misiones, start=1):
    print(f"{i}. Código: {m.get_codigo()}, Nombre: {m.get_nombre()}, Estado: {m.get_estado().value}")
La lista self.misiones puede contener, al mismo tiempo, objetos MisionExploracion, MisionInvestigacion y MisionRescate. El código de este método no sabe ni le importa de qué tipo concreto es cada m: solo sabe que, sea cual sea su tipo, todos entienden get_codigo(), get_nombre() y get_estado() (porque los heredan de Mision). Esto es polimorfismo: un mismo código (m.get_codigo()) se comporta correctamente sin importar la clase exacta del objeto, porque todas las clases hijas comparten esa "forma" (esa interfaz) heredada del padre.

También ocurre en Menu.ejecutar(), en las opciones 6 y 7:

mision = self.estacion.buscar_por_codigo(codigo)
if mision:
    mision.iniciar()
Aquí mision puede terminar siendo cualquiera de las tres subclases, y mision.iniciar() ejecutará automáticamente la versión correcta de iniciar() según el tipo real del objeto (la de exploración, la de investigación o la de rescate), sin que el código del menú tenga que preguntar "¿de qué tipo eres?" con if.

¿Qué pasaría si el objeto fuera de otra clase hija? Si mision fuera un objeto MisionRescate en vez de MisionExploracion, la misma línea mision.iniciar() ejecutaría el iniciar() escrito dentro de MisionRescate (mensaje "🆘 Rescate en curso..."), en lugar del de MisionExploracion ("🚀 Exploración iniciada..."). El código que llama (Menu.ejecutar) no necesita cambiar en absoluto para que esto funcione.

PARTE 12 — Clases abstractas
¿Qué es una clase abstracta? Una clase que define una estructura común (atributos y algunos métodos), pero que no se puede usar para crear objetos directamente; solo sirve como "plantilla" para que otras clases hereden de ella.
¿Por qué se usa aquí? Porque no tiene sentido que exista una "misión" sin tipo específico: toda misión real del proyecto debe ser de exploración, investigación o rescate. Mision solo existe para que esas tres compartan código en común.
¿Qué significa @abstractmethod? Es un decorador que se coloca justo encima de la definición de un método dentro de una clase que hereda de ABC. Marca ese método como obligatorio de reescribir en cualquier clase hija que se quiera poder instanciar.
¿Por qué un método puede existir "sin implementación completa"? Porque su único propósito en la clase padre es anunciar que ese método debe existir, dejando el "cómo" (la implementación real) a cada hija, ya que cada una lo hace distinto (como se ve en iniciar() de cada subclase).
¿Qué significa implementarlo en una hija? Escribir, dentro de la clase hija, un método con exactamente el mismo nombre (iniciar, finalizar) que sí tenga código real, como hacen MisionExploracion.iniciar(), etc.
¿Qué ocurre si una hija no lo implementa? Python no dejaría crear objetos de esa hija: lanzaría un error indicando que la clase sigue siendo abstracta porque le falta implementar ese método.
¿Por qué tiene sentido en este proyecto? Porque garantiza, desde el diseño, que toda misión concreta que exista en el programa obligatoriamente sepa iniciarse y finalizarse a su manera, sin que se pueda "olvidar" al crear un nuevo tipo de misión en el futuro.
PARTE 13 — Enum
¿Qué es un Enum? Una forma de agrupar un conjunto fijo y con nombre de valores constantes relacionados entre sí.
¿Para qué sirve? Para representar "una opción entre varias conocidas de antemano", evitando escribir ese valor como texto libre en distintas partes del código.
¿Por qué se usa aquí? Porque una misión solo puede estar en uno de cuatro estados posibles, ni uno más ni uno menos, y queremos que Python ayude a evitar errores de escritura.
¿Qué representa cada valor?
PLANIFICADA = "Planificada": la misión existe pero no ha comenzado.
PREPARACION = "En preparación": paso intermedio (solo lo usa MisionInvestigacion).
EJECUCION = "En ejecución": la misión está en curso.
FINALIZADA = "Finalizada": la misión ya terminó.
¿Cómo se usa después? Comparando con == (por ejemplo, self.get_estado() == EstadoMision.PLANIFICADA), asignando con set_estado(EstadoMision.EJECUCION), o leyendo su texto legible con .value (por ejemplo, mision.get_estado().value da "Planificada", no EstadoMision.PLANIFICADA).
Diferencia entre Enum y usar strings sueltos: con strings sueltos (como hacía el archivo de Rusia, self.__estado = "Planificada"), nada impide escribir por error "Planficada" en algún lugar del código, y esa comparación simplemente fallaría en silencio (la condición daría False sin avisar del error de tipeo). Con Enum, si se escribe mal EstadoMision.PLANIFICAD, Python da un error inmediato porque ese nombre no existe en la clase, ayudando a detectar el error mucho antes.
PARTE 14 — Funciones (que no son métodos de una clase)
validar_texto(texto) (en utils/validaciones.py)
Qué hace: revisa que un texto contenga solo palabras compuestas únicamente por letras (usando .isalpha() en cada palabra separada por espacios), y que no esté vacío.
Quién la llama: en la versión actual del proyecto, ningún otro archivo la invoca (ver la observación en la Parte 3 sobre validaciones.py); existe conservada tal como estaba en el archivo original.
Parámetros: texto (una cadena de texto).
Qué devuelve: True si todas las palabras son alfabéticas y hay al menos una palabra; False en caso contrario (incluyendo el caso de texto vacío).
Para qué se necesita: es una utilidad de validación reutilizable, pensada para confirmar que un dato de texto (como un nombre) no contenga números ni símbolos.
Qué pasaría si no existiera: no cambiaría el comportamiento actual del menú (porque no se está llamando desde ahí), pero se perdería una herramienta de validación ya disponible para usarse en el futuro.
No existen más funciones sueltas en el proyecto: todo lo demás está definido como métodos dentro de una clase.

PARTE 15 — Validaciones
En Mision.set_codigo
Comprueba: que el nuevo código propuesto sea solo dígitos (codigo.isdigit()).
Por qué existe: para que un código de misión nunca contenga letras o símbolos.
Recibe: un texto.
Si es correcto: se guarda como nuevo código.
Si es incorrecto: se imprime un mensaje de error y no se cambia nada.
Devuelve: nada explícitamente (no hay return).
Quién usa el resultado: nadie recoge un valor de retorno; el "efecto" es el cambio (o no) del atributo y el mensaje impreso.
En Mision.set_nombre
Comprueba: que, separando el texto por espacios, cada palabra sea completamente alfabética (palabra.isalpha()), y que haya al menos una palabra.
Por qué existe: para evitar nombres con números o símbolos.
Recibe: un texto (posiblemente con varias palabras).
Si es correcto: reemplaza __nombre.
Si es incorrecto: imprime el mensaje de error, sin cambiar nada.
En Menu.ejecutar, opción 1 (registrar misión)
if not nombre.replace(" ", "").isalpha(): comprueba que el nombre, al quitarle todos los espacios, sea puramente alfabético. Si falla, avisa y usa continue para volver al inicio del bucle while (mostrar el menú de nuevo) sin seguir pidiendo más datos.
if not codigo.isdigit(): comprueba que el código sean solo dígitos.
Si el tipo escrito no es "exploracion", "investigacion" ni "rescate", se avisa "Tipo inválido." y también se usa continue.
En Menu.ejecutar y en EstacionEspacial.cambiar_estado, al leer opciones numéricas
if not opcion.isdigit(): comprueba que lo escrito sea un número antes de convertirlo con int(opcion). Esto evita que el programa se caiga con un error si el usuario escribe letras donde se espera un número.
En EstacionEspacial.agregar_mision
La validación de duplicados (any(...), explicada en la Parte 8) es también una validación: comprueba que el nuevo código no repita uno ya existente antes de permitir el registro.
Nota sobre try/except/isinstance: el proyecto no utiliza try/except ni isinstance en ningún archivo. Todas las validaciones se hacen con if y métodos de texto (isdigit(), isalpha()).

PARTE 16 — Condicionales importantes
if not opcion.isdigit(): (en varios lugares): si lo escrito no es un número, avisa y no continúa procesando esa opción.
if self.get_estado() == EstadoMision.PLANIFICADA: (en iniciar() de cada subclase): decide si la misión puede pasar a ejecución según su estado actual; si es falso, no se permite iniciar de nuevo una misión que ya está en curso o terminada.
if self.get_estado() == EstadoMision.EJECUCION: (en finalizar()): solo se puede finalizar una misión que esté actualmente en ejecución.
if tipo == "exploracion": ... elif tipo == "investigacion": ... elif tipo == "rescate": ... else: ... (en Menu, opción 1): decide qué clase concreta crear según lo que el usuario escribió; el else cubre cualquier texto no reconocido.
if any(m.get_codigo() == mision.get_codigo() for m in self.misiones): ... else: ... (en agregar_mision): decide si rechazar o aceptar el registro según si el código ya existe.
if mision is None: ... return (en cambiar_estado y en varios lugares de Menu): si la búsqueda no encontró nada, se corta la operación antes de intentar usar algo que no existe.
PARTE 17 — Bucles
for m in self.misiones for ... (dentro de any(...)) en agregar_mision
Recorre cada misión ya guardada (m) comparándola con la nueva.
Termina en cuanto any encuentra una coincidencia, o al terminar de revisar toda la lista si no encuentra ninguna.
for i, m in enumerate(self.misiones, start=1): en mostrar_misiones
self.misiones es la lista completa de misiones.
m es, en cada vuelta, una misión de esa lista.
i es la posición de esa misión, empezando en 1 (gracias a start=1).
Se ejecuta tantas veces como misiones haya en la lista; si la lista está vacía, el for simplemente no ejecuta ninguna vuelta (por eso existe el if not self.misiones: antes, para el caso de lista vacía).
En cada vuelta: se imprime una línea con esa misión.
for mision in self.misiones: en buscar_por_codigo, buscar_por_nombre, mostrar_resumen
self.misiones es de dónde sale cada mision.
mision, en cada vuelta, es un objeto distinto de la lista.
En buscar_por_codigo/buscar_por_nombre: en cada vuelta se compara el dato buscado; si coincide, se guarda en encontrada y se corta el bucle con break (ya no hace falta seguir revisando).
En mostrar_resumen: en cada vuelta se suma 1 a total y se revisa a cuál contador de estado sumarle 1; no hay break, porque hay que recorrer todas las misiones para contar bien.
for palabra in palabras: en Mision.set_nombre y en validar_texto
palabras es el resultado de texto.split() (o nombre.split()): una lista con cada palabra separada por espacios.
palabra es, en cada vuelta, una de esas palabras individuales.
Se corta con break apenas se encuentra una palabra no alfabética, porque ya no hace falta seguir revisando: el resultado final ya está decidido (valido = False).
for _ in range(3): en Menu.ejecutar, opción de salir
range(3) genera 3 vueltas.
Se usa _ como nombre de variable porque no importa su valor (no se usa dentro del bucle); es una convención de Python para decir "esta variable no se va a usar, solo necesito repetir algo N veces".
En cada vuelta: espera 1 segundo (time.sleep(1)) e imprime un punto ("."), logrando el efecto de "...".
while True: en Menu.ejecutar
Es un bucle que, literalmente, nunca deja de repetirse por sí solo (True siempre es verdadero).
La única forma de salir es la instrucción break dentro de case 0:.
En cada vuelta: se muestra el menú completo, se lee una opción, y se ejecuta la acción correspondiente.
PARTE 18 — Estructuras de datos utilizadas
Listas: self.misiones en EstacionEspacial (contiene objetos Mision); palabras dentro de set_nombre/validar_texto (contiene texto, resultado de .split()).
Se modifica con .append(mision) (agrega al final).
Se consulta recorriéndola con for, o con enumerate() para tener también la posición.
Strings (texto): codigo, nombre, planeta, area, tripulacion, y todo lo que se lee con input().
Se consultan con métodos como .isdigit(), .isalpha(), .strip(), .lower(), .split(), .replace().
Números enteros (int): i en enumerate, los contadores de mostrar_resumen (total, planificadas, etc.), y el resultado de int(opcion) al convertir la opción del menú.
Booleanos (True/False): la bandera valido en set_nombre y validar_texto; el resultado implícito de comparaciones como mision.get_estado() == EstadoMision.PLANIFICADA; la condición del while True.
Enum: EstadoMision, ya explicado en la Parte 13.
Objetos: cada misión (MisionExploracion, etc.), cada EstacionEspacial, cada Menu, son objetos: instancias concretas de una clase, con sus propios atributos guardados en memoria.
None: valor especial de Python que representa "nada" o "ningún valor". Aparece como resultado posible de buscar_por_codigo() y buscar_por_nombre() cuando no se encuentra ninguna coincidencia (la variable encontrada se inicializa en None y solo cambia si se halla algo).
Diccionarios: el proyecto no utiliza diccionarios (dict) en ningún archivo.
PARTE 19 — Flujo completo del programa (ejemplo real)
Vamos a seguir el recorrido completo registrando una misión de exploración y luego iniciándola.

Se ejecuta python main.py. Python empieza a leer main.py de arriba hacia abajo.
main.py ejecuta from servicios.gestion_misiones import Menu: esto hace que Python abra servicios/gestion_misiones.py, el cual a su vez ejecuta from utils.menu import Menu, abriendo utils/menu.py (que importa time y las clases de misión y EstacionEspacial).
Como __name__ == "__main__" es verdadero (porque main.py es el archivo que se ejecutó directamente), se ejecuta menu = Menu().
Se crea un objeto Menu; dentro de su __init__, se crea también un objeto EstacionEspacial (self.estacion = EstacionEspacial()), cuyo propio __init__ deja self.misiones = [].
Se ejecuta menu.ejecutar(). Entra al while True: y muestra el menú con las 8 opciones.
El usuario escribe 1 (agregar misión). Python lee opcion = "1", pasa la validación isdigit(), y entra a case 1:.
El programa pide nombre, código y tipo por consola. Supongamos que el usuario escribe: nombre "Amanecer Rojo", código "7", tipo "exploracion", y planeta "Marte".
Cada dato pasa su validación (isalpha() en el nombre, isdigit() en el código).
Como tipo == "exploracion", se ejecuta mision = MisionExploracion("7", "Amanecer Rojo", "Marte"). Esto dispara el __init__ explicado en la Parte 7: queda un objeto con __codigo="7", __nombre="Amanecer Rojo", __estado=EstadoMision.PLANIFICADA, planeta="Marte".
Se llama self.estacion.agregar_mision(mision). Dentro, EstacionEspacial revisa que no haya otra misión con código "7" (la lista está vacía, así que no hay duplicado), agrega el objeto a self.misiones, e imprime "✅ Misión agregada correctamente."
El while True: vuelve a mostrar el menú. El usuario ahora escribe 6 (iniciar misión) y luego el código "7".
Menu.ejecutar() llama self.estacion.buscar_por_codigo("7"). Ese método recorre self.misiones, encuentra la misión con código "7" y la devuelve (corta el bucle con break).
De vuelta en Menu.ejecutar, mision ahora apunta a ese objeto MisionExploracion. Como no es None, se ejecuta mision.iniciar().
Gracias al polimorfismo (Parte 11), Python ejecuta automáticamente MisionExploracion.iniciar(). Como el estado actual es PLANIFICADA, cambia a EJECUCION (con set_estado) e imprime "🚀 Exploración iniciada en Marte: Amanecer Rojo".
El bucle while True: vuelve a mostrar el menú, esperando la próxima acción, hasta que el usuario escribe 0 y el programa termina (con la animación de puntos) dentro de case 0:, ejecutando break, lo cual termina el while, lo cual termina ejecutar(), lo cual termina main.py, lo cual termina el programa completo.
Resumen visual:

main.py
  → servicios/gestion_misiones.py (trae Menu)
    → utils/menu.py: Menu() creado
      → modelos/estacion_espacial.py: EstacionEspacial() creado
    → menu.ejecutar()
      → usuario elige "1" → crea MisionExploracion("7","Amanecer Rojo","Marte")
        → estacion.agregar_mision(mision) → guardada en self.misiones
      → usuario elige "6" y código "7"
        → estacion.buscar_por_codigo("7") → devuelve el objeto
        → mision.iniciar() → MisionExploracion.iniciar() → estado = EJECUCION
      → usuario elige "0" → break → fin del programa
PARTE 20 — Relación entre objetos
¿Quién crea las misiones? Menu.ejecutar(), en la opción 1, crea el objeto concreto (MisionExploracion, MisionInvestigacion o MisionRescate) según lo que escribió el usuario.
¿Quién las almacena? El objeto EstacionEspacial (dentro del objeto Menu), en su lista self.misiones.
¿Quién las consulta? EstacionEspacial, a través de buscar_por_codigo() y buscar_por_nombre(); también mostrar_misiones() y mostrar_resumen() las recorren.
¿Quién cambia su estado? Las propias misiones, a través de sus métodos iniciar()/finalizar() (llamados desde Menu), y también EstacionEspacial.cambiar_estado() (que llama set_estado() sobre la misión encontrada).
¿Quién muestra la información? EstacionEspacial (con mostrar_misiones, mostrar_resumen) y Menu (al imprimir resultados de búsquedas).
¿Quién valida los datos? Menu.ejecutar() valida lo que escribe el usuario antes de crear objetos; Mision valida dentro de sus propios set_codigo()/set_nombre() (aunque estos, en la versión actual del menú, no se llaman desde ahí); EstacionEspacial.agregar_mision() valida que no haya códigos repetidos.
Esquema de relaciones:

Menu ── crea y contiene ──► EstacionEspacial ── guarda muchas ──► Mision (y sus hijas)
 │                                │
 └── crea objetos concretos ─────┘  (MisionExploracion / MisionInvestigacion / MisionRescate)
Menu tiene una EstacionEspacial (relación de composición: la estación vive y muere junto con el menú). EstacionEspacial tiene muchas misiones dentro de su lista (relación de uno a muchos).

PARTE 21 — Por qué el proyecto está organizado así
modelos/ agrupa lo que el programa es (una misión, un estado, la estación); servicios/ agrupa el punto de acceso que usa main.py para llegar al menú; utils/ agrupa apoyos técnicos (la interfaz de consola y la validación de texto) que no son "cosas" del problema espacial en sí. El código actual refleja esa separación tal cual: ninguna clase de modelos/ sabe nada sobre input() o print() de menú (eso vive en utils/menu.py); y utils/menu.py, a su vez, no contiene la lógica de guardar o buscar misiones (eso vive en modelos/estacion_espacial.py). Cada carpeta concentra, en el código real, un tipo de responsabilidad distinto, que es justamente la razón por la que existen como carpetas separadas.

PARTE 22 — Biblioteca.txt
Qué contiene: una lista en texto plano de las bibliotecas (módulos de la librería estándar de Python) usadas en el proyecto: abc, enum y time, indicando en qué archivo se usa cada una y por qué.
Para qué se utiliza: es documentación de apoyo para quien lee el proyecto, no código.
¿El código realmente lo utiliza? No. Biblioteca.txt no es importado ni leído por ningún archivo .py del proyecto; es solo un documento de referencia para las personas, no para el programa.
¿En qué momento se usa? Nunca durante la ejecución del programa; solo cuando una persona lo abre para consultarlo (por ejemplo, para preparar esta sustentación).
Relación con el resto del proyecto: describe, en lenguaje humano, los import reales que sí aparecen en el código (Parte 4).
PARTE 23 — Diccionario de conceptos (con ejemplos del proyecto)
Clase: plantilla que define atributos y métodos. Ej.: class Mision(ABC):.
Objeto: algo creado a partir de una clase, con datos propios. Ej.: el resultado de MisionExploracion("7", "Amanecer Rojo", "Marte").
Instancia: es sinónimo de "objeto creado a partir de una clase". Decir "una instancia de Mision" es lo mismo que decir "un objeto de tipo Mision".
Atributo: dato guardado dentro de un objeto. Ej.: self.planeta.
Método: función definida dentro de una clase, que recibe self. Ej.: iniciar(self).
Función: bloque de código reutilizable que no pertenece a una clase. Ej.: validar_texto(texto).
Parámetro: nombre que recibe un método/función para trabajar con un valor que llega de fuera. Ej.: nombre en set_nombre(self, nombre).
Argumento: el valor real que se envía a un parámetro al llamar al método/función. Ej.: en MisionRescate("3","Rescate A","Tripulación 1"), "3", "Rescate A" y "Tripulación 1" son los argumentos.
self: el objeto sobre el cual se ejecuta el método (Parte 9).
__init__: método especial que se ejecuta al crear un objeto (Parte 7).
Herencia: mecanismo por el cual una clase (hija) reutiliza atributos y métodos de otra (padre). Ej.: MisionExploracion(Mision).
Clase padre / superclase: la clase de la que se hereda. Ej.: Mision.
Clase hija / subclase: la clase que hereda. Ej.: MisionExploracion.
Abstracción: ocultar los detalles de "cómo" se hace algo, mostrando solo "qué" se puede hacer. La clase Mision es abstracta: define que toda misión debe poder iniciar()/finalizar(), sin decir cómo, dejando ese detalle a cada hija.
Encapsulamiento: ocultar los atributos internos de un objeto detrás de métodos (get_/set_), como con self.__codigo en Mision.
Polimorfismo: que un mismo método (iniciar()) se comporte distinto según la clase real del objeto que lo ejecuta (Parte 11).
ABC: clase de la librería abc que, al heredarla, vuelve abstracta a la clase (Parte 4 y 12).
abstractmethod: decorador que obliga a las clases hijas a implementar un método. Ej.: @abstractmethod sobre iniciar(self): pass.
Enum: clase base para crear conjuntos fijos de constantes con nombre. Ej.: EstadoMision.
Decorador: una etiqueta que se escribe con @ justo antes de un método o función, y que modifica su comportamiento. Ej.: @abstractmethod.
import: instrucción que trae código definido en otro archivo o librería para poder usarlo. Ej.: import time.
Módulo: cada archivo .py es un módulo; se puede importar por su nombre. Ej.: modelos.mision es el módulo del archivo modelos/mision.py.
Lista: colección ordenada y modificable de elementos, escrita entre corchetes []. Ej.: self.misiones = [].
Bucle: instrucción que repite un bloque de código varias veces. Ej.: for mision in self.misiones:, while True:.
Condición: instrucción if/elif/else que decide qué hacer según si algo es verdadero o falso. Ej.: if not opcion.isdigit():.
return: instrucción que entrega un valor desde un método/función y termina su ejecución ahí. Ej.: return self.__codigo.
None: valor de Python que representa "ningún valor". Ej.: lo que devuelve buscar_por_codigo() cuando no encuentra nada.
match: estructura de selección múltiple de Python (parecida a switch en otros lenguajes), usada en Menu.ejecutar y en cambiar_estado para decidir qué hacer según un número.
(No aparece "diccionario" (dict) como estructura de datos en este proyecto, así que no se incluye con ejemplo propio.)

PARTE 24 — Preguntas de sustentación
Básicas
¿Qué hace la clase EstacionEspacial?
¿Qué es un objeto, con tus propias palabras, usando el ejemplo de una misión?
¿Qué hace el método get_codigo()?
¿Qué imprime el programa si eliges la opción 2 del menú sin haber registrado ninguna misión?
¿Qué contiene la lista self.misiones?
Intermedias
¿Por qué MisionExploracion hereda de Mision y no al revés?
¿Qué parámetros recibe MisionInvestigacion.__init__ y qué hace cada uno?
¿Por qué self aparece como primer parámetro en casi todos los métodos?
¿Qué diferencia hay entre __codigo (con doble guion bajo) y planeta (sin guion bajo) como atributos?
¿Qué hace exactamente EstadoMision y por qué no se usa simplemente el texto "Planificada" como en el archivo original de Rusia?
¿Por qué agregar_mision() puede rechazar una misión?
Difíciles
¿Qué ocurre internamente, paso a paso, cuando se ejecuta MisionRescate("9", "Rescate X", "Tripulación Alfa")?
¿Qué relación existe entre Menu y EstacionEspacial? ¿Es la misma relación que existe entre EstacionEspacial y Mision?
¿Por qué el archivo servicios/gestion_misiones.py no define ninguna clase propia, y qué contiene entonces?
¿Qué pasaría si MisionInvestigacion no implementara el método iniciar()?
¿Por qué MisionInvestigacion.iniciar() necesita llamarse dos veces para que la misión llegue a EJECUCION, y las otras dos clases no?
Explica con el código real dónde ocurre polimorfismo en EstacionEspacial.mostrar_misiones().
¿Por qué buscar_por_codigo() puede devolver None, y qué parte del código se encarga de comprobar eso antes de usar el resultado?
