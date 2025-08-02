from tkinter import ttk

def configurar_estilo():
    style = ttk.Style()
    style.theme_use("clam")  # Outros temas: 'alt', 'default', 'vista'

    # Estilo padrão de botões
    style.configure("TButton",
        background="#e1f5fe",
        foreground="#0277bd",
        font=("Segoe UI", 10, "bold"),
        padding=6
    )

    # Botão especial
    style.configure("Destaque.TButton",
        background="#ffe082",
        foreground="#bf360c",
        font=("Segoe UI", 11),
        padding=(10, 5)
    )

    # Combobox
    style.configure("TCombobox",
        fieldbackground="#ffffff",
        background="#b2ebf2",
        foreground="#004d40"
    )

    # Labels padrão
    style.configure("TLabel",
        foreground="#263238",
        font=("Segoe UI", 10)
    )

    # Labels de destaque
    style.configure("Legend.TLabel",
        foreground="#37474f",
        font=("Segoe UI", 11, "bold")
    )