import pygame
import sys

# Minimal test to isolate the issue
pygame.init()

# Try smaller screen size first
LARGURA_TELA = 900  # 20 * 45
ALTURA_TELA = 750   # 15 * 45 + 75

print(f"Attempting to create screen: {LARGURA_TELA}x{ALTURA_TELA}")

try:
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    print("Screen created successfully")
    
    pygame.display.set_caption("Test Window")
    print("Caption set successfully")
    
    # Try basic drawing
    tela.fill((20, 80, 40))
    print("Fill successful")
    
    # Try drawing a simple rectangle
    pygame.draw.rect(tela, (255, 0, 0), pygame.Rect(10, 10, 100, 100))
    print("Rectangle drawn successfully")
    
    pygame.display.flip()
    print("Display flip successful")
    
    # Keep window open for 3 seconds
    pygame.time.wait(3000)
    
except Exception as e:
    print(f"Error during pygame operations: {e}")
    import traceback
    traceback.print_exc()
finally:
    pygame.quit()
    print("Test completed")