# NumTab

Jogo de tabuleiro numérico para dois jogadores, jogado no terminal e desenvolvido em Python. Cada jogador recebe um objetivo secreto (formar uma sequência **ascendente**, **descendente**, de números **pares** ou **ímpares**) e precisa posicionar números estrategicamente na matriz para completá-lo antes do adversário — enquanto tenta impedir que ele complete o dele.

## Como jogar

- O tabuleiro é uma matriz quadrada (3x3, 4x4 ou 5x5, dependendo da dificuldade).
- A cada rodada, o jogador da vez escolhe uma posição livre (ex: `A1`) e um número disponível para colocar nela.
- No início da partida, cada jogador recebe um objetivo sorteado entre:
  - **ASCENDENTE** — sequência crescente (ex: 1, 2, 3)
  - **DESCENDENTE** — sequência decrescente (ex: 3, 2, 1)
  - **PAR** — sequência de números pares (ex: 2, 4, 6)
  - **ÍMPAR** — sequência de números ímpares (ex: 1, 3, 5)
- Vence a partida o primeiro jogador que formar uma sequência válida do seu objetivo em qualquer linha, coluna ou diagonal do tabuleiro.
- Se o tabuleiro for preenchido por completo sem que ninguém complete seu objetivo, a partida termina em empate e ambos os jogadores pontuam.

### Poder especial

Se ativado no início da partida, cada jogador tem direito a usar um **poder** uma única vez por jogo: ao digitar `P` no lugar de uma posição, o jogador pode escolher uma linha ou coluna inteira do tabuleiro para ser limpa, devolvendo os números usados nela para a lista de números disponíveis.

### Comandos durante a partida

| Entrada | Ação |
|---|---|
| Posição (ex: `A1`) | Joga na posição escolhida |
| `S` | Sai da partida (com opção de salvar o progresso) |
| `P` | Usa o poder especial (se disponível) |

## Menu inicial

1. **Novo Jogo** — inicia uma nova partida, com escolha de dificuldade (3x3, 4x4 ou 5x5), nomes dos jogadores e ativação do poder especial.
2. **Carregar jogo** — retoma uma partida salva anteriormente (`save.json`).
3. **Ranking** — exibe os 10 melhores resultados já registrados (`ranking.csv`).
4. **Sair** — encerra o programa.

## Requisitos

- Python 3
- Dependências listadas em `requirements.txt`:
  - [`tabulate`](https://pypi.org/project/tabulate/) — renderização do tabuleiro no terminal
  - [`colorama`](https://pypi.org/project/colorama/) — cores no terminal para diferenciar os jogadores

## Instalação

```bash
git clone https://github.com/levi-vasc/NumTab
cd NumTab
pip install -r requirements.txt
```

## Como executar

```bash
python main.py
```

## Estrutura do projeto

```
NumTab/
├── main.py            # Loop principal do jogo e fluxo do menu
├── numtab.py          # Funções auxiliares (configuração, matriz, vitória, ranking, poder)
├── requirements.txt   # Dependências do projeto
├── save.json          # Gerado automaticamente ao salvar uma partida
└── ranking.csv        # Gerado automaticamente ao final de cada partida
```

## Persistência de dados

- **Salvar partida**: ao sair de uma partida em andamento (`S`), é possível salvar o estado atual do jogo em `save.json` e retomá-lo depois pelo menu **Carregar jogo**.
- **Ranking**: ao final de cada partida (vitória ou empate), a pontuação dos jogadores é registrada em `ranking.csv`, exibida ordenada por pontuação no menu **Ranking**.
