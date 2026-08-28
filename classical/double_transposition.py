class DoubleTransposition:
    def __init__(self, row:int, col:int):
        self.row = row
        self.col = col
        self.matrix = [['' for i in range(col)] for i in range(row)]

    def _populate(self, text):
        k = 0
        for i in range(self.row):
            for j in range(self.col):
                self.matrix[i][j] = text[k]
                k += 1

    def encrypt(self, pt:str, row_key:list, col_key:list):
        ct = ""

        size = self.row * self.col
        pt = pt.ljust(size, 'X')

        self._populate(pt)

        tmp = []
        for i in row_key:
            tmp.append(self.matrix[i])

        result = []
        for i in range(self.row):
            row = []
            for j in col_key:
                row.append(tmp[i][j])
            result.append(row)

        self.matrix = result

        for i in self.matrix:
            for j in i:
                ct += j

        return ct

    def decrypt(self, ct:str, row_key:list, col_key:list):
        pt = ""

        self._populate(ct)

        temp = [['' for i in range(self.col)] for i in range(self.row)]

        for i in range(self.row):
            for j in range(self.col):
                temp[i][col_key[j]] = self.matrix[i][j]

        result = [['' for i in range(self.col)] for i in range(self.row)]

        for i in range(self.row):
            result[row_key[i]] = temp[i]

        self.matrix = result

        for i in self.matrix:
            for j in i:
                pt += j

        return pt.rstrip('X')

    def get_matrix(self):
        return self.matrix