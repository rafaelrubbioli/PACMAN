# PACMAN
Reinforcement learning - PACMAN 

## Modelagem
o objetivo é fazer o PacMan coletar uma pastilha, desviando dos fantasmas que felizmente não se movem. O cenário é um mundo  bidimensional, representado por uma matriz de caracteres. A pastilha é representada por `0`, um fantasma por `&`, uma parede por `#`, e um espaço vazio por `-`. 

Para o sistema de coordenadas, usaremos a notação de matriz em um programa. A primeira coordenada é a linha e a segunda é a coluna. A origem (0,0) é o caractere superior esquerdo. No exemplo abaixo, o mundo possui 5 linhas e 6 colunas. A pastilha está em (1,4) 2ª linha, 5ª coluna – e o fantasma em (2,4) – 3ª linha, 5ª coluna.

Origem (0,0) -> 
      ######
      #---0#
      #-#-&#
      #----#
      ######

O mundo é modelado como um MDP <S, A, R, T> com as seguintes características:
- S: conjunto de estados são as posições onde o agente pode estar `(-, 0 ou &)`;
- A: conjunto de ações: `{acima (U), abaixo (D), esquerda (L) e direita (R)}`;
- R: a função de recompensa é a seguinte: em `-` a recompensa é `-1`, em `0` a recompensa é `10` (oba, pílula!) e em `&` a recompensa é `-10` (ah! fantasma!). Isso vai incentivar o Pac-Man a encontrar o menor caminho até a pílula, evitando fantasmas;
- T: para facilitar, a função de transição é determinística: o agente consegue se mover na direção desejada. Por exemplo, a ação `U` em `(3,1)` leva o agente a `(2,1)`. Se tentar se mover para uma parede, o Pac-Man não se desloca e recebe (novamente) a recompensa do estado onde está.
- Considere o fator de desconto `γ = 0.9`

Este mundo possui uma característica adicional: os estados `0` e `&` são terminais (e pode haver múltiplas pílulas/fantasmas). Isto é, quando o agente chega em um deles, recebe a recompensa correspondente e depois é reinserido aleatoriamente em um estado não-terminal do mundo.

## Arquivo de entrada
O arquivo de entrada tem em sua 1ª linha o tamanho do mundo: `m` linhas e `n` colunas, separados por espaço. As próximas `m` linhas contém `n` caracteres cada (além da quebra de linha). Os `n` caracteres são `#, -, 0 ou &` (parede, espaço vazio, pastilha ou fantasma). Por exemplo, o conteúdo de um arquivo com o mundo do exemplo  é mostrado abaixo.

      5 6
      ######
      #---0#
      #-#-&#
      #----#
      ######

## Arquivo de saída

 - q.txt valores em Q no formato `linha,coluna,ação,valor`
 - pi.txt  política encontrada utilizando `L` para esquerda, `U` para acima, `D` para abaixo e `R` para direita  
 