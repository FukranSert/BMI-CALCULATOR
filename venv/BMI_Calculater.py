import tkinter as tk
window_1=tk.Tk()
window_1.title("BMI CALCULATER")
window_1.configure(bg="grey")
window_1.resizable(False,False)
window_1.config(width=800,height=600)
window_1.config(padx=50,pady=60)




def bmi():
    bmi_reference=""


    try:

        bmi_degeri = float(int(entery_1.get()) / ((int(entery_2.get())/100)*(int(entery_2.get())/100)))
        if 0<bmi_degeri<=18.4:
            bmi_reference="Underweight"
        elif 18.4<bmi_degeri<=24.9:
            bmi_reference="Normal"
        elif 24.9<bmi_degeri<=39.9:
            bmi_reference="Overweight"
        elif 39.9<bmi_degeri:
            bmi_reference="Obese"
        else:
            bmi_reference="not a human because it is negative bmi values"
        label_3.config(text=f"BMİ:{bmi_degeri},The person is {bmi_reference}")


        entery_2.delete(0, tk.END)
        entery_1.delete(0, tk.END)







    except:

        label_3.config(text="invalid values")
        entery_2.delete(0, tk.END)
        entery_1.delete(0, tk.END)


def the_mainfunction():
    global entery_2
    global entery_1



    if entery_1.get()=="" or entery_2.get() =="":

        global label_3
        label_3.config(text="Enter both of the values")
        entery_2.delete(0, tk.END)
        entery_1.delete(0, tk.END)

        label_3.pack(side="bottom")
    else:
        bmi()

label_1=tk.Label(text="ENTER YOUR WEIGHT",background="black",foreground="white",width=30)
#kg_frame.pack(x=25,y=25)
label_1.place(x=0,y=-40)


entery_1=tk.Entry(fg="black",bg="white")
entery_1.place(x=46,y=-15)

meter_frame=tk.Frame(master=window_1)
Label_2=tk.Label(text="Enter YOUR HEIGHT",bg="black",fg="white",width=30)
entery_2=tk.Entry(fg="black",bg="white")



#




label_3=tk.Label(master=window_1,bg="grey",fg="black",text="")



label_3.pack(side="bottom")

Label_2.pack()
entery_2.pack()

button_1=tk.Button(text="Calculate",command=the_mainfunction,width=15)
button_1.place(x=50,y=90)

window_1.mainloop()
