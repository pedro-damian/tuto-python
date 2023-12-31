
# PAQUETES
# Un módulo es un contenedor lleno de funciones
# un paquete es un contenedor de modulos
# Dicho contenedor se puede distribuir tal cual (como un lote de archivos implementados en un subárbol de directorio) o se puede empaquetar dentro de un archivo zip.
# Durante la primera importación del módulo, Python traduce su código fuente a un formato semi-compilado almacenado dentro de los archivos pyc y los implementa en el directorio __pycache__ ubicado en el directorio de inicio del módulo.
# Si se desea decirle al usuario del módulo que una entidad en particular debe tratarse como privada puedes marcar su nombre con el prefijo _ o __ .
""" Los nombres shabang, shebang, hasbang, poundbang y hashpling describen el dígrafo escrito como #!, se utiliza para instruir a los sistemas operativos similares a Unix sobre cómo se debe iniciar el archivo fuente de Python. Esta convención no tiene efecto en MS Windows. 
"""
# Si deseas convencer a Python de que debe tomar en cuenta el directorio de un paquete no estándar, su nombre debe insertarse/agregarse en/a la lista de directorios de importación almacenada en la variable path contenida en el módulo sys.
# Un archivo de Python llamado __init__.py se ejecuta implícitamente cuando un paquete que lo contiene está sujeto a importación y se utiliza para inicializar un paquete y/o sus subpaquetes (si los hay).

