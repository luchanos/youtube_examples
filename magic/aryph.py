class Maxtrix:
    def __init__(self, rows):
        self.rows = rows

    def __add__(self, other):
        res_matr = []
        for i in range(len(self.rows[0])):
            new_string = []
            for j in range(len(self.rows[0])):
                new_string.append(self.rows[i][j] + other.rows[i][j])
            res_matr.append(new_string)
        return Maxtrix(res_matr)

    def __str__(self):
        s = ""
        for line in self.rows:
            s += " ".join(list(map(str, line))) + "\n"
        return s


m_1 = Maxtrix([
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
])

m_2 = Maxtrix([
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
])

print(m_1)

c = 1
m_3 = m_1 + m_2
print(m_3)
