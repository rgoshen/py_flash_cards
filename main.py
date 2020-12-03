from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

# --------------------------- UI SETUP -------------------------------- #
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Flash card
canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
x_image = PhotoImage(file="./images/wrong.png")
check_image = PhotoImage(file="./images/right.png")
unknown_button = Button(image=x_image, highlightthickness=0)
unknown_button.grid(row=1, column=0)
known_button = Button(image=check_image, highlightthickness=0)
known_button.grid(row=1, column=1)
window.mainloop()
