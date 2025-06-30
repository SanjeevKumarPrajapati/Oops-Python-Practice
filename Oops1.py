class Employee:
    def __init__(self):
        print("Execution started ..........")
        self.Name="Sanjeev"
        self.Id=123
        self.Department="IT"
        self.Salary=45000
        self.Desg="Managar"
        print("Execution ended .............")
    
    def travel(self,Destination):
        print(f"Employee is going to {Destination}")
    
#create a instance of a class
san=Employee()


print("Name :- ",san.Name)
print("Designation : ",san.Desg)
print("Department :- ",san.Department)
print("Salary : ",san.Salary)
print("ID :- ",san.Id)
san.travel("Dubai")


        
        