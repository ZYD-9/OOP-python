#from string import ascii_letters
class Text_on_nine:

    def __init__(self,key_Sequence,digits):
        self.key_Sequence = key_Sequence
        self.digits = digits

    @classmethod
    def start(cls):
        return

    def get_keys(self):
        self.key_Sequence = input(int("Please input key sequence"))

    def get_digits(self):
        self.digits = input("Please input digits")

    def letter_to_digit(self,digits):
        assert 'a' <= digits <= 'z'
        return self.key_Sequence[ord(digits) - ord('a')]

t9 = Text_on_nine()








