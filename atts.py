import pygame as p

p.font.init()

x = 'Pygame Tutorial!'

small_font = p.font.Font("freesansbold.ttf", 20)

white = (255, 255, 255)
black = (0, 0, 0)


class Button:

    def __init__(self, length, width, xposition, yposition, color, surface):

        self.length = length
        self.width = width
        self.xposition = xposition
        self.yposition = yposition
        self.color = color
        self.surface = surface

    def create_square(self):

        one = small_font.render('1', 1, white)
        two = small_font.render('2', 1, white)
        three = small_font.render('3', 1, white)
        four = small_font.render('4', 1, white)
        five = small_font.render('5', 1, white)
        six = small_font.render('6', 1, white)
        seven = small_font.render('7', 1, white)
        eight = small_font.render('8', 1, white)
        nine = small_font.render('9', 1, white)
        zero = small_font.render('0', 1, white)

        numbers = [one, two, three, four, five, six, seven, eight, nine, zero]

        for num in numbers:

            count = 0

            while self.xposition < 100:

                square = [self.xposition, self.yposition, self.length, self.width]

                p.draw.rect(self.surface, self.color, square)
                self.surface.blit(num, (self.xposition + 9, self.yposition + 9))

                self.xposition += 40

                break

            else:

                square = [self.xposition, self.yposition, self.length, self.width]

                p.draw.rect(self.surface, self.color, square)
                self.surface.blit(num, (self.xposition + 9, self.yposition + 9))

                self.yposition += 40
                self.xposition -= 120









