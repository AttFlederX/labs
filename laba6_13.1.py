from enum import Enum
class country(Enum):
    Germany = 1
    Cuba = 2
    Laos = 3
    Bangladesh = 5
    Ukraine = 6
class continent(Enum):
    Asia = 1
    America = 2
    Europe = 3
while True:
    s = country[input("country: ")]
    if s.name == country.Cuba.name:
            print(continent.America.name)
    elif (s.name == country.Laos.name) or (s.name == country.Bangladesh.name):
            print(continent.Asia.name)
    elif (s.name == country.Germany.name) or (s.name == country.Ukraine.name):
            print(continent.Europe.name)


