# /usr/bin/env python
# -*- coding:utf-8 -*-

class thisislog(object):

    def __init__(self):
        self.paths = []
    def getCusPath(self):
        with open('cusPath', 'r') as f:
            for line in f:
                self.paths.append(line)

    def showPathOptions(self):
        self.getCusPath()
        for pathNo, cusPath in enumerate(self.paths):
            print pathNo, ': ', cusPath


    def run(self):
        self.showPathOptions()
        while True:
            cusOption = input('Please enter your path to show: ')
            if cusOption == "q":
                break
            print cusOption



if __name__ == '__main__':

    a = thisislog()
    a.run()