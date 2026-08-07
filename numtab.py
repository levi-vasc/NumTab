#Menu inicial que retornará a entrada do usuário, que fará com que o código principal execute diferentes condicionais.
def MenuInicial():
	titulo = "NUMTAB"
	print(f"|{titulo: ^50}|")
	print(2*"\n")
	print("\t\t[1] Novo Jogo\n\t\t[2] Carregar jogo\n\t\t[3] Ranking\n\t\t[4] Sair")
	opcao = input("\nDigite a opção: ")
	while opcao not in ("1","2","3", "4"):
		print("\nEntrada inválida!")
		opcao = input("\nDigite a opção: ")	
	return opcao

def VisualizacaoObjetivo(player, objetivo):
	print(f"Objetivo de {player}")
	print(2*"\n")
	input("Digite qualquer coisa para exibir.\n")
	print(f"\nSeu objetivo é {objetivo}.\n")
	match objetivo:
		case "ASCENDENTE":
			sequencia = "CRESCENTES"
			exemplos = "\t1,2,3\n\t4,5,6,7\n\t3,4,5,6,7"
		case "DESCENDENTE":
			sequencia = "DECRESCENTES"
			exemplos = "\t3,2,1\n\t7,6,5,4\n\t8,7,6,5,4"	
		case "PAR":
			sequencia = "PARES"
			exemplos = "\t2,4,6\n\t2,4,6,8\n\t6,4,2"
		case "ÍMPAR":
			sequencia = "ÍMPARES"
			exemplos = "\t1,3,5\n\t1,3,5,7\n\t7,5,3"
	print(f"\nVocê deverá fazer uma sequência de números {sequencia}, da esquerda para a direita e de cima para baixo.")
	print("\n")
	print("Exemplos:\n")
	print(exemplos)
	input("\nDigite qualquer coisa para continuar.\n")

#manipulação que serve tanto para a matriz de verificação (com números inteiros) e a matriz visual (com strings e cores)
def ManipularMatriz(matriz_variavel, slot, numero):
	slot = list(slot)
	linhas = ["A","B","C","D","E"]
	colunas = ["1","2","3","4","5"]
	for i in range(len(linhas)):
		if slot[0] == linhas[i]:
			pos_linha = i
		if slot[1] == colunas[i]:
			pos_coluna = i
	matriz_variavel[pos_linha][pos_coluna] = numero
	
	return matriz_variavel

#configuração inicial ao escolher iniciar um novo jogo. Retornará várias variavéis importantes para a execução do jogo.
def Config():
	print("\t1. Fácil")
	print("\t2. Médio")
	print("\t3. Difícil")
	print(2*"\n")
	
	dificuldade = input("Selecione a dificuldade: ")
	while dificuldade not in ("1","2","3"):
		print("\nEntrada inválida!")
		dificuldade = input("\nSelecione a dificuldade: ")

	ordem = 3
	colunas = ["1","2","3"]
	linhas = ["A", "B", "C"]
	if dificuldade == "2" or dificuldade == "3":
		ordem += 1
		colunas.append("4")
		linhas.append("D")
	if dificuldade == "3":
		ordem += 1
		colunas.append("5")
		linhas.append("E")
	
	matriz = []
	for i in range(ordem):
		linha = []
		for j in range(ordem):
			linha.append(1000)
		matriz.append(linha)
	
	tabuleiro = []
	for i in range(ordem):
		linha = []
		for j in range(ordem):
			linha.append(None)
		tabuleiro.append(linha)
	
	posicoes = []
	for i in range(ordem):
		for j in range(ordem):
			posicoes.append(linhas[i] + colunas[j])
	
	nums_disponiveis = []
	for i in range(1, ordem**2+1):
		i = str(i)
		nums_disponiveis.append(i)
		
	print(2*"\n")
	player_1 = input("Nome do jogador 1: ")
	player_2 = input("\nNome do jogador 2: ")
	
	poder = input("\nPoder\t[1]Ativado\t[2]Desativado\t")
	while poder not in ("1","2"):
		print("\nEntrada inválida.")
		poder = input("\nPoder\t[1]Ativado\t[2]Desativado\t")
	if poder == "1":
		poder = [True,True]
	else:
		poder = [False,False]
		
	return colunas, linhas, matriz, tabuleiro, posicoes, nums_disponiveis, player_1, player_2, poder

