class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Payroll:
    def __init__(self):
        # an empty list to store Employee objects
        self.employees = []

    def add_employee(self, name, salary):
        # Adding a new Employee object to the list
        employee = Employee(name, salary)
        self.employees.append(employee)

    def calculate_total_payroll(self):
        # Calculating the total payroll
        total = sum(employee.salary for employee in self.employees)
        return total

    def list_employees(self):
        # Listing all employees by names and salaries
        return [(employee.name, employee.salary) for employee in self.employees]


# Payroll instance
payroll = Payroll()

# Adding employees
git status
payroll.add_employee("Newton", 2000)
payroll.add_employee("Armstrong", 8000)
payroll.add_employee("Ouma", 70000)

# Calculating total payroll
total_payroll = payroll.calculate_total_payroll()

print(f"Total Payroll: {total_payroll}")

print("Employees: ", payroll.list_employees())