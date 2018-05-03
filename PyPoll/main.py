import csv
from collections import defaultdict

class PollAnalyzer:
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

    @property
    def total_votes(self):
        return len(self.data)

    @property
    def candidates(self):
        candidates = set([e[2] for e in self.data])
        candidate_list = [c for c in candidates]
        return candidate_list

    @property
    def percentage(self):
        candidate_dict_int = defaultdict(int)
        # candidates = self.candidates
        for candidate in self.data:
            candidate_dict_int[candidate[2]] += 1

        total_votes = self.total_votes
        percentage = defaultdict(list)
        for candidate_name, votes in candidate_dict_int.items():
            percentage[candidate_name].append(str(round(votes/total_votes*100,1))+'%')
            percentage[candidate_name].append(votes)

        return percentage

    @property
    def winner(self):
        percentage = self.percentage
        winner, votes = None, 0
        for candidate, value in percentage.items():
            if value[1] > votes:
                votes = value[1]
                winner = candidate

        return winner

    def report(self):
        candidate_percentage = self.percentage
        header = "Election Results"
        divider = "\n"+"-"*30+"\n"
        l1 = f"Total Votes: {self.total_votes}"
        l2 = ''
        content_format = "{name}: {percent} ({votes})"
        for candidate_name, d in candidate_percentage.items():
            content= content_format.format(name=candidate_name, percent=d[0], votes=d[1])
            l2 += content +"\n"
        l3 = f"Winner: {self.winner}"
        text = header + divider+l1+divider+l2+divider+l3+divider
        return text

    def export_to_text(self, report):
        output = self.csv_file_path.split('/')[-1].split('.')[0]+'_report.txt'
        with open(output, 'w') as f:
            f.write(report)

if __name__ == '__main__':
    analyzer1 = PollAnalyzer('raw_data/election_data_1.csv')
    report = analyzer1.report()
    print(report)
    analyzer1.export_to_text(report)

    analyzer2 = PollAnalyzer('raw_data/election_data_2.csv')
    report2 = analyzer2.report()
    print(report2)
    analyzer2.export_to_text(report2)


