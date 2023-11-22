import customtkinter

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
root.geometry("700x400")


def test():
    print("Hello World")

def leftSide():
    leftFrame = customtkinter.CTkFrame(master=root)
    leftFrame.pack(pady=20, padx=10, fill="both", expand=True, side=customtkinter.LEFT)

    headline = customtkinter.CTkLabel(master=leftFrame, text="Scanner", font=("Arial", 20))
    headline.pack(pady=10, padx=10)

    searchButton = customtkinter.CTkButton(master=leftFrame, text="Nach Karte suchen", command=test)
    searchButton.pack(pady=10, padx=10)

    errorFrame = customtkinter.CTkFrame(master=leftFrame, border_color="red", border_width=1)
    errorFrame.pack(pady=10, padx=10)

    cardNotFoundLabel = customtkinter.CTkLabel(master=errorFrame, text="Karte wurde nicht gefunden \n Karte ist defekt")
    cardNotFoundLabel.pack(pady=10, padx=10)




def rightSide():


    rightFrame = customtkinter.CTkFrame(master=root)
    rightFrame.pack(pady=20, padx=10, fill="both", expand=True, side=customtkinter.RIGHT)

    headline = customtkinter.CTkLabel(master=rightFrame, text="Ausgang", font=("Arial", 20))
    headline.pack(pady=10, padx=10)

    outputFrame = customtkinter.CTkFrame(master=rightFrame, border_color="green", border_width=1)
    outputFrame.pack(pady=10, padx=10)

    outputLabel = customtkinter.CTkLabel(master=outputFrame, text="Kunde: \n Kartennummer: \n Ausgang: ")
    outputLabel.pack(pady=10, padx=10)

    openBrowserButton = customtkinter.CTkButton(master=rightFrame, text="Registrierung öffnen", command=test)
    openBrowserButton.pack(pady=10, padx=10)




leftSide()
rightSide()

root.mainloop()

