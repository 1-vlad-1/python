import os

num_symbols = 0
num_strings = 0
num_words = 0
word = True
string = ''

with open("data.bin",mode="rb") as f :
     for line in f:
        line = line.decode().strip(os.linesep)
        print(line)
        wordslist = line.split()
        num_strings = num_strings + 1
        num_words = num_words + len(wordslist)
        num_symbols = num_symbols + sum(1 for c in line
                        if c not in (os.linesep, ' '))


print(num_symbols)
print(num_words)
print(num_strings)
