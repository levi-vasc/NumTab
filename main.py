#libaries
from tabulate import tabulate
import os, json, random, csv
import colorama as cl
from numtab import *

cl.init(autoreset=True)			
									
opcao = MenuInicial()
#loop que continuára enquanto o usuário não escolher a opção sair (4) no menu inicial.
while opcao != "4":
	match opcao:
			case "1":
				os.system('cls' if os.name == 'nt' else 'clear')
				#configuração inicial do novo jogo
				colunas, linhas, matriz, tabuleiro, posicoes, nums_disponiveis, player_1, player_2 , poder = Config()
				player_1_sem_cor = player_1
				player_2_sem_cor = player_2
				player_1 = cl.Fore.RED + player_1 + cl.Fore.RESET
				player_2 = cl.Fore.CYAN + player_2 + cl.Fore.RESET
				pontos_player_1,pontos_player_2 = 0,0
				objetivos = random.sample(["ASCENDENTE","DESCENDENTE","PAR","ÍMPAR"],2)	
				os.system('cls' if os.name == 'nt' else 'clear')	
				VisualizacaoObjetivo(player_1, objetivos[0])
				os.system('cls' if os.name == 'nt' else 'clear')
				VisualizacaoObjetivo(player_2, objetivos[1])
				os.system('cls' if os.name == 'nt' else 'clear')
				player_atual = random.choice([player_1, player_2])
				
				#variável "continuar" usada para não conflitar com a opção de carregar o jogo quando entrar no loop de repetição da partida
				continuar = "1"
				print("Início de jogo. Digite S em posição quando quiser sair.")
				if True in poder:
					print("\nPara usar o poder, digite P em posição.")
	
			case "2":
				try:
					with open("save.json", "r") as save:
						ConfigSave = json.load(save)
					#recuperação da configuração do jogo salvo por um arquivo json
					player_1, player_2, player_1_sem_cor, player_2_sem_cor, player_atual, objetivos, colunas, linhas, matriz, posicoes, nums_disponiveis, tabuleiro, pontos_player_1, pontos_player_2, poder = RecuperarConfig(ConfigSave)
					print("\n", f"Jogo de {player_1} e {player_2}")
					print(2*"\n"+tabulate(tabuleiro, headers=colunas, showindex=linhas, tablefmt="grid"))
					continuar = input("\n[1] Continuar Jogo\t[2] Voltar\t")
					while continuar not in ("1","2"):
						print("\nEntrada inválida."+2*"\n")
						continuar = input("[1] Continuar Jogo\n[2] Voltar")
					os.system('cls' if os.name == 'nt' else 'clear')
					if continuar == "2":
						opcao = MenuInicial()
					elif continuar == "1":
						#visualização dos objetivos para relembrar os jogadores
						VisualizacaoObjetivo(player_1, objetivos[0])
						os.system('cls' if os.name == 'nt' else 'clear')
						VisualizacaoObjetivo(player_2, objetivos[1])
						os.system('cls' if os.name == 'nt' else 'clear')
					
				#caso o arquivo json não seja encontrado, aparecerá a seguinte messagem
				except:
					input("\nNão há nenhum jogo salvo. Digite ENTER para voltar.\n")
					continuar = "2"
					os.system('cls' if os.name == 'nt' else 'clear')
					opcao = MenuInicial()
													
			case "3":
				try:
					with open("ranking.csv", "r") as ranking:
						tabela_ranking = csv.reader(ranking)
						os.system('cls' if os.name == 'nt' else 'clear')
						VisualizarRanking(list(tabela_ranking))
					
				except FileNotFoundError:
					print("\nOops! Ninguém pontuou ainda... Será que você consegue ser o primeiro?")
					input("\nAperte ENTER para voltar. ")
				
				os.system('cls' if os.name == 'nt' else 'clear')
				continuar = "2"
				opcao = MenuInicial()
				
	slot = None
	while slot!= "S" and continuar != "2":
		print(2*"\n")
		print(tabulate(tabuleiro, headers=colunas, showindex=linhas, tablefmt="grid"))
		print("\n", "Números disponíveis: ", ", ".join(nums_disponiveis))
		
		#algoritmo para verificar vitória ou empate. Enquanto a variável vitória confirmada tiver valor False, o código percorrerá as linhas, colunas e diagonais da matriz para verificar se alguma condição irá retornar True. 
		#No final, ainda, há uma função que retorna True caso a matriz esteja sem 1000 e a vitoria_confirmada continua False. Caso a variável ainda não seja True, a partida continua.
		vitoria_confirmada = False
		for linha in matriz:
			vitoria, player_vitorioso, sequencia_vitoriosa, pontos_player_1,pontos_player_2 = VitoriaObjetivos(linha,player_1,player_2,pontos_player_1,pontos_player_2,objetivos)
			if vitoria:
				vitoria_confirmada = True
				break
		if not vitoria_confirmada:
			for j in range(len(matriz)):
				coluna = []
				for i in range(len(matriz)):
					coluna.append(matriz[i][j])
				vitoria, player_vitorioso, sequencia_vitoriosa,pontos_player_1,pontos_player_2 = VitoriaObjetivos(coluna,player_1,player_2,pontos_player_1,pontos_player_2,objetivos)
				if vitoria:
					vitoria_confirmada = True
					break
		if not vitoria_confirmada:
			diagonal = [matriz[i][i] for i in range(len(matriz))]
			vitoria, player_vitorioso, sequencia_vitoriosa,pontos_player_1,pontos_player_2 = VitoriaObjetivos(diagonal,player_1,player_2,pontos_player_1,pontos_player_2,objetivos)
			if vitoria:
				vitoria_confirmada = True
		if not vitoria_confirmada:
			diagonal_sec = [matriz[i][-(i+1)] for i in range(len(matriz))]
			vitoria, player_vitorioso, sequencia_vitoriosa,pontos_player_1,pontos_player_2 = VitoriaObjetivos(diagonal_sec,player_1,player_2,pontos_player_1,pontos_player_2,objetivos)
			if vitoria:
				vitoria_confirmada = True
		if not vitoria_confirmada:
			vitoria_confirmada, pontos_player_1,pontos_player_2 = Empate(matriz,pontos_player_1,pontos_player_2)
			
		if vitoria_confirmada:
			print(f"\n{player_vitorioso} ganhou! Sua sequência era {sequencia_vitoriosa}.")
		elif vitoria_confirmada == None:
			print(f"Houve empate! A sequência de {player_1} era {objetivos[0]} e a de {player_2} era {objetivos[1]}.")
		if vitoria_confirmada == True or vitoria_confirmada == None:
			print(f"\nPontuação de {player_1}: {pontos_player_1}\nPontuação de {player_2}: {pontos_player_2}")
			novo_jogo = input("\nDeseja começar um novo jogo? [1]Sim [2]Não\t")
			while novo_jogo not in ("1","2"):
				novo_jogo = input("\nEntrada inválida.\n")
			os.system('cls' if os.name == 'nt' else 'clear')
			if novo_jogo == "2":
				pontos_players = [[player_1_sem_cor, pontos_player_1], [player_2_sem_cor, pontos_player_2]]
				try:
					ranking = open("ranking.csv", "a")
				except FileNotFoundError:
					ranking = open("ranking.csv", "w")
				conteudo = csv.writer(ranking)
				conteudo.writerows(pontos_players)
				ranking.close()
				
				opcao = MenuInicial()
				break
				
			else:	
				player_atual = random.choice([player_1, player_2])
				objetivos = random.sample(["ASCENDENTE","DESCENDENTE","PAR","ÍMPAR"],2)
				colunas, linhas, matriz, tabuleiro, posicoes, nums_disponiveis, poder = ConfigNovoJogo()
				os.system('cls' if os.name == 'nt' else 'clear')
				VisualizacaoObjetivo(player_1, objetivos[0])
				os.system('cls' if os.name == 'nt' else 'clear')
				VisualizacaoObjetivo(player_2,objetivos[1])
				os.system('cls' if os.name == 'nt' else 'clear')
				print("Início de jogo. Digite S em posição quando quiser sair.")
				print(2*"\n")
				print(tabulate(tabuleiro, headers=colunas, showindex=linhas, tablefmt="grid"))
				print("\n", "Números disponíveis: ", ", ".join(nums_disponiveis))
		
		print(2*"\n", f"Vez de {player_atual}")
		slot = input("\nPosição: ").upper()
		#condicionais utilizadas para que o jogador não consiga inserir P no slot, caso ele já tenha usado ou não tem poder.
		if player_atual == player_1:
			if poder[0]:
				while slot not in posicoes and slot!= "S" and slot!= "P":
					print("\nEntrada inválida ou já ocupada.")
			elif poder[0] == False:
				while slot not in posicoes and slot!= "S":
					print("\nEntrada inválida ou já ocupada.")
					slot = input("\nPosição: ").upper()
		
		elif player_atual == player_2:
			if poder[1]:		
				while slot not in posicoes and slot!= "S" and slot!= "P":
					print("\nEntrada inválida ou já ocupada.")
					slot = input("\nPosição: ").upper()
			elif poder[1] == False:
				while slot not in posicoes and slot!= "S":
					print("\nEntrada inválida ou já ocupada.")
					slot = input("\nPosição: ").upper()
		
		if slot in posicoes:
			#metódo remove, para evitar que o usuário use um slot já ocupado posteriormente, sem a necessidade de uma função de verificação.
			posicoes.remove(slot)
			num = input("\nNúmero: ")
			while num not in nums_disponiveis:
				print("\nEntrada inválida ou número já foi usado.")
				num = input("\nNúmero: ")
			num_int = int(num)
			#mesma estratégia do slot
			nums_disponiveis.remove(num)
			matriz = ManipularMatriz(matriz, slot, num_int)
			
			if player_atual == player_1:
				num_visual = cl.Fore.RED + num + cl.Fore.RESET
				player_atual = player_2
			else:
				num_visual = cl.Fore.CYAN + num + cl.Fore.RESET
				player_atual = player_1
				
			tabuleiro = ManipularMatriz(tabuleiro, slot, num_visual)
	
		elif slot == "S":
			salvar = input("\nDeseja salvar o jogo?\t[1]Sim\t[2]Não\t")
			while salvar not in ("1","2"):
				print("\nEntrada inválida."+2*"\n")
				salvar = input()
				
			if salvar == "1":
				#definição de dicionário com todas as variáveis importantes para salvar o jogo
				config = {"matriz":matriz, "tabuleiro":tabuleiro, "linhas":linhas, "colunas":colunas, "posicoes":posicoes, "nums_disponiveis":nums_disponiveis, "player_1":player_1, "player_2":player_2, "player_1_sem_cor":player_1_sem_cor, "player_2_sem_cor":player_2_sem_cor, "objetivos":objetivos, "pontos_player_1":pontos_player_1,"pontos_player_2":pontos_player_2, "player_atual":player_atual, "poder": poder} 
					
				with open("save.json", "w") as save:
					json.dump(config, save)
			
			os.system('cls' if os.name == 'nt' else 'clear')
			opcao = MenuInicial()
			
		elif slot == "P":
				
			remover_poder = input("\nLinha ou coluna: ").upper()
			while remover_poder not in linhas and remover_poder not in colunas:
				print("\nEntrada inválida.")
				remover_poder = input("\nLinha ou coluna: ").upper()
			matriz, tabuleiro, nums_disponiveis, posicoes, poder = Poder(matriz, tabuleiro, linhas,colunas,poder, remover_poder,nums_disponiveis, posicoes, player_atual,player_1,player_2)
