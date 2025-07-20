# NOME DO CANDIDATO: Guilherme Maximiano S. Lazzarini
# CURSO DO CANDIDATO: Engenharia Mecatrônica
# AREAS DE INTERESSE: Movimento e Behavior

from queue import PriorityQueue
import math

class Node:
    """
    Uma classe para representar um nó no grid.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.g_score = float('inf')
        self.h_score = 0
        self.f_score = float('inf')
        self.parent = None
        self.is_obstacle = False

    def get_pos(self):
        return self.x, self.y

    def __lt__(self, other):
        return self.f_score < other.f_score

def reconstruct_path(current_node, largura_grid, altura_grid):
    """
    Cria a lista de coordenadas do caminho final.
    Garante que todas as posições estão dentro dos limites da grade.
    """
    path = []
    while current_node.parent is not None:
        x, y = current_node.get_pos()
        if not (0 <= x < largura_grid and 0 <= y < altura_grid):
            print(f"ERRO: Coordenada inválida detectada no caminho: ({x}, {y}) — ignorando.")
            break
        path.append((x, y))
        current_node = current_node.parent
    path.reverse()
    return path

def manhattan_heuristic(p1, p2):
    """
    Calcula a distância de Manhattan (similar à distância vetorial). Com essa heurística temos o que a literatura chama de A* Greedy, 
    essa variação do algorítmo apenas busca a forma mais curta chegar ao destino. Segue análise:

    - Vantagens: 
        - O algorítmo converge mais rápido visto que a exigência de cáculos é baixa.
        - Requer menos poder computacional.

    - Desvantagens:
        - Fornece uma trajetória não otimizada.
    """
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)

def octile_heuristic(p1, p2):
    """
    Calcula a distância Octal. Essa heurística é a melhor aplicável em Grids pois permite
    uma acurácia maior para movimentos com 8 direções.
    """
    x1, y1 = p1
    x2, y2 = p2
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    return max(dx, dy) + (math.sqrt(2) - 1) * min(dx, dy)

def encontrar_caminho(pos_inicial, pos_objetivo, obstaculos, largura_grid, altura_grid, tem_bola=False):
    """
    Implementação do algoritmo A* com um limite de iterações para segurança.
    """
    
    # Validação dos tipos de entrada
    if not isinstance(pos_inicial, tuple) or len(pos_inicial) != 2:
        print(f"ERRO: pos_inicial deve ser uma tupla (x, y), recebido: {pos_inicial}")
        return []
    if not isinstance(pos_objetivo, tuple) or len(pos_objetivo) != 2:
        print(f"ERRO: pos_objetivo deve ser uma tupla (x, y), recebido: {pos_objetivo}")
        return []
    
    # Validação limites da janela do pygame
    for nome, pos in [("inicial", pos_inicial), ("objetivo", pos_objetivo)]:
        x, y = pos
        if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
            print(f"ERRO: Coordenadas {nome} devem ser números: ({x}, {y})")
            return []
        if not (0 <= x < largura_grid and 0 <= y < altura_grid):
            print(f"ERRO: Posição {nome} fora dos limites da grade: ({x}, {y})")
            return []

    # Criação grid [y][x] 
    grid = []
    for y in range(altura_grid):
        row = []
        for x in range(largura_grid):
            row.append(Node(x, y))
        grid.append(row)
    
    # Marcando obstáculos
    for obs_pos in obstaculos:
        if not isinstance(obs_pos, tuple) or len(obs_pos) != 2:
            print(f"AVISO: Obstáculo inválido ignorado: {obs_pos}")
            continue
        x, y = obs_pos
        if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
            print(f"AVISO: Coordenadas do obstáculo devem ser números: {obs_pos}")
            continue
        if 0 <= x < largura_grid and 0 <= y < altura_grid:
            grid[int(y)][int(x)].is_obstacle = True
        else:
            print(f"AVISO: Obstáculo fora da grade ignorado: {obs_pos}")

    start_node = grid[int(pos_inicial[1])][int(pos_inicial[0])]  # [y][x]
    end_node = grid[int(pos_objetivo[1])][int(pos_objetivo[0])]    # [y][x]
    
    start_node.g_score = 0
    start_node.h_score = octile_heuristic(start_node.get_pos(), end_node.get_pos())
    start_node.f_score = start_node.h_score

    # Inicializando o Algorítmo A*
    open_set = PriorityQueue()
    count = 0
    open_set.put((start_node.f_score, count, start_node))
    open_set_hash = {start_node.get_pos()}
    closed_set = set()

    # Loop principal do A*
    max_iterations = largura_grid * altura_grid * 5 
    iterations = 0

    while not open_set.empty():
        iterations += 1
        if iterations > max_iterations:
            print("Pathfinding timeout: A* excedeu o limite de iterações.") # verificando se algo ia pra fora do grid
            return []  

        current_node = open_set.get()[2]
        open_set_hash.remove(current_node.get_pos())
        closed_set.add(current_node.get_pos())

        if current_node.get_pos() == end_node.get_pos():
            return reconstruct_path(current_node, largura_grid, altura_grid)

        # Analisando os vizinhos
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue

                check_x = current_node.x + dx
                check_y = current_node.y + dy

                # Verificação de fronteira da grade ~ tive mt bug com a renderização do pygame pois o Linux não tem driver nativo pra ela.
                if not (0 <= check_x < largura_grid and 0 <= check_y < altura_grid):
                    continue

                # Verificação adicional de segurança ~ os bugs acusavam explosão de valor, como se algo estivesse indo pra fora do grid
                # então tentei verificar se tudo tava dentro do grid
                if check_x < 0 or check_x >= largura_grid or check_y < 0 or check_y >= altura_grid:
                    print(f"ERRO: Índice fora dos limites detectado: ({check_x}, {check_y})")
                    continue
                # No final, esse bug de algo fora do grid era coisa da minha cabeça. O problema era que eu estava tentando rodar no linux
                # tem uns B.O com a renderização das janelas do pygame. Tentei forçar drivers pra renderização mas enquanto mexia nos driver obtive um 
                # carinhoso erro de dpkg(1) após atualizar os drivers do Ubuntu e aí TODOS os meus drivers foram de caixa (driver de WiFi, Bluetooth, USB
                # TouchPad, entrada de rede). Ou seja, no final meu SO tava sem wifi, n lia entrada de rede e nem USB de jeito nenhum... Tentei recorrer
                # ao recovery_mode na bios mas nada feito....tive q reinstalar o Ubuntu :'/
                # Depois descobri q era só rodar no Windows q o pygame rodava bonitinho e tava tudo certo :'p

                neighbor_node = grid[check_y][check_x] 

                if neighbor_node.get_pos() in closed_set:
                    continue

                if neighbor_node.is_obstacle:
                    continue

                move_cost = 1.0 if dx==0 or dy==0 else math.sqrt(2)

                # Penalidade quanto à 'rotação' (transição de movimento envolvendo posições diagonais).
                parent_node = current_node.parent
                if parent_node:
                    prev_dx = current_node.x - parent_node.x
                    prev_dy = current_node.y - parent_node.y
                    if (dx,dy) != (prev_dx, prev_dy):
                        move_cost += 0.5
                    
                # Penalidade quanto às redondezas dos oponentes (zona de perigo)
                is_danger_zone = False
                for obs_pos in obstaculos:
                    if abs(neighbor_node.x - obs_pos[0]) <= 1 and abs(neighbor_node.y - obs_pos[1]) <= 1:
                        is_danger_zone = True
                        break
                if is_danger_zone:
                    move_cost += 8.5

                # Adicionando peso para o estado com bola.
                if tem_bola:
                    move_cost *= 2

                temp_g_score = current_node.g_score + move_cost

                if temp_g_score < neighbor_node.g_score:
                    neighbor_node.parent = current_node
                    neighbor_node.g_score = temp_g_score
                    neighbor_node.h_score = octile_heuristic(neighbor_node.get_pos(), end_node.get_pos())
                    neighbor_node.f_score = neighbor_node.g_score + neighbor_node.h_score

                    if neighbor_node.get_pos() not in open_set_hash:
                        count += 1
                        open_set.put((neighbor_node.f_score, count, neighbor_node))
                        open_set_hash.add(neighbor_node.get_pos())

    return []  