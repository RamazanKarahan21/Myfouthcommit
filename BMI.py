import tkinter

#pencere
windoww = tkinter.Tk()
windoww.title("practice")
windoww.geometry("200x200")

#label
labell=tkinter.Label(windoww, text="Enter your weight (kg)")
labell.pack()
labell.place(x= 30 , y=25)

labell2=tkinter.Label(windoww, text="Enter your height (cm)")
labell2.pack()
labell2.place(x= 30 , y=90)

result_label = tkinter.Label(windoww, text="")
result_label.place(x=25, y=180)

#entry
entry = tkinter.Entry(width=15)
entry.pack()
entry.place(x= 25 , y=55)
entry2 = tkinter.Entry(width=15)
entry2.pack()
entry2.place(x= 25 , y=120)


def calculate_bmi():
    weight_text = entry.get()
    height_text = entry2.get()

    #Boş
    if weight_text == "" or height_text == "":
        result_label.config(text="Lütfen tüm alanları doldurun!")
        return

    #rakam
    if not weight_text.isdigit() or not height_text.isdigit():
        result_label.config(text="Lütfen sadece sayı girin!")
        return

    weight = int(weight_text)
    height = int(height_text)

    #0olamaz
    if height == 0:
        result_label.config(text="Boy 0 olamaz!")
        return

    #BMI
    bmi = weight / ((height / 100) ** 2)

    #Kategori
    if bmi < 18.5:
        kategori = "Zayıf"
    elif 18.5 <= bmi < 25:
        kategori = "Orta"
    else:
        kategori = "Obez"

    result_label.config(text=f"BMI: {bmi:.2f} - {kategori}")


#button
buttonn = tkinter.Button(windoww, text="Calculate", command=calculate_bmi)
buttonn.pack()
buttonn.place(x = 50 , y= 155)





windoww.mainloop()