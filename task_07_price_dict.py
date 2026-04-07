"""
Задача 7: Прайс-лист материалов
Работа со словарём - добавление, изменение, удаление, статистика.
"""

materials ={
    "Бетон": 5500,
    "Древесина": 6800,
    "Кирпич": 12600,
    "Металл": 18000,
    "Газобетон": 6500
}

"""Добавляем два элемента в словарь"""
materials["Гипс"] = 3600
materials["Керамзитоблок"] =6600
print("\nСловарь после добавления материалов")
for material, price in materials.items():
    print(f" {material}: {price}, руб.")

"""Изменим цену Кирпича на 10%"""
old_price = materials["Кирпич"]
new_price = int(old_price * 1.10)
materials["Кирпич"] = new_price
print("\nНовая стоимость кирпича: ", new_price)

"""Удаляем один материал"""
materials.pop("Металл")

"""Рассчитаваем среднюю цену"""
average_price = sum(materials.values()) / len(materials)
print("\nСредняя цена всех материалов", round(average_price, 2), "руб.")

"""Выводим итоговый словарь"""
print("\nИтоговый словарь материалов")
for material, price in materials.items():
    print(f" {material}: {price}, руб.")