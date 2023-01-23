def decorator(uskor):

    def rast(V_nach, V_kon, t):
        a = (V_kon - V_nach) / t
        uskor(V_nach, V_kon, t)
        S = (V_kon * V_kon - V_nach * V_nach) / 2 * a
        print("Расстояние = ", S)
    return(rast)


def uskor(V_nach, V_kon, t):


    a = (V_kon - V_nach) / t

    print("ускорение = ", a)

    return(a)

try:
    V_nach = (input("Начальная скорость: "))
    V_kon = (input("Конечная скорость: "))
    t = (input("Время: "))

    V_nach = float(V_nach)
    V_kon = float(V_kon)
    t = float(t)
    t != 0

except ValueError:
    print("Данные не являются числами или время равно нулю")

else:
    uskor = decorator(uskor)
    uskor(V_kon, V_nach, t)

