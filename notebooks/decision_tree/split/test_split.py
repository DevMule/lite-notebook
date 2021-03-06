# Разделить выборку по выбранному предикату
def test_split(index, value, dataset):
    # создаём два новых списка - левая подвыборка и правая подвыборка
    left = list()
    right = list()

    # проверяем каждый элемент выборки на соответствие заданному предикату
    # предикат состоит из критерия - index и значения критерия - value
    for row in dataset:
        if row[index] < value:  # если соответствует предикату
            right.append(row)  # то отправляем в правое поддерево
        else:  # а если не соответствует предикату
            left.append(row)  # то отправляем в левое поддерево

    # возвращаем наше разбиение
    return left, right