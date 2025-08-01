import numpy as np
import matplotlib.pyplot as plt

# Solución exacta
def exact_solution(t):
    return np.exp(t) / (1 + np.exp(t))

# Método de Euler
def euler_method(f, y0, t0, tf, h):
    t_values = np.arange(t0, tf + h, h)
    y_values = np.zeros(len(t_values))
    y_values[0] = y0
    
    for i in range(1, len(t_values)):
        y_values[i] = y_values[i-1] + h * f(t_values[i-1], y_values[i-1])
    
    return t_values, y_values

# Definición de la EDO: dy/dt = y - y^2
def f(t, y):
    return y - y**2

# Parámetros
t0 = 0
tf = 1
h = 0.2
y0 = 0.5  # Condición inicial y(0) = 0.5

# Soluciones
t_euler, y_euler = euler_method(f, y0, t0, tf, h)
t_exact = np.linspace(t0, tf, 100)
y_exact = exact_solution(t_exact)

# Resultados
print("Método de Euler:")
for t, y in zip(t_euler, y_euler):
    print(f"t = {t:.1f}, y ≈ {y:.6f}")

print("\nSolución exacta en los mismos puntos:")
for t in t_euler:
    print(f"t = {t:.1f}, y = {exact_solution(t):.6f}")

# Gráfico
plt.figure(figsize=(10, 6))
plt.plot(t_exact, y_exact, label='Solución exacta', color='blue')
plt.plot(t_euler, y_euler, 'o--', label='Método de Euler (h=0.2)', color='red')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.title('Comparación entre solución exacta y método de Euler')
plt.legend()
plt.grid(True)
plt.show()