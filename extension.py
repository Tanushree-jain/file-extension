filename = input("Input the Filename: ")
f_extns = filename.split(".")
file = {"py": "python", "txt": "text"}
for a in file:
    if a in f_extns:
        print ("The extension of the file is : " + repr(file[a]))
        break
else:
    print ("The extension of the file is : " + repr(f_extns[-1]))
