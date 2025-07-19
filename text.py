'''
file = open("sample.txt")
file_sample = file.read()
file.close
print(file_sample)


file = open("sample.txt", "a")
file_sample = file.write("good job\n")
file.close()
print(file_sample)
'''

one1 = open("one.txt")
one1_txt = one1.read()
one1.close()

two2 = open("two.txt")
two2_txt = two2.read()
two2.close()

print(int(one1_txt) + int(two2_txt))


'''
file = open("sample.txt", "w")
file_sample = file.write("orange favorite fruit")
file.close()
print(file_sample)
'''

import os

os.rmdir("good.txt")
