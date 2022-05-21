import random


def matrix_admin(size=8, bomb=8):
    sapper_matrix = [[0 for y in range(size)] for x in range(size)]

    bombs = []
    i = 0
    while i < bomb:
        x = random.randint(0, size - 1)
        y = random.randint(0, size - 1)
        if sapper_matrix[x][y] != -1:
            sapper_matrix[x][y] = -1
            i += 1
            bombs.append((x, y))
        else:
            continue

    angle = [(0, 0), (0, size - 1), (size - 1, 0), (size - 1, size - 1)]
    for elem in angle:
        if elem in bombs:
            if elem == angle[0]:
                sapper_matrix[elem[0] + 1][elem[1]] += 1
                sapper_matrix[elem[0] + 1][elem[1] + 1] += 1
                sapper_matrix[elem[0]][elem[1] + 1] += 1
            elif elem == angle[1]:
                sapper_matrix[elem[0]][elem[1] - 1] += 1
                sapper_matrix[elem[0] + 1][elem[1]] += 1
                sapper_matrix[elem[0] + 1][elem[1] - 1] += 1
            elif elem == angle[2]:
                sapper_matrix[elem[0] - 1][elem[1]] += 1
                sapper_matrix[elem[0]][elem[1] + 1] += 1
                sapper_matrix[elem[0] - 1][elem[1] + 1] += 1
            else:
                sapper_matrix[elem[0] - 1][elem[1]] += 1
                sapper_matrix[elem[0]][elem[1] - 1] += 1
                sapper_matrix[elem[0] - 1][elem[1] - 1] += 1

    left_edge = [(x, 0) for x in range(1, size - 1)]
    right_edge = [(x, size - 1) for x in range(1, size - 1)]
    top_edge = [(0, x) for x in range(1, size - 1)]
    lower_edge = [(size - 1, x) for x in range(1, size - 1)]

    for elem in left_edge:
        if elem in bombs:
            sapper_matrix[elem[0] + 1][elem[1]] += 1
            sapper_matrix[elem[0] - 1][elem[1]] += 1
            sapper_matrix[elem[0] + 1][elem[1] + 1] += 1
            sapper_matrix[elem[0] - 1][elem[1] + 1] += 1
            sapper_matrix[elem[0]][elem[1] + 1] += 1

    for elem in right_edge:
        if elem in bombs:
            sapper_matrix[elem[0] - 1][elem[1]] += 1
            sapper_matrix[elem[0] + 1][elem[1]] += 1
            sapper_matrix[elem[0]][elem[1] - 1] += 1
            sapper_matrix[elem[0] - 1][elem[1] - 1] += 1
            sapper_matrix[elem[0] + 1][elem[1] - 1] += 1

    for elem in top_edge:
        if elem in bombs:
            sapper_matrix[elem[0]][elem[1] - 1] += 1
            sapper_matrix[elem[0]][elem[1] + 1] += 1
            sapper_matrix[elem[0] + 1][elem[1]] += 1
            sapper_matrix[elem[0] + 1][elem[1] + 1] += 1
            sapper_matrix[elem[0] + 1][elem[1] - 1] += 1

    for elem in lower_edge:
        if elem in bombs:
            sapper_matrix[elem[0]][elem[1] + 1] += 1
            sapper_matrix[elem[0]][elem[1] - 1] += 1
            sapper_matrix[elem[0] - 1][elem[1]] += 1
            sapper_matrix[elem[0] - 1][elem[1] + 1] += 1
            sapper_matrix[elem[0] - 1][elem[1] - 1] += 1

    middle = [[(y, x) for x in range(1, size - 1)] for y in range(1, size - 1)]

    for row in middle:
        for elem in row:
            if elem in bombs:
                sapper_matrix[elem[0] + 1][elem[1]] += 1
                sapper_matrix[elem[0] - 1][elem[1]] += 1
                sapper_matrix[elem[0]][elem[1] + 1] += 1
                sapper_matrix[elem[0]][elem[1] - 1] += 1
                sapper_matrix[elem[0] + 1][elem[1] + 1] += 1
                sapper_matrix[elem[0] - 1][elem[1] - 1] += 1
                sapper_matrix[elem[0] + 1][elem[1] - 1] += 1
                sapper_matrix[elem[0] - 1][elem[1] + 1] += 1

    for elem in bombs:
        sapper_matrix[elem[0]][elem[1]] = -1

    return sapper_matrix


