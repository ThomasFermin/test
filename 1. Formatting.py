def convert(degreesCelsius):
    return degreesCelsius * 1.8 + 32


def table():
    print('F', 'C')
    for degreeC in range(-30, 41, 10):
        print('{0} {1}'.format(convert(degreeC), degreeC))


table()