# Parent_class of Employee
class Employee:
    def calculate_salary(self):
        # Default message for the salary calculation
        print("Salary calculation is not for General Employees.")

# Child_class for Manager which overrides the calculate_salary function
class Manager(Employee):
    def __init__(self, base_salary, bonus):
        self.base_salary = base_salary
        self.bonus = bonus

    # Overriding the calculate_salary function for a manager
    def calculate_salary(self):
        # calculation for Manager: Basic salary and Bonus
        total_salary = self.base_salary + self.bonus
        print(f"Manager's total salary is KSh. {total_salary}")

# instance for Employee
employee = Employee()
employee.calculate_salary()

# instance for Manager
manager = Manager(base_salary=50000, bonus=15000)
manager.calculate_salary()