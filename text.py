file = open("sample.txt")
file_sample = file.read()
file.close
print(file_sample)


file = open("sample.txt", "a")
file_sample = file.write("good job\n")
file.close()
print(file_sample)

'''
file = open("sample.txt", "w")
file_sample = file.write("orange favorite fruit")
file.close()
print(file_sample)
'''
