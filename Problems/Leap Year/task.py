year = int(input())


def type_of_year(__year__):
    if ((__year__ % 4 == 0) and (__year__ % 100 != 0)) or (__year__ % 400 == 0):
        print("Leap")
    else:
        print("Ordinary")


type_of_year(year)
