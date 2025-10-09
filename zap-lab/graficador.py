import matplotlib.pyplot as plt

# Datos
meses = ["Julio", "Agosto", "Septiembre"]
delivery = [725, 680, 717]
comedor = [700, 709, 734]

# --- Gráfico de líneas comparativo ---
plt.figure(figsize=(8,5))
plt.plot(meses, delivery, marker="o", color="orange", linewidth=2, label="Delivery")
plt.plot(meses, comedor, marker="o", color="blue", linewidth=2, label="Comedor")

# Estilo
plt.title("Órdenes Mensuales: Delivery vs Comedor", fontsize=14)
plt.xlabel("Mes", fontsize=12)
plt.ylabel("Órdenes", fontsize=12)
plt.ylim(650, 750)  # rango ajustado para que se note la variación
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()

# Mostrar valores en cada punto
for i, val in enumerate(delivery):
    plt.text(meses[i], val+3, str(val), ha='center', color="orange", fontsize=9)
for i, val in enumerate(comedor):
    plt.text(meses[i], val-15, str(val), ha='center', color="blue", fontsize=9)

plt.tight_layout()
plt.show()
