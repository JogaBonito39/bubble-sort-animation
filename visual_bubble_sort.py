#visualization of bubble sort algorithm
#time complexity O(n^2) space complexity O(n)
#least to greatest. higher values float up to the top
#Visualization made with pygame libary
import pygame
import random

def bubble_sort_visual(elements: list()):
    pygame.init()
    screen_width = 800
    screen_height = 500
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    running = True
    
    
    def show_bubble(elements: list(),color="white"):
        initial_position = 0
        for i in range(0,len(elements)-1):
            #pygame.draw.rect(screen,"green",pygame.Rect(initial_position, 0, 4, elements[i]))
            pygame.draw.rect(screen,color,pygame.Rect(initial_position, elements[i], 4, screen_height-elements[i]))
            initial_position += 5
            
    while running:
        
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                running = False
            
        #screen.fill("black")
        screen.fill((0, 0, 0))
        #pygame.transform.rotate(screen,90)
        show_bubble(elements)
        pygame.display.update()
       # x=400
        #i=0
        #for elem_height in elements:
            #print(elem_height)
            #pygame.draw.rect(screen,"white",pygame.Rect((x,elem_height),(4,screen_height-elem_height)))
            #x+=5
        
        #bubble sort algorithm
        #'''
        key = pygame.key.get_pressed()
        if key[pygame.K_p] == True:
            for i in range(0,len(elements)-1):
                swapped = False
                for j in range(0,len(elements)-1-i):
                    if elements[j] < elements[j+1]:
                        temp = elements[j]
                        elements[j] = elements[j+1]
                        elements[j+1] = temp
                        swapped = True
                        #screen.fill((0,0,0))
                        #show_bubble(elements,"green")
                    #for elem_height in elements:
                        #print(elem_height)
                        #x=400
                        #pygame.draw.rect(screen,"white",pygame.Rect((x,elem_height),(4,screen_height-elem_height)))
                        #x+=5
                    screen.fill((0, 0, 0))
                    show_bubble(elements)
                    pygame.time.delay(50)
                    pygame.display.update()
                    #pygame.display.flip()
                if not swapped:
                    break
        #   '''
        pygame.display.flip()
        
        clock.tick(60)
   
pygame.quit()
                
if __name__ == "__main__":
    #elements = [350,50,180,300,100,240]
    elements = []
    for i in range(0,50):
        elements.append(random.randint(0,500))
    random.shuffle(elements)
    bubble_sort_visual(elements)
    print(elements)