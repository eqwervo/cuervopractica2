Esteban Cuervo
17948/3
cuervoesteban87@gmail.com


1. Creacion del entorno virtual

Creación del entorno virtual con el comando 
    "python3 -m venv /path/to/new/virtual/environment".

Activar con el comando el entorno virtual dependiendo la Plataforma:
    
POSIX
    bash/zsh
    $ source <venv>/bin/activate
    fish
    $ . <venv>/bin/activate.fish
    csh/tcsh
    $ source <venv>/bin/activate.csh
    PowerShell Core
    $ <venv>/bin/Activate.ps1

Windows
    cmd.exe
    C:\> <venv>\Scripts\activate.bat
    PowerShell
    PS C:\> <venv>\Scripts\Activate.ps1 

2. Instalar las librerias del entorno con:

    "pip install -r requirements.txt"

Observación: Es posible que tenga que instalar el kernel para poder ejecutar python en notebook, la versión debe coincidir con la del entorno virtual especificado en requirements.txt

3. Ejecución
Se descarga el paquete de archivos desde el archivo "tp2.ipynb" se ejecuta el siguiente comando:

    "jupyter lab"

para iniciarla aplicacion web de Jupyter:
    

