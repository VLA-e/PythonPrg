print('Obi4nii slovar ne smotrit na poryadok elementov')
# dictionary 1
d1 = {}
d1['a'] = 'A'
d1['b'] = 'B'
d1['c'] = 'C'
# dictionary 2
d2 = {}
d2['b'] = 'B'
d2['a'] = 'A'
d2['c'] = 'C'
# dictionary 3
d3 = {}
d3['a'] = 'A'
d3['b'] = 'B'
d3['c'] = 'C'
print(d1 == d2)
print(d1 == d3)

for k, v in d1.items():
    print(k, v)

print('A vot ordered slovar smotrit na poryadok elementov')
from  collections import OrderedDict
# dictionary 1
d1 = OrderedDict()
d1['a'] = 'A'
d1['b'] = 'B'
d1['c'] = 'C'
# dictionary 2
d2 = OrderedDict()
d2['b'] = 'B'
d2['a'] = 'A'
d2['c'] = 'C'
# dictionary 3
d3 = OrderedDict()
d3['a'] = 'A'
d3['b'] = 'B'
d3['c'] = 'C'

print(d1 == d2)
print(d1 == d3)

for k, v in d2.items():
    print(k, v)

print('==============Tuple ili Karteg=============\n')
print('===Ego mogno vosprinimat kak neizmenyaemii list(spisok)!!=========')
strings = ('str1', 'str2', 'str3')
#strings[0] = 'str0' # nevozmogno dobavit element!!
print('===No Tuple eto nabor dannix kotorie svuazani megdy soboi i zasi4eni ot izmeneniya!!=========')

person = ['John', 'Silver', 22]# eto list(spisok)-izmenyaemii
print(person)
print(type(person))

person_info = ('John', 'Silver', 22)# eto tuple(karteg)-neizmenyaemii
print(person_info)
print(type(person_info))

print(len(person_info))
print(person_info[-1])
print(person_info[0])


print(person_info.count('John\n'))# skolko John v tuple
print('==============NamedTuple ili Seti  (eto yge class)=============\n')

players = [('Carlsen', 1990, 2842), ('Caruana', 1992, 2822), ('Mamedyarov', 1985,2801)]
print(players[0]) # vivodom pervii element spiska
#players[0].name  # A vot eto yge ne rabotaet i tyt prigodyatsya svoistva tupla!!

print('==============NamedTuple ili Seti  (eto yge class)=============\n')
from collections import namedtuple

Player = namedtuple('Player', 'name age rating')
players = [Player('Carlsen', 1990, 2842), Player('Caruana', 1992, 2822), Player('Mamedyarov', 1985,2801)]
print(players[0])
print(players[0].name)

print('==============Logi4eskie operatori vetvleniya =============\n')

if True:
    print('Indeed, true')

if 3 > 2:
    print('3 is less than 2')

selected_character = input('Enter a race\n ')

if selected_character == 'Protos':
    print('Protos is the most powerful race')
elif selected_character == 'Zerg':
    print('Zorg is the most weak race but it is speads like a plague')
else:
    print('Hmm... it seems we have a new race')