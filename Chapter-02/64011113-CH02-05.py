# funString class

class funString():

    def __init__(self, string=""):
        self.string = string
        ### Enter Your Code Here ###

    def __str__(self):
        return self.string

    def size(self) :
        return sum(1 for i in self.string)

    def changeSize(self):
        ascii_values = [ord(char) for char in self.string]
        
        for i, value in enumerate(ascii_values):
            # UpperCase
            if value in range(65, 90+1):
                ascii_values[i] += 32
            # LowerCase
            elif value in range(97, 122+1):
                ascii_values[i] -= 32
        changed_string = ''.join(map(chr, ascii_values))
        
        return changed_string

    def reverse(self):
        return self.string[::-1]

    def deleteSame(self): 
        return ''.join(sorted(set(self.string), key=self.string.index))

str1,str2 = input("Enter String and Number of Function : ").split()

res = funString(str1)

if str2 == "1" :   print(res.size())

elif str2 == "2":  print(res.changeSize())

elif str2 == "3" : print(res.reverse())

elif str2 == "4" : print(res.deleteSame())