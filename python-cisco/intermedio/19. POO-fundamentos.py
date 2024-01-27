

# CLASES
# Una clase es un modelo de una parte muy específica de la realidad, que refleja las propiedades y actividades que se encuentran en el mundo real.
# La definición comienza con la palabra clave reservada class. La palabra clave reservada es seguida por un identificador que le dará nombre a la clase (nota: no lo confundas con el nombre del objeto: estas son dos cosas diferentes). A continuación, se agregan dos puntos (:)

# Cuando una clase se deriva de otra clase, su relación se denomina herencia.
# La clase que deriva de la otra clase se denomina subclase. El segundo lado de esta relación se denomina superclase.
# De modo que esta la clase por debajo de la clase esta la subclase y por encima esta la superclase: subclase --> clase --> superclase

class TheSimplestClass:
    pass
  
  
# OBJETO
# Para crear un objeto debes asignar una variable para almacenar el objeto recién creado de esa clase y crear un objeto al mismo tiempo.
# El objeto recién creado está equipado con todo lo que trae la clase. Como esta clase está completamente vacía, el objeto también está vacío.
# El acto de crear un objeto de la clase seleccionada también se llama instanciación (ya que el objeto se convierte en una instancia de la clase).

class TheSimplestClass:
  my_first_object = TheSimplestClass()