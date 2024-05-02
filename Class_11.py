'''
f = open("C:/Users/User/Desktop/미래모빌리티공학과/202415039 최지웅/copyright_python/newfile2.txt", 'w')
f.close()
'''

'''
f = open('ex_memo.txt', 'w')
students = ['최지웅', '이동현', '이윤호', '신민성']
for student in students:
    msg = student
    f.write(msg+"\n")
f.close()
'''

'''
file = open('hello.txt', 'wt')
file.write('미국 거지가 한국 천재보다 영어를 잘한다.')
file.close()
'''

'''
f = open('test.txt','a',encoding='UTF-8')

for i in range(4,10):
    data= "%d 번째 줄입니다. \n"%i
    f.write(data)
f.close()
'''

'''
dict1 = {'hello' :1,'brother':2}
file1 = open("Original.txt","w")

str1 = repr(dict1)
file1.write("dict1 ="+ str1 + "\n")

file1.close()
'''

'''
test_file = open("test2.txt","w")

a=13
b=31
test_file.write('%d + %d = %d'%(a,b,a+b)+'\n')
test_file.write('%d - %d = %d'%(a,b,a-b))
test_file.close
'''

'''
from random import randint

with open('test3.txt', 'w') as f:
    f.write('이번 주 로또 번호는 ->')
    for lotto in range(6):
        f.write(str(randint(0,50))+', ')
'''

'''
lines = ['안녕하세요.\n', '파이썬\n', '코딩 도장입니다.\n']

with open('hello2.txt', 'w') as file:
    file.writelines(lines)
file.close()
'''

'''
f= open('ex_memo1.txt', 'w')
students = ['최지웅', '김민준', '손민', '이윤호']
for student in students:
		msg = student
		f.write(msg+' ')
f.close()

f= open('ex_memo1.txt', 'w')
students = ['최지웅', '김민준', '손민', '이윤호']
f.writelines ("\n".join(students))
f.close()
'''

'''
print('\n1.read()')
print(f'위치: {f.tell()}')
s1 = f.read(2)
print(s1)
'''

'''
print('\n2.readline()')
print(f'위치: {f.tell()}')
s2 = f.readline()
print(s2)

s2 = f.readline()
print(s2)
'''

'''
print('\n2.readline()')
print(f'위치: {f.tell()}')
s2 = f.readline()
print(s2)

s2 = f.readline()
print(s2)
'''

'''
print('\n1. read()')
print(f'위치 : (f. tell()}')
s1 = f.read(1)
print (s1)
print(f'위치 : {f.tell()}')
s1 = f.read (1)
print (s1)
print(f'위치 : {f.tell()}')
'''

'''
f = open('test.txt', 'r', encoding='UTF-8')
line = f.readline()
line - line.strip()
print(line) # 1번째 줄입니다.
line - f.readline()
line - line-strip()
print(line) # 2번째 줄입니다.
line = f.readline()
line - line-strip()
print(line) # 3번째 플입니다.
line - f.readline)
line - line.strip()
print(line) # 4번째 줄입니다.

f.close()
'''


f = open('test.txt', 'r', encoding='UTF-8')
line = f.readline()
line - line.strip()
print(line) # 1번째 줄입니다.
line - f.readline()
line - line-strip()
print(line) # 2번째 줄입니다.
line = f.readline()
line - line-strip()
print(line) # 3번째 플입니다.
f.seek(0) # seek() 함수
line - f.readline)
line - line.strip()
print(line) # 4번째 줄입니다.

f.close()

