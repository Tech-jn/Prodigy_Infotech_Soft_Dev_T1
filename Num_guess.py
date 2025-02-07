import tkinter as tk

from tkinter import ttk



def convert_temperature():

    temp = float(entry_temp.get())

    if selected_unit.get() == 'Celsius to Fahrenheit':

        result = (temp * 9/5) + 32

    else:

        result = (temp - 32) * 5/9

    label_result.config(text=f'Result: {result:.2f} degrees')



# Create the main window

root = tk.Tk()

root.title('Temperature Converter')

root.configure(bg='dark blue')  # Set background color of the main window



# Create and place widgets with colors

label_temp = tk.Label(root, text='Enter Temperature:', bg='brown', fg='white')

label_temp.grid(row=0, column=0, padx=10, pady=10)

entry_temp = tk.Entry(root, bg='gray', fg='black')

entry_temp.grid(row=0, column=1, padx=10, pady=10)



selected_unit = tk.StringVar()

selected_unit.set('Celsius to Fahrenheit')

combo_units = ttk.Combobox(root, textvariable=selected_unit)

combo_units['values'] = ('Celsius to Fahrenheit', 'Fahrenheit to Celsius')

combo_units.grid(row=1, column=0, columnspan=2, padx=10, pady=10)



button_convert = tk.Button(root, text='Convert', command=convert_temperature, bg='#008CBA', fg='white')

button_convert.grid(row=2, column=0, columnspan=2, padx=10, pady=10)



label_result = tk.Label(root, text='Result:', bg='green', fg='white')

label_result.grid(row=3, column=0, columnspan=2, padx=10, pady=10)



# Run the main event loop

root.mainloop()

      
