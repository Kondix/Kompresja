import string


class FileReader:
    def __init__(self, filepath):
        self.data = self.InitGetData(filepath)

    def InitGetData(self, path):
        try:
            with open(path) as f:
                data = f.read()
                print(data)
                return data
        except IndexError:
            print("Error - Please specify an input file.")

    def CountCharactersInData(self):
        printableCharactersCountList = []
        for letter in string.printable:
            printableCharactersCountList.append(self.data.count(letter))
        return printableCharactersCountList


