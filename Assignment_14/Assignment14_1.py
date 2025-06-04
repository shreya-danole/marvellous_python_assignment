
class Employee:

    def __init__(self,A,B,C):
        self.name = A
        self.salary = B
        self.emp_id = C

def main():
    emp1 = Employee('Rohit',50000,'101')
   

    print("name of employee:"+emp1.name)
    print("salary of employee:",emp1.salary)
    print("emp_id of employee:"+emp1.emp_id)
    
if __name__=="__main__":
    main()
