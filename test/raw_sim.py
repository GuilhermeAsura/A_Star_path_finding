
import pygame
import sys
import candidato
import random

# Configurações
COR_FUNDO = (20, 80, 40)
COR_LINHA = (255, 255, 255)
COR_ROBO = (0, 0, 255)
COR_ROBO_COM_BOLA = (100, 140, 255)
COR_BOLA = (255, 165, 0)
COR_OBSTACULO = (255, 0, 0)
COR_CAMINHO = (0, 255, 255)
COR_GOL = (255, 255, 0)
COR_PAINEL = (40, 40, 40)
COR_BOTAO = (80, 80, 80)
COR_TEXTO_BOTAO = (255, 255, 255)

# Dimensões da Grade e da Tela
LARGURA_GRID = 20
ALTURA_GRID = 15
TAMANHO_CELULA = 45
ALTURA_PAINEL = 75

LARGURA_TELA = LARGURA_GRID * TAMANHO_CELULA
ALTURA_TELA = ALTURA_GRID * TAMANHO_CELULA + ALTURA_PAINEL

print(f"Configurações: Grid {LARGURA_GRID}x{ALTURA_GRID}, Tela {LARGURA_TELA}x{ALTURA_TELA}")

# Desenho
def desenhar_grade(tela):
    try:
        for x in range(0, LARGURA_TELA, TAMANHO_CELULA):
            pygame.draw.line(tela, COR_LINHA, (x, 0), (x, ALTURA_GRID * TAMANHO_CELULA))
        for y in range(0, ALTURA_GRID * TAMANHO_CELULA + 1, TAMANHO_CELULA):
            pygame.draw.line(tela, COR_LINHA, (0, y), (LARGURA_TELA, y))
    except Exception as e:
        print(f"Erro ao desenhar grade: {e}")

def desenhar_retangulo(tela, pos_grid, cor):
    try:
        x, y = pos_grid
        if not (0 <= x < LARGURA_GRID and 0 <= y < ALTURA_GRID):
            print(f"Posição fora dos limites: {pos_grid}")
            return
        
        rect_x = int(x * TAMANHO_CELULA)
        rect_y = int(y * TAMANHO_CELULA)
        
        if rect_x < 0 or rect_y < 0:
            print(f"Coordenadas negativas: {rect_x}, {rect_y}")
            return
            
        rect = pygame.Rect(rect_x, rect_y, TAMANHO_CELULA, TAMANHO_CELULA)
        pygame.draw.rect(tela, cor, rect)
    except Exception as e:
        print(f"Erro ao desenhar retângulo: {e}")

