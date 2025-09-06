import pandas as pd

# Leer dataset de clientes
df = pd.read_csv("clientes.csv")

# 1. Limpiar duplicados
df = df.drop_duplicates()

# 2. Ordenar por nombre
df = df.sort_values(by="Nombre")

# 3. Crear columna de gasto promedio por compra
df['Gasto_Promedio'] = df['Total_Gastado'] / df['Compras_Mensuales']

# 4. Resumen estadístico
resumen = df.describe()
print("Resumen estadístico de clientes:\n", resumen)

# 5. Exportar CSV limpio
df.to_csv("clientes_limpio.csv", index=False)
print("CSV limpio guardado como clientes_limpio.csv")

# 6. Visualización rápida (opcional)
import matplotlib.pyplot as plt

plt.bar(df['Nombre'], df['Gasto_Promedio'])
plt.xlabel("Clientes")
plt.ylabel("Gasto promedio por compra")
plt.title("Gasto promedio por cliente")
plt.xticks(rotation=45, fontsize=6)
plt.tight_layout()
plt.show()
