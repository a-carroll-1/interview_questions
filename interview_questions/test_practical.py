# from interview_questions import practical
from interview_questions import practical_answers as practical


class TestStringInt:
    int_string_list = ['-1', '2', '3']
    whole_number_string = '23456'

    def test_list_returned(self):

        assert isinstance(practical.string_list_to_int(self.int_string_list),
                          list)

    def test_all_ints(self):
        for element in practical.string_list_to_int(self.int_string_list):
            assert isinstance(element, int)

    def test_int_returned(self):
        assert isinstance(practical.string_to_int(self.whole_number_string),
                          int)

    def test_correct_int_returned(self):
        assert practical.string_to_int(self.whole_number_string) == 23456


class TestNameCaseMod:
    @staticmethod
    def test_basic_name():
        assert practical.name_case_modifier('jon batiste') == \
               'Jon Batiste'

    @staticmethod
    def test_middle_name():
        assert practical.name_case_modifier('alex daniel carroll') == \
               'Alex Daniel Carroll'

    @staticmethod
    def test_hyphenated_name():
        assert practical.name_case_modifier('daniel day-lewis') == \
               'Daniel Day-Lewis'

    @staticmethod
    def test_first_name_only():
        assert practical.name_case_modifier('sting') == 'Sting'

    @staticmethod
    def test_apostrophe_name():
        assert practical.name_case_modifier('sir d’anville o’m’darlin’') == \
               'Sir D’Anville O’M’Darlin’'

    @staticmethod
    def test_initials_name():
        assert practical.name_case_modifier('b. j. novak') == 'B. J. Novak'


class TestSortedValues:
    @staticmethod
    def test_simple():
        simple_dict = {
            'three': 'charlie',
            'two': 'beta',
            'one': 'alpha'
        }
        assert practical.sorted_values(simple_dict) == ['alpha', 'beta', 'charlie']


class TestGivenValue:
    @staticmethod
    def test_alpha():
        unnested_dict = {
            'alpha': 1,
            'bravo': 2,
            'charlie': 3
        }
        assert practical.given_value(unnested_dict) == 1
