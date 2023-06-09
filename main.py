from tkinter import *;
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
#import mysql.connector


class Hospital:
    def __init__(self,root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")

        lbltitle = Label(self.root,bd=20,relief=RIDGE,text="HOSPITAL MANAGEMENT SYSTEM",fg='red',bg='white',font=("times new roman",50,"bold"))
        lbltitle.pack(side=TOP,fill=X)

        #=======================================================Data Frame=========================================
        DataFrame = Frame(self.root,bd=20,relief=RIDGE)
        DataFrame.place(x=0,y=130,width=1530,height=400)

        DataFrameLeft = LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=10,font=("times new roman",12,"bold"),text="Patient Information")
        DataFrameLeft.place(x=0,y=5,width=980,height=350)

        DataFrameRight = LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=10,font=("times new roman",12,"bold"),text="Prescription")
        DataFrameRight.place(x=990,y=5,width=460,height=350)

        #=========================================================Button Frame=============================================
        ButtonFrame = Frame(self.root,bd=20,relief=RIDGE)
        ButtonFrame.place(x=0,y=530,width=1530,height=70)

        #===================================================Details Frame==============
        ButtonFrame = Frame(self.root,bd=20,relief=RIDGE)
        ButtonFrame.place(x=0,y=600,width=1530,height=190)

        #===============================================Data Frame Left=================
        lblNameTablet = Label(DataFrameLeft,text="Name of tablet",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblNameTablet.grid(row=0,column=0,sticky=W)

        comNameTablet = ttk.Combobox(DataFrameLeft,font=("times new roman",12,"bold"),width=33)
        comNameTablet["values"] = ("Nice","Corona Vaccine","Acetaminophen","Adderall","Almodipine","Ativan")
        comNameTablet.grid(row=0,column=1)

        lblDose = Label(DataFrameLeft,text="Dosage",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblDose.grid(row=1,column=0,sticky=W)

        lblNoOfTablet = Label(DataFrameLeft,text="No. of Tablet",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblNoOfTablet.grid(row=2,column=0,sticky=W)


root = Tk()
ob = Hospital(root)
root.mainloop()