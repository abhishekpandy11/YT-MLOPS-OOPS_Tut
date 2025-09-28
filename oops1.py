# initiate a class

class employee:
    # special method/magic method/dunder method - constructor
    def __init__(self):
        print('Started executing attribute/data')
        self.id = 123
        self.salary = 50000
        self.designation = 'SDE'
        print('attribute/data have been initiated')
    
    def travel(self,destination):
        print('this method was called manually')
        print(f'Employee is now travelling to {destination}')


# creating an obj/instance of class

sam = employee()
# print(sam.salary)

# printing an attribute
sam.travel('Bihar')

print(type(sam))