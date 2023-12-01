import sys
from algoritmo_euclideo import MCD

def find_inverso_moltiplicativo(n: int, m: int) -> int:
  """
  Resituisce l'inverso moltiplicativo di `n` mod `m`

  Esempio:
  ``` python
  res = find_inverso_moltiplicativo(2, 7)
  print(res) # 4
  ```
  """
  gcd = MCD(n,m)
  assert gcd == 1, f"Numero e modulo devono essere coprimi: MCD({n},{m})={gcd}!=1"
  for i in range(1, m+1):
    rem = n*i % m
    if rem == 1:
      return i
  return -1
  
def print_error(e):
  print(f"Errore: {e}\nUsage: python {sys.argv[0]} 2 7")
  exit()
    
if __name__ == "__main__":
  args = sys.argv[1:]
  user_input1, user_input2 = args[0], args[1]
  number = modulo = 0
  try:
    number = int(user_input1)
    modulo = int(user_input2)
  except ValueError as e:
    print_error(e)
  res = find_inverso_moltiplicativo(number, modulo)
  print(f"Inverso di {number} in Z_{modulo} = {res}")