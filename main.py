import pygame as p
import atts as a

window = p.display.set_mode([350, 500])

p.display.set_caption(a.x)

p.init()
running = True

window.fill(a.white)

while running:
        for event in p.event.get():
            if event.type == p.QUIT:
                running = False

        Button = a.Button(30, 30, 10, 100, a.black, window)

        mouse = p.mouse.get_pos()

        print(mouse)

        Button.create_square()

        p.display.update()
