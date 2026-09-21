import tkinter as tk
from tkinter import messagebox


class LoginView(tk.Frame):

    def __init__(self, master, on_login):
        super().__init__(master)

        self.on_login = on_login

        tk.Label(
            self,
            text="INICIO DE SESIÓN",
            font=("Arial", 16, "bold")
        ).pack(pady=10)

        tk.Label(self, text="Usuario").pack(pady=5)

        self.txt_usuario = tk.Entry(self)
        self.txt_usuario.pack()

        tk.Label(self, text="Contraseña").pack(pady=5)

        self.txt_password = tk.Entry(
            self,
            show="*"
        )
        self.txt_password.pack()

        tk.Button(
            self,
            text="Ingresar",
            command=self.validar
        ).pack(pady=10)

    def validar(self):

        usuario = self.txt_usuario.get()
        password = self.txt_password.get()

        if usuario == "admin" and password == "1234":
            self.on_login()
        else:
            messagebox.showerror(
                "Error",
                "Credenciales incorrectas"
            )