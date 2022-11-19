print("Program by Wojtekb30, Bird Tech, 26.04.2022")
print("Visit birdtech.weebly.com")
print("Welcome! This program allows you to render images as colourful text.")
from colr import color
from PIL import Image

import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.title("RenderBird ItCT")
root.withdraw()
wynik=""
x = 0
y = 0
nowyx = 0
nowyy = 0
trybpracy = int(input("Would you like to open a .btctif render file or JPG/BMP image? Type 1 if .btctif: "))
if trybpracy == 1:
    pliknazwaa = filedialog.askopenfilename(filetypes=(('Bird Tech Colorful Text Image File','*.btctif'),))
    if pliknazwaa:
        im = open(pliknazwaa, "r")
        print(im.read())
        im.close()
        print("Done. Unzoom your Terminal window to see the image.")
        print("Hold Ctrl and use mouse wheel to Zoom/Unzoom.")
        print("If image looks weird or something not renders, minimise and then maximise this program's window to make your computer rerender.")
        print("Screenshot (you can use Prt Sc) and eventually trim to save as image.")
        input("Press ENTER/RETURN to end program")
        quit()

    
im = Image.open(filedialog.askopenfilename(filetypes=(('JPG image','*.jpg'),('BMP image','*.bmp'))))
pytanie = int(input("Resize image? Type 1 if yes: "))
if pytanie == 1:
    nowyx = int(input("Type new height in pixels: "))
    nowyy = int(input("Type new width in pixels: "))
    im = im.resize((nowyy, nowyx))
slowo = str(input("Type a word or letter to render with (use ██ for pixel-like render): "))

dslowo = len(slowo)
nslowo = 0
print("Working. Might take several minutes.")
pix = im.load()
szerokosc, wysokosc = im.size
while (x<szerokosc and y<=wysokosc):
    if x+1==szerokosc and y+1==wysokosc:
        
        kolor = pix[szerokosc-1,wysokosc-1]
        wynik = wynik+str(color(slowo[nslowo]+" ", fore=kolor, back=(0, 0, 0)))
        break
    kolor = pix[x,y]

    if nslowo+1!=dslowo:
        wynik = wynik+str(color(slowo[nslowo]+slowo[nslowo+1], fore=kolor, back=(0, 0, 0)))
    else:
        wynik = wynik+str(color(slowo[nslowo], fore=kolor, back=(0, 0, 0)))
    nslowo = nslowo+2
    if nslowo == dslowo or nslowo == dslowo+1:
        nslowo = 0
    x = x+1
    if x>=szerokosc:
        x = 0
        y = y+1
#        print(wynik)
        wynik=wynik+"\n"

    
print(wynik)
#tempwynikfile = open("WordTermPicTemp.data", "w")
#tempwynikfile.write(wynik)
#tempwynikfile.close()
#tempwynikfile = open("WordTermPicTemp.data", "r")
#print(tempwynikfile.read())
#tempwynikfile.close()

print("Done. Unzoom your Terminal window to see the image.")
print("Hold Ctrl and use mouse wheel to Zoom/Unzoom.")
print("If image looks weird or something not renders, minimise and then maximise this program's window to make your computer rerender.")
print("Screenshot (you can use Prt Sc) and eventually trim to save as image.")
trybzapis = int(input("Save a .btctif? 1 if yes: "))
if trybzapis == 1:
    zapisfilename = filedialog.asksaveasfilename(filetypes=[("Bird Tech Colorful Text Image File","*.btctif")], defaultextension = "*.btctif")
    if zapisfilename:
        zapisanyplikk = open(zapisfilename, "w")
        zapisanyplikk.write(wynik)
        zapisanyplikk.close()
        
input("Press ENTER/RETURN to end the program")
    

