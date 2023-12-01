inf: int = int(10e10)

def read_int(msg: str, min: int = inf, max: int = -inf) -> int:
    res: int = 0
    while True:
        got_error = False
        try:
            res = int(input(msg))
        except ValueError as e:
            print(f"ERRORE: {e}")
            got_error = True
        if min != inf and max == -inf and not (res >= min): # lower bound set
            print(f"Inserire un numero maggiore di {min}")
            got_error = True
        if min == inf and max != -inf and not (res <= max): # upper bound set
            print(f"Inserire un numero minore di {max}")
            got_error = True
        if min != inf and max != -inf and not (res >= min and res <= max): #upper and lower bound set
            print(f"Inserire un numero compreso tra {min} e {max}")
            got_error = True
        if not got_error: break
    return res