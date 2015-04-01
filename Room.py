import Table


class Room:

    def __init__(self, tablenum):
        for x in range(0, tablenum):
            self.tables[x] = Table()
