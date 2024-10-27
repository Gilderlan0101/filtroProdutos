def filtrar_produtos():
    produtos = [
        {'nome': 'p1', 'valor': 10},
        {'nome': 'p2', 'valor': 10},
        {'nome': 'p3', 'valor': 20},
        {'nome': 'p4', 'valor': 20},
        {'nome': 'p5', 'valor': 40},
        {'nome': 'p6', 'valor': 40},
        {'nome': 'p7', 'valor': 50},
        {'nome': 'p7', 'valor': 50}
    ]
    filtro = int(input('Qual valor deseja busca ?: '))
    produtos_filtrados = [ produto  for produto in produtos if produto['valor']== filtro ]
    print(produtos_filtrados, sep='\n')

filtrar_produtos()


