import description
import getRandom
import hint


class Main:
        def __init__(self):
            description.describe()
            self.mode = input('Enter the age:\n C for 3-5 and A for 5-9')
            if (self.mode not in ['C', 'A']):
                print('+++  We think your age is not suitable for this game :(  +++\n')
                quit()

        def numberIs(self):
            num = getRandom.getNumber(self.mode)
            hint.disp_hint(num, self.mode)


m=Main()
while(True):
    m.numberIs()
    print("========================================================================================")


