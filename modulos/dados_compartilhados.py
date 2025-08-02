import tkinter as tk


variaveis = {}  # ✅ Agora está no escopo global

def inicializar_variaveis(master):
    variaveis["var_tipo_pacote"] = tk.StringVar(master=master, value="Avulso")
    variaveis["var_porte"] = tk.StringVar(master=master)
    variaveis["var_raca"] = tk.StringVar(master=master)
    variaveis["var_tipopelo"] = tk.StringVar(master=master)
    variaveis["var_pagamento"] = tk.StringVar(master=master)
    variaveis["var_descricao"] = tk.StringVar(master=master)
    variaveis["var_data_cadastro"] = tk.StringVar(master)
    variaveis["var_pelagem"] = tk.StringVar(master)
    variaveis["var_caracteristicas"] = tk.StringVar(master)
    # ... outras variáveis




# dados_compartilhados.py

# Aqui você declara suas variáveis e dicionários globais
pacotes_servicos = {}

# Outras variáveis...

# 🔣 Serviços disponíveis


def montar_aba_relatorios(janela):
    frame_admins = ttk.LabelFrame(janela, text="Administradores para notificação")
    ...


servicos_disponiveis = [
    "Banho", "Hidratação", "Desembolo", "Remoção de Pelos",
    "Corte de Unhas", "Tosa Higiênica", "Tosa na Máquina",
    "Tosa na Tesoura", "Escovação de Dentes", "Leva e Trás"
]


# 🧮 Estrutura auxiliar para controle financeiro

variaveis_servicos = {}
labels_valores = {}
entrys_desconto_individual = {}
descontos_por_servico = {}
desconto_total = {"tipo": None, "valor": 0.0}



# 🎁 Pacotes contratados

pacotes_servicos = {
    "Quinzenal": {
        "incluidos": ["Banho", "Banho"],
        "bonus_opcoes": ["Hidratação", "Tosa Higiênica"]
    },
    "Mensal": {
        "incluidos": ["Banho"] * 4,
        "bonus_opcoes": ["Hidratação", "Tosa Higiênica"]
    }
}


# Dados estáticos de raças por porte e preços
# 🐕 Dados estáticos por porte

dados_pet = {
    "pequeno": {
        "raças": ['Schitzu', 'Lhasa Apso', 'Maltes', 'Yorkshire', 'Dachshund', 'Cavalier King Charles Spaniel',
                  'Biewer Terrier', 'Bulldog Francês', 'Pug', 'Chihuahua', 'Cocker Spaniel', 'Papillon',
                  'Spitz Alemao', 'Pinscher', 'Poodle', 'Jack Russell Terrier', 'Galgo Italiano', 'Pequinês',
                  'Bichon Frise', 'Boston Terrier', 'Fox Paulistinha', 'Petit Basset Griffon Vendéen'],
        "preços": {"Banho": 55, "Hidratação": 20, "Desembolo": 20, "Remoção de Pelos": 20, "Corte de Unhas": 15,
                   "Escovação de Dentes": 15, "Tosa Higiênica": 20, "Tosa na Máquina": 115,
                   "Tosa na Tesoura": 125, "Leva e Trás": 10},
    },
    "médio": {
        "raças": ['American Bully', 'Australian Cattle Dog', 'Basset Hound',
                  'Bulldog Campeiro', 'Bulldog', 'Bulldog Ingles', 'Bull Terrier', 'Basset Fulvo',
                  'Boxer', 'Clumber Spaniel', 'Cocker Americano', 'Cocker Ingles', 'Flat Coated Retriever',
                  'Pastor de Shetland', 'Pumi', 'Schnauzer Standard', 'Shar Pei', 'Spaniel Bretao', 'Spaniel Frances',
                  'Spitz Japones', 'Spriger Spaniel Ingles', 'Terrier Tibetano', 'S.R.D. Médio'],
        "preços": {"Banho": 65, "Hidratação": 20, "Desembolo": 20, "Remoção de Pelos": 20, "Corte de Unhas": 15,
                   "Escovação de Dentes": 15, "Tosa Higiênica": 20, "Tosa na Máquina": 115,
              "Tosa na Tesoura": 125, "Leva e Trás": 10},
    },
    "grande": {
        "raças": ['Pastor Alemao', 'Dogue Alemao', 'Terra Nova', 'Rottweiler', 'Sao-Bernardo', 'Labrador Retriever',
                  'Golden Retriever', 'Fila brasileiro', 'Cane corso', 'Border collie', 'Boiadeiro de Berna',
                  'Akita Inu', 'Mastim Ingles', 'Husky Siberiano', 'Dogo argentino', 'Dalmata', 'Weimaraner',
                  'Bull terrier', 'Mastim tibetano', 'Leonberger', 'Pastor australiano', 'Setter irlandes',
                  'Bulmastife', 'Mastim napolitano', 'Dogue de bordeus', 'Bulmastife', 'cao de Santo Humberto',
                  'Rhodesian ridgeback', 'Boiadeiro da Flandres', 'Bearded collie', 'Bichon bolonhes', 'Basenji',
                  'Boerboel', 'Pastor do caucaso', 'Veadeiro Pampeano', 'Buhund noruegues',
                  'Basset artesiano normando', 'Braco de Auvernia', 'Galgo Ingles', 'Pastor Belga', 'Mastiff',
                  'Bernese', 'Akita', 'Bloodhound', 'Australian Shepherd'],
        "preços": {"Banho": 70, "Hidratação": 20, "Desembolo": 20, "Remoção de Pelos": 20, "Corte de Unhas": 15,
                   "Escovação de Dentes": 15, "Tosa Higiênica": 20, "Tosa na Máquina": 115,
                "Tosa na Tesoura": 125, "Leva e Trás": 10},
    },
    "maior": {
        "raças": ['American Pit Bull Terrier', 'Fila Brasileiro', 'Chow Chow', 'Doberman', 'Chip-dog', 'American Pit Bul terrier',
                  'Chow-chow'],
        "preços": {"Banho": 120, "Hidratação": 20, "Desembolo": 20, "Remoção de Pelos": 80, "Corte de Unhas": 50,
               "Escovação de Dentes": 55, "Tosa Higiênica": 75, "Tosa na Máquina": 85,
               "Tosa na Tesoura": 100, "Leva e Trás": 10},
    },
}

