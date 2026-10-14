def convert_temp(temp, Fahrenheit = False):
    c = (5 / 9) * (temp - 32)
    f = (9 / 5) * temp + 32
    if Fahrenheit:
        if temp > -459.67:
            return round(c, 2)
        return None
    if temp < -273.15:
        return None
    return round(f, 2)


def main():
    print(convert_temp(20))


main()