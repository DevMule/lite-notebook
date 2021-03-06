# проверим реализацию на небольшом кусочке выборки из Ирисов Рональда Фишера
criterions = ["Длина чашелистника", "Ширина чашелистника", "Длина лепестка", "Ширина лепестка", "класс"     ]
dataset = [[  5.1,                  3.5,                    1.4,              0.2,              "setosa"    ],
           [  5.3,                  3.7,                    1.5,              0.2,              "setosa"    ],
           [  5.0,                  3.3,                    1.4,              0.2,              "setosa"    ],
           [  6.3,                  3.3,                    4.7,              1.6,              "versicolor"],
           [  5.8,                  2.7,                    3.9,              1.2,              "versicolor"],
           [  6.0,                  2.7,                    5.1,              1.6,              "versicolor"],
           [  6.7,                  3.3,                    5.7,              2.1,              "virginica" ],
           [  7.2,                  3.2,                    6.0,              1.8,              "virginica" ],
           [  5.9,                  3.0,                    5.1,              1.8,              "virginica" ]]

split = get_split(dataset)
print('лучший предикат:', criterions[split.criterion], '<', split.value)

print('правое поддерево:')
for obj in split.right:
    print("- ", obj[-1], criterions[split.criterion], "=", obj[split.criterion])

print('левое поддерево:')
for obj in split.left:
    print("- ", obj[-1], criterions[split.criterion], "=", obj[split.criterion])
