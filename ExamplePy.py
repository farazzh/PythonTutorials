'''print(1+3)
print('i\'m abc')
print(2.7/3.9)
#print(4**2)
'''
cond = 1
while cond < 10:
    print(cond)
    cond+=1
'''while True:
    print('infinte')

exampleList = [2,3,5,31,3]

for item in exampleList:
    print(item)

for x in range(5,10):
    print(x)'''

def example():
     x=2
     y=4
     print(x+y)

     if x<y:
         print(x,'is less than',y)

example()

def addition(num1,num2):
    ans = num1+num2
    return ans

x = addition(5,6)
print(x)

def website(background_color='White',
            font='TNR',
            font_size=11):
    print('font:',font)
    print('Bg:',background_color)
    print('font size:',font_size)

#website('TNR','White',11)
#website(background_color='White',font='TNR',font_size=11)
#website()
'''website(font='MS')

x=6

def example():
    z=5
    print(z)

#example()
def example2():
    z=7
    print(z)
    #print(x)
    y=x+1
    print(y)

example2()

writeMe = 'Example Text'
saveF = open('exwrite.txt','w')
saveF.write(writeMe)
saveF.close()

appendMe = 'Even more text'
saveF= open('exwFile.txt','a')
saveF.write('\n')
saveF.write(appendMe)
saveF.close()'''

'''readMe = open('exwFile.txt','r').read()
print(readMe)

readme2 = open('exwFile.txt','r').readlines()
print(readme2)
'''

'''class calc:
    def add(x,y):
        answer = x+y
        print(answer)
        
    def sub(x,y):
        answer = x-y
        print(answer)

    def mult(x,y):
        answer = x*y
        print(answer)'''
''' name = input('What is yout name?: ')
print('Hello',name)'''

#from statistics import mean as m
#from statistics import mean as m, stdev as s
#import statistics as s
#from statitics import *
#exList = [5,3,6,9,8,9,93,13,31]
'''x=statistics.mean(exList)
print(x)

x=statistics.median(exList)
print('Median:',x)

x = statistics.mode(exList)
print('Mode:',x)
'''
'''#print(s.mean(exList))
print(mean(exList))
print(stdev (exList))'''

'''try:
    print('Running')
    print('3'+7)
except Exception as e:
    print(e)'''

#tuple not mutable
def example():
    return 15,19

a,b = example()

print(a)
print(b)

#list
x=[5,3,4,2,4,11,23]
print('list',x)
print(x[1])

x.append(10)
print(x)
x.insert(1,7)
print(x)

x.remove(7)
print(x)

print(x.index(4))

print(x.count(4))

x.sort()

print(x)

x = ['spot','cam','mac','jam','rev']
print(x)
x.sort()
print(x)
x.reverse()
print(x)

#dictionaries are unodered group, also mutable

gradeDict = {'Kelly':89,'David':65,'Jack':85}
print(gradeDict)
print(gradeDict['David'])

gradeDict['David']=92
print(gradeDict)

gradeDict['Mac']=78
print(gradeDict)

del gradeDict['David']
print(gradeDict)


gradeDict = {'Kelly':[89,98,],
             'David':[65,90],
             'Jack':[90,76]}
print(gradeDict)
print(gradeDict['Jack'][0])


def log_message(func):
    def retString():
        appendMe = func()
        saveF= open('/tmp/decorator_logs.txt','a')
        saveF.write('\n')
        saveF.write(appendMe)
        saveF.close()
    return  retString

@log_message
def a_function_that_returns_a_string():
    return "A string"

@log_message
def a_function_that_returns_a_string_with_newline(s):
    return "{}\n".format(s)

@log_message
def a_function_that_returns_another_string(string=""):
    return "Another string"

























































