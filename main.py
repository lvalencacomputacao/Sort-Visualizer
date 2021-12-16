import pygame, threading, time

import sorting

def draw(phases, height, width, display):
    for i in range(len(phases)):
        k=1
        time.sleep(1/len(phases[0])*k)
        display.fill((0, 0, 0))
        for j in range(len(phases[0])):
            y = height-phases[i][j]
            x = j * width/len(phases[0])
            pygame.draw.circle(display, (255, 255, 255), (x, y), 5)
        pygame.display.update()

pygame.init()
width = 800
height = 600
gameDisplay = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sort Visualizer")

file = open("input.txt", "r")
numbers = list(map(int, file.readlines()[0].split()))

sorting_methods = [sorting.bubble_sort, sorting.insertion_sort, sorting.inversed_bubble_sort]

gameDisplay.fill((0, 0, 0))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
                if event.key-48 < len(sorting_methods) and event.key-48 >= 0:
                    sorting_method = sorting_methods[event.key-48]
                    phases = sorting_method(numbers)

                    thread = threading.Thread(target=draw, args=(phases, height, width, gameDisplay,))
                    thread.start()

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()