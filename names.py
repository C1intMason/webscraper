import csv


class Name:
    def __init__(self, f_name, l_name, ssn, test1, test2, test3, test4, final, grade):
        self.grade = grade
        self.final = final
        self.test4 = test4
        self.test3 = test3
        self.test2 = test2
        self.test1 = test1
        self.ssn = ssn
        self.l_name = l_name
        self.f_name = f_name


csv_file = csv.reader(open("data.csv"))

print(dir(csv_file))

def get_data():
    rows = []
    for row in csv_file:
        rows.append(row)
    return rows

test = Name(*get_data()[1])

print(testq.__dict__)