from pessoa import Pessoa

Pessoas = {}
for i in range(5):
    nome = imput('nome ')
    idade = int(input('idade '))
    pessoas.append( Pessoa(nome,idade ))
    
 
    Pessoas(0).fazer_aniver()
    pessoas[0].apresentar()
    
    for p in pessoas:
        p.apresentar(0)
        
