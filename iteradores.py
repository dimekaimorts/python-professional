
class EvenNumbers:
  """Clase que implementa un iterador de todos los números pares,
  o los números pares hasta un máximo que definimos
  """

  # Constructor
  def __init__(self, max=None): # self = objeto futuro creado con esta clase
    self.max = max

  # Método para tener elementos o atributos que voy a necesitar para que el iterador funcione
  def __iter__(self):
    self.num = 0            # Primer número par
    return self             # Retorno al objeto de si mismo

  # Método para tener la función "next" del ciclo for, es decir, extraer/recorrer cada valor.
  def __next__(self):
    if not self.max or self.num <= self.max:
      result = self.num
      self.num += 2
      return result
    else:
      raise StopIteration