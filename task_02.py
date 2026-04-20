# 2 Постройте столбчатую диаграмму: среднее число поездок (casual и registered отдельно) по сезонам
seasonal_data = df_1.groupby("season")[["casual", "registered"]].mean()

fig, ax = plt.subplots(figsize=(10, 5))
x = range(4)
width = 0.35
ax.bar([i - width/2 for i in x], seasonal_data["casual"], width)
ax.bar([i + width/2 for i in x], seasonal_data["registered"], width)

ax.set_title("Среднее кол-во поездок", fontsize=14)
ax.set_xlabel("Сезон")
ax.set_ylabel("Число поездок")
ax.set_xticks(x)
ax.set_xticklabels(["Зима", "Весна", "Лето", "Осень"])
ax.grid(axis="y", alpha=0.3)
plt.show()