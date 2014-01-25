Creación de una página en python-django con javascript y jquery utilizando nuestra plantilla y colores corporativos. Los datos se almacenarán en una base de datos SQLite. 
Puede estar en español o inglés.

 1. PÁGINA DE REGISTRO/INICIO DE SESIÓN 

Será una página de registro/inicio de sesión ESTÁNDAR con nuestro logo y colores corporativos. 
En la primera página se da la bienvenida al usuario y se le ofrecen las opciones de iniciar la sesión con un nombre de usuario y contraseña o registrarse para crear una cuenta nueva.

PÁGINA DE INICIO DE SESIÓN ESTÁNDAR 

Se presentará al usuario una ventana de inicio de sesión ESTÁNDAR, con un cuadro para introducir el nombre de usuario, otro para introducir la contraseña, y un botón para registrarse y crear una cuenta nueva que redirigirá al usuario a la ventana de registro.

Habrá disponible un enlace para solicitar el reenvío del nombre de usuario y la contraseña ("Forgot your username/password?").
Si el usuario hace clic en este enlace, aparecerá un cuadro en el que se le pedirá que introduzca su dirección de correo electrónico.
Se verificará la dirección de correo electrónico. 
Si existe, se enviará un mensaje a esa dirección incluyendo su nombre de usuario y una contraseña creada automáticamente por el sistema, con la frase habitual "Your access data for...",.
Si la dirección de correo electrónico no es correcta, se informará al usuario de que la dirección de correo no existe en nuestro sistema ("The email address you have entered does not exist in our system"), y se le pedirá que la introduzca de nuevo o se registre para crear una cuenta nueva ("Please try again or register for a new account").
Si la contraseña no es correcta, se informará al usuario de que no lo es y se le pedirá que lo intente de nuevo o se registre en el sistema ("Password incorrect. Please try again or register for a new account"). Habrá disponible un enlace para solicitar el reenvío del nombre de usuario y la contraseña ("Forgot your username/password?") . 

Si el inicio de sesión se realiza correctamente, el usuario accederá a la página para subir/elegir el archivo.

VENTANA DE REGISTRO ESTÁNDAR

Al registrarse para crear una cuenta nueva, se presentará al usuario una ventana de registro ESTÁNDAR en la que podrá introducir su información personal.

La información será la siguiente, y todos los campos serán obligatorios ("All fields are compulsory."):

Nombre de usuario ("Username")
Contraseña ("Password")
Vuelva a introducir la contraseña ("Please retype your password"). (Se comprobará si las contraseñas coinciden, y se le pedirá que vuelva a introducirlas si no coinciden)
Nombre ("Name")
Empresa ("Company")
Correo electrónico ("Email")

Después de iniciar la sesión o registrarse correctamente, el usuario accederá a su propia carpeta en el servidor, y se le pedirá que cargue un nuevo archivo o elija uno existente que haya cargado previamente ("Upload a new file, or choose an existing one").

Para poder pasar al paso siguiente, el usuario deberá marcar una casilla ESTÁNDAR en la que indica que acepta los términos y condiciones de uso y la política de privacidad ("I accept the terms and conditions, and agree to the privacy policy"). La frase incluirá enlaces a los términos y condiciones y a la política de privacidad.


PÁGINA DE CARGA/SELECCIÓN DE ARCHIVO

En todo momento estará disponible un menú (por ejemplo, en la esquina superior derecha) con las opciones de cerrar la sesión y modificar los detalles de la cuenta, así como la de acceder a su carpeta para ver/borrar los archivos que ya se hayan subido.

CARGAR O SUBIR ARCHIVO 1

El usuario podrá cargar archivos en formato comprimido o sin comprimir (una sugerencia informará al usuario de los formatos admitidos). Este archivo comprimido contendrá siempre un único archivo.

Tras elegir el archivo, el usuario hará clic en un botón para subirlo ("Upload") y comenzará el proeso de subida.

Durante el proceso, el usuario verá un indicador del progreso de subida.

Al acabar, el usuario recibirá un mensaje de confirmación de que la subida se ha realizado y el archivo se ha descomprimido correctamente, y dispondrá de un botón para pasar al paso siguiente ("Next").

Cuando el archivo se haya cargado, se descomprimirá (si es necesario). El usuario verá un cuadro o un mensaje de texto que le indicará que se está descomprimiento el archivom("Your file has been successfully uploaded and is being extracted").

Si el archivo no se descomprime correctamente, se informará al usuario de que la extracción ha fallado, y se le ofrecerán dos botones o enlaces para volver a intentarlo o cancelar la operación ("File extraction has failed. Please retry or cancel the operation").

Si el usuario hace clic en la opción de intentarlo de nuevo, accederá a la pantalla anterior del proceso (seleccionar y cargar un archivo).


CARGAR O SELECCIONAR UN ARCHIVO 2

Una vez cargado el primer archivo, se pedirá al usuario que cargue un segundo archivo. Este segundo archivo podrá también estar comprimido o sin comprimir. 

El proceso será el mismo que para el archivo 1.

En este caso, si el archivo está comprimido, podrá contener: 
- un único archivo
- varios archivos
- una carpeta con varios archivos y/o subcarpetas. 
Se deberá descomprimir en la carpeta personal del usuario.

Al igual que antes, el usuario verá un indicador de progreso y, al terminar, recibirá un mensaje de confirmación de que la subida y la extracción se han realizado correctamente, etc., y se le presentará un botón para proceder al paso siguiente.

En todo momento habrá disponible un botón para cancelar la operación.

VENTANA DE FINALIZACIÓN DEL TIEMPO DE ESPERA (TIMEOUT)

Después de un cierto tiempo de inactividad, se cancelará el proceso y se cerrará la sesión del usuario. Un mensaje indicará que ha finalizado el tiempo de espera de la sesión y le orecerá un enlace o botón para acceder de nuevo a la pantalla de inicio de sesión ("Your session has timed out. Please login again.") .


