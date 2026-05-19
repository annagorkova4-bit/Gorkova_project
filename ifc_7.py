# Задание 7. Фильтрация элементов по условию и экспорт подмодели

import ifcopenshell

file_path = r"C:\Users\Anna\Desktop\Политех 2 семестр\Анализ данных\IFC\Example_1.ifc"

model = ifcopenshell.open(file_path)

doors = model.by_type("IfcDoor")

min_width = 900
filtered_doors = []

for door in doors:
    name = door.Name
    width = getattr(door, "OverallWidth", None)
    height = getattr(door, "OverallHeight", None)
    if width is not None and width >= min_width:
        filtered_doors.append(door)
        print("Дверь: ", name, "Ширина: ", round(width), "Высота", height)

print(f"Количество дверей с шириной >= {min_width}: {len(filtered_doors)}")

new_model = ifcopenshell.file(schema=model.schema)

for door in filtered_doors:
    new_model.add(door)

for building in model.by_type("IfcBuilding"):
    new_model.add(building)

for storey in model.by_type("IfcBuildingStorey"):
    new_model.add(storey)

output_path = r"C:\Users\Anna\Desktop\Политех 2 семестр\Анализ данных\IFC\_filtered_doors.ifc"
new_model.write(output_path)

check_model = ifcopenshell.open(output_path)
check_doors = check_model.by_type("IfcDoor")
print(f"Проверка: в подмодели {len(check_doors)} дверей")