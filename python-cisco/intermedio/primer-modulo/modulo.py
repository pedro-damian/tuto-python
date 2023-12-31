
# Este archivo modulo,py sera el archivo que contendra el modulo
# Cuando se ejecuta un archivo directamente, su variable __name__ se establece a __main__
print(__name__)

if __name__ == "__main__":
    print("Estoy en el archivo del módulo")
else:
    print("EStoy siendo importado desde otro archivo")

