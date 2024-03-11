import tkinter

def calculate_km():
    miles = float(miles_entry.get())
    km = miles * 1.609
    result_label.configure(text=km)
    return


window = tkinter.Tk()
window.title("Miles to Km Convertor")
window.config(padx=20, pady=20)

miles_entry = tkinter.Entry(width=20)
miles_entry.grid(row=0,column=1)

miles_label = tkinter.Label(text="Miles")
miles_label.grid(row=0,column=2)

equals_label = tkinter.Label(text="is equal to")
equals_label.grid(row=1,column=0)

result_label = tkinter.Label(text="")
result_label.grid(row=1,column=1)

km_label = tkinter.Label(text="Km")
km_label.grid(row=1,column=2)

calculate_button = tkinter.Button(text="Click Me", command=calculate_km)
calculate_button.grid(row=2,column=1)

window.mainloop()
