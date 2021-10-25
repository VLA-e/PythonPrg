########################### OSNOVI PYTHON ######################################
print(3 / 57)
print(round(3 / 57, 3))  # Vnimanie, okruglyaet na verx!!
print(type(3 / 55))  # class float
print('Vnimanie, okruglyaet na verx!!')

print("############################# VARIABLES & SIMPLE MATH #######################")

a = 10
b = 5
c = 7

import math

p = (a + b + c) / 2
area = math.sqrt(p * (p - a) * (p - b) * (p - c))
print('Area is=', round(area, 3))

print('Voer eerste getal in')
x = float(input())  # funciya "input" prinimaet strokovoe zna4enie!!!
print('Voer tweede getal in')
y = float(input())
print('Som van de getallen is=', x + y)

print("############################# BOOOL ########################################")

print(type(x == y))  # class bool
are_equal = 2 == x
print(are_equal)
are_equal = None  # kogda xo4esh ispolzovat peremennyu no ne inicializirovat ee

print("############################### STRING #######################################")

print('Hello')
print("I'm Vladimir")  # kogda xo4esh propisat appostraf i kavi4ki
print("I'm Vlad and i'm a \"strong\" programmer")  # kogad nygno propisat kavi4i i appostraf
print("I'm Vlad and i'm a \"strong\\\" programmer")  # kogad nygno propisat kavi4i i appostraf i slash
print("c:\\users\\EnigineerSpock")  # kogda nygno propisat backSlash
print(r'c:\users\EnigineerSpock')  # ili prosto ispolzovat- r''
print("I'm Vladimir \r\nI'am a programmer")
greeting = str("hello, i'm Vladimir")
print(greeting)
print(greeting[0])
print(greeting[-1])
# greeting[0]='h'# stroki yavlyatsua neizmenyaemimi posle ee sodaniya!!!

print("############################## SREZI (PODSTROKI) ##############################")

print(greeting[2:])  # srez- vivesti na4inaya so vtrogo elemnta stroki
print(greeting[0:3])  # srez - vivesti na4inaya s 0go i po 3ti element stroki
print(greeting[::3])  # eto shag vivoda atroki
print(greeting[0:20:2])  # [na4alnii elemnt: kone4nii element: shag vivoda stroki]
print('My name' + ' is' + ' Vladimir')  # eto nerekomenduetsya - iz za nekonomnsoti pamyati!
hello = 'HELLO'
world = 'WORLD!'
print("%s %s" % (hello, world))  # Lu4she delat TAK
print("{} {}".format(hello, world))  # Ili TAK
print('2' + '3')
print(float('2') * float('3'))

print("######################## FUNCTIONS AND FORMATTING OF STRINGS ####################")
x = "hello, my name is Vladimir"
print(len(x))  # Pods4et simvolov v stroke s pomos4iu funcii "len()"
print(x[len(x) - 1])  # Vivod poslednego elemneta sroki
print(x.count('l'))  # Pods4et bukov 'l' v sroke "x"
print(x.capitalize())  # Funciaya "capitalyze" delaet tolko pervii simbol stroki Bolshim a ostalnie malenkimi
print("--------------------------------------")

upeer_cased = x.upper()  # vse simboli stroki budu v bolshom registre
print(upeer_cased)
print("--------------------------------------")

lower_cased = x.lower()  # ili vse simboli stroki budu v nignem registre
print(lower_cased)
print("--------------------------------------")

print(upeer_cased.isupper())  # Proverka!
print(lower_cased.islower())
print(x.isupper())
print(x.islower())
print("--------------------------------------")

print(x.find('l'))  # Naiti nomer(int) elementa
print(x.find('l', 5))  # Naiti nomer(int) elementa v stroke na4inaya s 5go
print(x.find('l', 5, 8))  # Naiti nomer(int) elementa na4inaya s 5go i zakan4ivaya 8, avot
# resultat " -1 " ozna4aet 4to element nenaiden !!
print("--------------------------------------")

print(x.find('my'))  # Na4inaetsya s sedmogo 7go simbola
print("--------------------------------------")

print('123abcd'.isalnum())  # Proverka, sostoit li stroka toko is bukv i 4isel??
print('123abcd!!'.isalnum())

