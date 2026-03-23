import matplotlib.pyplot as plt

def collatz_steps(n):
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps

#datos
n_inicio = range(1, 10001)
iteraciones = [collatz_steps(i) for i in n_inicio]

#gráfico
plt.scatter(n_inicio, iteraciones, s = 0.5) # s =tamaño del punto

plt.title("Conjetura de Collatz: n inicial vs Iteraciones")
plt.xlabel("Número de inicio (n)")
plt.ylabel("Iteraciones para llegar a 1")

plt.show() 