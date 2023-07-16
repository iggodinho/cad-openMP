import matplotlib.pyplot as plt

# Dados de tempo de execução obtidos em diferentes configurações
num_threads = [1, 2, 4, 8]
execution_time_fixed = [280.088842, 203.873161, 171.709426, 136.446875]
execution_time_scaling = [5.493821, 57.793222, 180.453473, 164.935696]

# Gráfico de escalabilidade forte (tamanho do problema fixo, aumentando o número de threads)
plt.figure()
plt.plot(num_threads, execution_time_fixed, marker='o')
plt.xlabel('Número de Threads')
plt.ylabel('Tempo de Execução (s)')
plt.title('Escalabilidade Forte')
plt.grid(True)
plt.show()

# Gráfico de escalabilidade fraca (aumentando o tamanho do problema e o número de threads)
plt.figure()
plt.plot(num_threads, execution_time_scaling, marker='o')
plt.xlabel('Número de Threads')
plt.ylabel('Tempo de Execução (s)')
plt.title('Escalabilidade Fraca')
plt.grid(True)
plt.show()
