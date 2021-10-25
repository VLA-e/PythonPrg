# ========================= list ===========================

print('\n========================= list ===========================\n')
int_list = [1, 2, 3]
mix_list = [1, 2.0, 'string']  # obi4no eto odnorodnii dannie v liste
print('%s No obi4no eto odnorodnii dannie v liste\n' % mix_list)
print(len(mix_list))
print(int_list[0])
print(int_list[-1])  # napi4ataet poslednii element lista
print('list[-1] :Napi4ataet poslednii element lista %s\n' %int_list[-1])
print('V liste mogno takge delat srezi')
print('Naprimer -int_list[1:]- zabraet vse 4isla (elementi) na4inaya so 2go %s' % int_list[1:])
names1 = ['John', 'Bob', 'Alice']
names2 = ['Tracy', 'Elijah', 'Mason']
names_combined = names1 + names2
print(names_combined)
print(names1)
names1[0] = 'Liam'
print('\nList v otli4ii ot spiskov yavlyaetsa izmenyaemim tipom!!! perepeshiem pervii element - names1[0] ="Liam" %s' % names1)
names1.append('Vladimir')
print('\nNy ili dobavit imya(element) pri pomos4i objecta append -names1.append(''Vladimir'')-  %s' % names1)
names1.pop(0)
print('\nNy iliydalayt imya(element) pri pomos4i objecta pop po opredelennomy adresy! -names1.pop(0)-  %s \n' % names1)
names1.sort()
print('\nTakge list mogno sotirovat bojectom sort -names1.sort()- %s\n' % names1)
letters = ['aa', 'ab', 'ac']
print(letters)
letters = ['abc', 'a', 'ab']
print('Yporyado4im list po dlinne elementa komansdoi -letters.sort(key=len)')
letters.sort(key=len)
print(letters)
numbers = [2, 1, 1, 4, 10, 9, 5]
numbers.sort()
print('\nTak ge mogno pomenyat posledovatelnost vivoda elementov lista -numbers.reverse()-')
numbers.reverse()
print(numbers)
print('\nMogno vstavit po adresy lista, 4islo 22 megdu pervim i vtorim -numbers.insert(posle elemnta, kakoi elemnt)-')
numbers.insert(1, 22)
print(numbers)
print('\nMogno po indexy naiti elemnt -numbers.index(elemnt)-')
numbers.index(5)
print(numbers)
print('\nMogno naiti skolko 1 est v list -numbers.count(kol elemntov v liste)-')
print(numbers.count(1))
print('\nMogno Tak ge skopirovat list(spisok) objektom -copy=numbers.copy()- vse izmeneniya orig list bydyt i copy')
copy = numbers.copy()
print('copy numbers %s'%copy)
print('\nMogno Tak ge i ydalit(o4istit) list objektom -numbers.clear()- ')
numbers.clear()
print(numbers)
print('\n========================= Dictionary ===========================\n')

train = [
    ([0, 0, 0], 0),
    ([0, 0, 1], 1),
    ([0, 1, 0], 0),
    ([0, 1, 1], 0),
    ([1, 0, 0], 1),
    ([1, 0, 1], 1),
    ([1, 1, 0], 0),
    ([1, 1, 1], 1),
]
for i in train:
    print(i)



