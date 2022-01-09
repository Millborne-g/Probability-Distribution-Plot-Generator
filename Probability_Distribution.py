"""
   Probability Distribution (CPE223_SC5)
   Members:
    Casey Joys Bendijo
    Christine Jane Ladesma
    Jonh Anthony Batal
    Millborne A. Galamiton
"""


# for inline plots in jupyter
#matplotlib inline
# import matplotlib
import matplotlib.pyplot as plt
# for latex equations
from IPython.display import Math, Latex
# for displaying images
from IPython.core.display import Image
# import seaborn
import seaborn as sns
# settings for seaborn plotting style
sns.set(color_codes=True)
# settings for seaborn plot sizes
sns.set(rc={'figure.figsize':(5,5)})
# import uniform distribution
from scipy.stats import uniform
# random numbers from uniform distribution
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import pandas
from scipy.stats import norm
from scipy.stats import gamma
from scipy.stats import expon
from scipy.stats import poisson
from scipy.stats import binom
from scipy.stats import bernoulli
import pygame
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect
from enum import Enum


BLUE = (47,79,79)
WHITE = (255, 255, 255)



def create_surface_with_text(text, font_size, text_rgb, bg_rgb):
    """ Returns surface with text written on """
    font = pygame.freetype.SysFont("Courier", font_size, bold=True)
    surface, _ = font.render(text=text, fgcolor=text_rgb, bgcolor=bg_rgb)
    return surface.convert_alpha()


class UIElement(Sprite):
    """ An user interface element that can be added to a surface """

    def __init__(self, center_position, text, font_size, bg_rgb, text_rgb, action=None):
        """
        Args:
            center_position - tuple (x, y)
            text - string of text to write
            font_size - int
            bg_rgb (background colour) - tuple (r, g, b)
            text_rgb (text colour) - tuple (r, g, b)
            action - the gamestate change associated with this button
        """
        self.mouse_over = False

        default_image = create_surface_with_text(
            text=text, font_size=font_size, text_rgb=text_rgb, bg_rgb=bg_rgb
        )

        highlighted_image = create_surface_with_text(
            text=text, font_size=font_size * 1.2, text_rgb=text_rgb, bg_rgb=bg_rgb
        )

        self.images = [default_image, highlighted_image]

        self.rects = [
            default_image.get_rect(center=center_position),
            highlighted_image.get_rect(center=center_position),
        ]

        self.action = action

        super().__init__()

    @property
    def image(self):
        return self.images[1] if self.mouse_over else self.images[0]

    @property
    def rect(self):
        return self.rects[1] if self.mouse_over else self.rects[0]

    def update(self, mouse_pos, mouse_up):
        """ Updates the mouse_over variable and returns the button's
            action value when clicked.
        """
        if self.rect.collidepoint(mouse_pos):
            self.mouse_over = True
            if mouse_up:
                return self.action
        else:
            self.mouse_over = False

    def draw(self, surface):
        """ Draws element onto a surface """
        surface.blit(self.image, self.rect)

pygame.init()
width = 1200
height = 600

win =pygame.display.set_mode((width, height))
pygame.display.set_caption("Probability Distribution")
background = pygame.image.load('869.jpg')
background = pygame.transform.scale(background, (1200, 600))
background2 = pygame.image.load('6XxLQkY.gif')
background2 = pygame.transform.scale(background2, (1200, 600))
background3 = pygame.image.load('pixel-jeff-mario.gif')
background3 = pygame.transform.scale(background3, (1200, 600))
dialog = pygame.image.load('put-your-text-in-famous-video-game-dialogue-boxes-removebg-preview.png')
dialog = pygame.transform.scale(dialog, (600, 300))

Title = pygame.image.load('cd9ac625722bb76f67606e50340f84df.png')
Title = pygame.transform.scale(Title, (600, 70))

#menuBG = pygame.image.load('HUD_Menus-removebg-preview.png')
#menuBG  = pygame.transform.scale(menuBG , (300, 130))

