import tkinter as tk

def show_choices(option):
    # Clear the previous choices frame
    for widget in choices_frame.winfo_children():
        widget.destroy()

    # Add a back button in the top left corner
    tk.Button(choices_frame, text="Back", command=go_back_to_main, bg="gray", fg="white").pack(pady=5)

    # Add new choices based on the selected option
    if option == 1:
        choices = ["Acceleration", "Area", "Electricity", "Energy", "Force", "Length", "Mass", "Pressure", "Speed", "Temperature", "Time", "Volume"]
    elif option == 2:
        choices = ["Calculate Density", "Calculate Displacement", "Calculate Force", "Calculate Pressure"]

    # Create buttons for each new choice with the same size
    for choice in choices:
        tk.Button(choices_frame, text=choice, command=lambda c=choice: show_sub_choices(c), width=20, height=1).pack(pady=2)

def go_back_to_main():
    # Clear the previous choices frame
    for widget in choices_frame.winfo_children():
        widget.destroy()
    
    # Recreate the main option buttons with the same size
    tk.Button(choices_frame, text="Simple Conversions", command=lambda: show_choices(1), width=20, height=2).pack(side="left", padx=5)
    tk.Button(choices_frame, text="Complex Conversions", command=lambda: show_choices(2), width=20, height=2).pack(side="left", padx=5)

def show_sub_choices(choice):
    # Clear the previous choices frame
    for widget in choices_frame.winfo_children():
        widget.destroy()

    # Add a back button in the top left corner
    tk.Button(choices_frame, text="Back", command=go_back_to_main, bg="gray", fg="white").pack(pady=5)

    # Display the selected choice text
    choice_label = tk.Label(choices_frame, text=f"You selected: {choice}")
    choice_label.pack(pady=5)

def gui():
    main_bg = 'lightblue'

    root = tk.Tk()
    root.geometry("700x500")

    root.configure(bg=main_bg)

    # Add main label
    label = tk.Label(root, text="Metricus GUI", bg=main_bg, fg="black", font=("Helvetica", 18))
    label.grid(row=0, column=0, columnspan=3, sticky="n", padx=10, pady=10)

    # Create the frame to display choices based on the selected option
    global choices_frame
    choices_frame = tk.Frame(root, bg=main_bg)
    choices_frame.grid(row=2, column=0, columnspan=3, pady=10)

    # Show main options initially
    go_back_to_main()

    # Add close button
    close_button = tk.Button(root, text="Close", bg="darkred", fg="white", width=10, height=1, command=root.destroy)
    close_button.grid(row=3, column=1, pady=10)

    # Configure grid to expand and center the widgets
    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=1)
    root.grid_rowconfigure(2, weight=1)
    root.grid_rowconfigure(3, weight=0)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)
    root.grid_columnconfigure(2, weight=1)

    root.mainloop()

