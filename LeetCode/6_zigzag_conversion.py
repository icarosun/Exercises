class Solution:
    def convert(self, s: str, numRows: int) -> str:
        matriz = []
        line = 0
        down = False

        for i in range(0, numRows):
            matriz.append([])

        if (numRows == 1):
            return s

        for letter in s:
            if (line == (numRows - 1) or line == 0):
                down = not(down)
    
            matriz[line].append(letter)
    
            if (down):
                line += 1
            else:
                line -= 1

        output = ""
        for row in matriz:
            output += "".join(row)

        return output
