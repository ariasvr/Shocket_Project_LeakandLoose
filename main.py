import pygame
from random import randint
import time
from json import load

card_width = pygame.image.load('id_card.png').get_width() // 3.2
card_height = pygame.image.load('id_card.png').get_height() // 3.2


class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height) #rectangle
        self.fill_color = color
    def color(self, new_color):
        self.fill_color = new_color
    def fill(self):
        pygame.draw.rect(window, self.fill_color, self.rect)
    def outline(self, frame_color, thickness): #outline of an existing rectangle
        pygame.draw.rect(window, frame_color, self.rect, thickness)   
    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)      

class Label(Area):
    def set_text(self, text, fsize=12, text_color=(0, 0, 0)):
        self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)
    def draw(self, shift_x=0, shift_y=0):
        window.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))


class Card(pygame.sprite.Sprite):
    def __init__(self, x, y, img, card_num):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(img, (card_width, card_height))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x 
        self.rect.y = y 
        self.card_num = card_num

    def resize(self, width, height):
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        pass

    def draw(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Deck():
    def __init__(self):
        self.cards = []

    def shuffle(self):
        pass

    def draw(self):
        pass

    def update(self):
        pass

class Player():
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.init_dect()
        self.identity = 3

    def init_dect(self):
        init_pos = width // 2 - card_width // 2 * 2 - 100
        id_card = Card(init_pos, height - card_height // 2 + 30, pygame.image.load('id_card.png'), 6)
        medical_card = Card(init_pos + card_width // 2 + 30, height - card_height // 2 + 30, pygame.image.load('medical_record.png'), 7)
        payment_card = Card(init_pos + card_width // 2 * 2 + 30 * 2, height - card_height // 2 + 30, pygame.image.load('payment.png'), 8)
        white_card = Card(init_pos + card_width // 2 * 3 + 30 * 3, height - card_height // 2 + 30, pygame.image.load('white_hat.png'), 9)
        self.hand.append(id_card)
        self.hand.append(medical_card)
        self.hand.append(payment_card)
        self.hand.append(white_card)

    def draw(self, window):
        for card in self.hand:
            card.draw(window)

    def update(self):
        pass

    def play(self):
        pass

def image_data(img_file):
    file = open(img_file, 'r')
    file = load(file)
    image_db = file
    return image_db


pygame.init()
window = pygame.display.set_mode((800, 360), pygame.RESIZABLE)
pygame.display.set_caption('Leak-and-Loose')
#background = transform.scale(image.load(), (800, 360))
clock = pygame.time.Clock()

running = True

width = window.get_width()
height = window.get_height()

img_data = image_data('image.json')

player1 = Player('Player1')
player2 = Player('Player2')

prev_card = None

deck_card = Card(width // 2 - card_width // 2 - 200, height // 2 - card_width // 2, pygame.image.load('back.png'), 0)
deck_card.resize(card_width // 2, card_height // 2)

choose_card = False

start_time = time.time()
curr_time = start_time

duration = 15

timer = Label(0, 0, 100, 50, (255, 255, 255))
timer.set_text(str(duration), 130, (255, 0, 0))

turn = 1

while running:
    choose = False
    if turn == 1:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False

            if not player1.hand:            
                print('You lose!')
                running = False
            
            if e.type == pygame.MOUSEBUTTONDOWN:
                x, y = e.pos
                if deck_card.rect.collidepoint(x, y):
                        if prev_card:
                            prev_card.rect.y += card_height // 2
                            prev_card = None
                        choose = True
                        # Take a card
                        card_num = randint(1, 5)

                        if card_num == 1:
                            for card in player1.hand:
                                if card.card_num == 4 or card.card_num == 5:
                                    print("You are secured!")
                                    del card
                                else:
                                    print('All your data is leaked!')
                                    running = False

                        if card_num == 4 or card_num == 5:
                            number_card = len(player1.hand) - 1
                            new_card = Card(player1.hand[number_card - 1].rect.x + card_width, player1.hand[number_card - 1].rect.y, pygame.image.load(img_data[str(card_num)]), card_num)
                            player1.hand.append(new_card)

                            # Change position
                            if player1.hand[0].rect.x > 0:
                                for card in player1.hand:
                                    card.rect.x -= card_width // 4
                            else:
                                player1.hand[0].rect.x = 0
                                for i in range(1, len(player1.hand)):
                                    player1.hand[i].rect.x = player1.hand[i - 1].rect.x + card_width // 3

                        if card_num == 2:                                
                            print("Lose 1 card")
                            del player1.hand[0]
                        if card_num == 3:                                
                            print("Lose 2 card")
                            del player1.hand[0]
                            del player1.hand[1]
                        break
                
                # If a card is chosen
                for card in player1.hand:
                    if card.rect.collidepoint(x, y):
                        card.rect.y -= card_height // 2

                        if prev_card:
                            prev_card.rect.y += card_height // 2
                        prev_card = card 
                        choose_card = True
                        break                                                   

        window.fill((255, 255, 255))

        for card in player1.hand:
            if card != prev_card and prev_card:
                card.draw(window)
            else:
                card.draw(window)
        if prev_card:
            prev_card.draw(window)

        # Draw timer
        new_time = time.time()
        if int(new_time - start_time) <= duration:
            timer.set_text(str(duration - int(new_time - start_time)), 130, (255, 0, 0))
            curr_time = new_time
        else:
            timer.set_text('Player ' + str(turn) + '\'s turn', 50, (255, 0, 0))
            pygame.time.wait(3000)
            curr_time = start_time
            turn = turn % 2 + 1

        timer.draw(width // 2, height // 2 - 100)        

    if turn == 2:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False

            if not player2.hand:            
                print('You lose!')
                running = False
            
            if e.type == pygame.MOUSEBUTTONDOWN:
                x, y = e.pos
                if deck_card.rect.collidepoint(x, y):
                        if prev_card:
                            prev_card.rect.y += card_height // 2
                            prev_card = None
                        choose = True
                        # Take a card
                        card_num = randint(1, 5)

                        if card_num == 1:
                            for card in player2.hand:
                                if card.card_num == 4 or card.card_num == 5:
                                    print("You are secured!")
                                    del card
                                else:
                                    print('All your data is leaked!')
                                    running = False

                        if card_num == 4 or card_num == 5:
                            number_card = len(player2.hand) - 1
                            new_card = Card(player2.hand[number_card - 1].rect.x + card_width, player2.hand[number_card - 1].rect.y, pygame.image.load(img_data[str(card_num)]), card_num)
                            player2.hand.append(new_card)

                            # Change position
                            if player2.hand[0].rect.x > 0:
                                for card in player2.hand:
                                    card.rect.x -= card_width // 4
                            else:
                                player2.hand[0].rect.x = 0
                                for i in range(1, len(player2.hand)):
                                    player2.hand[i].rect.x = player2.hand[i - 1].rect.x + card_width // 3

                        if card_num == 2:                                
                            print("Lose 1 card")
                            del player2.hand[0]
                        if card_num == 3:                                
                            print("Lose 2 card")
                            del player2.hand[0]
                            del player2.hand[1]
                        break
                
                # If a card is chosen
                for card in player2.hand:
                    if card.rect.collidepoint(x, y):
                        card.rect.y -= card_height // 2

                        if prev_card:
                            prev_card.rect.y += card_height // 2
                        prev_card = card 
                        choose_card = True
                        break               
                                                                 

        window.fill((255, 255, 255))

        for card in player2.hand:
            if card != prev_card and prev_card:
                card.draw(window)
            else:
                card.draw(window)
        if prev_card:
            prev_card.draw(window)

        # Draw timer
        new_time = time.time()
        if int(new_time - start_time) <= duration:
            timer.set_text(str(duration - int(new_time - start_time)), 130, (255, 0, 0))
            curr_time = new_time
        else:
            turn = turn % 2 + 1
            timer.set_text('Player ' + str(turn) + '\'s turn', 50, (255, 0, 0))
            pygame.time.wait(3000)
            curr_time = start_time

        timer.draw(width // 2, height // 2 - 100)              

    deck_card.draw(window)
    pygame.display.update()
    clock.tick(60)

