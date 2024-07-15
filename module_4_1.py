task = 'Домашняя работа по уроку "Модули и пакеты"'
avtor = 'Студент Крылов Эдуард Васильевич'
thanks = 'Благодарю за внимание :-)'
print()
print(task)
print(avtor)
print()
from true_math import divide as true_div
from fake_math import divide as fake_div


# Исходный код (названия функций могут быть другими):
res1 = fake_div(69, 3)
res2 = fake_div(3, 0)
res3 = true_div(49, 7)
res4 = true_div(15, 0)
print(res1)
print(res2)
print(res3)
print(res4)
print()
print(thanks)