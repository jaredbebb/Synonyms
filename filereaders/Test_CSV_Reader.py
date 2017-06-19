import unittest
from filereaders.ReadCSV import ReadCSV


class Test_CSV_Reader(unittest.TestCase):

    def test_parse_string(self):
        test_csv_reader_obj = ReadCSV(
            'comcast_consumeraffairs_complaints.csv')
        test_csv_reader_obj.load_csv()
        test_csv_reader_obj.parse_column('text')
        new_line = test_csv_reader_obj.parse_string('in the \nwindow \n')
        tab_char = test_csv_reader_obj.parse_string('in the\t window \t')
        carriage_return = test_csv_reader_obj.parse_string('in \rthe window \r')
        self.assertEqual(new_line, 'in the window ')
        self.assertEqual(tab_char, 'in the window ')
        self.assertEqual(carriage_return, 'in the window ')