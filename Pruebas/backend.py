import tkinter
import tkinter.messagebox
from tkinter import *
from PIL import ImageTk, Image
import customtkinter

root = Tk()
root.title('imagen')
#_______________________apariencia de la ventana_______________________
customtkinter.set_appearance_mode("light")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        #_______________________dimensiones de la ventana_______________________
        self.title("Reporte mensual de productividad")
        self.geometry(f"{300}x{450}")

        #_______________________grid layout_______________________
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1) 

        
       # _______________________Graficas individuales_______________________
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=7, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(7, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="¡Escoge que vas a graficar!", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text="Año", command=graph_año)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text="Mes",command=graph_mes)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, text="Dia del mes",command=graph_dia_mes)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame, text="Dia de la semana",command=graph_dia_semana)
        self.sidebar_button_4.grid(row=4, column=0, padx=20, pady=10)
        self.sidebar_button_5 = customtkinter.CTkButton(self.sidebar_frame, text="Tiempos de entrega",command=graph_tiempo_entrega)
        self.sidebar_button_5.grid(row=5, column=0, padx=20, pady=10)
        self.sidebar_button_6 = customtkinter.CTkButton(self.sidebar_frame, text="Carrier",command=graph_carrier)
        self.sidebar_button_6.grid(row=6, column=0, padx=20, pady=10) 
        self.sidebar_button_7 = customtkinter.CTkButton(self.sidebar_frame, text="Destinos",command=graph_destinos)
        self.sidebar_button_7.grid(row=7, column=0, padx=20, pady=10)
        self.sidebar_button_8 = customtkinter.CTkButton(self.sidebar_frame, text="Reporte General",command=graph_general)
        self.sidebar_button_8.grid(row=8, column=0, padx=20, pady=10)

    
#_______________________ventanas emergentes de los botones para mostar las graficas_______________________
def graph_año():
    año = tkinter.Toplevel()
    año.title("Gráfico anual")
    año.config(width=300, height=200)
    self.sidebar_button_1
    
def graph_mes():
    año = tkinter.Toplevel()
    año.title("Gráfico mensual general")
    año.config(width=300, height=200)
    self.sidebar_button_2
    
def graph_dia_mes():
    año = tkinter.Toplevel()
    año.title("Gráfico mensual por dia")
    año.config(width=300, height=200)
    imagen = ImageTk.PhotoImage(Image.open('enviodedia.jpeg'))
    label = Label(image=imagen)
    label.pack()
    self.sidebar_button_3
    
def graph_dia_semana():
    año = tkinter.Toplevel()
    año.title("Gráfica semanal")
    año.config(width=300, height=200)
    self.sidebar_button_4
    
def graph_tiempo_entrega():
    año = tkinter.Toplevel()
    año.title("Gráfico de tiempos de entrega")
    año.config(width=300, height=200)
    self.sidebar_button_5
    
def graph_carrier():
    año = tkinter.Toplevel()
    año.title("Gráfico de carrier")
    año.config(width=300, height=200)
    self.sidebar_button_6
    
def graph_destinos():
    año = tkinter.Toplevel()
    año.title("Gráfico de destinos")
    año.config(width=300, height=200)
    self.sidebar_button_7
    
def graph_general():
    año = tkinter.Toplevel()
    año.title("Gráfico general")
    año.config(width=300, height=200)
    self.sidebar_button_8
 
    
    
if __name__ == "__main__":
    app = App()
    app.mainloop()

   



