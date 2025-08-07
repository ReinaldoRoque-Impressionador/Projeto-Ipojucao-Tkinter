def menu_lateral(frame_principal):
    menu = tk.Frame(frame_principal, bg="gray", width=200)
    menu.pack(side="left", fill="y")

    ttk.Button(menu, text="Login", command=chamar_aba_login_fusion).pack(pady=5)
    ttk.Button(menu, text="Cadastro", command=chamar_aba_cadastro).pack(pady=5)
    ttk.Button(menu, text="Financeiro", command=chamar_aba_financeiro).pack(pady=5)
    ttk.Button(menu, text="Clientes", command=chamar_aba_clientes).pack(pady=5)
    ttk.Button(menu, text="Consulta", command=chamar_aba_consulta).pack(pady=5)
    ttk.Button(menu, text="Relatórios", command=chamar_aba_relatorios).pack(pady=5)
    ttk.Button(menu, text="Clima", command=chamar_aba_clima).pack(pady=5)
    ttk.Button(menu, text="Itaú", command=chamar_aba_itau).pack(pady=5)
    # etc...