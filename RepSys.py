#!/usr/bin/env python
# coding: utf-8

# In[37]:


#Librerias 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img
import seaborn as sns
from datetime import datetime
import pandas as pd
from collections import Counter 


# In[38]:


fecha=datetime.now().strftime("%m-%d-%Y_%H'%M'%S")
print(fecha)


# In[39]:


#funcion para abrir el csv
def open_csv(file):
    data=pd.read_csv(file)
    print(type(data))
    return data


# In[192]:


#funcion de escritura del csv
def write_csv(df,name):
    fecha=str(datetime.now().strftime("%m-%d-%Y"))
    name=name+"_"+fecha
    name_pdf="reports/"+name+".pdf"
    plt.suptitle("Gráficas "+name,position=(0.5, 0.91), fontsize=14, fontweight='bold')
    name_csv="reports/"+name+".csv"
    df.to_csv(name_csv,header=True, index=True)
    plt.savefig(name_pdf,dpi=600, bbox_inches='tight')
    print("archivo guardado")
    


# In[164]:


'''funcion de escritura del pdf
def write_pdf(df,name):
    pdf_name=write_csv(df,name)
    name_pdf="reports/"+pdf_name+".pdf"
    plt.suptitle("Gráficas "+pdf_name, fontsize=14, fontweight='bold')
    name_pdf="./"+name+".pdf"   
    plt.savefig(namepdf,dpi=600, bbox_inches='tight')
    print("archivo pdf guardado")'''


# In[42]:


#Cargar base de datos de csv
file="file/delivery_dataset.csv"
dt_report=open_csv(file)
dt_report.info()
dt_report


# In[43]:


dt_report.shape


# In[44]:


dt_report.count()


# In[45]:


dt_report.dtypes


# In[46]:


dt_report.columns


# In[47]:


dt_report.isnull().sum()


# In[48]:


dt_report=dt_report.dropna() 


# In[49]:


dt_report.isnull().sum()


# In[50]:


dt_report.head() 


# In[166]:


#Plot con resumen del reporte mensual (Categorias entre cantidad de unidades enviadas)
fig=plt.figure(figsize=(15,20))
ax=fig.gca()
dt_report.hist(ax=ax)
plt.suptitle("Resumen del reporte mensual por categorias",position=(0.5, 0.91),
          fontdict={'family': 'Arial', 
                    'color' : 'darkblue',
                    'weight': 'bold',
                    'size': 25},fontsize=20)
#fig.suptitle(' Set a Single Main Title for All the Subplots ', fontsize=30)
plt.savefig("graph/graphic1.jpg")
plt.show()


# In[167]:


# Grafica que muestra la cantidad de paquetes enviados en el registro de un mes
fig= plt.figure(figsize=(8,12))
pd.crosstab(dt_report['Month'],dt_report['Delivery_Status']).plot(kind='bar',figsize=(20,10))
plt.suptitle("Grafica que muestra la cantidad de paquetes enviados en el registro de un mes",position=(0.5, 0.93),
          fontdict={'family': 'Arial', 
                    'color' : 'darkblue',
                    'weight': 'bold',
                    'size': 25},fontsize=20)
plt.savefig("graph/graphic2.jpg")


# In[168]:


#Grafica que muestra el Dia que mas hubo envios
fig= plt.figure(figsize=(8,8))
fig = dt_report.DayOfWeek.value_counts()
plt.suptitle("Grafica que muestra el Dia que mas hubo envios",position=(0.5, 0.9),
          fontdict={'family': 'Arial', 
                    'color' : 'darkblue',
                    'weight': 'bold',
                    'size': 25},fontsize=20)
fig.plot.pie()
plt.savefig("graph/graphic2.jpg")


# In[169]:


#Grafica que muestra el Dia que mas hubo retraso de entregas de paquetes
fig= plt.figure(figsize=(15,10))
dt_report.plot.scatter(y="DayOfWeek", x="Shipment_Delay")
plt.suptitle("Grafica que muestra el Dia que mas hubo envios",position=(0.5, 0.95),
          fontdict={'family': 'Arial', 
                    'color' : 'darkblue',
                    'weight': 'bold',
                    'size': 25},fontsize=15)
plt.savefig("graph/graphic3.jpg")


# In[171]:


#Graficas de Carrier_Name, Source y Destination segun el estado de envio
fig= plt.figure(figsize=(9,9))
fig.add_subplot(311)
dt_feature1=pd.crosstab(dt_report['Carrier_Name'],dt_report['Delivery_Status']).plot(kind='bar',figsize=(30,20))
plt.title("Grafica para Carrier_Name",fontsize=50)
plt.savefig("graph/graphic4.jpg")
fig.add_subplot(312)
dt_feature2=pd.crosstab(dt_report['Source'],dt_report['Delivery_Status']).plot(kind='bar',figsize=(30,20))
plt.title("Grafica para Source",fontsize=50)
plt.savefig("graph/graphic5.jpg")
fig.add_subplot(313)
dt_feature3=pd.crosstab(dt_report['Destination'],dt_report['Delivery_Status']).plot(kind='bar',figsize=(30,20))
plt.title("Grafica para Destination",fontsize=50)
plt.savefig("graph/graphic6.jpg")


# In[181]:


#creacion del conjunto de graficas
def show_with_matplotlib(color_img, pos):
    """Mostar una imagen usando MatPlotLib"""
    # Convertir imagen BGR a RGB
    #img_RGB = color_img[:, :, ::-1]
    ax = plt.subplot(6, 1, pos)
    plt.imshow(color_img)
    plt.axis('off')


