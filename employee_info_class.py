class Employee:
    def __init__(self,employee_id,first_name,last_name,position,birth_year,birth_month,birth_day,is_graduated):
        self.employeeid = employee_id
        self.firstname = first_name
        self.lastname = last_name
        self.positioning = position
        self.birthyear = birth_year
        self.birthmonth = birth_month
        self.birthday = birth_day
        self.isgraduate = is_graduated

    def print_data(self):
        print(f"The self.employeeid = {self.employeeid}")
        print(f"The self.firstname = {self.firstname}")
        print(f"The self.lastname = {self.lastname}")
        print(f"The self.positioning = {self.positioning}")
        print(f"The self.birthyear = {self.birthyear}")
        print(f"The self.birthmonth = {self.birthmonth}")
        print(f"The self.birthday = {self.birthday}")
        print(f"The self.isgraduate = {self.isgraduate}")

def read_employee_id():
    while True:
        id_str = input("Please Enter the Employee ID:")
        id_str = id_str.strip()

        if id_str.isdigit():
            id = int(id_str)
            if id > 0 :
                return id
            else:
                print("Error, The Employee ID should be positive number")
        else:
            print("Error, The Employee ID should be a number")


def read_first_name():
    while True:
        first_name = input("Please Enter The Employee First Name:")
        first_name = first_name.strip()

        if len(first_name) >= 2:
            return first_name
        else:
            print("Error, The Employee First Name should be at least 2 Characters")

def read_last_name():
    while True:
        last_name = input("Please Enter The Employee Last Name:")
        last_name = last_name.strip()

        if len(last_name) >= 2:
            return last_name
        else:
            print("Error, The Employee Last Name should be at least 2 Characters")

def read_position():
    while True:
        position = input("Please Enter The Employee Position:")
        position = position.strip()

        if len(position) >= 1:
            return position
        else:
            print("Error, The Employee Position should be at least 1 Characters")

def read_year():
    while True:
        year_str = input("Please Enter the Employee Birth Year:")
        year_str = year_str.strip()

        if year_str.isdigit():
            year = int(year_str)
            if (year >= 1900) and (year <= 2004):
                return year
            else:
                print("Error, The Employee Birth Year should be between 1900 and 2004")
        else:
            print("Error, The Employee Birth Year should be a number")

def read_month():
    while True:
        month_str = input("Please Enter the Employee Birth Month:")
        month_str = month_str.strip()

        if month_str.isdigit():
            month = int(month_str)
            if (month >= 1) and (month <= 12):
                return month
            else:
                print("Error, The Employee Birth Month should be between 1 and 12")
        else:
            print("Error, The Employee Birth Month should be a number")

def read_day():
    while True:
        day_str = input("Please Enter the Employee Birth Day:")
        day_str = day_str.strip()

        if day_str.isdigit():
            day = int(day_str)
            if (day >= 1) and (day <= 31):
                return day
            else:
                print("Error, The Employee Birth Day should be between 1 and 31")
        else:
            print("Error, The Employee Birth Day should be a number")

def read_is_graduated():
    while True:
        is_graduated_str = input("Have the Employee graduated from the univesity (y/n):")
        is_graduated_str = is_graduated_str.strip()

        if is_graduated_str in ["y", "n"]:
            if is_graduated_str == "y":
                return True
            else:
                return False
        else:
            print("Error, Please Enter y or n")

if __name__ == "__main__":
    employees = {}
    employee_id = read_employee_id()
    first_name = read_first_name()
    last_name = read_last_name()
    position = read_position()
    birth_year = read_year()
    birth_month = read_month()
    birth_day = read_day()
    is_graduated = read_is_graduated()
    employee = Employee(employee_id,first_name,last_name,position,birth_year,birth_month,birth_day,is_graduated)
    print(employee)
    employee.print_data()

