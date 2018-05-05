import re


class ParagraphAnalyzer:

    def __init__(self, file_path):
        self.text_file_path = file_path
        self.text = self.__read(file_path)

    def __read(self, file_path):
        with open(file_path) as f:
            lines = f.readlines()
        paragraph = str()
        for line in lines:
            paragraph += line
        return paragraph

    @property
    def words_count(self):
        words = re.findall(r'[-a-zA-Z\'0-9]+', self.text)
        return len(words)

    @property
    def sentences_count(self):
        s = re.findall(r'[\.?!]+[\n]*', self.text)
        return len(s)

    @property
    def average_letter_count(self):
        letters = re.findall(r'[a-zA-Z]', self.text)
        word_count = self.words_count
        return round(len(letters)/word_count,2)

    @property
    def average_sentence_length(self):
        word_count = self.words_count
        sentence_count = self.sentences_count
        return round(word_count/sentence_count,2)

    def report(self):
        header = "Paragraph Analysis \n"
        divider = "-"*30
        l1 = f"\nApproximate Word Count: {self.words_count}"
        l2 = f"\nApproximate Sentence Count: {self.sentences_count}"
        l3 = f"\nAverage Letter Count: {self.average_letter_count}"
        l4 = f"\nAverage Sentence Length: {self.average_sentence_length}"
        text = header + divider+l1+l2+l3+l4
        return text

    def export_to_text(self, report):
        output = self.text_file_path.split('/')[-1].split('.')[0]+'_report.txt'
        with open(output, 'w') as f:
            f.write(report)

if __name__ == '__main__':
    text_file = 'raw_data/paragraph_1.txt'
    analyzer = ParagraphAnalyzer(text_file)
    report = analyzer.report()
    print(report)
    analyzer.export_to_text(report)

    print("\n")
    text_file2 = 'raw_data/paragraph_2.txt'
    analyzer2 = ParagraphAnalyzer(text_file2)
    report2 = analyzer2.report()
    print(report2)
    analyzer2.export_to_text(report2)
