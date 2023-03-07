all_employees = [
        'JOHNSON WILLIAMS','BROWN JONES','GARçIæ MILLER','DAVIS RODRIGUEZ','MARTINEZ HERNANDEZ','LOPEZ GONZALEZ',
        'WILSON ANDERSON','THOMAS TAYLOR','MÖÖRE JACKSON','MARTIN LEE','PEREZ THOMPSON','WHITE HARRIß',
        'SANCHEZ CLARK','RAMIREZ LEWIS','ROBINSON WALKER','YÖUNG ALLEN','KING WRIGHT','SCOTT TORRES',
        'NGUYEN HILL','FLORES GREEN','ADAMS NELSON','BAKER HALL','RIVERA CAMPBELL','MITCHELL CARTER',
        'ROBERTS GOMEZ','PHILLIPẞ EVANS','TURNER DIAZ','PARKER CRUZ','EDWARDS COLLINS','REYES STEWART',
        'MORRIS MORALES','MURPHY COOK','ROGERS GUTIERREZ','ORTIZ MORGAN','COOPER PETERSON',
        'BAILEY REED','HANẞ HOWARD','RAMOS KIM','CÖX WARD','RICHARDSON WATSON','BROOKS CHAVEZ',
        'WOOD JAMES','BENNETT GRAY','MENDOZA RUIZ','HUGHES PRICE','ALVAREZ çASTILLO'
    ]
    #46 names in array

def get_all_employees_input(message):
    """ Ignore this function you don't need to understand or change it """
    if "testInput" in message:
        testInputString = message.split("testInput")[1].rstrip().lstrip()
        allEmployeesTestingInput = testInputString.split(",")
        return allEmployeesTestingInput
    return all_employees

# Functions that your team will implement
def problem2_1(message):
    all_employees = get_all_employees_input(message)
    beginsWithLetterCCount = 0
    
    #loop through the array: all_employees
    for name in all_employees:
        #make the whole name lower case
        name = name.lower()
        #if the name starts with "c" then: beginsWithLetterCCount++
        if name.startswith("c"):
            print(name)
            beginsWithLetterCCount += 1

    
    

    return str(beginsWithLetterCCount)


def problem2_2(message):
    all_employees = get_all_employees_input(message)
    peopleWithLongerThan8CharacterLastnamesCount = 0

    last_name = ""

    #loop through the array: all_employees
    for name in all_employees:
        #get the last name
        last_name_list = name.split()
        last_name = last_name_list[1]

        #if the last_name has more than 8 characters then: peopleWithLongerThan8CharacterLastnamesCount++
        if len(last_name) > 8:
            print(name)
            peopleWithLongerThan8CharacterLastnamesCount += 1

    return str(peopleWithLongerThan8CharacterLastnamesCount)


def problem2_3(message):
    all_employees = get_all_employees_input(message)
    employeesWhoWillGetBonusesCount = 0

    #loop through the array: all_employees
    for name in all_employees:
        #if the name has "ẞ, ö, æ, or ç" then: employeesWhoWillGetBonusesCount++
        #name.contains("ẞ") or name.contains("ö") or name.contains("æ") or name.contains("ç")
        if "ẞ" in name or "ö" in name or "æ" in name or "ç" in name:
            print(name)
            employeesWhoWillGetBonusesCount += 1
    
    return str(employeesWhoWillGetBonusesCount)

print(problem2_1(all_employees))
print(problem2_2(all_employees))
print(problem2_3(all_employees))