def open_zero(x, y, matrix, matrix_p, size):
    if matrix[x][y] == 0:
        angle = [(0, 0), (0, size - 1), (size - 1, 0), (size - 1, size - 1)]
        el = (x, y)
        if el in angle:
            if el == angle[0]:
                matrix_p[x+1][y] = matrix[el[0] + 1][el[1]]
                matrix_p[x+1][y+1] = matrix[el[0] + 1][el[1] + 1]
                matrix_p[x][y+1] = matrix[el[0]][el[1] + 1]
            elif el == angle[1]:
                matrix_p[x][y-1] = matrix[el[0]][el[1] - 1]
                matrix_p[x+1][y] = matrix[el[0] + 1][el[1]]
                matrix_p[x+1][y-1] = matrix[el[0] + 1][el[1] - 1]
            elif el == angle[2]:
                matrix_p[x-1][y] = matrix[el[0] - 1][el[1]]
                matrix_p[x][y+1] = matrix[el[0]][el[1] + 1]
                matrix_p[x-1][y+1] = matrix[el[0] - 1][el[1] + 1]
            else:
                matrix_p[x-1][y] = matrix[el[0] - 1][el[1]]
                matrix_p[x][y-1] = matrix[el[0]][el[1] - 1]
                matrix_p[x-1][y-1] = matrix[el[0] - 1][el[1] - 1]

        left_edge = [(x, 0) for x in range(1, size - 1)]
        right_edge = [(x, size - 1) for x in range(1, size - 1)]
        top_edge = [(0, x) for x in range(1, size - 1)]
        lower_edge = [(size - 1, x) for x in range(1, size - 1)]

        if el in left_edge:
            matrix_p[x+1][y] = matrix[el[0] + 1][el[1]]
            matrix_p[x-1][y] = matrix[el[0] - 1][el[1]]
            matrix_p[x+1][y+1] = matrix[el[0] + 1][el[1] + 1]
            matrix_p[x-1][y+1] = matrix[el[0] - 1][el[1] + 1]
            matrix_p[x][y+1] = matrix[el[0]][el[1] + 1]

        if el in right_edge:
            matrix_p[x-1][y] = matrix[el[0] - 1][el[1]]
            matrix_p[x+1][y] = matrix[el[0] + 1][el[1]]
            matrix_p[x][y-1] = matrix[el[0]][el[1] - 1]
            matrix_p[x-1][y-1] = matrix[el[0] - 1][el[1] - 1]
            matrix_p[x+1][y-1] = matrix[el[0] + 1][el[1] - 1]

        if el in top_edge:
            matrix_p[x][y-1] = matrix[el[0]][el[1] - 1]
            matrix_p[x][y+1] = matrix[el[0]][el[1] + 1]
            matrix_p[x+1][y] = matrix[el[0] + 1][el[1]]
            matrix_p[x+1][y+1] = matrix[el[0] + 1][el[1] + 1]
            matrix_p[x+1][y-1] = matrix[el[0] + 1][el[1] - 1]

        if el in lower_edge:
            matrix_p[x][y+1] = matrix[el[0]][el[1] + 1]
            matrix_p[x][y-1] = matrix[el[0]][el[1] - 1]
            matrix_p[x-1][y] = matrix[el[0] - 1][el[1]]
            matrix_p[x-1][y+1] = matrix[el[0] - 1][el[1] + 1]
            matrix_p[x-1][y-1] = matrix[el[0] - 1][el[1] - 1]

        middle = [[(y, x) for x in range(1, size - 1)] for y in range(1, size - 1)]

        for row in middle:
            if el in row:
                matrix_p[x+1][y] = matrix[el[0] + 1][el[1]]
                matrix_p[x-1][y] = matrix[el[0] - 1][el[1]]
                matrix_p[x][y+1] = matrix[el[0]][el[1] + 1]
                matrix_p[x][y-1] = matrix[el[0]][el[1] - 1]
                matrix_p[x+1][y+1] = matrix[el[0] + 1][el[1] + 1]
                matrix_p[x-1][y-1] = matrix[el[0] - 1][el[1] - 1]
                matrix_p[x+1][y-1] = matrix[el[0] + 1][el[1] - 1]
                matrix_p[x-1][y+1] = matrix[el[0] - 1][el[1] + 1]


def matrix_print(matrix):
    q = ''
    for elem in matrix:
        for i in elem:
            if i == -1:
                q += ' ' + str(i)
            else:
                q += '  ' + str(i)
        print(q)
        q = ''


def matrix_plyer(size=8):
    matrix = [['X' for y in range(size)] for x in range(size)]
    return matrix


def sapper_start(size=8, bomb=8):
    matrix_a = matrix_admin(size, bomb)
    matrix_print(matrix_a)

    matrix_p = matrix_plyer(size)
    input("Привіт!\n"
          "Щоб почати гру натисни 'Enter'")

    while True:
        matrix_print(matrix_p)

        xy = input("Яку клітинку відкриваємо?").split(' ')
        x = int(xy[0]) - 1
        y = int(xy[1]) - 1

        if matrix_a[x][y] == -1:
            print("Міна!\nГра закінчена")
            matrix_print(matrix_a)
            break

        elif matrix_a[x][y] == 0:
            print("Молодець! Продовжуемо...")
            matrix_p[x][y] = matrix_a[x][y]
            open_zero(x, y, matrix_a, matrix_p, size)


        else:
            print("Молодець! Продовжуемо...")
            matrix_p[x][y] = str(matrix_a[x][y])
        c = 0
        for elem in matrix_p:
            for i in elem:
                if i == 'X':
                    c += 1
        print('Залишилося розмінувати ' + str(c-bomb) + ' клітинок')
        if c == bomb:
            print('Гра пройдена!')
            break


sapper_start(4, 4)
