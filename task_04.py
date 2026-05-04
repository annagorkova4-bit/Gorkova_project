#4. Сохраните в CSV таблицу: средняя температура и среднее число поездок по каждому месяцу
monthly_stats = df.groupby(df['datetime'].dt.month).agg({
    'temp': 'mean',
    'count': 'mean'
}).round(1)
monthly_stats.columns = ['Средняя температура', 'Среднее число поездок']
monthly_stats.to_csv("monthly_stats.csv", sep=";", encoding='utf-8-sig')
print("Файл сохранён: monthly_stats.csv")