#recupera um jogo anteriormente salvo	
def RecuperarConfig(Config):
	player_1 = Config["player_1"]
	player_2 = Config["player_2"]
	player_1_sem_cor = Config["player_1_sem_cor"]
	player_2_sem_cor = Config["player_2_sem_cor"]
	player_atual = Config["player_atual"]
	objetivos = Config["objetivos"]
	colunas = Config["colunas"]
	linhas = Config["linhas"]
	matriz = Config["matriz"]
	posicoes = Config["posicoes"]
	nums_disponiveis = Config["nums_disponiveis"]
	tabuleiro = Config["tabuleiro"]
	pontos_player_1 = Config["pontos_player_1"]
	pontos_player_2 = Config["pontos_player_2"]
	poder = Config["poder"]
	
	return player_1, player_2, player_1_sem_cor, player_2_sem_cor, player_atual, objetivos, colunas, linhas, matriz, posicoes, nums_disponiveis, tabuleiro, pontos_player_1, pontos_player_2, poder

def ConfigNovoJogo():
	print("\t1. Fácil")
	print("\t2. Médio")
	print("\t3. Difícil")
	print(2*"\n")
	
	dificuldade = input("Selecione a dificuldade: ")
	while dificuldade not in ("1","2","3"):
		print("\nEntrada inválida!")
		dificuldade = input("\nSelecione a dificuldade: ")

	ordem = 3
	colunas = ["1","2","3"]
	linhas = ["A", "B", "C"]
	if dificuldade == "2" or dificuldade == "3":
		ordem += 1
		colunas.append("4")
		linhas.append("D")
	if dificuldade == "3":
		ordem += 1
		colunas.append("5")
		linhas.append("E")
	
	poder = input("\nPoder\t[1]Ativado\t[2]Desativado\t")
	while poder not in ("1","2"):
		print("\nEntrada inválida.")
		poder = input("\nPoder\t[1]Ativado\t[2]Desativado\t")
	if poder == "1":
		poder = [True,True]
	else:
		poder = [False,False]
	
	matriz = []
	for i in range(ordem):
		linha = []
		for j in range(ordem):
			linha.append(1000)
		matriz.append(linha)
	
	tabuleiro = []
	for i in range(ordem):
		linha = []
		for j in range(ordem):
			linha.append(None)
		tabuleiro.append(linha)
	
	posicoes = []
	for i in range(ordem):
		for j in range(ordem):
			posicoes.append(linhas[i] + colunas[j])
	
	nums_disponiveis = []
	for i in range(1, ordem**2+1):
		i = str(i)
		nums_disponiveis.append(i)
		
	return colunas, linhas, matriz, tabuleiro, posicoes, nums_disponiveis, poder
						
