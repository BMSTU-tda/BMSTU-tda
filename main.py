from operator import itemgetter


class Detail:
    """Детали"""
    def __init__ (self, id, name, value, manufacturer_id):
        self.id = id
        self.name = name
        self.value = value
        self.manufacturer_id = manufacturer_id

class Manufacturer:
    """Производители"""
    def __init__(self, id, name):
        self.id = id
        self.name = name

class ManufactDetail:
    """Детали от производителей"""
    def __init__(self, manufacturer_id, detail_id):
        self.manufacturer_id = manufacturer_id
        self.detail_id = detail_id

#Производители
manufacturers = [
    Manufacturer(1, 'Schlieckmann'),
    Manufacturer(2, 'Klokkerholm'),
    Manufacturer(3, 'Signeda'),

    Manufacturer(11, 'Sigma'),
    Manufacturer(22, 'Tyg'),
    Manufacturer(33, 'Kito')
]
#Детали
details = [
    Detail(1, 'Кузов', 15000, 1),
    Detail(2, 'Поршни', 20000, 1),
    Detail(3, 'Ремень ГРМ', 5000, 2),
    Detail(4, 'Подушки двигателя', 25000, 3),
    Detail(5, 'Система охлаждения', 7000, 3)
]

detail_manufacs = [
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

def res_1(arr):
    answer_list = []
    for detail, value, manufacturer in arr:
        if detail[0] == 'П':
            answer_list.append([detail, manufacturer])
    return answer_list

def res_2(arr):
    answer_list = [[arr[0][2], arr[0][1]]]
    for detail, value, manufacturer in arr:
        if manufacturer == answer_list[len(answer_list)-1][0]:
            if value < answer_list[len(answer_list)-1][1]:
                answer_list[len(answer_list)-1][1]= value
        else:
            answer_list.append([manufacturer, value])
    return sorted(answer_list, key=itemgetter(1))

def res_3(arr):
    answer_list = []
    for detial, value, manufacturer in arr:
        answer_list.append([detial, manufacturer])
    return sorted(answer_list, key=itemgetter(0))
def main():
    # Соединение данных один-ко-многим
    one_to_many = [(d.name, d.value, m.name)
                   for m in manufacturers
                   for d in details
                   if d.manufacturer_id == m.id]

    # Соединение данных многие-ко-многим
    many_to_many_temp = [(m.name, md.manufacturer_id, md.detail_id)
                         for m in manufacturers
                         for md in detail_manufacs
                         if m.id == md.manufacturer_id]

    many_to_many = [(d.name, d.value, m_name)
                    for m_name, m_id, d_id in many_to_many_temp
                    for d in details if d.id == d_id]

    print('Задание В1')
    """
        «Производитель» и «Деталь» связаны соотношением один-ко-многим. 
        Выведите список всех деталей, у которых названия 
        начинаются с буквы «П», и названия их производителей.
    """
    print(res_1(one_to_many))

    print('Задание В2')
    """ 
        «Производитель» и «Деталь» связаны соотношением один-ко-многим. 
        Выведите список производителей с минимальной стоимостью деталей 
        у каждого производителя, отсортированный по минимальной стоимости.
    """
    print(res_2(one_to_many))

    print('Задание В3')
    """
    «Производитель» и «Деталь» связаны соотношением многие-ко-многим. 
    Выведите список всех связанных производителей и деталей, 
    отсортированный по деталям, сортировка по производителям произвольная. 
    """
    print(res_3(many_to_many))

if __name__=="__main__":
    main()
