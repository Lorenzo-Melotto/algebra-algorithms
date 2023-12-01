import sys
from algoritmo_euclideo import MCD 

def find_invertibili(modulo: int) -> list[int]:
  """
    Restituisce la lista di elementi invertibili in Z_modulo
    
    Esempio: 
    
    ```python
    inv = find_invertibili(16) 
    print(inv) #-> [1, 3, 5, 7, 9, 11, 13, 15]
    ```
  """
  assert modulo > 1, "Il modulo deve essere > 1"
  invertibili = []
  for i in range(1, modulo):
    if(MCD(modulo, i) == 1):
      invertibili.append(i)
  return invertibili

def print_error(e):
  print(f"Errore: {e}\nUsage: python {sys.argv[0]} 10")
  exit()

if __name__ == "__main__":
  args = sys.argv[1:]
  user_input = args[0]
  modulo = 0
  try:
    modulo = int(user_input)
  except ValueError as e:
    print_error(e)
  res = find_invertibili(modulo)
  print(f"{len(res)} elementi: {res}")