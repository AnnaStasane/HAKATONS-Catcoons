import pygame, sys, random, time
pygame.init()

WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("HAKATONS PYGIRLS")

goodchoice_img = pygame.image.load("img/good_img.png")
badchoice_img = pygame.image.load("img/bad_img.png")

sum = 0
turns = 0

city_image = {
    0: pygame.image.load("img/base.jpg"),
    1: pygame.image.load("img/gre1.png"),
    2: pygame.image.load("img/gre2.png"),
    3: pygame.image.load("img/gre3.png"),
    4: pygame.image.load("img/gre4.png"),
    5: pygame.image.load("img/gre5.png"),
    -1: pygame.image.load("img/red1.png"),
    -2:pygame.image.load("img/red2.png"),
    -3:pygame.image.load("img/red3.png"),
    -4:pygame.image.load("img/red4.png"),
    -5:pygame.image.load("img/red5.png")
}

stand_img = pygame.image.load("img/stand.png")

font = pygame.font.SysFont(None, 100)
text_font = pygame.font.SysFont(None, 30)
start_font = pygame.font.SysFont(None, 40)

good_text = [
    'Piešķirt lielāku finansējumu skolām?',
    'Ieviest stingrākas regulācijas un sodus par bezatbildīgu vides piesārņošanu?',
    'Ieviest vairāk resursu zaļā un atjaunojamā enerģijā?',
    'Ieviest jaunus sabiedriskā transporta maršrutus pilsētas rajonu un priekšpilsētas savienošanai?',
    'Aizliegt centrā iebraukt ar transportlīdzekļiem, kuri izdala izmešus?',
    'Ieviest lielāku finansējumu ceļu uzlabošanā un drošībā?',
    'Iekārtot vairāk jauniešiem draudzīgas vietas?',
    'Iekārtot bērniem un ģimenēm draudzīgas vides?',
    'Piešķirt lielaku atbalstu bezpajumtniekiem un daudzbērnu ģimenēm?'
    ]
bad_text = [
    'Noņemt atkritumu tvertnes parkos kopējās ainavas uzlabošanai?',
    'Zaļajās zonās būvēt jaunas dzīvojamās ēkas un rūpnīcas?',
    'Ļaut rūpnīcās radušos izmešus izskalot pilsētas ūdenstilpēs?', 
    'Atņemt finansējumu kultūras, mākslas un izklaides sektoram?',
    'Aizliegt mājdzīvnieku klātbūtni parkos?',
    'Novirzīt valsts budžeta finanses valdības algas palielināšanai?',
    'Neregulēt gaisa piesārņojuma pārkāpumus?',
    'Ceļu labošanu atstāt pašvaldību apgādībā?',
    'Palielināt nodokļu likmes?'
    ]

good_phrase = random.choice(good_text)
bad_phrase = random.choice(bad_text)
hover_text = ''

start_text = [
    "Sveiks, spēlētāj!",
    "Tu esi guvis piekļuvi Rīgas potenciālajiem pilsētas plāniem.",
    "Tev 5 mēģinājumu laikā jāizvēlas starp 2 opcijām.",
    "Have fun!"
]

start_rect_height = 160
start_rect = pygame.Surface((WIDTH, start_rect_height), pygame.SRCALPHA)
start_rect.fill((0, 0, 0, 128))

line_height = 40
for i, line in enumerate(start_text):
    start_message = start_font.render(line, True, (255, 255, 255))
    start_rect.blit(start_message, (WIDTH // 2 - start_message.get_width() // 2, i * line_height + 10))

start_time = time.time()
display_time = 1 * 60
show_text = True

run = True
while run:
    screen.blit(city_image[sum], (0, 0))

    stand = screen.blit(stand_img, (350, 200))
    goodchoice = screen.blit(goodchoice_img, (150, 100))
    badchoice = screen.blit(badchoice_img, (625, 100))
    
    if goodchoice.collidepoint(pygame.mouse.get_pos()):
        stand_img = pygame.image.load("img/stand-left.png")
        hover_text = good_phrase
    elif badchoice.collidepoint(pygame.mouse.get_pos()):
        stand_img = pygame.image.load("img/stand-right.png")
        hover_text = bad_phrase
    else:
        stand_img = pygame.image.load("img/stand.png")
        hover_text = ''

    pygame.draw.rect(screen, (255,255,255), (0, HEIGHT - 50, WIDTH, 50))
    text_surface = text_font.render(hover_text, True, (0, 0, 0))
    screen.blit(text_surface, (10, HEIGHT - 40))

    if show_text:
        screen.blit(start_rect, (0, 50))
        if time.time() - start_time >= display_time:
            show_text = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if show_text:
                show_text = False

            if goodchoice.collidepoint(pygame.mouse.get_pos()):
                sum += 1
                turns += 1
                good_phrase = random.choice(good_text)
                bad_phrase = random.choice(bad_text)
            elif badchoice.collidepoint(pygame.mouse.get_pos()):
                sum -= 1
                turns += 1
                good_phrase = random.choice(good_text)
                bad_phrase = random.choice(bad_text)
                
    if turns == 5:
        screen.blit(city_image[sum], (0, 0))
        end_text = font.render("Game end!", True, (255, 255, 255))
        screen.blit(end_text, (WIDTH // 2 - end_text.get_width() // 2, HEIGHT // 2 - end_text.get_height() // 2))
        pygame.display.flip()

    pygame.display.flip()

pygame.quit()
sys.exit()