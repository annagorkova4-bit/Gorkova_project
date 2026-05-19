# Задание 5. Анализ размеров дверей и поиск «узких» дверей

import ifcopenshell
from ifcopenshell.express.rules.IFC4 import modelview

file_path = r"C:\Users\Anna\Desktop\Политех 2 семестр\Анализ данных\IFC\Example_1.ifc"

model = ifcopenshell.open(file_path)

doors = model.by_type("IfcDoor")

min_width = 900
narrow_doors = []

for door in doors:
    name = door.Name
    width = getattr(door, "OverallWidth", None)
    height = getattr(door, "OverallHeight", None)
    if width is not None and width < min_width:
        narrow_doors.append((door.Name, width, height))

for name, width, height in narrow_doors:
    print("Дверь: ", name, "Ширина: ", round(width), "Высота", height)

print(f"Количество узких дверей: {len(narrow_doors)}")