# centro_controle_relatorios

from tkcalendar import DateEntry

# Seleção de período
ttk.Label(frame_controle, text="De:").grid(row=4, column=0)
data_inicio = DateEntry(frame_controle, width=12, background='darkblue', foreground='white', borderwidth=2)
data_inicio.grid(row=4, column=1, padx=5)

ttk.Label(frame_controle, text="Até:").grid(row=4, column=2)
data_fim = DateEntry(frame_controle, width=12, background='darkblue', foreground='white', borderwidth=2)
data_fim.grid(row=4, column=3, padx=5)

# Botão para aplicar filtro
ttk.Button(frame_controle, text="Filtrar", command=filtrar_por_periodo).grid(row=4, column=4, padx=10)



def filtrar_por_periodo():
    inicio = data_inicio.get_date()
    fim = data_fim.get_date()

    # Filtrando dados fictícios para ilustrar
    dados_filtrados = [envio for envio in historico if inicio <= envio["data"] <= fim]

    # Atualiza o Treeview
    for item in treeview.get_children():
        treeview.delete(item)
    for envio in dados_filtrados:
        treeview.insert("", "end", values=(envio["data"].strftime("%d/%m/%Y %H:%M"), envio["cliente"], envio["status"]))

ttk.Label(frame_controle, text="📋 Centro de Controle de Relatórios", font=("Segoe UI", 14)).grid(row=0, column=0, columnspan=3, pady=10)

# Histórico de envios
treeview = ttk.Treeview(frame_controle, columns=("Data", "Cliente", "Status"), show="headings")
treeview.heading("Data", text="Data/Hora")
treeview.heading("Cliente", text="Cliente")
treeview.heading("Status", text="Status")
treeview.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

# Status atual
label_status = ttk.Label(frame_controle, text="🔄 Aguardando envio...")
label_status.grid(row=2, column=0, columnspan=3)

# Botão para exportar histórico
ttk.Button(frame_controle, text="Exportar Histórico", command=exportar_historico).grid(row=3, column=0, pady=10)