# In[197]:


#cargar imagenes
grap_1=img.imread("graph/graphic1.jpg")
grap_2=img.imread("graph/graphic2.jpg")
grap_3=img.imread("graph/graphic3.jpg")
grap_4=img.imread("graph/graphic4.jpg")
grap_5=img.imread("graph/graphic5.jpg")
grap_6=img.imread("graph/graphic6.jpg")

plt.figure(figsize=(50, 50))

# Graficar las images:
show_with_matplotlib(grap_1, 1)
show_with_matplotlib(grap_2, 2)
show_with_matplotlib(grap_3, 3)
show_with_matplotlib(grap_4, 4)
show_with_matplotlib(grap_5, 5)
show_with_matplotlib(grap_6, 6)
write_csv(dt_report,"Reporte_Mensual")
# Mostrar los resultados de la aplicacion en lugar de un alto mando
plt.show()


# In[286]:


#Interfaz grafica
import tkinter
import tkinter.messagebox
from tkinter import *
from PIL import ImageTk, Image
import customtkinter


# In[287]:


#_______________________apariencia de la ventana_______________________
customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"


# In[288]:


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
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text="Resumen mensual por categorias", command=graph_año)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text="Paquetes enviados en un mes",command=graph_mes)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, text="Dias que mas hubo envios",command=graph_dia_mes)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame, text="Carrier",command=graph_dia_semana)
        self.sidebar_button_4.grid(row=4, column=0, padx=20, pady=10)
        self.sidebar_button_5 = customtkinter.CTkButton(self.sidebar_frame, text="Source",command=graph_tiempo_entrega)
        self.sidebar_button_5.grid(row=5, column=0, padx=20, pady=10)
        self.sidebar_button_6 = customtkinter.CTkButton(self.sidebar_frame, text="Destination",command=graph_carrier)
        self.sidebar_button_6.grid(row=6, column=0, padx=20, pady=10) 
        


# In[351]:


#_______________________ventanas emergentes de los botones para mostar las graficas_______________________

def graph_año():
    
    año = tkinter.Toplevel()
    año.title("Resumen del reporte mensual por categorias")
    año.config(width=700, height=900)   
    canvas = Canvas(año,width=700, height=900) 
    canvas.pack()
    img=Image.open('graph/graphic1.jpg')
    img_resize=img.resize((690, 890), Image.ANTIALIAS)
    imagen=ImageTk.PhotoImage(img_resize)
    canvas.create_image(10,10,anchor=NW,image=imagen)
    self.sidebar_button_1
    
    
def graph_mes():
    año = tkinter.Toplevel()
    año.title("Grafica que muestra la cantidad de paquetes enviados en el registro de un mes")
    año.config(width=576, height=576)
    canvas = Canvas(año,width=576, height=576) 
    canvas.pack()
    img=Image.open('graph/graphic2.jpg')
    img_resize=img.resize((566, 566), Image.ANTIALIAS)
    imagen=ImageTk.PhotoImage(img_resize)
    canvas.create_image(10,10,anchor=NW,image=imagen)   
    self.sidebar_button_2
    
def graph_dia_mes():
    año = tkinter.Toplevel()
    año.title("Grafica que muestra el Dia que mas hubo envios")
    año.config(width=432, height=288)
    canvas = Canvas(año,width=432, height=288) 
    canvas.pack()
    img=Image.open('graph/graphic3.jpg')
    img_resize=img.resize((422, 278), Image.ANTIALIAS)
    imagen=ImageTk.PhotoImage(img_resize)
    canvas.create_image(10,10,anchor=NW,image=imagen)
    self.sidebar_button_3
    
def graph_dia_semana():
    año = tkinter.Toplevel()
    año.title("Gráfica semanal")
    año.config(width=900, height=700)
    canvas = Canvas(año,width=900, height=700) 
    canvas.pack()
    img=Image.open('graph/graphic4.jpg')
    img_resize=img.resize((890, 690), Image.ANTIALIAS)
    imagen=ImageTk.PhotoImage(img_resize)
    canvas.create_image(10,10,anchor=NW,image=imagen)
    self.sidebar_button_4
    
def graph_tiempo_entrega():
    año = tkinter.Toplevel()
    año.title("Gráfico de tiempos de entrega")
    año.config(width=900, height=700)
    canvas = Canvas(año,width=900, height=700) 
    canvas.pack()
    img=Image.open('graph/graphic5.jpg')
    img_resize=img.resize((890, 690), Image.ANTIALIAS)
    imagen=ImageTk.PhotoImage(img_resize)
    canvas.create_image(10,10,anchor=NW,image=imagen)
    self.sidebar_button_5
    
def graph_carrier():
    año = tkinter.Toplevel()
    año.title("Gráfico de carrier")
    año.config(width=900, height=700)
    canvas = Canvas(año,width=900, height=700) 
    canvas.pack()
    img=Image.open('graph/graphic6.jpg')
    img_resize=img.resize((890, 690), Image.ANTIALIAS)
    imagen=ImageTk.PhotoImage(img_resize)
    canvas.create_image(10,10,anchor=NW,image=imagen)
    self.sidebar_button_6


# In[352]:


app = App()
app.mainloop()


# In[ ]:





# In[ ]:





# In[ ]:




