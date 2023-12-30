from math import pi, sqrt, sin, cos, tan, acos
from ttkbootstrap import Window, IntVar
from ttkbootstrap import Radiobutton, Label, Entry, Button
from tkinter.messagebox import showinfo, showerror

r = Window()
r.title("Triangles")
r.resizable(False, False)
al = Label(r, text="Edge a:")
bl = Label(r, text="Edge b:")
cl = Label(r, text="Edge c:")
Al = Label(r, text="∠A(°):")
Bl = Label(r, text="∠B(°):")
Cl = Label(r, text="∠C(°):")
ae = Entry(r)
be = Entry(r)
ce = Entry(r)
Ae = Entry(r)
Be = Entry(r)
Ce = Entry(r)
iv = IntVar()


def sas():
    al.grid(row=0, column=2)
    bl.grid(row=1, column=2)
    Cl.grid(row=2, column=2)
    Al.grid_forget()
    Bl.grid_forget()
    cl.grid_forget()
    ae.grid(row=0, column=3)
    be.grid(row=1, column=3)
    Ce.grid(row=2, column=3)
    Ae.grid_forget()
    Be.grid_forget()
    ce.grid_forget()


def sss():
    al.grid(row=0, column=2)
    bl.grid(row=1, column=2)
    cl.grid(row=2, column=2)
    Al.grid_forget()
    Bl.grid_forget()
    Cl.grid_forget()
    ae.grid(column=3)
    be.grid(row=1, column=3)
    ce.grid(row=2, column=3)
    Ae.grid_forget()
    Be.grid_forget()
    Ce.grid_forget()


sas()
Radiobutton(r, text="SAS", variable=iv, value=0, command=sas).grid(row=0, column=0)
Radiobutton(r, text="SSS", variable=iv, value=1, command=sss).grid(row=1, column=0)


def p():
    try:
        if iv.get() == 0:
            C = float(Ce.get())
            if C < 180:
                a = float(ae.get())
                b = float(be.get())
                radC = C * pi / 180
                cosC = cos(radC)
                c = sqrt(a * a + b * b - 2 * a * b * cos(radC))
                cosA = (b * b + c * c - a * a) / (2 * b * c)
                cosB = (a * a + c * c - b * b) / (2 * a * c)
                radA = acos(cosA)
                radB = acos(cosB)
                halfC = (a + b + c) / 2
                showinfo("Information",
                         """S = %f.
C = %f.
c = %f.
∠A = %f°.
∠B = %f°.
sinA = %f.
sinB = %f.
sinC = %f.
cosA = %f.
cosB = %f.
cosC = %f.
tanA = %f.
tanB = %f.
tanC = %f."""
                         % (sqrt(halfC*(halfC-a)*(halfC-b)*(halfC-c)), 2 * halfC, c, radA/pi*180, radB/pi*180,
                            sin(radA), sin(radB), sin(radC), cosA, cosB, cosC, tan(radA), tan(radB), tan(radC)))
            else:
                showerror("Error", "This is not a triangle.")
        else:
            a = float(ae.get())
            b = float(be.get())
            c = float(ce.get())
            if a + b > c and a + c > b and b + c > a:
                halfC = (a + b + c) / 2
                cosA = (b * b + c * c - a * a) / (2 * b * c)
                cosB = (a * a + c * c - b * b) / (2 * a * c)
                cosC = (a * a + b * b - c * c) / (2 * a * b)
                radA = acos(cosA)
                radB = acos(cosB)
                radC = acos(cosC)
                showinfo("Information",
                         """S = %f.
C = %f.
∠A = %f°.
∠B = %f°.
∠C = %f°.
sinA = %f.
sinB = %f.
sinC = %f.
cosA = %f.
cosB = %f.
cosC = %f.
tanA = %f.
tanB = %f.
tanC = %f.""" % (sqrt(halfC * (halfC-a)*(halfC-b)*(halfC-c)), 2*halfC, radA/pi*180, radB/pi*180, radC/pi*180,
                 sin(radA), sin(radB), sin(radC), cosA, cosB, cosC, tan(radA), tan(radB), tan(radC)))
            else:
                showerror("Error", "This is not a triangle.")
    except ValueError:
        showerror("Error", "Invalid value.")


Button(r, text="Process", command=p).grid(row=2, column=0)
r.mainloop()
