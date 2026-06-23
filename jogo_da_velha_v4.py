def mostrar_tabuleiro(tab):
    print(f"\n {tab[0]} | {tab[1]} | {tab[2]} ")
    print("----+----+----")
    print(f"{tab[3]} | {tab[4]} | {tab[5]} ")
    print("----+----+----")
    print(f" {tab[6]} | {tab[7]} | {tab[8]} ")
    
def verificar_Vitoria(tab, jogador):
    combinacoes = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    
    for combo in combinacoes:
        if tab[combo[0]] == tab[combo[1]] == tab[combo[2]] == jogador:
          return True
        return False
        
#Funcao Motor do Jogo 
def jogo_da_velha():
    tabuleiro = [" "] * 9
    jogador_atual = "X"
    jogadas = 0
    
    print("JOGO DA VELHA SAMURAI...")
    
    while True:
        mostrar_tabuleiro(tabuleiro)
        
        try:
            posicao = int(input(f"Jogador {jogador_atual}, Escolha a posicao de 0-8 "))
        except ValueError:
            print("SAMURAI DIGITA NUNERO. NAO LETRA.")
            continue
          
        if posicao < 0 or posicao > 8:
            print("POSICAO INVALIDA SO VALE 0 -8, Lutador.")
            continue
          
        if tabuleiro[posicao] != " ":
            print("CASA OCUPADA! Escolhe outra, ninja.")
            continue
        
        tabuleiro[posicao] = jogador_atual
        jogadas = jogadas + 1
        
        
        if verificar_Vitoria(tabuleiro, jogador_atual):
            mostrar_tabuleiro(tabuleiro)
            print(f"JOGADOR {jogador_atual} GANHOU! VITORIA SAMURAI ")
            break
          
        if jogadas == 9:
            mostrar_tabuleiro(tabuleiro)
            print("DEU VELHA EMPATE! Ninguem Gnahou, dois samurais honrrados..")
            break
        
        if jogador_atual == "X":
            jogador_atual = "O"
        else:
            jogador_atual = "X"
            
jogo_da_velha()
