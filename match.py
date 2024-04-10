import pygame

pygame.init()


screen = pygame.display.set_mode((600,600))
screen.fill("green")

pygame.display.update()

candy_crush = pygame.image.load("candycrush.jpg")
ludo = pygame.image.load("ludo.png")
subway_surfers = pygame.image.load("subwaysurfer.png")
temple_run = pygame.image.load("templerun.png")


screen.blit(subway_surfers, (150,100))
screen.blit(ludo, (150,200))
screen.blit(temple_run, (150,300))
screen.blit(candy_crush, (150,400))

font = pygame.font.SysFont("Times New Roman", 35)

text_1 = font.render("Ludo", True, "pink")
text_2 = font.render("Candy Crush", True, "pink")
text_3 = font.render("Subway Surfers", True, "pink")
text_4 = font.render("Temple Run", True, "pink")

screen.blit(text_1, (350,100))
screen.blit(text_2, (350,200))
screen.blit(text_3, (350,300))
screen.blit(text_4, (350,400))

pygame.display.update()

# 1 = True 0 = False 
while 1:
    event = pygame.event.poll()
    if event.type == pygame.MOUSEBUTTONDOWN:
        pos = pygame.mouse.get_pos()
        pygame.draw.circle(screen, (0,0,0), (pos), 20,0)
        pygame.display.update()
    elif event.type == pygame.MOUSEBUTTONUP:
        pos_2 = pygame.mouse.get_pos()
        pygame.draw.line(screen, (0,0,0), (pos), (pos_2), 5)
        pygame.draw.circle(screen, (0,0,0), (pos_2), 20,0)
        pygame.display.update()
        



