import tkinter as tk
from tkinter import ttk

class AboutFrame(ttk.Frame):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.label = ttk.Label(self)
        self.label["text"] = ("Visitanos en recursospython.com y "
                              "foro.recursospython.com.")
        self.label.pack()
        
        self.web_button = ttk.Button(self, text="Visitar web")
        self.web_button.pack(pady=10)
        
        self.forum_button = ttk.Button(self, text="Visitar foro")
        self.forum_button.pack()

class Application(ttk.Frame):
    
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Panel de pestañas en Tcl/Tk")
        
        self.notebook = ttk.Notebook(self)
        
        self.about_frame = AboutFrame(self.notebook)
        self.notebook.add(
            self.about_frame, text="Acerca de", padding=10)
        
        self.notebook.pack(padx=10, pady=10)
        self.pack()
main_window = tk.Tk()
app = Application(main_window)
app.mainloop()