import tkinter as tk
import operations
import operations.acceleration
import operations.area
import operations.complex_operations

def send_data(choice):
    # Capture inputs
    try:
        from_unit_row = from_unit_entry.get().lower()
        to_unit_row = to_unit_entry.get().lower()

        input_value = float(input_entry.get())
        from_unit = from_unit_row.replace(' ', '_')
        to_unit = to_unit_row.replace(' ', '_')

        if choice == 'Acceleration':
          result = operations.acceleration.acceleration_converter(input_value, from_unit, to_unit, with_unit=True)
        else:
          result = "Conversion not implemented for this choice."

        result_label.config(text=f"Result: {result}", fg="black")
    except Exception as e:
        result_label.config(text=f"Error: {e}", fg="red")

def show_choices(option):
    for widget in choices_frame.winfo_children():
        widget.destroy()

    back_button = tk.Button(choices_frame, text="Back", command=go_back_to_main, bg="gray", fg="white")
    back_button.grid(row=0, column=0, padx=5, pady=5, sticky="w")

    if option == 1:
        choices = ["Acceleration", "Area", "Electricity", "Energy", "Force", "Length", "Mass", "Pressure", "Speed", "Temperature", "Time", "Volume"]
    elif option == 2:
        choices = ["Calculate Density", "Calculate Displacement", "Calculate Force", "Calculate Pressure"]

    for i, choice in enumerate(choices):
        tk.Button(choices_frame, text=choice, command=lambda c=choice: show_sub_choices(c), width=20, height=1).grid(row=i + 1, column=1, padx=10, pady=2, sticky="n")

def go_back_to_main():
    for widget in choices_frame.winfo_children():
        widget.destroy()
    
    tk.Button(choices_frame, text="Simple Conversions", command=lambda: show_choices(1), width=20, height=2).grid(row=0, column=1, padx=10, pady=10)
    tk.Button(choices_frame, text="Complex Conversions", command=lambda: show_choices(2), width=20, height=2).grid(row=1, column=1, padx=10, pady=10)

def show_sub_choices(choice):
    global input_entry, from_unit_entry, to_unit_entry, result_label

    for widget in choices_frame.winfo_children():
        widget.destroy()

    back_button = tk.Button(choices_frame, text="Back", command=go_back_to_main, bg="gray", fg="white")
    back_button.grid(row=0, column=0, padx=5, pady=5, sticky="w")

    tk.Label(choices_frame, text=f"{choice} Input (num):", bg="lightblue").grid(row=1, column=0, padx=10, pady=5, sticky="e")
    input_entry = tk.Entry(choices_frame)
    input_entry.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(choices_frame, text="From Unit (str):", bg="lightblue").grid(row=2, column=0, padx=10, pady=5, sticky="e")
    from_unit_entry = tk.Entry(choices_frame)
    from_unit_entry.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(choices_frame, text="To Unit (str):", bg="lightblue").grid(row=3, column=0, padx=10, pady=5, sticky="e")
    to_unit_entry = tk.Entry(choices_frame)
    to_unit_entry.grid(row=3, column=1, padx=10, pady=5)

    submit_button = tk.Button(choices_frame, text="Submit", command=lambda: send_data(choice))
    submit_button.grid(row=4, column=0, columnspan=2, pady=10)

    # Label to display the result
    result_label = tk.Label(choices_frame, text="Result: ", bg="lightblue", fg="black", wraplength=400)
    result_label.grid(row=5, column=0, columnspan=2, pady=10)

def gui():
    main_bg = 'lightblue'

    root = tk.Tk()
    root.geometry("700x500")
    root.configure(bg=main_bg)

    label = tk.Label(root, text="Metricus GUI", bg=main_bg, fg="black", font=("Helvetica", 18))
    label.grid(row=0, column=1, pady=10)

    global choices_frame
    choices_frame = tk.Frame(root, bg=main_bg)
    choices_frame.grid(row=1, column=1, pady=10, sticky="nsew")

    go_back_to_main()

    close_button = tk.Button(root, text="Close", bg="darkred", fg="white", width=10, height=1, command=root.destroy)
    close_button.grid(row=2, column=1, pady=10)

    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=1)
    root.grid_rowconfigure(2, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(2, weight=1)

    root.mainloop()

gui()
