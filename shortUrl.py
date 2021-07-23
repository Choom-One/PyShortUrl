from tkinter import *
import pyshorteners
import pyperclip

root = Tk()
root.title("Сокращатель URL")
root.configure(bg="blue")
url = StringVar()
sortUrl = StringVar()


def urlsort():
    sort_Url = url.get()
    generatedurl = pyshorteners.Shortener().tinyurl.short(sort_Url)
    sortUrl.set(generatedurl)


def copy():
    generateurl = sortUrl.get()
    pyperclip.copy(generateurl)


Label(root, text="Сокращатель ссылок", font="Arial").pack(pady=15)
Entry(root, textvariable=url).pack(pady=5)
Button(root, text="Создать URl", command=urlsort).pack(pady=5)
Entry(root, textvariable=sortUrl).pack(pady=5)
Button(root, text="Скопировать URL", command=copy).pack(pady=5)

root.mainloop()
