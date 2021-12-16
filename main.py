import pygame, threading

import sorting

pygame.init()
width = 800
height = 600
gameDisplay = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sort Visualizer")

gameDisplay.fill((0, 0, 0))
clock = pygame.time.Clock()
running = True

file = open("input.txt", "r")
numbers = list(map(int, file.readlines()[0].split()))

sorting_methods = [sorting.bubble_sort, sorting.insertion_sort, sorting.inversed_bubble_sort]

def draw(phases):
    print(phases[len(phases)-1])


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
                if event.key-48 < len(sorting_methods) and event.key-48 >= 0:
                    sorting_method = sorting_methods[event.key-48]
                    phases = sorting_method(numbers)
                    thread = threading.Thread(target=draw, args=(phases))
                    thread.start()
                    thread.join()

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()