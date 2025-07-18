# NOME DO CANDIDATO: [Seu Nome Aqui]
# CURSO DO CANDIDATO: [Seu Curso Aqui]
# AREAS DE INTERESSE: [Suas Áreas de Interesse Aqui]

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

def heuristic(p1, p2):
    """
    Calcula a distância de Manhattan.
    """
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)

def encontrar_caminho(pos_inicial, pos_objetivo, obstaculos, largura_grid, altura_grid, tem_bola=False):
    """
    Implementação do algoritmo A* com um limite de iterações para segurança.
    """
    # 1. --- CRIAÇÃO DO GRID ---
    grid = [[Node(x, y) for y in range(altura_grid)] for x in range(largura_grid)]
    for obs_pos in obstaculos:
        x, y = obs_pos
        if 0 <= x < largura_grid and 0 <= y < altura_grid:
            grid[x][y].is_obstacle = True
        else:
            print(f"AVISO: Obstáculo fora da grade ignorado: {obs_pos}")

    start_node = grid[pos_inicial[0]][pos_inicial[1]]
    end_node = grid[pos_objetivo[0]][pos_objetivo[1]]
    
    start_node.g_score = 0
    start_node.h_score = heuristic(start_node.get_pos(), end_node.get_pos())
    start_node.f_score = start_node.h_score

    # 2. --- INICIALIZAÇÃO DO A* ---
    open_set = PriorityQueue()
    count = 0
    open_set.put((start_node.f_score, count, start_node))
    open_set_hash = {start_node.get_pos()}

    # 3. --- LOOP PRINCIPAL DO A* COM SAFEGUARD ---
    max_iterations = largura_grid * altura_grid * 5 
    iterations = 0

    while not open_set.empty():
        iterations += 1
        if iterations > max_iterations:
            print("Pathfinding timeout: A* excedeu o limite de iterações.")
            return []  # Evita crash

        current_node = open_set.get()[2]
        open_set_hash.remove(current_node.get_pos())

        if current_node.get_pos() == end_node.get_pos():
            return reconstruct_path(current_node, largura_grid, altura_grid)

        # 4. --- ANÁLISE DOS VIZINHOS ---
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue

                check_x, check_y = current_node.x + dx, current_node.y + dy

                # Verificação de fronteira da grade
                if not (0 <= check_x < largura_grid and 0 <= check_y < altura_grid):
                    continue

                neighbor_node = grid[check_x][check_y]

                if neighbor_node.is_obstacle:
                    continue

                move_cost = math.sqrt(dx*dx + dy*dy)
                temp_g_score = current_node.g_score + move_cost

                if temp_g_score < neighbor_node.g_score:
                    neighbor_node.parent = current_node
                    neighbor_node.g_score = temp_g_score
                    neighbor_node.h_score = heuristic(neighbor_node.get_pos(), end_node.get_pos())
                    neighbor_node.f_score = neighbor_node.g_score + neighbor_node.h_score

                    if neighbor_node.get_pos() not in open_set_hash:
                        count += 1
                        open_set.put((neighbor_node.f_score, count, neighbor_node))
                        open_set_hash.add(neighbor_node.get_pos())

    return []  # Nenhum caminho encontrado
