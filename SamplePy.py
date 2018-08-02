from statistics import mean as m 

admins = {'Python':'Pass123@','User2':'Pass213@'}

studentDict = {'Jeff':[78,70,90],
               'Alex':[90,67,94],
               'Sam':[76,56,82]}


def enterGrades():
    nameToEnter = input('Student Name: ')
    gradeToEnter = input('Student Grade: ')

    if nameToEnter in studentDict:
        print('Adding Grade..')
        studentDict[nameToEnter].append(int(gradeToEnter))
    else:
        print('Student does not exist.')

    print(studentDict)

def removeStudent():
    nameToRemove = input('Which student to remove')
    if nameToRemove in studentDict:
        print('Removing student..')
        del studentDict[nameToRemove]

    print(studentDict)


def studentAVGs():
    for eachStudent in studentDict:
        gradeList = studentDict[eachStudent]
        avgGrade = m(gradeList)

        print(eachStudent,'has an average grade of: ', avgGrade)


def main():
    print("""
    Welcome to Grade Central

    [1] - Enter Grades
    [2] - Remove Student
    [3] - Student Average Grade
    [4] - Exit
    """)

    action = input('What would you like do? (Enter a number)')

    if action == '1':
        enterGrades()
    elif action == '2':
        removeStudent()
    elif action == '3':
        studentAVGs()
    elif action == '4':
        exit()
    else:
        print('Not Valid Choice, Try Again')



login = input('Username: ')
passw = input('Password: ')

if login in admins:
    if admins[login] == passw:
        print('Welcome',login)
        while True:
            main()
    else:
        print('Invalid password, Retry')
else:
    print('Invalid username, Enter a valid username')






















