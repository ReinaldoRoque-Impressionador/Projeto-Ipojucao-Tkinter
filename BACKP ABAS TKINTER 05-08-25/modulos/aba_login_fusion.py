import tkinter as tk


def criar_login(janela, ao_logar_callback=None):
    login_window = tk.Toplevel(janela)
    login_window.title("Login")

    tk.Label(login_window, text="Usuário:").grid(row=0, column=0, padx=10, pady=10)
    entry_usuario = tk.Entry(login_window)
    entry_usuario.grid(row=0, column=1, padx=10)

    tk.Label(login_window, text="Senha:").grid(row=1, column=0, padx=10, pady=10)
    entry_senha = tk.Entry(login_window, show="*")
    entry_senha.grid(row=1, column=1, padx=10)

    def autenticar():
        usuario = entry_usuario.get()
        senha = entry_senha.get()
        if usuario == "admin" and senha == "123":
            login_window.destroy()
            if ao_logar_callback:
                ao_logar_callback(usuario, "Administrador")
        else:
            tk.messagebox.showerror("Erro", "Credenciais inválidas")

    tk.Button(login_window, text="Entrar", command=autenticar).grid(row=2, columnspan=2, pady=20)