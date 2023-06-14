def is_prime(n):
    """Verifica se um número é primo."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Solicita os valores de P, E, x e y ao usuário
P = int(input("Digdite o valor de P (número primo): "))
while not is_prime(P):
    P = int(input("P deve ser um número primo. Digite novamente: "))

E = int(input("Digite o valor de E (número primo menor ou igual a P): "))
while not (is_prime(E) and E <= P):
    E = int(input("E deve ser um número primo e menor ou igual a P. Digite novamente: "))

x = int(input("Digite o valor de x: "))
y = int(input("Digite o valor de y: "))

# Calcula A e B
A = pow(E, x, P)
B = pow(E, y, P)

# Calcula K
K1 = pow(A, y, P)
K2 = pow(B, x, P)

# Verifica se K1 é igual a K2
if K1 == K2:
    print("A fórmula está correta. K1 = K2 = ", K1)
else:
    print("A fórmula está incorreta. K1 =", K1, "e K2 =", K2)
