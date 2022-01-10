import pygame, speech_recognition, threading, time

import sorting

def draw(phases, height, width, display):
    for i in range(len(phases)):
        k=0.5
        time.sleep(1/(len(phases[0])**2)*k)
        display.fill((0, 0, 0))
        for j in range(len(phases[0])):
            y = max(0, height-phases[i][j])
            x = j * width/len(phases[0])
            pygame.draw.circle(display, (255, 255, 255), (x, y), 5)
        pygame.display.update()

def listen():
    global numbers, height, width, gameDisplay
    while True:
        recognizer = speech_recognition.Recognizer()
        with speech_recognition.Microphone() as source:
            print("Listening")
            recognizer.pause_threshold = 0.5
            recognizer.energy_threshold = 4000
            audio = recognizer.listen(source)
        try:
            query = recognizer.recognize_google(audio, language="pt-br")
            print(query)

            if "ordenar crescente" in query:
                sorting_method = sorting_methods[0]
                phases = sorting_method(numbers)

                thread = threading.Thread(target=draw, args=(phases, height, width, gameDisplay,))
                thread.start()
            elif "ordenar decrescente" in query:
                sorting_method = sorting_methods[1]
                phases = sorting_method(numbers)

                thread = threading.Thread(target=draw, args=(phases, height, width, gameDisplay,))
                thread.start()
            elif "embaralhar" in query:
                sorting_method = sorting_methods[2]
                phases = sorting_method(numbers)

                thread = threading.Thread(target=draw, args=(phases, height, width, gameDisplay,))
                thread.start()
            elif query == "owo":
                print("uwu")

        except Exception as e:
            print("I couldn't hear you. Exception:", e)

listening_thread = threading.Thread(target=listen)
listening_thread.start()

pygame.init()
width = 800
height = 600
gameDisplay = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sort Visualizer")

file = open("input.txt", "r")
numbers = list(map(int, file.readlines()[0].split()))

sorting_methods = [sorting.bubble_sort, sorting.inversed_bubble_sort, sorting.numbers_shuffle]

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
                    print(event.key)

                    thread = threading.Thread(target=draw, args=(phases, height, width, gameDisplay,))
                    thread.start()

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()