from main import Detail, Manufacturer, ManufactDetail, res_1, res_2, res_3
from unittest import TestCase

class Test(TestCase):
    def setUp(self) -> None:
        # Производители
        self.manufacturers = [
            Manufacturer(1, 'Schlieckmann'),
            Manufacturer(2, 'Klokkerholm'),
            Manufacturer(3, 'Signeda'),

            Manufacturer(11, 'Sigma'),
            Manufacturer(22, 'Tyg'),
            Manufacturer(33, 'Kito')
        ]
        # Детали
        self.details = [
            Detail(1, 'Кузов', 15000, 1),
            Detail(2, 'Поршни', 20000, 1),
            Detail(3, 'Ремень ГРМ', 5000, 2),
            Detail(4, 'Подушки двигателя', 25000, 3),
            Detail(5, 'Система охлаждения', 7000, 3)
        ]
        self.detail_manufacs = [
            ManufactDetail(1, 1),
            ManufactDetail(1, 2),
            ManufactDetail(2, 3),
            ManufactDetail(3, 4),
            ManufactDetail(3, 5),

            ManufactDetail(11, 1),
            ManufactDetail(22, 2),
            ManufactDetail(22, 3),
            ManufactDetail(33, 4),
            ManufactDetail(33, 5)
        ]
        self.one_to_many = [(d.name, d.value, m.name)
                   for m in self.manufacturers
                   for d in self.details
                   if d.manufacturer_id == m.id]
        self.many_to_many_temp = [(m.name, md.manufacturer_id, md.detail_id)
                         for m in self.manufacturers
                         for md in self.detail_manufacs
                         if m.id == md.manufacturer_id]
        self.many_to_many = [(d.name, d.value, m_name)
                    for m_name, m_id, d_id in self.many_to_many_temp
                    for d in self.details if d.id == d_id]

    def test1(self):
        result = res_1(self.one_to_many)
        desired = [['Поршни', 'Schlieckmann'], ['Подушки двигателя', 'Signeda']]
        self.assertEqual(result, desired)

    def test2(self):
        result = res_2(self.one_to_many)
        desired = [['Klokkerholm', 5000], ['Signeda', 7000], ['Schlieckmann', 15000]]
        self.assertEqual(result, desired)

    def test3(self):
        result = res_3(self.many_to_many)
        desired = [['Кузов', 'Schlieckmann'], ['Кузов', 'Sigma'],
                   ['Подушки двигателя', 'Signeda'], ['Подушки двигателя', 'Kito'],
                   ['Поршни', 'Schlieckmann'], ['Поршни', 'Tyg'], ['Ремень ГРМ', 'Klokkerholm'],
                   ['Ремень ГРМ', 'Tyg'], ['Система охлаждения', 'Signeda'], ['Система охлаждения', 'Kito']]
        self.assertEqual(result, desired)