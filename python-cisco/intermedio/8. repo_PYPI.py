
#--------------------------------------------- Que es PyPI? -------------------------------------

# PyPI (es la abreviatura de Python Package Index) 
# Puedes encontrar su sitio web aquí: https://wiki.python.org/psf/PackagingWG
# Debemos señalar que PyPI no es el único repositorio de Python existente. Por el contrario, hay muchos de ellos, creados para proyectos y dirigidos por muchas comunidades Python más grandes y más pequeñas
# De todos modos, PyPI es el repositorio de Python más importante del mundo.
# El repositorio de PyPI a veces se denomina la Tienda de Quesos. la razon es por es uno de los sketches más famosos de Monty Python The Cheese Shop (La Tienda de Quesos)
# Para hacer uso del repo PYPI hace falta de una herramienta llamada "pip"

# ------------------------------------Cómo instalar pip -----------------------------

#>>>>>>>>>>> En WINDOWS
# El instalador de Python para MS Windows ya contiene pip
# Para verificar Abre la consola de Windows (CMD o PowerShell, lo que sea que prefieras) y Ejecuta el siguiente comando: pip --version

#>>>>>>>>>> En LINNUX 
# algunas distribuciones de Linux pueden utilizar más de una versión de Python al mismo tiempo, por ejemplo, un Python 2 y un Python 3 coexistiendo uno al lado del otro.
# En este caso, puede haber dos pip diferentes identificados como (pip o pip2) y pip3.
# compruebalo de la siguiente manera: pip --version | pip3 --version

#>>>>>>>> Instalar PIP en LINUX
# Desafortunadamente, algunas distribuciones de Linux no tienen pip preinstalado, incluso si Python está instalado por defecto en estos casos hay 2 posibilidades: 
## Instalar pip como un paquete del sistema usando un administrador de paquetes dedicado (por ejemplo, apt en sistemas tipo Debian, yum fedora, pacman archlinux). (recomendado)
## Instalar pip usando mecanismos internos de Python. (no recomendado)

# sudo apt install python3-pip --> Debian o ubuntu
# sudo pacman -S python-pip --> ArchLinux

#>>>>>>>> En MacOS
# usando el instalador brew, pip ya está presente en tu sistema y listo para funcionar

