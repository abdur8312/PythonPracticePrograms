from tkinter import *

window = Tk() #instantiate an instance of a window
window.geometry("500x500") #sets the size of the window
window.title("abdur's first GUI window")

window.iconbitmap(r'C:\Users\abdur\Documents\python\cam.ico') #uses only .ico file for the favicon
window.config(background="blue")

photo = PhotoImage(file="C:\\Users\\abdur\\Documents\\python\\heart.gif")

#label example
# label = Label(window,
#               text="ABDUR RAHMAN",
#               font=("Lucida Console",50,"bold"),
#               fg="#00FF00",
#               bg="black",
#               relief=RAISED,
#               bd=10,
#               padx=20,
#               pady=20,
#               image=photo,
#               compound="bottom")
#label.pack()
# count = 0
# def click():
#     global count
#     count += 1
#     print(count)
    
#button example
# button = Button(window,text="click me",
#                 command=click,
#                 font=("Garamond",30),
#                 fg="green",
#                 bg="black",
#                 activebackground="black",
#                 activeforeground="green",
#                 image=photo,
#                 compound="bottom")
# button.pack()

entry = Entry(window,font=("Arial",40),
              fg="#00FF00",
              bg="black")
entry.pack()

window.mainloop() #place window on computer screen and listern for events