print("--------------------------------------")

print("  ".isspace())  # Proverka stroki nanali4ie elementov (pystaya li ona?)
print("".isspace())
print("--------------------------------------")

empty_string = ""
print(empty_string == "")
print("--------------------------------------")

empty_string = ' '
print(empty_string.strip(' ') == "")
if not empty_string:
    print('not empty')
else:
    print('empty')
print("--------------------------------------")

h = 'hello'  # metod startswitch i endswitch- proveryaet na4alnie i kone4nie elemti stroki na ix nali4ie
print(h.startswith('he'))
print(h.endswith('lo'))
print("--------------------------------------")

split = h.split('l')  # metod slplit ydalyaet vibranni elemnt iz spiska
print(type(split))
print(split)
split = h.split('e')
print(split)
print(h)
print("--------------------------------------")
print('!!!Primer razbora stroki po elemntam i privedeniya ix k tipy int!!!!!')
data = '12;10;8;10'
d = 0
separeted_datda = data.split(';')  # Primer razbora stroki po elemntam i privedeniya ix k tipy 'int'
print(separeted_datda)
for d in separeted_datda:
    print(int(d))

print("--------------------------------------")
def print_str(str_1, len): # Funkciya dlya vivoda elementov stroki
    i = 0
    while len:
        print(str_1[i])
        len -= 1
        i += 1


tt = 'abracadabraaaa'
print_str(tt, len(tt))
print("--------------------------------------")

python = "Python is fun"
print(python.partition('is '))
print(python.partition('not '))
python = "Python is fun,isn't it?"
print(python.partition('is'))
print("######################## FORMATTING OF STRINGS ####################")

print("Hello, my name is {}".format("Vladimir"))
my_name = 'Vladimir'
print("Hello, my name is {}".format(my_name))
print("Hello, my name is {} and i'am {} years old".format("Vladimir", 36))  # Xyinya , kotorya yslognyaet kod
print("Hello, my name is {0} and i'am {1} years old".format("Vladimir", 36))
print("Hello, my name is {1} and i'am {0} years old".format("Vladimir", 36))

print("--------------------------------------")
pi = 3.1415
print('Pi equals {pi:1.2f}'.format(pi=pi))  # okruglili na 2 znaka posle zapyatoi

print("--------------------------------------")
q = range(1, 12, 1)  # iteriruemii object- range(start , stop_by (do 4esla) , step)
print(type(q))
print(*q)  # tak mogno kagdii elemnt object range vivesti
for i in q:
    print(i)

print("--------------------------------------")
w = [(1, 10), (2, 12), (3, 45), (5, 565)]  # karteg-
print(type(w))
print(len(w))
for angle, length in w:
    print(angle, length)

print("######################## OPERATORI SRAVNENIYA ####################")
print(3 > 3)
print(2 == 3)
print(3 != 4)
print('string' == 'another string')
f = 'string'
g = 'string'
print(f.lower() == g.lower())
print(1 < 2 < 3)
print(1 < 2 and 2 < 3)
print(1 > 2 and 2 < 3)
print(1 > 2 or 2 < 3)

print('--------------------------------------')

is_admin = True
file_exists = True
schould_open_file = is_admin and file_exists

print('--------------------------------------')

is_admin = False
if not is_admin:
    print('not an admin')
if is_admin == False:
    print('not an admin')

print("######################## RABOTA S FALAMI ** FILE SYSTEEM  ####################")

file = open('sample.TXT')  # Otkrivaem file sample.txt
print(file)  # <_io.TextIOWrapper name='sample.TXT' mode='r' encoding='cp1251'>
data = file.read()  # s4itivaem file 'file' v premennyu 'data'
print(data)
print(file.read())  # Teper mi v konce file i nam ni4ego ne vivoditsya! No kursorom mogno ypravlyat
file.seek(0)  # Perevodim kurso v na4olo
print(file.read())  # I mogem file snovo pro4itat
file.seek(0)
print(type(data))  # type 'str'

print('--------------------------------------')
lines = file.readlines()
print(type(lines))  # <class 'list'>
print(lines)  # vivod v stroky "['Name|Phone\n', 'John;1233\n', 'Bob;5678\n', 'Alice;9432']"
print(len(lines))  # 4 stroki

