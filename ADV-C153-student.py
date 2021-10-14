 import random *
 from tkinter import *
 root=Tk()
 root.title("Array Dimentions")
 
 root.geometry("400x400")
 label = Label(root)
 
 array_3d =[[[1,2,3,4,5,6],["Hard","tall"],["A","B","C","G","S","J","T","R"]]]

 print(array_3d[0][2][3])
 
 def newPassword():
     randomNumberOne = random.randint(0,5)
     randomNumberTwo = random.randint(0,1)
     randomNumberThree = random.randint(0,7)
     
     letterOne = str(array_3d[0][0][randomNumberOne])
     letterTwo =(array_3d[0][1][randomNumberTwo])
     letterThree =(array_3d[0][2][randomNumberThree])
     label["text"] = letterOne +""+ letterTwo +""+ letterThree
     
 btn=Button(root, text="New Password", command=newPassword)
 btn.place(relx=0.5,rely=0.5, anchor=CENTER)
     
     
 label.place(relx=0.5, rely=0.6, anchor=CENTER)
     
     
 root.mainloop()