# FILE OPERATION
This particular piece of code  explain how python file handling is use(how to use them)
## Below are  how to use the python file handling modules
1. remvove() a file
2. rmdir() a folder
3. mkdir() a folder
4. open() a file
5. write() a file 
6. read() a file 
7. close() a file 
## EXAMPLE
1. remove()
```
import os

os.remove("filename")
```
2. rmdir()
```
import os

os.rmdir("foldername")
```
3. mkdir()
```
import os

os.mkdir("foldername")
```
4. open()
```
file = open("sample.txt")
```
5. write()
```
file = open("sample.txt", "w")
file_sample = file.write("over write")

file = open("sample.txt", "a")
file_sample = file.write("append")
```
6. read()
```
file_sample = file.read()
```
7. close
```
file.close()
```
##COMPLET EXAMPLE
```
file = open("sample.txt")
file_sample = file.read()
file.close()
print(file_sample)

file = open("sample.txt", "a")
file_sample = file.write()
file.close()
print(file_sample)

file = open("sample.txt", "w")
file_sample = file.write()
file.close()
print(file_sample)
```
