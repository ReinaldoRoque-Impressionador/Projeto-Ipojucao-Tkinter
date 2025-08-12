import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from datetime import datetime
import sys
import subprocess
from modulos.utilitarios import caminho_arquivo

from modulos import dados_compartilhados as dc
from modulos.utilitarios import caminho_arquivo


janela = tk.Tk()
janela.title("Sistema Petshop")
janela.geometry("800x600")

notebook = ttk.Notebook(janela)
notebook.grid(row=0, column=0, sticky="nsew")



def criar_menu_diagnostico(janela_principal, notebook):
    menubar = tk.Menu(janela_principal)
    janela_principal.config(menu=menubar)

    menu_ferramentas = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Ferramentas", menu=menu_ferramentas)

    def abrir_aba_diagnostico():
        aba_diag = ttk.Frame(notebook)
        notebook.add(aba_diag, text="Diagnóstico")
        montar_painel_diagnostico(aba_diag)
        notebook.select(aba_diag)

    menu_ferramentas.add_command(label="Diagnóstico do Sistema 🩺", command=abrir_aba_diagnostico)

def montar_painel_diagnostico(parent):
    frame_diag = ttk.LabelFrame(parent, text="🔧 Diagnóstico do Sistema")
    frame_diag.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    text_output = tk.Text(frame_diag, width=80, height=20, state="disabled", bg="#f0f0f0")
    text_output.grid(row=1, column=0, columnspan=3, padx=10, pady=5)

    pacotes = {
        "matplotlib": "Visualização de gráficos",
        "pandas": "Planilhas e tabelas",
        "PIL": "Manipulação de imagens (Pillow)",
        "tkcalendar": "Calendário em tkinter",
        "openpyxl": "Planilhas Excel",
        "sqlite3": "Banco de dados interno"
    }

    pacotes_faltando = []

    def testar():
        nonlocal pacotes_faltando
        pacotes_faltando = []

        text_output.configure(state="normal")
        text_output.delete("1.0", tk.END)
        text_output.insert(tk.END, f"Verificação - {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n\n")

        for nome in pacotes:
            try:
                if nome == "PIL":
                    import PIL
                else:
                    __import__(nome)
                text_output.insert(tk.END, f"✅ {nome} - OK ({pacotes[nome]})\n")
            except ImportError:
                text_output.insert(tk.END, f"❌ {nome} - NÃO INSTALADO! ({pacotes[nome]})\n")
                pacotes_faltando.append(nome)

        if pacotes_faltando:
            text_output.insert(tk.END, "\n📦 Para instalar manualmente:\n")
            for nome in pacotes_faltando:
                text_output.insert(tk.END, f"   pip install {nome}\n")
        else:
            text_output.insert(tk.END, "\n✅ Tudo pronto, sem pendências!\n")

        text_output.configure(state="disabled")

    def corrigir_automaticamente():
        if not pacotes_faltando:
            messagebox.showinfo("AutoCorrigir", "Tudo já está instalado!")
            return

        for nome in pacotes_faltando:
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", nome])
                messagebox.showinfo("AutoCorrigir", f"{nome} instalado com sucesso.")
            except Exception as e:
                messagebox.showerror("Erro na instalação", f"Falha ao instalar {nome}:\n{e}")

        testar()  # reexecutar após instalar

    def exportar_log():
        log = text_output.get("1.0", tk.END)
        if not log.strip():
            messagebox.showwarning("Exportação", "Sem conteúdo para exportar.")
            return
        caminho = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Arquivo de Texto", "*.txt")])
        if caminho:
            with open(caminho, "w", encoding="utf-8") as f:
                f.write(log)
            messagebox.showinfo("Exportado", f"Log salvo em:\n{caminho}")

    ttk.Button(frame_diag, text="🔍 Testar", command=testar).grid(row=0, column=0, padx=10, pady=5)
    ttk.Button(frame_diag, text="🛠 AutoCorrigir", command=corrigir_automaticamente).grid(row=0, column=1, padx=10, pady=5)
    ttk.Button(frame_diag, text="💾 Exportar Log", command=exportar_log).grid(row=0, column=2, padx=10, pady=5)