# Imagens dos portes e das raças
# 🖼️ Imagens dos portes

imagens_portes = {
    "pequeno": "pequeno.jpg",
    "médio": "medio.jpg",
    "grande": "grande.jpg",
    "maior": "maior.jpg"
}

# Dicionário para armazenar imagens das raças
# 🐶 Imagens específicas por raça

imagens_racas = {
    'Schitzu':'schitzu.jpg','Lhasa Apso':'lhasa_apso.jpg','Maltês':'maltes.jpg','Yorkshire':'yorkshire.jpg','Dachshund':'dachshund.jpg',
    'Cavalier King Charles Spaniel':'cavalier_king_charles_spaniel.jpg','Biewer Terrier':'biewer_terrier.jpg','Bulldog Francês':'bulldog_frances.jpg',
    'Pug':'pug.jpg','Chihuahua':'chihuahua.jpg','Cocker Spaniel':'cocker_spaniel.jpg','Papillon':'papillon.jpg','Spitz Alemao':'spitz_alemao.jpg',
    'Pinscher':'pinscher.jpg','Poodle':'poodle.jpg','Jack Russell Terrier':'jack_russell_terrier.jpg','Galgo Italiano':'galgo_italiano.jpg',
    'Pequinês':'pequines.jpg','Bichon Frise':'bichon_frise.jpg','Boston Terrier':'boston_terrier.jpg','Fox Paulistinha':'fox_paulistinha.jpg',
    'American Pit Bull Terrier':'american_pit_bull_terrier.jpg','Australian Cattle Dog':'australian_cattle.jpg','Australian Shepherd':'australian_shepherd.jpg',
    'Petit Basset Griffon Vendéen':'petit_basset_griffon_vendéen.jpg','Basset Hound':'basset_hound.jpg','Bulldog Campeiro':'bulldog_campeiro.jpg','Bulldog':'bulldog.jpg',
    'Bulldog Inglês':'bulldog_ingles.jpg','Bull Terrier':'bull_terrier.jpg','Basset Fulvo':'basset_fulvo.jpg','Boxer':'boxer.jpg',
    'Clumber Spaniel':'clumber_spaniel.jpg','Cocker Americano':'cocker_americano.jpg','Cocker Inglês':'cocker_ingles.jpg',
    'Flat Coated Retriever':'flat_coated_retriever.jpg','Pastor de Shetland':'pastor_de_shetland.jpg','Pumi':'pumi.jpg',
    'Schnauzer Standard':'schnauzer_standard.jpg','Shar Pei':'shar_pei.jpg','Spaniel Bretão':'spaniel_bretao.jpg','Spaniel Francês':'spaniel_frances.jpg',
    'Spitz Japonês':'spitz_japones.jpg','Springer Spaniel':'springer_spaniel.jpg','Springer Spaniel Inglês':'springer_spaniel_ingles.jpg',
    'Terrier Tibetano':'terrier_tibetano.jpg','American Bully':'american_bully.jpg','SRD Médio':'s_r_d_medio.jpg','Dogo Argentino':'dogo_argentino.jpg',
    'Dálmata':'dalmatian.jpg','Weimaraner':'weimaraner.jpg','Mastim Tibetano':'mastim_tibetano.jpg','Leonberger':'leonberger.jpg',
    'Pastor Australiano':'pastor_australiano.jpg','Setter Irlandês':'setter_irlandes.jpg','Bulmastife':'bulmastife.jpg','Mastim Napolitano':'mastim_napolitano.jpg',
    'Dogue de Bordeaux':'dogue_de_bordeaux.jpg','Cão de Santo Humberto':'cao_de_santo_humberto.jpg','Rhodesian Ridgeback':'rhodesian_ridgeback.jpg',
    'Boiadeiro da Flandres':'boiadeiro_da_flandres.jpg','Bearded Collie':'bearded_collie.jpg','Bichon Bolonhês':'bichon_bolonhes.jpg','Basenji':'basenji.jpg',
    'Boerboel':'boerboel.jpg','Pastor do Cáucaso':'pastor_do_caucaso.jpg','Veadeiro Pampeano':'veadeiro_pampeano.jpg','Buhund Norueguês':'buhund_noruegues.jpg',
    'Basset Artesiano Normando':'basset_artesiano_normando.jpg','Braco de Auvernia':'braco_de_auvernia.jpg','Galgo Inglês':'galgo_ingles.jpg',
    'Pastor Belga':'pastor_belga.jpg','Mastiff':'mastiff.jpg','Bernese':'bernese.jpg','Akita':'akita.jpg','Bloodhound':'bloodhound.jpg','Pit Bull':'pit_bull.jpg',
    'Fila Brasileiro':'fila_brasileiro.jpg','Chow Chow':'chow_chow.jpg','Doberman':'doberman.jpg','Chip Dog':'chip_dog.jpg',
}



