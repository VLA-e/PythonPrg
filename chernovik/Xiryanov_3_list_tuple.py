A = [1, 2, 'privet', 4, 5, (30, 40), [50, 60]]  # spisok-list, karteg-(30, 40) vse izmenyaemoe
print(type(A[5]))# tuple- karteg ON neizmenyaem!!!
print(A[6])#(30, 40)
B = A
print(B)
B[0]=10
print(A)#[10, 2, 'privet', 4, 5, (30, 40), [50, 60]]
print(B[5][1]) # 40
#B[5][1]=3 # TypeError: 'tuple' object does not support item assignmen
print(B[5][1]) # vse rovno 40)
#
#     MASSIV - eto odno typnaya array! a spisok on o4en gibkii)
#

######## spiski - list

A.append([34,34,3])
print(A)

#modulnoePRG

print(__name__)#Xiryanov_3_list_tuple
if __name__ == '__main__':
    print('Library is executed separetly')
else:
    print('library is just imported')

###
objects = []

def create_object(name):
    objects.append("object[" + name +"]")

def print_object():
    print('Vse objecti dobavni')
    for obj in objects:
        print(obj)