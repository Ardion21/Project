def Fun():
    list_a = []
    print("Введите количество элементом в списке: ")
    size = int(input())

    for number in range(size):
        print("Ввидите элемент " + str(number + 1))
        a = int(input())
        list_a.append(a)

    min = int(list_a[0])
    min_index = 0

    print("Введенный список: ")
    print(list_a)

    for number in range(size):
        test = int(list_a[number])
        if test < min:
            min = list_a[number]
            min_index = number

    list_a = list_a[min_index:] + list_a[:min_index]
    print("Перестроенный список: ")
    print(list_a)

Fun()