# Dicionário de características
# 📋 Características por raça (para relatórios ou sugestões visuais)

caracteristicas_racas = {
    "Chihuahua": {"peso": "2kg", "tamanho": "Pequeno", "temperamento": "Ativo"},
    "Labrador": {"peso": "30kg", "tamanho": "Grande", "temperamento": "Amigável"},
    "Bulldog": {"peso": "20kg", "tamanho": "Médio", "temperamento": "Calmo"},
    "Dogue Alemão": {"peso": "50kg", "tamanho": "Gigante", "temperamento": "Gentil"},
    # ... complemente com mais raças
}





# Referência aos widgets (serão inicializados em aba_config)
# 🧩 Referência aos widgets que serão preenchidos em tempo real

combobox_porte = None
combobox_raca = None
label_imagem = None
texto_caracteristicas = None

# 💳 Forma de pagamento widgets
radiobutton_pix = None
radiobutton_debito = None
radiobutton_credito = None
radiobutton_dinheiro = None


# Faixa de preços atual (atualizada ao selecionar porte)
precos_atuais = {}

widgets_pagamento = {
    "pix": None,
    "debito": None,
    "credito": None,
    "dinheiro": None,
}

# Forma de pagamento
# var_pagamento = None
# radiobutton_pix = None
# radiobutton_debito = None
# radiobutton_credito = None
# radiobutton_dinheiro = None






















# def inicializar_variaveis(master):
#     variaveis["var_tipo_pacote"] = tk.StringVar(master=master, value="Avulso")
#     # (e demais variáveis...)


# def inicializar_variaveis(master):
#     variaveis["var_porte"] = tk.StringVar(master)
#     variaveis["var_raca"] = tk.StringVar(master)
#     variaveis["var_tipopelo"] = tk.StringVar(master)
#     variaveis["var_pagamento"] = tk.StringVar(master)
#     variaveis["var_descricao"] = tk.StringVar(master)
#     variaveis["var_data_cadastro"] = tk.StringVar(master)
#     variaveis["var_pelagem"] = tk.StringVar(master)
#     variaveis["var_caracteristicas"] = tk.StringVar(master)


    #global var_porte, var_raca, var_tipopelo, var_pagamento, var_descricao
    # var_porte = tk.StringVar(master, value="")
    # var_raca = tk.StringVar(master, value="")
    # var_tipopelo = tk.StringVar(master, value="")
    # var_pagamento = tk.StringVar(master, value="")
    # var_descricao = tk.StringVar(master, value="")

# def inicializar_variaveis(master):
#     global var_porte, var_raca, var_tipopelo, var_pagamento, var_descricao
#     var_porte = tk.StringVar(master, value="")
#     var_raca = tk.StringVar(master, value="")
#     var_tipopelo = tk.StringVar(master, value="")
#     var_pagamento = tk.StringVar(master, value="")
#     var_descricao = tk.StringVar(master, value="")  # ✅ Aqui está no momento certo!

# var_porte = tk.StringVar()
# var_raca = tk.StringVar()
# var_tipopelo = tk.StringVar()


# Variáveis globais ligadas aos Combobox
# var_porte = tk.StringVar(value="pequeno")
# var_raca = tk.StringVar()

