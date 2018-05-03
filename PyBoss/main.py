import csv
from datetime import datetime as dt
from us_state_abbrev import us_state_abbrev


class EmployeeConverter:
    def __init__(self, csv_path):
        self.csv_file_path = csv_path
        self.data = self.__csv_data()

    def __csv_data(self):
        """
        Open the csv file and read.
        :return: a list
        """
        with open(self.csv_file_path, newline="") as csvfile:
            reader = csv.reader(csvfile, delimiter=",")
            raw_data = [row for row in reader]
        # Remove the header
        data = raw_data[1:]

        return data

    def conversion(self):
        original_data = self.data
        new_data = list()

        for employee in original_data:
            new_employee_info = list()
            # ID
            new_employee_info.append(employee[0])
            # First name
            new_employee_info.append(employee[1].split(' ')[0])
            # Last name
            new_employee_info.append(employee[1].split(' ')[1])
            # DOB
            old_dob = employee[2]
            new_dob = dt.strptime(old_dob, "%Y-%m-%d").strftime("%m/%d/%Y")
            new_employee_info.append(new_dob)
            # ssn
            new_ssn = "***-**-"+employee[3].split('-')[-1]
            new_employee_info.append(new_ssn)

            # State
            new_employee_info.append(us_state_abbrev.get(employee[4]))

            new_data.append(new_employee_info)
        return new_data

    def export_to_csv(self):
        output = self.csv_file_path.split('/')[-1].split('.')[0]+'_new.csv'
        new_data = self.conversion()
        with open(output, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(new_data)

if __name__ == '__main__':
    converter = EmployeeConverter('raw_data/employee_data2.csv')
    converter.export_to_csv()

