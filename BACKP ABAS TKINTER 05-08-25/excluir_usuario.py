# import tkinter as tk
# from tkinter import messagebox
# from PIL import Image, ImageTk
# # Se 'usuarios' estiver definido em outro arquivo:
# from aba_login import usuarios  # ou o arquivo correto
#
#
# usuario_atual = None
#
#
#
#
# def excluir_usuario(janela_principal):
#     janela_excluir = tk.Toplevel(janela_principal)
#     janela_excluir.title("Excluir Usuário")
#     janela_excluir.geometry("400x200")
#
#     tk.Label(janela_excluir, text="Email do usuário a excluir:").pack(pady=10)
#     email_entry = tk.Entry(janela_excluir)
#     email_entry.pack()
#
#     def excluir():
#         email = email_entry.get().strip()
#         if email in usuarios:
#             confirmacao = messagebox.askyesno("Confirmar", f"Tem certeza que deseja excluir {email}?")
#             if confirmacao:
#                 del usuarios[email]
#                 messagebox.showinfo("Excluído", "Usuário removido com sucesso.")
#                 janela_excluir.destroy()
#         else:
#             messagebox.showerror("Não encontrado", "Usuário não localizado.")
#
#     tk.Button(janela_excluir, text="Excluir", command=excluir, bg="#f44336", fg="white").pack(pady=20)