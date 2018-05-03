import csv


class BudgetAnalyzer:
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
        new_data = [[e[0], int(e[1])] for e in data]
        return new_data

    def __revenue_change(self):
        revenue_list = [e[1] for e in self.data]
        revenue_change_list = [later - prev for prev, later in zip(revenue_list, revenue_list[1:])]
        revenue_changes = [0]+revenue_change_list
        return revenue_changes

    @property
    def total_months(self):
        """
        Total months in a data set.
        :return: int
        """
        months = [date[0] for date in self.data]
        # Unique months
        return len(months)

    @property
    def total_revenue(self):
        # use Sum() to add up the numbers
        revenue = sum(map(lambda row: int(row[1]), self.data))
        return revenue

    @property
    def average_revenue_change(self):
        total_months = self.total_months
        revenue_change = self.__revenue_change()
        average_revenue_change = sum(revenue_change)/(total_months-1)
        return round(average_revenue_change, 3)

    @property
    def greatest_increase_in_revenue(self):
        revenue_change_list = self.__revenue_change()
        greatest_increase = max(revenue_change_list)
        index = revenue_change_list.index(greatest_increase)
        date = self.data[index][0]
        return date,greatest_increase

    @property
    def greatest_decrease_in_revenue(self):
        revenue_change_list = self.__revenue_change()
        greatest_decrease = min(revenue_change_list)
        index = revenue_change_list.index(greatest_decrease)
        date = self.data[index][0]

        return date,greatest_decrease

    def report(self):
        header = "Financial Analysis \n"
        divider = "-"*30
        l1 = f"\nTotal Months: {self.total_months}"
        l2 = f"\nTotal Revenue: ${self.total_revenue}"
        l3 = f"\nAverage Revenue Change: ${self.average_revenue_change}"
        l4 = f"\nGreatest Increase in Revenue: {self.greatest_increase_in_revenue[0]} "\
              f"(${self.greatest_increase_in_revenue[1]})"
        l5 = f"\nGreatest Decrease in Revenue: {self.greatest_decrease_in_revenue[0]} "\
              f"(${self.greatest_decrease_in_revenue[1]})"
        text = header + divider+l1+l2+l3+l4+l5
        return text

    def export_to_text(self, report):
        output = self.csv_file_path.split('/')[-1].split('.')[0]+'_report.txt'
        with open(output, 'w') as f:
            f.write(report)

if __name__ == '__main__':
    analyzer1 = BudgetAnalyzer('raw_data/budget_data_1.csv')
    report = analyzer1.report()
    print(report)
    analyzer1.export_to_text(report)

    print("\n"*2)
    analyzer2 = BudgetAnalyzer('raw_data/budget_data_2.csv')
    report2 = analyzer2.report()
    print(report2)
    analyzer2.export_to_text(report2)