print('--------------------------------------')
sample_file = open(r'C:\Users\vladi\Documents\PythonProgi\Test001\sample.TXT')  # Mogni file i tak otkrit
print(sample_file)  # <_io.TextIOWrapper name='sample.TXT' mode='r' encoding='cp1251'> Tyt mode = r -ozna4aet na 4tenie
data = sample_file.read()  # s4itivaem file 'sample_read' v premennyu 'data'
print(data)  # Vivodim filw 'sample_file'
sample_file.seek(0)  # Perevodim kurso v na4olo

file.close()  # Zakrivaem file posle raboti
sample_file.close()  # Zakrivaem file posle raboti
print(file.closed)  # I mogem proverit zakrit li file?
print(sample_file.closed)  # I mogem proverit zakrit li file?

print('--------------------------------------')

# dlya zakritiya file avtomati4eski mogno ispolzovat slduus4ie viragenie
with open('sample.TXT') as sample_file:
    sample_data = sample_file.read()
print(sample_data)

print('--------------------------------------')
# with open('sample.TXT', mode='w') as sample_file: # Zdes file otkrivaetsya tolko na 4tenie  (mode='w')i..
# data = sample_file.read()  # pisat v nego nelzya (io.UnsupportedOperation: not readable)

print('--------------------------------------')
with open('sample.TXT', mode='a') as sample_file:  # mode='a' ozna4aet dopolnit file
    sample_file.write('Vladimir; 21324')
with open('sample.TXT', mode='r') as sample_file:
    sample_data = sample_file.read
    print(sample_data)

print('--------------------------------------')
with open('sample.TXT', mode='r+') as sample_file:
    sample_file.seek(0, 2)  # 2- kyrsor v samii konec
    sample_file.write('\nToub;5626')  # Dobavlyaem Toub
    sample_file.seek(0)  # Perevodim kyrsor v konec
    print(sample_file.read())  # I vivodim dannie

print('--------------------------------------')
# with open('abrbrbr.TXT', mode='w+') as spell_file:
#    spell_file.write('abra-cadabra- abrarabbabbb')
#    spell_file.seek(0)
#    print(spell_file.read())

print("######################## str, bytes, bytearray  ####################")

import sys

print(sys.getdefaultencoding())  # UTF8
z = 'hello'
enc_ascii = z.encode('ascii')
enc_utf8 = z.encode('utf8')
enc_utf16 = z.encode('utf16')

print(type(enc_ascii))
print(enc_ascii)
print(enc_utf8)
print(enc_utf16)

print(len(enc_ascii))  # 1 byte na symbol
print(len(enc_utf8))  # 1 byte na symbol
print(len(enc_utf16))  # 2 byta na symbol

print('--------------------------------------')
str_in_bytes = b'hello'
str_in_bytes = z.encode('utf8')
str_in_text = 'hello'
print(type(str_in_bytes))  # <class 'bytes'>
print(type(str_in_text))  # <class 'str'>

print('bytes'.encode('utf8'))
print(str_in_bytes[0])  # 104
print(str_in_text[0])  # h

print('--------------------------------------')
ba = bytearray(b'hello')
ba[0] = 87  # menyaem 'h' na 'w'
print(ba)  # bytearray(b'Wello')

result = str(str_in_bytes)  # pri preobrazovanii v str nygo ykazat format UTF8
print(result)  # b'hello'
print(len(result))  # 8 bytes

result = str(str_in_bytes, 'utf8')  # pri preobrazovanii v str nygo ykazat format UTF8
print(result)  # hello
print(len(result))  # 5 bytes

print('--------------------------------------')
result = str_in_bytes.decode('utf8')
print(result)

print('--------------------------------------')
# jpeg = [123, 3, 255, 0, 100]
# with open(r'C:\tmp\btest.bin', 'w+b') as file:
#   file.write(bytes(jpeg))

print('######## SMOTRI DZ V FILE DZ.PY )#####################\n')

x = int(input('vvedite 4eslo krugek s kofem\n\r'))
print('Vi poly4aete {} bonusnnix krugek s kofee\n '.format(int(x / 6)))

print('################# DZ n2 #############################')


