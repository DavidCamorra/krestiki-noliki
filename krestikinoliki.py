nums = list(range(1, 10))

def field():
    print(' +-----------------+')
    for i in range(3):
        print(" | ", nums[0 + i * 3], " | ", nums[1 + i * 3], " | ", nums[2 + i * 3], " |  \n +-----------------+")

field()

step0 = []
stepX = []

def game0():
    a = int(input('На какую клетку поставить нолик? '))
    if stepX.count(a) == 1 or step0.count(a) == 1:
        print('Выберите другую клетку, эта уже занята')
        game0()
    else:
        nums[a - 1] = "0"
        step0.append(a)


def gameX():
    b = int(input('На какую клетку поставить крестик? '))
    if step0.count(b) == 1 or stepX.count(b) == 1:
        print('Выберите другую клетку, эта уже занята')
        gameX()
    else:
        nums[b - 1] = "X"
        stepX.append(b)

i = 1

for i in range(10):
    if i == 9:
        print('Ничья!')
    elif i % 2 == 1:
        game0()
        field()
        if ((step0.count(1) and step0.count(2) and step0.count(3)) == 1) or \
                ((step0.count(1) and step0.count(4) and step0.count(7)) == 1) or \
                ((step0.count(1) and step0.count(5) and step0.count(9)) == 1) or \
                ((step0.count(2) and step0.count(5) and step0.count(8)) == 1) or \
                ((step0.count(3) and step0.count(6) and step0.count(9)) == 1) or \
                ((step0.count(4) and step0.count(5) and step0.count(6)) == 1) or \
                ((step0.count(7) and step0.count(8) and step0.count(9)) == 1) or \
                ((step0.count(3) and step0.count(5) and step0.count(7)) == 1):
            print('Выиграли нолики!')
            break
        else:
            i += 1
    else:
        gameX()
        field()
        if ((stepX.count(1) and stepX.count(2) and stepX.count(3)) == 1) or \
                ((stepX.count(1) and stepX.count(4) and stepX.count(7)) == 1) or \
                ((stepX.count(1) and stepX.count(5) and stepX.count(9)) == 1) or \
                ((stepX.count(2) and stepX.count(5) and stepX.count(8)) == 1) or \
                ((stepX.count(3) and stepX.count(6) and stepX.count(9)) == 1) or \
                ((stepX.count(4) and stepX.count(5) and stepX.count(6)) == 1) or \
                ((stepX.count(7) and stepX.count(8) and stepX.count(9)) == 1) or \
                ((stepX.count(3) and stepX.count(5) and stepX.count(7)) == 1):
            print('Выиграли крестики!')
            break
        i += 1

