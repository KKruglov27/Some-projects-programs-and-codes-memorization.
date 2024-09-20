

class student:

    def __init__(self, id, name, module):
        self.id = id
        self.name = name
        self.module = module

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def getModule(self):
        return self.module

    def setId(self, id):
        self.id = id

    def setName(self, name):
        self.name = name

    def setModule(self, module):
        self.module = module


def addStudent(std):
    file = open("student.txt", "a+")
    file.write(std.getId() + "." + "\t" + std.getName() + " | " + "Course:" + "\t" + std.getModule() + "\n")
    print("Record has been saved successfully")
    file.close()


def Search(SrchMod1):
    getLines = []
    results = []
    file = open("student.txt", "r")
    for line in file:
        getLines.append(line)
    for line in getLines:
        if SrchMod1 in line:
            results.append(line)
    if not results:
        print("Record is not fount")
    else:
        print(*results, sep="")
        print("Record found")
    file.close()


def display():
    getlines = []
    results = []
    print("\n id \t name \t module")
    file = open("student.txt", "r")
    for line in file:
        getlines.append(line)
    for line in getlines:
        results.append(line)
    print(*results, sep="")
    file.close()


while True:
    print("         Main Menu")
    print("   ==> Press 1 for add new student ")
    print("   ==> Press 2 for search a student")
    print("   ==> Press 3 for display all student")
    print("   ==> press 4 for Exit")
    choice = eval(input("Enter your choice = "))

    if choice == 1:
        id = input("Enter the id number = ")
        name = input("Enter the name = ")
        module = input("Enter the module name ")
        std = student(id, name, module)
        addStudent(std)

    elif choice == 2:
        SearchModule = input("Enter the Module to search = ")
        Search(SearchModule)

    elif choice == 3:
        display()

    else:
        break


