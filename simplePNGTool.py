import tkinter
from bindglobal import BindGlobal

def HotKey1(event):
    onHotkey(1)
def HotKey2(event):
    onHotkey(2)
def HotKey3(event):
    onHotkey(3)

def onHotkey(i: int) -> None:
    print(f"switch to preset {i}")

mainWindow = tkinter.Tk()
mainWindow.title("Simple PNG Tool")
mainWindow.minsize(300, 300)

bg = BindGlobal(widget=mainWindow)
bg.gbind("<Control-1>", HotKey1)
bg.gbind("<Control-2>", HotKey2)
bg.gbind("<Control-3>", HotKey3)

mainWindow.mainloop()