def desenhar_circulo(tela, pos_grid, cor, raio_fator=0.4):
    try:
        x, y = pos_grid
        if not (0 <= x < LARGURA_GRID and 0 <= y < ALTURA_GRID):
            print(f"Posição fora dos limites: {pos_grid}")
            return
            
        centro_x = int(x * TAMANHO_CELULA + TAMANHO_CELULA // 2)
        centro_y = int(y * TAMANHO_CELULA + TAMANHO_CELULA // 2)
        raio = max(1, int(TAMANHO_CELULA * raio_fator))
        
        if centro_x < 0 or centro_y < 0 or raio <= 0:
            print(f"Parâmetros inválidos: centro=({centro_x}, {centro_y}), raio={raio}")
            return
            
        pygame.draw.circle(tela, cor, (centro_x, centro_y), raio)
    except Exception as e:
        print(f"Erro ao desenhar círculo: {e}")

def desenhar_caminho(tela, caminho):
    try:
        if not caminho:
            return
        for passo in caminho:
            if len(passo) == 2:
                desenhar_circulo(tela, passo, COR_CAMINHO, raio_fator=0.2)
    except Exception as e:
        print(f"Erro ao desenhar caminho: {e}")

# Lógica
def resetar_cenario():
    # Posições fixas
    pos_robo = (2, ALTURA_GRID // 2)
    pos_gol = (LARGURA_GRID - 1, ALTURA_GRID // 2)

    # Posição da Bola
    pos_bola = (LARGURA_GRID // 2 + 2, ALTURA_GRID // 2 + 1)

    # Posição dos Adversários (Obstaculos) - reduzido para teste
    obstaculos = [(10, 5), (12, 7), (15, 3), (8, 10), (14, 12)]

    return {
        "pos_robo": pos_robo, "pos_bola": pos_bola, "pos_gol": pos_gol, "obstaculos": obstaculos,
        "tem_bola": False, "caminho_atual": [], "simulacao_rodando": False,
        "mensagem": "Teste iniciado"
    }

# Loop do Simulador
def main():
    print("Inicializando pygame...")
    pygame.init()
    
    print("Criando tela...")
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption("EDROM - Teste")
    
    print("Inicializando relógio...")
    clock = pygame.time.Clock()
    
    print("Resetando cenário...")
    estado_jogo = resetar_cenario()
    
    print("Entrando no loop principal...")
    frame_count = 0

    while True:
        try:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("Saindo...")
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        estado_jogo["simulacao_rodando"] = not estado_jogo["simulacao_rodando"]
                        print(f"Simulação: {'ligada' if estado_jogo['simulacao_rodando'] else 'desligada'}")
                    if event.key == pygame.K_r:
                        estado_jogo = resetar_cenario()
                        print("Cenário resetado")

            if estado_jogo["simulacao_rodando"]:
                if not estado_jogo["caminho_atual"]:
                    objetivo_atual = estado_jogo["pos_bola"] if not estado_jogo["tem_bola"] else estado_jogo["pos_gol"]
                    print(f"Calculando caminho de {estado_jogo['pos_robo']} para {objetivo_atual}")
                    
                    try:
                        caminho = candidato.encontrar_caminho(
                            pos_inicial=estado_jogo["pos_robo"], 
                            pos_objetivo=objetivo_atual, 
                            obstaculos=estado_jogo["obstaculos"],
                            largura_grid=LARGURA_GRID, 
                            altura_grid=ALTURA_GRID, 
                            tem_bola=estado_jogo["tem_bola"])
                        
                        if caminho:
                            estado_jogo["caminho_atual"] = caminho
                            print(f"Caminho encontrado com {len(caminho)} passos")
                        else:
                            print("Nenhum caminho encontrado")
                    except Exception as e:
                        print(f"Erro ao calcular caminho: {e}")
                        estado_jogo["caminho_atual"] = []
                        
                if estado_jogo["caminho_atual"]:
                    proximo_passo = estado_jogo["caminho_atual"].pop(0)
                    estado_jogo["pos_robo"] = proximo_passo

                if not estado_jogo["tem_bola"] and estado_jogo["pos_robo"] == estado_jogo["pos_bola"]:
                    estado_jogo["tem_bola"] = True
                    estado_jogo["caminho_atual"] = []
                    print("Bola capturada!")
                    
                if estado_jogo["tem_bola"] and estado_jogo["pos_robo"] == estado_jogo["pos_gol"]:
                    print("GOL!")
                    estado_jogo = resetar_cenario()

            # Desenhar
            tela.fill(COR_FUNDO)
            desenhar_grade(tela)
            
            if estado_jogo["caminho_atual"]:
                desenhar_caminho(tela, estado_jogo["caminho_atual"])

            desenhar_retangulo(tela, estado_jogo["pos_gol"], COR_GOL)
            
            for obs in estado_jogo["obstaculos"]:
                desenhar_retangulo(tela, obs, COR_OBSTACULO)

            if estado_jogo["tem_bola"]:
                desenhar_retangulo(tela, estado_jogo["pos_robo"], COR_ROBO_COM_BOLA)
                desenhar_circulo(tela, estado_jogo["pos_robo"], COR_BOLA, raio_fator=0.3)
            else:
                desenhar_retangulo(tela, estado_jogo["pos_robo"], COR_ROBO)
                desenhar_circulo(tela, estado_jogo["pos_bola"], COR_BOLA)
            
            # Desenhar painel simples
            painel_rect = pygame.Rect(0, ALTURA_GRID * TAMANHO_CELULA, LARGURA_TELA, ALTURA_PAINEL)
            pygame.draw.rect(tela, COR_PAINEL, painel_rect)

            pygame.display.flip()
            clock.tick(5)
            
            frame_count += 1
            if frame_count % 50 == 0:
                print(f"Frame {frame_count} - Robô em {estado_jogo['pos_robo']}")

        except Exception as e:
            print(f"Erro no loop principal: {e}")
            import traceback
            traceback.print_exc()
            break

    pygame.quit()

if __name__ == '__main__':
    main()