#!/usr/bin/env python
# coding: utf-8

# In[9]:


import tkinter
import tkinter.messagebox
import customtkinter

#_______________________apariencia de la ventana_______________________
customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        #_______________________dimensiones de la ventana_______________________
        self.title("Reporte mensual de productividad")
        self.geometry(f"{1100}x{580}")

        #_______________________grid layout_______________________
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)  


# In[ ]:




