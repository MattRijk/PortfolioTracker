
class TextParser:
    def _openfile(self, path):
        f = open(path)
        return f.read()

    def splitbylines(self, path):
        contents = self._openfile(path)
        return self._splitbytabs(contents.split("\n"))

    def _splitbytabs(self, array):
        return [line.split("\t") for line in array]

    def first_column(self, array):
        columns = []
        return self._pull_column(array, columns)

    def _pull_column(self, array, columns):
        for idx in range(len(array)):
            self.add_item(array, columns, idx)
        return columns

    def add_item(self, array, columns, idx):
        if array[idx][0] != '':
            columns.append(array[idx][0])
        return columns

    def compare(self, a, b):
        not_found = []
        self.find_item(a, b, not_found)
        return not_found

    def find_item(self, a, b, n):
        container = self.add_to_map(a)
        self.add_target(b, container, n)

    def add_target(self, b, container, n):
        for i in b:
            c = self._add_not_found(container, i, n)
        return c

    def _add_not_found(self, container, i, not_found):
        if i not in container.values():
            not_found.append(i)
        return not_found

    def add_to_map(self, a):
        d = {}
        return self._accumulate_map(a, d)

    def _accumulate_map(self, a, d):
        for i in range(len(a)):
            self.not_found(a, d, i)
        return d

    def not_found(self, a, d, i):
        if i not in d:
            d[i] = a[i]
        return d

class XMLParser:
    pass