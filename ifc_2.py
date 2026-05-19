# Задание 2. Вывод информации о первой стене

import ifcopenshell
from ifcopenshell.express.rules.IFC4 import modelview

file_path = r"C:\Users\Anna\Desktop\Политех 2 семестр\Анализ данных\IFC\Example_1.ifc"

model = ifcopenshell.open(file_path)

walls = model.by_type("IfcWall")
print("Количество стен в модели: ", len(walls))

first_wall = walls[0]
print(first_wall)