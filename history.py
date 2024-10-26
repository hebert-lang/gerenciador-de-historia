import  random

# Função que gera a introdução da história
def gerar_introdução():
    introducoes = ["Era uma vez", "Há muito tempo atrá", "Num reino distante" ]
    return random.choice(introducoes)

# função que gera o desenvolvimeto da história
def gerar_desenvolvimento():
    desenvolvimentos = {"um valente cavaleiro", "uma destemida guerreira", "um bravo guerreiro 
                        "uma  poderosa  feiteceira", " um sabio mago"}
    
    return random.choice(desenvolvimentos)
    # Função que gera o final da história
def gerar_final():
    finais = ["enfrentando dragões ferozes.", "derrotando um terrível vilão.",
              "descobrindo um tesouro escondido.", "salvando o reino da escuridão.",
              "encontrando um amor verdadeiro."]
    return random.choice(finais)

# Função principal que gera toda a história
def gerar_historia():
    introducao = gerar_introducao()
    desenvolvimento = gerar_desenvolvimento()
    final = gerar_final()

    historia = f"{introdução} {desenvolvimento} {final}"
    return historia  

# Exibe a história gerada 
if _name_== " _main_":
    print(gerar_historia())
