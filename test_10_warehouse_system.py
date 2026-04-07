"""
Задача 10: Система учета склада
Создать систему учета материалов с контролем критических остатков
"""

"""Исходные дланные о складе"""
warehouse = {
 "Кирпич": {"quantity": 5000, "price": 12.50, "min_quantity": 1000},
 "Цемент": {"quantity": 120, "price": 450.00, "min_quantity": 50},
 "Песок": {"quantity": 8, "price": 800.00, "min_quantity": 10},
 "Арматура": {"quantity": 30, "price": 48000.00, "min_quantity": 20},
 "Бетон": {"quantity": 45, "price": 4200.00, "min_quantity": 15}
}

print("=" * 100)
print("СИСТЕМА УЧЁТА СКЛАДА")
print("=" * 100)

"""Вывод таблицы материалов"""

print(f"{'Материал':<10} | {'Кол-во':<6} | {'Цена':<8} | {'Мин.':<6} | {'Стоимость':<10}")
print("-" * 100)
print("----")

total_cost = 0
for name, props in warehouse.items():
    quantity = props["quantity"]
    price = props["price"]
    min_quantity = props["min_quantity"]
    cost = quantity * price
    total_cost += cost
    print(f"{name:<10} | {quantity:<6} | {price:<8} | {min_quantity:<6} | {cost:<10}")

print("=" * 100)
print(f"ОБЩАЯ СТОИМОСТЬ: {total_cost:.2f} руб")