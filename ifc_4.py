# Задание 4. Получение этажей и информации о модели

import ifcopenshell
from ifcopenshell.express.rules.IFC4 import modelview

file_path = r"C:\Users\Anna\Desktop\Политех 2 семестр\Анализ данных\IFC\Example_1.ifc"

model = ifcopenshell.open(file_path)

storeys = model.by_type("IfcBuildingStorey")

print("Схема IFC: ", model.schema)
print("Этажей: ", len(storeys))
print()

for storey in storeys:
    elevation = getattr(storey, 'Elevation', None)
    print(f"Этаж: {storey.Name}, Elevation={elevation}")

print("TITLE window")