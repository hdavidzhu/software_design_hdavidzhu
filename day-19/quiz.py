class Person:
    def __init__(self, name, date_of_birth):
        self.name = name
        self.date_of_birth = date_of_birth

class Employee(Person):
    def __init__(self, name, date_of_birth, date_of_hire, salary):
        Person.__init__(self, name, date_of_birth)
        self.date_of_hire = date_of_hire
        self.salary = salary

    def earns_more_than(self, threshold):
        return self.salary >= threshold

class Manager(Employee):
    def __init__(self, name, date_of_birth, date_of_hire, salary):
        Employee.__init__(self, name, date_of_birth, date_of_hire, salary)
        self.direct_reports = []

    def add_direct_report(self, new_report):
        self.direct_reports.append(new_report)

# if __name__ == '__main__':
    # David = Person('David', '08/25/1995')
    # David = Employee('David', '08/25/1995', '09/25/2014', 50000.00)
    # David = Manager('David', '08/25/1995', '09/25/2014', 50000.00)
    # David.add_direct_report(David)
    # print David.direct_reports  
    # print David.date_of_birth
    # print David.date_of_hire
    # print David.earns_more_than(400000)