#import part
from tkinter import *
import tkinter.font
from PIL import ImageTk, Image

#Function part
def click():
    #check if user chioce English or ASCII
    if clicked.get()=="English" and clicked2.get()=="ASCII":
        # convert English text to ASCII then send value to second entry
        entry1.insert(0,convertEtoac(entry.get()))
    elif clicked2.get()=="English" and clicked.get()=="ASCII":
        #convert ASCII  to English then send value to second entry
        entry1.insert(0,convertAtoE(entry.get()))
    else:
        #if user select the same lang donot change text
        entry1.insert(0,entry.get())


#function to delete all countant of all entery
def clear():
    entry.delete(0,END)
    entry1.delete(0,END)


# convert English text to ASCII then send value to second entry
def convertEtoac(latter):
    num=''
    for i in latter:
        num+=str(ord(i))+' '
    return num
# convert ASCII  to English then send value to second entry
def convertAtoE(num):
    letter=''
    num=num.split(" ")
    for i in num[:-1]:
        if i==" ":
            letter+=" "
        else:
            letter+=chr(int(i))
    return letter
rt=Tk()
rt.title("from venus to universe")
rt.geometry("664x667")

#create font
my_font=tkinter.font.Font(family='Helvetica')

# Add image to background
img =Image.open(r'C:\Users\ASUS\PycharmProjects\pythonProject3\bgFVTU.jpg')
bg = ImageTk.PhotoImage(img)
label = Label(rt, image=bg)
label.place(x = 100,y = 10)

# Create a photoimage object of the image in the path
image1 = Image.open(r'C:\Users\ASUS\PycharmProjects\pythonProject3\logoall.PNG')
test = ImageTk.PhotoImage(image1)
label_img = tkinter.Label(image=test)
label_img.image = test
#Resize the Image
resized_image= image1.resize((600,100), Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_image)
#Create a canvas
canvas= Canvas(rt, width= 600, height= 400)
canvas.create_image(15,5, anchor=NW, image=new_image)

#creating a label widget
mylabel=Label(rt,text="Welcome to FVTU Competition",bg="pink",font=my_font)
mylabel1=Label(rt,text="One Language",bg="pink",font=my_font)
mylabel2=Label(rt,text="From Language",bg="pink",font=my_font)
mylabel3=Label(rt,text="To Language",bg="pink",font=my_font)
mylabel4=Label(rt,text="Converted Language",bg="pink",font=my_font)
mylabel5=Label(rt,text="                            ")

#shoving it onto the screen
mylabel5.grid(row=0,column=0,pady=0,padx=0)
mylabel.grid(row=1,column=2,pady=5,padx=5)
mylabel1.grid(row=7,column=1,padx=5)
mylabel2.grid(row=8,column=1,padx=5)
mylabel3.grid(row=9,column=1,padx=5)
mylabel4.grid(row=11,column=1,padx=5)

#creat entry (input space)
entry=Entry(rt,fg="black",bg="white",relief='sunken')
entry.grid(row=7,column=2,ipady=50,ipadx=80,pady=15,padx=13)

#create select_box
clicked=StringVar()
clicked.set("lang-code")
drop=OptionMenu(rt,clicked,"English","ASCII")
drop.grid(row=8,column=2,pady=5,padx=2)
clicked2=StringVar()
clicked2.set("lang-code")
drop2=OptionMenu(rt,clicked2,"English","ASCII")
drop2.grid(row=9,column=2,pady=5,padx=2)

#create convert button
button=Button(rt,text="convert",padx=15,command=click,fg="pink",bg="black")
button.grid(row=10,column=2,padx=100)

#creat entry (output space)
entry1=Entry(rt)
entry1.grid(row=11,column=2,ipady=50,ipadx=80,pady=15,padx=13)

#create clear button
button1=Button(rt,text="clear",padx=15,command=clear,fg="pink",bg="black")
button1.grid(row=12,column=2,pady=13)

#shoving logo onto the screen
canvas.grid(row=14,column=2,ipady=5,ipadx=5)

#show the interface
rt.mainloop()


