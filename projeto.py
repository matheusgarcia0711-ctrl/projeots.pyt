carrinho = ['Notebook','Mouse','Teclado']

for item in carrinho:
    print(item)
    
    carrinho.append('Headset')
    carrinho.remove('Mouse')
    carrinho.insert(1,'Impressora')
    print(carrinho)