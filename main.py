from tkinter import *
import requests
import random


def get_quote():
    dict = {
        1:random.randrange(1,47), 2:random.randrange(1,72), 3:random.randrange(1,43), 4:random.randrange(1,42), 5:random.randrange(1,29),
        6:random.randrange(1,47), 7:random.randrange(1,30), 8: random.randrange(1,28), 9: random.randrange(1,32), 10: random.randrange(1,42),
        11: random.randrange(1,55), 12:random.randrange(1,20), 13: random.randrange(1,35), 14: random.randrange(1,27), 
        15: random.randrange(1,20), 16:random.randrange(1,24), 17: random.randrange(1,28), 18: random.randrange(1,78)
    }
    chapter,verse=random.choice(list(dict.items()))
    random_url = f"https://bhagavadgitaapi.in/slok/{chapter}/{verse}"
    print(random_url)

    response = requests.get(url=random_url)
    response.raise_for_status()
    data = response.json()
    canvas.itemconfig(slok_text, text=data["slok"])
    canvas.itemconfig(transliteration_text, text=data["transliteration"])
    canvas.itemconfig(hindi_text, text=data["tej"]["ht"])
    canvas.itemconfig(english_text, text=data["gambir"]["et"])


window = Tk()
window.title("Geeta says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=720, height=480)
background_img = PhotoImage(file="background.png")
canvas.create_image(400, 360, image=background_img)
slok_text = canvas.create_text(380, 50, text="Geeta Slok goes HERE", width=600, font=(
    "Arial", 12,"bold"), fill="black")
canvas.grid(row=0, column=0)
transliteration_text = canvas.create_text(380, 170, text="Geeta Slok goes HERE", width=600, font=(
    "Arial", 12,"bold"), fill="black")
hindi_text = canvas.create_text(380, 290, text="Geeta Slok goes HERE", width=600, font=(
    "Arial", 12,"bold"), fill="black")
english_text = canvas.create_text(380, 410, text="Geeta Slok goes HERE", width=600, font=(
    "Arial", 12,"bold"), fill="black")


get_quote()

next_button = Button(text="NEXT",
                      borderwidth=1, command=get_quote)
next_button.grid(row=1, column=0)
next_button.config(pady=5,padx=10)


window.mainloop()
