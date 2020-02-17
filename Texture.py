from PIL import Image
import pytesseract
import tkinter
from tkinter.filedialog import askopenfilename

#tkinter.Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
window=tkinter.Tk()

window.title("Texture")
window.geometry("512x256")
window.resizable(0,0)

top=tkinter.Frame(window).pack(pady=10)

label=tkinter.Label(window,text="Texture",font=("Courier New",25,"bold"))
label.pack(side='top',pady=10)
def open(event):
    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    print(filename)
    im=Image.open(filename)
    text=pytesseract.image_to_string(im,lang='eng')
    print(text)
    info = tkinter.Label(window,text='(Ctrl+C to Copy after drag selection)',font=("Courier New",10,"bold"))
    info.pack(pady=10)
    texture = tkinter.Entry(window,state='readonly',text=text,justify='center',font=("Courier New",15,"bold"),width=20)
    texture.pack(side='top',fill=tkinter.X,padx=30,pady=3)
    var = tkinter.StringVar()
    var.set(text)
    texture.configure(textvariable=var,relief='flat',background="white")
    #texture.configure(inactiveselectbackground=texture.cget("selectbackground"))
    
button=tkinter.Button(window,text="Open image files",font=("Courier New",10,"bold"))
button.bind("<Button-1>",lambda event:open(event))
button.pack(side='top',pady=10)

window.mainloop()