def fade(width, height): 
    fade = pygame.Surface((width, height))
    fade.fill((0,0,0))
    for alpha in range(0, 100):
        fade.set_alpha(alpha)
        #redrawWindow()
        win.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(1)
class button():
    def __init__(self, color, x,y,width,height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
    def draw(self,win,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pygame.font.SysFont('comicsans', 60)
            text = font.render(self.text, 1, (255,255,255))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False

def main():
    pygame.init()

    #screen = pygame.display.set_mode((800, 600))
    game_state = GameState.TITLE

    while True:
        if game_state == GameState.TITLE:
            game_state = title_screen(win)

        if game_state == GameState.NEWGAME:
            game_state = play_level(win)

        if game_state == GameState.QUIT:
            pygame.quit()
            return
def Uniform(text):
    n = int(text)
    start = 10
    width1 = 20
    data_uniform = uniform.rvs(size=n, loc = start, scale=width1)
    ax = sns.distplot(data_uniform,
                      bins=100,
                      kde=True,
                      color='skyblue',
                      hist_kws={"linewidth": 15,'alpha':1})
    ax.set(xlabel='Uniform Distribution ', ylabel='Frequency')
    plt.show()
    return
def Uniform_Distribution(screen):
    fade(width, height)
    Generate_Button = button((47,79,79),480, 380,300,70,'Generate Plot')
    
    text = ''
    #text = pygame.font.Font('digifaw.ttf', int(450*100/768))

    input1 = pygame.Rect(550, 280,600,100)
    color = pygame.Color(42, 8, 40)
    base_font = pygame.font.Font(None,100)
    #fadeout(width, height)
    return_btn = UIElement(
        center_position=(140, 570),
        font_size=20,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="Return to Selection",
        action=GameState.TITLE,
    )

    while True:
        mouse_up = False
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode
            if event.type == pygame.MOUSEMOTION:
                if Generate_Button.isOver(pos):
                    Generate_Button.color = (0,0,0)
                else:
                    Generate_Button.color = (47,79,79)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Generate_Button.isOver(pos):
                    #title_screen(screen)
                    if text.isdigit():
                        Uniform(text)
                    else:
                        text = 'Invalid'
            
           
        win.blit(background3 ,(0,0))
        win.blit(dialog,(320,140))
        text_surface = base_font.render(text,True,(255, 255, 255))
        pygame.draw.rect(win,color,input1)
        win.blit(text_surface,(input1.x + 5, input1.y + 10))

        input1.w = max(100, text_surface.get_width()+10)
        #win.blit(background3 ,(0,0))
        

        ui_action = return_btn.update(pygame.mouse.get_pos(), mouse_up)
        if ui_action is not None:
            print("hello "+text)
            return ui_action
        return_btn.draw(screen)
        Generate_Button.draw(screen,(0,0,0)) 
        pygame.display.flip()

def Normal(text):
    n = int(text)
    data_normal = norm.rvs(size=n ,loc=0,scale=1)
    ax = sns.distplot(data_normal,
                      bins=100,
                      kde=True,
                      color='skyblue',
                      hist_kws={"linewidth": 15,'alpha':1})
    ax.set(xlabel='Normal Distribution', ylabel='Frequency')
    plt.show()
    return
def Normal_Distribution(screen):
    fade(width, height)
    Generate_Button = button((47,79,79),480, 380,300,70,'Generate Plot')
    
    text = ''
    #text = pygame.font.Font('digifaw.ttf', int(450*100/768))

    input1 = pygame.Rect(550, 280,600,100)
    color = pygame.Color(42, 8, 40)
    base_font = pygame.font.Font(None,100)
    #fadeout(width, height)
    return_btn = UIElement(
        center_position=(140, 570),
        font_size=20,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="Return to Selection",
        action=GameState.TITLE,
    )

    while True:
        mouse_up = False
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode
            if event.type == pygame.MOUSEMOTION:
                if Generate_Button.isOver(pos):
                    Generate_Button.color = (0,0,0)
                else:
                    Generate_Button.color = (47,79,79)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Generate_Button.isOver(pos):
                    #title_screen(screen)
                    if text.isdigit():
                        Normal(text)
                    else:
                        text = 'Invalid'
            
           
        win.blit(background3 ,(0,0))
        win.blit(dialog,(320,140))
        text_surface = base_font.render(text,True,(255, 255, 255))
        pygame.draw.rect(win,color,input1)
        win.blit(text_surface,(input1.x + 5, input1.y + 10))

        input1.w = max(100, text_surface.get_width()+10)
        #win.blit(background3 ,(0,0))
        

        ui_action = return_btn.update(pygame.mouse.get_pos(), mouse_up)
        if ui_action is not None:
            #print("hello "+text)
            return ui_action
        return_btn.draw(screen)
        Generate_Button.draw(screen,(0,0,0)) 
        pygame.display.flip()
        
def Gamma(text):
    n = int(text)
    data_gamma = gamma.rvs(a=5, size=n)
    ax = sns.distplot(data_gamma,
                      kde=True,
                      bins=100,
                      color='skyblue',
                      hist_kws={"linewidth": 15,'alpha':1})
    ax.set(xlabel='Gamma Distribution', ylabel='Frequency')
    plt.show()
    return
def Gamma_Distribution(screen):
    fade(width, height)
    Generate_Button = button((47,79,79),480, 380,300,70,'Generate Plot')
    
    text = ''
    #text = pygame.font.Font('digifaw.ttf', int(450*100/768))

    input1 = pygame.Rect(550, 280,600,100)
    color = pygame.Color(42, 8, 40)
    base_font = pygame.font.Font(None,100)
    #fadeout(width, height)
    return_btn = UIElement(
        center_position=(140, 570),
        font_size=20,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="Return to Selection",
        action=GameState.TITLE,
    )

    while True:
        mouse_up = False
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode
            if event.type == pygame.MOUSEMOTION:
                if Generate_Button.isOver(pos):
                    Generate_Button.color = (0,0,0)
                else:
                    Generate_Button.color = (47,79,79)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Generate_Button.isOver(pos):
                    #title_screen(screen)
                    
                    if text.isdigit():
                        Gamma(text)
                        #Normal(text)
                    else:
                        text = 'Invalid'
                    
            
           
        win.blit(background3 ,(0,0))
        win.blit(dialog,(320,140))
        text_surface = base_font.render(text,True,(255, 255, 255))
        pygame.draw.rect(win,color,input1)
        win.blit(text_surface,(input1.x + 5, input1.y + 10))

        input1.w = max(100, text_surface.get_width()+10)
        #win.blit(background3 ,(0,0))
        

        ui_action = return_btn.update(pygame.mouse.get_pos(), mouse_up)
        if ui_action is not None:
            print("hello "+text)
            return ui_action
        return_btn.draw(screen)
        Generate_Button.draw(screen,(0,0,0)) 
        pygame.display.flip()
        
def Exponential(text):
    n = int(text)
    data_expon = expon.rvs(scale=1,loc=0,size=n)
    ax = sns.distplot(data_expon,
                      kde=True,
                      bins=100,
                      color='skyblue',
                      hist_kws={"linewidth": 15,'alpha':1})
    ax.set(xlabel='Exponential Distribution', ylabel='Frequency')
    plt.show()
    return
def Exponential_Distribution(screen):
    fade(width, height)
    Generate_Button = button((47,79,79),480, 380,300,70,'Generate Plot')
    
    text = ''
    #text = pygame.font.Font('digifaw.ttf', int(450*100/768))

    input1 = pygame.Rect(550, 280,600,100)
    color = pygame.Color(42, 8, 40)
    base_font = pygame.font.Font(None,100)
    #fadeout(width, height)
    return_btn = UIElement(
        center_position=(140, 570),
        font_size=20,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="Return to Selection",
        action=GameState.TITLE,
    )

    while True:
        mouse_up = False
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode
            if event.type == pygame.MOUSEMOTION:
                if Generate_Button.isOver(pos):
                    Generate_Button.color = (0,0,0)
                else:
                    Generate_Button.color = (47,79,79)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Generate_Button.isOver(pos):
                    #title_screen(screen)
                    #Exponential(text)
                    if text.isdigit():
                        Exponential(text)
                    else:
                        text = 'Invalid'
                    
            
           
        win.blit(background3 ,(0,0))
        win.blit(dialog,(320,140))
        text_surface = base_font.render(text,True,(255, 255, 255))
        pygame.draw.rect(win,color,input1)
        win.blit(text_surface,(input1.x + 5, input1.y + 10))

        input1.w = max(100, text_surface.get_width()+10)
        #win.blit(background3 ,(0,0))
        

        ui_action = return_btn.update(pygame.mouse.get_pos(), mouse_up)
        if ui_action is not None:
            print("hello "+text)
            return ui_action
        return_btn.draw(screen)
        Generate_Button.draw(screen,(0,0,0)) 
        pygame.display.flip()




def title_screen(screen):
    fade(width, height)
    start_btn = UIElement(
        center_position=(600, 320),
        font_size=35,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="Start",
        action=GameState.NEWGAME,
    )
    quit_btn = UIElement(
        center_position=(600, 390),
        font_size=35,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="Quit",
        action=GameState.QUIT,
    )

    buttons = [start_btn, quit_btn]

    while True:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
            
        #screen.fill(BLUE)
        win.blit(background,(0,0)) 
        win.blit(Title,(320,200))
        for button in buttons:
            ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
            if ui_action is not None:
                return ui_action
            button.draw(screen)

        pygame.display.flip()


def play_level(screen):
    fade(width, height)
    Button1 = button((47,79,79),300, 80,600,100,'Uniform Distribution')
    Button2 = button((47,79,79),300, 200,600,100,'Normal Distribution')
    Button3 = button((47,79,79),300, 320,600,100,'Gamma Distribution')
    Button4 = button((47,79,79),300, 440,600,100,'Exponential Distribution')
    #fadeout(width, height)
    return_btn = UIElement(
        center_position=(140, 570),
        font_size=20,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="Return to main menu",
        action=GameState.TITLE,
    )

    while True:
        mouse_up = False
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
            if event.type == pygame.MOUSEMOTION:
                if Button1.isOver(pos):
                    Button1.color = (0,0,0)
                else:
                    Button1.color = (47,79,79)
                if Button2.isOver(pos):
                    Button2.color = (0,0,0)
                else:
                    Button2.color = (47,79,79)
                if Button3.isOver(pos):
                    Button3.color = (0,0,0)
                else:
                    Button3.color = (47,79,79)
                if Button4.isOver(pos):
                    Button4.color = (0,0,0)
                else:
                    Button4.color = (47,79,79)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Button1.isOver(pos):
                    #title_screen(screen)
                    Uniform_Distribution(screen)
                if Button2.isOver(pos):
                    Normal_Distribution(screen)
                if Button3.isOver(pos):
                    Gamma_Distribution(screen)
                if Button4.isOver(pos):
                    Exponential_Distribution(screen)
        win.blit(background2 ,(0,0)) 
        #win.blit(Title,(320,200))

        ui_action = return_btn.update(pygame.mouse.get_pos(), mouse_up)
        if ui_action is not None:
            return ui_action
        return_btn.draw(screen)
        Button1.draw(screen,(0,0,0))
        Button2.draw(screen,(0,0,0))
        Button3.draw(screen,(0,0,0))
        Button4.draw(screen,(0,0,0)) 
        pygame.display.flip()


class GameState(Enum):
    QUIT = -1
    TITLE = 0
    NEWGAME = 1


if __name__ == "__main__":
    main()
