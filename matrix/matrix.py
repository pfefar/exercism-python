class Matrix:
    def __init__(self, matrix_string):
        self.matrix = matrix_string.split("\n")

        self.final = []

        for i in self.matrix:
            arr2 = []
            l = i.split(" ")
            for j in l:
                arr2.append(int(j))
            self.final.append(arr2)

    def row(self, index):
        return self.final[index - 1]

    def column(self, index):
        t = [*zip(*self.final)]
        return list(t[index - 1])


# ----- Pythonic Solution --------------

# class Matrix:
#     def __init__(self, matrix_string):
#         self.matrix = [[int(item) for item in row.split(' ')] for row in matrix_string.split('\n')]

#     def row(self, index):
#         return self.matrix[index-1]

#     def column(self, index):
#         return list(list(zip(*self.matrix))[index-1])
