import tkinter, toml
from bindglobal import BindGlobal

config = toml.load("./config.toml")
print(config)

def onKeyPress(event):
    match event.char:
        case '1':
            onHotkey(1)
        case '2':
            onHotkey(2)
        case '3':
            onHotkey(3)
        case _:
            pass

def onHotkey(i: int) -> None:
    print(f"switch to preset {i}")

mainWindow = tkinter.Tk()
mainWindow.title("Simple PNG Tool")
mainWindow.minsize(500, 500)

# TODO: Add a widget for the avatar image

bg = BindGlobal(widget=mainWindow)
bg.gbind("<Control-Key>", onKeyPress)

mainWindow.mainloop()