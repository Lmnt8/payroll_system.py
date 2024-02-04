class Employee:
    def __init__(self, employee_id, first_name, last_name, position, salary):
        self.employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.position = position
        self.salary = salary

    def display_info(self):
        print(f"Employee ID: {self.employee_id}")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Position: {self.position}")
        print(f"Salary: {self.salary}\n")


class Department:
    def __init__(self, department_id, department_name, location):
        self.department_id = department_id
        self.department_name = department_name
        self.location = location
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def display_employees(self):
        print(f"Department: {self.department_name} ({self.location})")
        for employee in self.employees:
            employee.display_info()


# Example usage:
if __name__ == "__main__":
    employee1 = Employee(1, "John", "Doe", "Manager", 50000)
    employee2 = Employee(2, "Jane", "Smith", "Developer", 40000)

    it_department = Department(101, "IT", "New York")
    it_department.add_employee(employee1)
    it_department.add_employee(employee2)

    it_department.display_employees()
