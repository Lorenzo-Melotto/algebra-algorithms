import equation
from algoritmo_euclideo import MCD
from bezout import bezout
from utils import read_int

def main() -> None:
    eq_num: int = read_int("Number of equation in the system (min 2): ", min=2)
    eqs: list[equation.eq] = []

    for i in range(eq_num):
        a: int = read_int(f"Input the coefficient of the equation {i+1}: ")
        b: int = read_int(f"Input the known term of the equation {i+1}: ")
        n: int = read_int(f"Input the modulo of the equation {i+1}: ")
        eqs.append(equation.eq(a % n, b % n, n))
        print()

    print("System in standard form\n")
    R: int = 1
    for eq in eqs:
        # MCD(n, a) and inverse of a
        d, _, inv = bezout(eq.n, eq.a)
        if eq.b % d == 0: # divide by the MCD(n, a)
            eq.a, eq.b, eq.n = eq.a//d, eq.b//d, eq.n//d
        else: 
            print(f"The equation {eq.a}x = {eq.b} mod {eq.n} has no solution. Exiting program.")
            return
        # transform the system in standard form
        eq.a, eq.b = (eq.a * inv)%eq.n, (eq.b * inv)%eq.n
        if eq.a != 1:
            print(f"  {eq.a}x = {eq.b} mod {eq.n}")
        else:
            print(f"  x = {eq.b} mod {eq.n}")
        R *= eq.n
    print()

    for i in range(len(eqs)):
        for j in range(len(eqs)):
            if i != j and MCD(eqs[i].n, eqs[j].n) != 1:
                print("All modules in the system are not coprime. The functionality of splitting equations it's not implemented yet.")
                return 

    print(f"R = {R}")
    
    Ri: list[tuple[int, int]] = []
    for i in range(eq_num):
        curr_Ri = 1
        for j in range(eq_num):
            if i != j:
                curr_Ri *= eqs[j].n
        
        _, _, inv = bezout(eqs[i].n, curr_Ri)
        inv = inv % eqs[i].n
        xi = (eqs[i].b * inv) % eqs[i].n
        Ri.append((curr_Ri, (eqs[i].b * inv) % eqs[i].n))
        print(f"R{i+1} = {curr_Ri}, x{i+1} = {xi}")

    # final result calculation
    final_sol: int = 0
    x0_str: str = "x0 = "
    for r in Ri: 
        final_sol += r[0]*r[1]
        x0_str += f"{r[0]}*{r[1]} + "
    x0_str = x0_str[:-2] + f"= {final_sol} = "
    final_sol = final_sol % R
    x0_str += f"{final_sol} mod {R}"
    print(x0_str + "\n")

    print(f"The set of all solutions is: {final_sol} + {R}Z")

if __name__ == "__main__":
    main()
