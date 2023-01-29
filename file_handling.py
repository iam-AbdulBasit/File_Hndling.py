def file_name():
    print("#####FILE HANDLING#####")

file_name()

filename = "D:\\newfile.txt"  #############D:\\newfile.pdf  #####D:\\newfile.PNG
Your_choice = input("enter yuor choice")
text = input("enter text")
filepath = (filename)

if Your_choice == "1":
    myfile = open(filepath,"w")
    myfile.write(text)
    print("your text is added to your file")

elif Your_choice == "2":
    myfile = open(filepath,"a")
    myfile.write(text)
    print("new line is added to the text file")

elif Your_choice == "3":
    myfile = open(filepath,"r")
    print(myfile.read())

else:
    print("your file does not exist")

