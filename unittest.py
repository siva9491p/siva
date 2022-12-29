import unittest
class TestStringMethods(unittest.Testcase):
    def setup(self):
        pass

if __name__ =='__main__':
    unittest.main()


class student:
    marks_bonus= 1.5

    def __init__(self,first,last,marks):
        self.first=first
        self.last=last
        self.marks=marks
    def email(self):
        return '{}.{}@gmail.com'.format(self.first,self.last)
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    def  apply_bonus(self):
        self.marks=int(self.marks*self.marks_bonus)







