file=str(input("Input the Filename: "))
i=file.index(".",0,len(file)-1)
s=file[i+1:]
if s=="py":
    print("The extension of the file is : python")
else:
    print("The extension of the file is : ",s)
