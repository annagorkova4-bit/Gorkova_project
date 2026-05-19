# Задание 6. Изменение свойства стены и сохранение новой модели

import ifcopenshell
from ifcopenshell.express.rules.IFC4 import modelview
import ifcopenshell.util.element

file_path = r"C:\Users\Anna\Desktop\Политех 2 семестр\Анализ данных\IFC\Example_1.ifc"

model = ifcopenshell.open(file_path)

walls = model.by_type("IfcWall")
first_wall = walls[0]

print(f"Исходное Name: {first_wall.Name}")
print(f"ObjectType: {getattr(first_wall, 'ObjectType', None)}")

first_wall.Name = "MODIFIED_" + first_wall.Name

psets = ifcopenshell.util.element.get_psets(first_wall)
if 'Pset_WallCommon' in psets:
    psets['Pset_WallCommon']['IsExternal'] = True

model.write(r"C:\Users\Anna\Desktop\Политех 2 семестр\Анализ данных\IFC\_modified.ifc")

new_model = ifcopenshell.open(r"C:\Users\Anna\Desktop\Политех 2 семестр\Анализ данных\IFC\_modified.ifc")
new_walls = new_model.by_type("IfcWall")
new_first_wall = new_walls[0]
new_psets = ifcopenshell.util.element.get_psets(new_first_wall)

print(f"Обновленное Name: {new_first_wall.Name}")
if 'Pset_WallCommon' in new_psets:
    print(f"IsExternal: {new_psets['Pset_WallCommon'].get('IsExternal')}")