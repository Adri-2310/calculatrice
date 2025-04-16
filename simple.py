import ttkbootstrap as ttk

def action_button_numpad_number(nbr: str):
    print(nbr)

def action_button_numpad_clear():
    pass


def action_button_numpad_division():
    pass


def action_button_numpad_multiplication():
    pass


def action_button_numpad_subtraction():
    pass


def action_button_numpad_addition():
    pass


def action_button_numpad_equals():
    pass

def create_numpad(frame: ttk.Frame):
    button_numpad = [None] * 9
    row = 1
    column = 0
    for i in range(1, 10):  # Corrected range to generate numbers from 1 to 9
        button_numpad[i-1] = ttk.Button(frame, text=str(i), command=lambda i=i: action_button_numpad_number(str(i)))
        button_numpad[i-1].grid(row=row, column=column, padx=5, pady=5,sticky="nsew")
        if column == 2:
            column = 0
            row += 1
        else:
            column += 1


def action_button_numpad_decimal_point():
    pass


def create_new_window(title: str, size: tuple) -> ttk.Window:
    """
    Creates a new application window with the specified title, theme, and size.

    This function initializes and returns a newly created window with a predefined theme
    and the specified parameters.

    :param title: The title of the window.
    :type title: Str
    :param size: A tuple representing the dimensions of the window in (width, height).
    :type size: Tuple
    :return: The newly created window instance.
    :rtype: Ttk.Window
    """
    root = ttk.Window(
        title=title,
        themename="superhero",
        size=size,
    )
    root.place_window_center()
    root.columnconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)

    # Frame screen calculator
    frame_screen_calculator = ttk.Frame(root)
    frame_screen_calculator.grid(row=0, column=0, sticky="ew")
    # Configure frame screen calculator
    frame_screen_calculator.columnconfigure(0, weight=1)
    frame_screen_calculator.rowconfigure(0, weight=1)

    # Frame numpad
    frame_numpad = ttk.Frame(root)
    frame_numpad.grid(row=1, column=0, sticky="nsew")
    # Configure frame numpad
    for i in range(4):
        frame_numpad.columnconfigure(i, weight=1)
        frame_numpad.rowconfigure(i, weight=1)

    # Label
    label = ttk.Label(frame_screen_calculator, text="...", font=("Helvetica", 16))
    label.pack(padx=10, pady=10,anchor="center")

    create_numpad(frame_numpad)

    #create operator buttons, button 0, button virgule and clear
    ttk.Button(frame_numpad, text="Effacer", command=lambda : action_button_numpad_clear()).grid(row=0, column=0, padx=5, pady=5,sticky="nsew")
    ttk.Button(frame_numpad, text="/", command=lambda: action_button_numpad_division()).grid(row=0, column=1, padx=5, pady=5,sticky="nsew")
    ttk.Button(frame_numpad, text="X", command=lambda: action_button_numpad_multiplication()).grid(row=0, column=2, padx=5,pady=5,sticky="nsew")
    ttk.Button(frame_numpad, text="-", command=lambda: action_button_numpad_subtraction()).grid(row=0, column=3, padx=5,pady=5,sticky="nsew")
    ttk.Button(frame_numpad, text="+", command=lambda: action_button_numpad_addition()).grid(row=1, rowspan=2 ,column=3, padx=5,pady=5,sticky="nsew")
    ttk.Button(frame_numpad, text="=", command=lambda: action_button_numpad_equals()).grid(row=3, rowspan=2, column=3,padx=5, pady=5,sticky="nsew")
    ttk.Button(frame_numpad, text="0", command=lambda: action_button_numpad_number("0")).grid(row=4, column=0, columnspan=2, padx=5,pady=5,sticky="nsew")
    ttk.Button(frame_numpad, text=".", command=lambda: action_button_numpad_decimal_point()).grid(row=4, column=2, padx=5,pady=5,sticky="nsew")

    return root

