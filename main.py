from tkinter import *
from tkinter import messagebox
import base64
import os

def encrypt():
    password = code.get()
    if password =="1234":
        screen_2 = Toplevel(screen)
        screen_2.title("Encryption")
        screen_2.geometry("400x200")
        
        message = text_1.get(1.0, END)
        encode_message = message.encode("ascii")
        base = base64.b64encode(encode_message)
        encrypt = base.decode("ascii")
        
        Label(screen_2, text="Encrypt",fg="black").place(x=15, y=10)
        text_2 = Text(screen_2, bg="white", wrap=WORD)
        text_2.place(x=15,y=20)
        
        text_2.insert(END,encrypt)
        
    elif password =="":
        messagebox.showerror("ecryption", "Password is missing")
        
    elif password != "1234":
        messagebox.showerror("ecryption", "Wrong password")
            
def decrypt():
    password = code.get()
    
    if password =="1234":
        screen_2 = Toplevel(screen)
        screen_2.title("Decryption")
        screen_2.geometry("400x200")
        
        message = text_1.get(1.0, END)
        decode_message = message.encode("ascii")
        base = base64.b64decode(decode_message)
        decrypt = base.decode("ascii")
        
        Label(screen_2, text="Decrypt",fg="black").place(x=15, y=10)
        text_2 = Text(screen_2, bg="white", wrap=WORD)
        text_2.place(x=15,y=20)
        
        text_2.insert(END,decrypt)
        
    elif password =="":
        messagebox.showerror("decryption", "Password is missing")
        
    elif password != "1234":
        messagebox.showerror("decryption", "Wrong password")



def main_screen():
    global screen
    global code
    global text_1
    
    screen = Tk()
    screen.geometry("340x300")
    screen.title("Message encrypt")
    def reset():
        code.set("")
        text_1.delete(1.0, END)
    
    Label(text='Enter the text to ecrypt or to decrypt', fg="black").place(x=15, y=10)
    text_1 = Text(background="white", wrap=WORD)
    text_1.place(x=15, y=50, width=300,height=90)
    
    Label(text="Enter secret key for encryption and decryption", fg="black").place(x=15, y=150)
    code = StringVar()
    Entry(textvariable=code, width=23, show="*").place(x=15, y=170)
    
    Button(text="Encrypt",width="10", bg="#ff3333", fg="white", bd=0, command=encrypt).place(x=15, y=200)
    Button(text="Decrypt",width="10", bg="#33cc33", fg="white", bd=0, command=decrypt).place(x=100, y=200)
    Button(text="Reset",width="20", bg="#4d88ff", fg="white", bd=0, command=reset).place(x=15, y=250)
    
    screen.mainloop()
main_screen()
    