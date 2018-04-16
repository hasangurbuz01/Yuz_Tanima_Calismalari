import tkinter as tk

root = tk.Tk()

v = tk.IntVar()
v.set(1)

languages = [
    ("NewYork",1),
    ("Paris",2),
    ("Dubai",3),
    ("Sydney",4),
    ("Istanbul",5)
]

def ShowChoice():
    print(v.get())

tk.Label(root,
         text="""Select a city:""",
         justify = tk.LEFT,
         padx = 20).pack()

for val, language in enumerate(languages):
    tk.Radiobutton(root,
                  text=language,
                  padx = 20,
                  variable=v,
                  command=ShowChoice,
                  value=val).pack(anchor=tk.W)


root.mainloop()
