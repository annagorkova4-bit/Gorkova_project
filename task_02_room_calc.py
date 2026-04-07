""""
Расчет геометрических параметров помещения и стоимости покраски стен.

Примечание:
1. Геометрические размеры (длина, ширина ,высота) указаны в метрах;
2. Стоимость покраски (cost_1) указана в руб/м2;
3. Площадь стен рассчитывается без учета дверных и оконных проемов.
"""

length = 5.4
width = 3.63
height = 2.83
cost_1 = 125.0

floor_area = length * width
walls_area = 2 * length * height + 2 * width * height
volume = length * width * height
cost = cost_1 * walls_area

print("Площадь пола: ", round(floor_area, 2), "м2")
print("Площадь стен: ", round(walls_area, 2), "м2")
print("Объем комнаты:", round(volume, 2), "м3")
print("Стоимость покраски стен:", round(cost, 2), "руб.")