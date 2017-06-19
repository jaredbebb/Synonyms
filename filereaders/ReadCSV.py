import tensorflow as tf
import csv
import string

class ReadCSV:
    def __init__(self, csvfilepath):
        self.csvfilepath = csvfilepath
        self.filetext = []
        self.file_column = []
        self.term_list = []

    def load_csv(self):
        with open(self.csvfilepath, newline='', encoding='utf-8') as csvfile:
            print('opening', self.csvfilepath)
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.filetext.append(row)
                #output_file.write((row))
        csvfile.close()

    def print_filetext(self):
        print(str(self.filetext))

    def parse_string(self, curr_string):
        parsed_string = curr_string.lower()
        parsed_string = parsed_string.replace('\n', '')
        parsed_string = parsed_string.replace('\t', '')
        parsed_string = parsed_string.replace('\r', '')
        translator = str.maketrans('', '', string.punctuation)
        parsed_string = parsed_string.translate(translator)
        return parsed_string

    def parse_column(self, which_column):
        for line in self.filetext:
            translator = str.maketrans('', '', string.punctuation)
            line = line[which_column]
            line = self.parse_string(line) + '\n'
            self.file_column.append(line)

    def word_list(self):
        for sentence in self.file_column:
            words = sentence.split()
            for word in words:
                self.term_list.append(word)