def VitoriaObjetivos(sequencia,player_1,player_2,pontos_player_1,pontos_player_2,objetivos):
	vitoria = False
	player_vitorioso = ""
	sequencia_vitoriosa = ""
	
	if "ASCENDENTE" in objetivos:
		if all(sequencia[i] == sequencia[i+1]-1 for i in range(len(sequencia)-1)):
			vitoria = True
			sequencia_vitoriosa = "ascendente"
			if objetivos[0] == "ASCENDENTE":
				player_vitorioso = player_1
				pontos_player_1 += len(sequencia)
			else:
				player_vitorioso = player_2
				pontos_player_2 += len(sequencia)
	
	if "DESCENDENTE" in objetivos:
		if all(sequencia[i] == sequencia[i+1]+1 for i in range(len(sequencia)-1)):
			vitoria = True
			sequencia_vitoriosa = "descendente"
			if objetivos[0] == "DESCENDENTE":
				player_vitorioso = player_1
				pontos_player_1 += len(sequencia)
			else:
				player_vitorioso = player_2
				pontos_player_2 += len(sequencia)
			
	
	if "PAR" in objetivos:
		if all(sequencia[i] % 2 == 0 and (sequencia[i] == sequencia[i+1] - 2 or sequencia[i] == sequencia[i+1] + 2) for i in range(len(sequencia)-1)):
			vitoria = True
			sequencia_vitoriosa = "par"
			if objetivos[0] == "PAR":
				player_vitorioso = player_1
				pontos_player_1 += len(sequencia)
			else:
				player_vitorioso = player_2
				pontos_player_2 += len(sequencia)	
			
	if "ÍMPAR" in objetivos:
		if all(sequencia[i] % 2 != 0 and (sequencia[i] == sequencia[i+1]-2 or sequencia[i] == sequencia[i+1]+2) for i in range(len(sequencia)-1)):
			vitoria = True
			sequencia_vitoriosa = "ímpar"
			if objetivos[0] == "ÍMPAR":
				player_vitorioso = player_1
				pontos_player_1 += len(sequencia)
			else:
				player_vitorioso = player_2
				pontos_player_2 += len(sequencia)
	
	return vitoria, player_vitorioso, sequencia_vitoriosa, pontos_player_1, pontos_player_2
	
def VisualizarRanking(ranking):
	ranking = sorted(ranking, key=lambda x: x[1], reverse=True)
	if len(ranking) >= 10:
		tamanho = 10
	else:
		tamanho = len(ranking)
	print("Posição\t\tNome\t\tPontuação\n")
	for i in range(tamanho):
		print(f"{i+1}º\t|\t{ranking[i][0]}\t|\t{ranking[i][1]}")
		print("\n")
	
	input("Aperte ENTER para voltar ")

def Empate(matriz,pontos_player_1,pontos_player_2):
	linhas_full = 0
	for i in range(len(matriz)):
		if all(matriz[i][j] != 1000 for j in range(len(matriz))):
			linhas_full += 1
	if linhas_full == len(matriz):
		pontos_player_1 += 1
		pontos_player_2 += 1
		return None, pontos_player_1, pontos_player_2
	else:
		return False, pontos_player_1, pontos_player_2
		
#a função irá identificar a linha ou coluna escolhida para o jogador, removerá os números da mesma e retornará para a lista de números disponivéis.
def Poder(matriz,tabuleiro, linhas,colunas, poder, escolha, nums_disponiveis, posicoes_disponiveis, player_atual, player_1, player_2):
	if escolha not in colunas:
		for i in range(len(matriz)):
			if escolha == linhas[i]:
				escolha = i
				break	
		
		nums_retorno = [matriz[escolha][j] for j in range(len(matriz)) if matriz[escolha][j] != 1000]
		pos = []
		for j in range(len(matriz)):
			matriz[escolha][j] = 1000
			tabuleiro[escolha][j] = None
			pos.append(linhas[escolha] + colunas[j])
	
	else:
		escolha = int(escolha) - 1
		nums_retorno = [matriz[i][escolha] for i in range(len(matriz)) if matriz[i][escolha] != 1000]
		pos = []
		for i in range(len(matriz)):
			matriz[i][escolha] = 1000
			tabuleiro[i][escolha] = None
			pos.append(linhas[i] + colunas[escolha])
	
	if player_atual == player_1:
		poder[0] = False
	else:
		poder[1] = False
	
	nums_disponiveis = [int(i) for i in nums_disponiveis]
	nums_disponiveis.extend(nums_retorno)
	nums_disponiveis.sort()
	nums_disponiveis = [str(i) for i in nums_disponiveis]
	
	posicoes_disponiveis.extend(pos)
	
	return matriz, tabuleiro, nums_disponiveis, posicoes_disponiveis, poder