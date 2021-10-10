filename = input("Input the Filename: ")
f = filename.split(".")
if(f[-1]=="py"):
    print ("The extension of the file is : Python")

else:    
    print ("The extension of the file is : " + f[-1])


