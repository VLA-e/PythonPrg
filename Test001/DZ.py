import math

print('################# DZ n1 #############################\n')

x = int(input('vvedite 4eslo krugek s kofem\n\r'))
print('Vi poly4aete {} bonusnnix krugek s kofee\n '.format(int(x / 6)))

print('################# DZ n2 #############################')

a = {'x': input('voer x coordinaat van punt a\n'), 'y': input('voer y coordinaat van punt a\n')}
b = {'x': input('voer x coordinaat van punt b\n'), 'y': input('voer x coordinaat van punt b\n')}
print("a is van het type %s" % type(a))
print(a)
print(b)
AC = float(b['x']) - float(a['x'])
BC = float(b['y']) - float(a['y'])
print(AC)
print(BC)
lengte = math.sqrt((AC**2) + (BC**2))  #  ili math.sqrt = **0.5
print("расстояние между заданными точками = %.3f" % lengte)

print("AC is van het type %s" % type(AC))
print('len van x is {}'.format(len(a)))
print('len van y is {}'.format(len(b)))

print('################# DZ n3 #############################\n')

ferma = {'kippen': 2, 'varkens': 4, 'koeien': 4}
apkip = int(ferma['kippen']) * int(input('Voer het aantal kippen in\n'))
apvar = int(ferma['varkens']) * int(input('Voer het aantal varkens in\n'))
apkoe = int(ferma['koeien']) * int(input('Voer het aantal koeien in\n'))
print('Totale aantal potten is: %d' % (apkoe+apkip+apvar))
print(type((apkoe+apkip+apvar)))
print(ferma)