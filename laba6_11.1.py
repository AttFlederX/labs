print("Введите день в формате (8:4:2016) где 8 это дни , 4 это месяцы,2016 это год")
while True:
    while True:

        while True:
            d = int(input("Введите дни"))
            if 1<d<31:
                break
            else:
                print("Вы ввели не допустимое значение")
                continue
        while True:
            m = int(input("введите месяц"))
            if 1<m<12:
                break
            else:
                print("Вы ввели не допустимое значение")
                continue
        while True:
            g = int(input("введите года"))
            if 1901<g<2016:
                break
            else:
                print("вы ввели не дорпустимое значение")
                continue
        print("вы ввели дату")
        print(d, m, g, sep=":")

        if (d == 31) and (g == 12):
            print("Новый год!!!!Дата будет иметь такой вид!")
            print(d, m, g+1, sep=":")
            break

        elif (m == 2) and (d>27):
            print("в феврале не может быть более 28 дней")
            continue

        elif (m == 4 or m == 6 or m == 9 or m == 11) and (d >= 30):
            print("в данных месяцах не может быть более 30 дней")
            continue

        elif (m == 1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12) and (d == 31):
            print("следующяя дата будет иметь такой вид")
            print("1", m+1, g, sep=":")
            break

        elif (m == 4 or m == 6 or m == 9 or m == 11) and (d == 30):
            print("следующяя дата будет иметь такой вид")
            print("1", m + 1, g, sep=":")
            break

        elif (m == 1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12) and (1<d<31):
            print("следующяя дата будет иметь такой вид")
            print(d+1, m, g, sep=":")
            break

        elif (m == 4 or m == 6 or m == 9 or m == 11) and (1<d<30):
            print("следующяя дата будет иметь такой вид")
            print(d+1, m, g, sep=":")
            break
    ask = input(" Ещё даты считаем [y/n]: ")
    if ask == 'y':
        continue
    else:
        break

