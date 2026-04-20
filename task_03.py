# 3 Фильтр: найдите все наблюдения, где count > 500 — сколько их? В какое время года чаще всего?
count_500 = df_1[df_1["count"] > 500]
count_high = len(count_500)
print(count_high)