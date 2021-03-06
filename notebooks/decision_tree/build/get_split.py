# Расчитать индекс Джини для данного разделения
# эта реализация позволяет работать с любым количеством разделений
def gini_index(groups,  # список подвыборок
               classes  # список всех возможных классов
               ):
    # посчитать количество элементов в подвыборках
    total_samples = sum([len(group) for group in groups])

    # сумма индексов Джини для всех подвыборок
    gini = 0

    for group in groups:  # для каждой подвыборки

        group_size = len(group)

        if group_size == 0:
            # в случае, если подвыборка равна нулю, нет смысла считать
            # и чтобы избежать ошибки деления на ноль,
            # завершаем этот цикл, начинаем следующий
            continue

        # score - сумма квадратов пропорций
        score = 0

        for class_val in classes:
            # расчитываем в выборке пропорции для каждого класса
            class_count = [ob[-1] for ob in group].count(class_val)
            proportion = class_count / group_size
            # суммируем квадраты пропорции
            score += proportion * proportion

        # прибавляем индекс Джини для данной подвыборки
        # к итоговому значению индекса Джини
        gini += (1 - score) * (group_size / total_samples)

    return gini  # критерий джини для данного разделения


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


# Внутренний узел
class InnerNode:
    def __init__(self, criterion, value, groups):
        # содержит в себе предикат, который состоит из
        self.criterion = criterion  # критерия
        self.value = value  # и значения критерия

        self.left, self.right = groups  # ссылки на последующие узлы


# Выбрать лучшее разбиение для датасета
def get_split(dataset):
    class_values = list(set(row[-1] for row in dataset))

    best_criterion = 0
    best_value = 0
    best_gini = 99999
    best_groups = None
    # пройтись по всем столбцам, кроме последнего
    # то есть, пройтись по всем критериям т.к. последний столбец - класс
    for index in range(len(dataset[0]) - 1):
        # пройтись по каждой строчке в выборке
        for row in dataset:
            # здесь мы проходим по каждому критерию каждого элемента выборки,
            # пробуем разделить выборку по выбранному критерию и расчитать его индекс Джини
            groups = test_split(index, row[index], dataset)
            gini = gini_index(groups, class_values)  # ! gini_index мы реализовали в предыдущей статье

            # если значение индекса Джини лучше чем у предыдущего разбиения,
            # то сохраняем его. Таким образом у нас в конце останется лучшее разбиение
            if gini < best_gini:
                best_criterion = index
                best_value = row[index]
                best_gini = gini
                best_groups = groups

    # возвращаем лучшее разбиение и его предикат
    return InnerNode(best_criterion, best_value, best_groups)
