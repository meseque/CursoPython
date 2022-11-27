from math import sqrt
var_a = int(input("Digite o valor coeficiente 'a':\n"))
var_b = int(input("Digite o valor coeficiente 'b':\n"))
var_c = int(input("Digite o valor coeficiente 'c':\n"))

delta = var_b**2-4*var_a*var_c

print(delta)

if delta < 0:
    print("Delta Negativo")
else:
    raiz_delta = sqrt(delta)
    print(raiz_delta)
    x1 = (-var_b+raiz_delta)/2*var_a
    x2 = (-var_b-raiz_delta)/2*var_a

print("As raízes são", x1, "e", x2)
