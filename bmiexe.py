from tkinter import *
#Tạo ra của sổ
a = Tk()
a.title("Chương trình tính chỉ số đo cơ thể")
a.geometry("300x400")
a.attributes("-topmost", True)
#tạo ra label1
name1 = Label(a, font = ("Arial",10), text = "Nhập Chiều Cao(m): ")
name1.place(x = 10, y = 10)
#tạo ra label2
name2 = Label(a, font = ("Arial",10), text = "Nhập Cân nặng(kg): ")
name2.place(x = 10, y = 50)
#tạo ra label3
#tạo ra entry1
entry = Entry(a, width = 15, font = ("Time New Roman",10))
entry.place(x = 130, y = 10)
entry.focus()
#tạo ra entry2
entry2 = Entry(a, width = 15, font = ("Time New Roman",10))
entry2.place(x = 130, y = 50)
#def dieukien():
    
#Tạo ra button
def anvao():
    name1 = Label(a , font = ("Arial",10), text =  "Chỉ số BMI của bạn là: " + str(float(entry2.get()) /( float(entry.get()) * 2)), fg="red")
    name1.place(x= 20, y = 110)
    name3 = Label(a, font = ("Arial",10), text = "BMI <18,5 : Bạn đang gầy")
    name3.place(x = 10, y = 140)
    #tạo ra label4
    name4 = Label(a, font = ("Arial",10), text = "BMI = 18,5 - 22,9: Bạn đang bình thường")
    name4.place(x = 10, y = 160)
    #tạo ra label5
    name5 = Label(a, font = ("Arial",10), text = "BMI >=23,0 : Bạn đang thừa cân")
    name5.place(x = 10, y = 180)
    #tạo ra label6
    name6 = Label(a, font = ("Arial",10), text = "BMI > 25,0 : Bạn đang béo phì")
    name6.place(x = 10, y = 200)
but = Button(a, text = "Tính Toán", width = 10, height = 1, font = ("Time New Roman",10), command = anvao )
but.place(x=105 , y = 80)

a.mainloop()    