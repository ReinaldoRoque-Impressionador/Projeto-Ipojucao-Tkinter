# estrutura.py
import tkinter as tk
from tkinter import ttk

# 🧭 Frame principal para navegação
frame_navegacao = None  # será inicializado no main.py

# 📊 Notebook que mantém as abas
notebook = None  # criado em main.py

# 🖼️ Inner Frame utilizado em abas com rolagem ou estrutura detalhada
inner_frame = None  # opcional, depende de cada aba

# 🎯 Label para mostrar o título da aba atual
titulo_aba = None  # pode ser usado em topo de cada aba

# 📋 Variáveis de controle extras (se desejar)
aba_ativa = None  # será criado depois  # para rastrear qual aba está ativa