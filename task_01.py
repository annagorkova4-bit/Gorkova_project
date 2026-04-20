# 1 Найдите час суток с максимальным числом поездок в выходные дни
workingday_data = df_1[df_1["workingday"] == 0]
workingday_hour = workingday_data.groupby(workingday_data["datetime"].dt.hour).agg({"count": "mean"})
max_hour = workingday_hour["count"].idxmax()
print("Час суток с максимальным числом поездок в выходные дни:", max_hour)