import ttkbootstrap as ttk
from tkinter import StringVar

# Fonction appelée lorsqu'un bouton numérique est pressé
def action_button_add_input_screen(msg: str):
    global label_screen_text
    current_text = label_screen_text.get()
    if current_text == "...":
        current_text = ""
    label_screen_text.set(current_text + msg)

# Fonction appelée lorsque le bouton "Effacer" est pressé
def action_button_numpad_clear():
    global label_screen_text
    label_screen_text.set("...")

# Fonction appelée lorsque le bouton "égal" est pressé
def action_button_numpad_equals():
    global label_screen_text
    current_text = label_screen_text.get()
    if current_text == "...":
        label_screen_text.set("...")
    else:
        try:
            result = eval(current_text)
            label_screen_text.set(str(result))
        except Exception as e:
            label_screen_text.set("Erreur: " + str(e))

# Fonction pour créer le pavé numérique dans un cadre donné
def create_numpad(frame: ttk.Frame):
    button_numpad = [None] * 9  # Liste pour stocker les boutons numériques
    row = 1  # Commencer à la première ligne pour les boutons numériques
    column = 0  # Commencer à la première colonne
    for i in range(1, 10):  # Boucle pour créer les boutons de 1 à 9
        # Créer un bouton avec le texte correspondant au nombre et la commande associée
        button_numpad[i-1] = ttk.Button(frame, text=str(i), command=lambda i=i: action_button_add_input_screen(str(i)))
        # Placer le bouton dans la grille avec un padding et le faire s'étendre
        button_numpad[i-1].grid(row=row, column=column, padx=5, pady=5, sticky="nsew")
        if column == 2:  # Si on atteint la troisième colonne, passer à la ligne suivante
            column = 0
            row += 1
        else:  # Sinon, passer à la colonne suivante
            column += 1

# Fonction appelée lorsque le bouton de virgule est pressé
def action_button_numpad_decimal_point():
    pass

# Fonction pour créer une nouvelle fenêtre d'application
def create_new_window(title: str, size: tuple) -> ttk.Window:
    """
    Crée une nouvelle fenêtre d'application avec le titre, le thème et la taille spécifiés.

    Cette fonction initialise et retourne une nouvelle fenêtre avec un thème prédéfini
    et les paramètres spécifiés.

    :param title: Le titre de la fenêtre.
    :type title: str
    :param size: Un tuple représentant les dimensions de la fenêtre (largeur, hauteur).
    :type size: tuple
    :return: L'instance de la nouvelle fenêtre créée.
    :rtype: ttk.Window
    """
    global label_screen_text

    root = ttk.Window(
        title=title,
        themename="superhero",
        size=size,
    )
    root.place_window_center()  # Centre la fenêtre sur l'écran
    root.columnconfigure(0, weight=1)  # Configure la colonne pour s'étendre
    root.rowconfigure(1, weight=1)  # Configure la ligne pour s'étendre

    # Initialisation de la variable globale après la création de la fenêtre principale
    label_screen_text = StringVar(value="...")

    # Cadre pour l'écran de la calculatrice
    frame_screen_calculator = ttk.Frame(root)
    frame_screen_calculator.grid(row=0, column=0, sticky="ew")  # Place le cadre en haut
    frame_screen_calculator.columnconfigure(0, weight=1)  # Configure la colonne pour s'étendre
    frame_screen_calculator.rowconfigure(0, weight=1)  # Configure la ligne pour s'étendre

    # Cadre pour le pavé numérique
    frame_numpad = ttk.Frame(root)
    frame_numpad.grid(row=1, column=0, sticky="nsew")  # Place le cadre en bas
    for i in range(4):  # Configure les colonnes et lignes pour s'étendre
        frame_numpad.columnconfigure(i, weight=1)
        frame_numpad.rowconfigure(i, weight=1)

    # Label pour afficher le résultat ou l'entrée actuelle
    label_screen = ttk.Label(frame_screen_calculator, text="...", font=("Helvetica", 16), textvariable=label_screen_text)
    label_screen.pack(padx=10, pady=10, anchor="center")  # Centre le label dans le cadre

    create_numpad(frame_numpad)  # Crée le pavé numérique dans le cadre

    # Création des boutons d'opérateurs, du bouton 0, du bouton virgule et du bouton effacer
    ttk.Button(frame_numpad, text="Effacer", command=action_button_numpad_clear).grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
    ttk.Button(frame_numpad, text="/", command=lambda: action_button_add_input_screen("/")).grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
    ttk.Button(frame_numpad, text="X", command=lambda: action_button_add_input_screen("*")).grid(row=0, column=2, padx=5, pady=5, sticky="nsew")
    ttk.Button(frame_numpad, text="-", command=lambda: action_button_add_input_screen("-")).grid(row=0, column=3, padx=5, pady=5, sticky="nsew")
    ttk.Button(frame_numpad, text="+", command=lambda: action_button_add_input_screen("+")).grid(row=1, rowspan=2, column=3, padx=5, pady=5, sticky="nsew")
    ttk.Button(frame_numpad, text="=", command=action_button_numpad_equals).grid(row=3, rowspan=2, column=3, padx=5, pady=5, sticky="nsew")
    ttk.Button(frame_numpad, text="0", command=lambda: action_button_add_input_screen("0")).grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
    ttk.Button(frame_numpad, text=".", command=lambda: action_button_add_input_screen(".")).grid(row=4, column=2, padx=5, pady=5, sticky="nsew")

    return root
