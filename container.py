class PascalList:
    def __init__(self, python_list=None):
        self.container = python_list or []

    def __getitem__(self, index):
        return self.container[index - 1]

    def __setitem__(self, index, value):
        self.container[index - 1] = value

    def __str__(self):
        return self.container.__str__()
