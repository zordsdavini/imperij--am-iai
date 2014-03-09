# -*- coding: utf-8 -*-

from guilib import *
import pygame
from pygame.locals import *
import math


def main():
    pygame.init()

    # Window
    display_flags = DOUBLEBUF #FULLSCREEN  #DOUBLEBUF
    width, height = 1366, 768

    pygame.display.set_mode((width, height), display_flags)
    pygame.display.set_caption(u'Imperiju amzius!')
    screen = pygame.display.get_surface()

    gs = GameSettings() # main game settings
    
    while gs.een:
        stage = gs.get_stage()
        eval(stage+'(screen, gs)')
        pygame.display.flip()



def start(screen, gs):
    bgcolor = pygame.Surface(screen.get_size())
    bgcolor = bgcolor.convert()
    bgcolor.fill((235, 235, 155))
    screen.blit(bgcolor, (0, 0))

    txt = u'Imperijų amžius!'
    fonts = pygame.font.Font(None, 72)
    a = fonts.render(txt, True, (0, 0, 0))
    screen.blit(a, (470, 30))

    img = pygame.image.load("images/menu.png")
    screen.blit(img, (383, 110))

    mygt(screen, 575, 350, 215, 50, u'Pradėti', gs)
    mygt(screen, 575, 410, 215, 50, u'Užkrauti', gs)
    mygt(screen, 575, 470, 215, 50, u'Nustatymai', gs)
    mygt(screen, 575, 530, 215, 50, u'Šalys', gs)
    mygt(screen, 575, 590, 215, 50, u'Žemėlapiai', gs)
    mygt(screen, 575, 650, 215, 50, u'Išeiti', gs)

    # Inputs
    events = pygame.event.get()
    for event in events:
        if event.type == MOUSEBUTTONUP and event.button == 1:
            x_m, y_m = event.pos

            if (x_m > 575 and x_m < 790):
                if (y_m > 350 and y_m < 400):
                    gs.set_stage('new')
                    pygame.mouse.set_cursor(*pygame.cursors.arrow)

                if (y_m > 410 and y_m < 460):
                    gs.set_stage('load')
                    pygame.mouse.set_cursor(*pygame.cursors.arrow)

                if (y_m > 470 and y_m < 520):
                    gs.set_stage('settings')
                    pygame.mouse.set_cursor(*pygame.cursors.arrow)

                if (y_m > 530 and y_m < 580):
                    gs.set_stage('countries')
                    pygame.mouse.set_cursor(*pygame.cursors.arrow)

                if (y_m > 590 and y_m < 640):
                    gs.set_stage('maps')
                    pygame.mouse.set_cursor(*pygame.cursors.arrow)

                if (y_m > 650 and y_m < 700):
                    gs.set_stage('exit')
                    pygame.mouse.set_cursor(*pygame.cursors.arrow)



def exit(screen, gs):
    gs.quit_game()



def countries(screen, gs):
    bgcolor = pygame.Surface(screen.get_size())
    bgcolor = bgcolor.convert()
    bgcolor.fill((235, 235, 155))
    screen.blit(bgcolor, (0, 0))

    txt1 = u'Imperijų amžius!'
    fonts = pygame.font.Font(None, 72)
    a = fonts.render(txt1, True, (0, 0, 0))
    screen.blit(a, (470, 30))

    mygt(screen, 1140, 30, 215, 50, u'Atgal', gs)
    mygt(screen, 1140, 90, 215, 50, u'Nauja šalis', gs)

    start_y = 100
    age = 'XIX'
    for short in gs.countries:
        country = gs.countries[short]

        fonts = pygame.font.Font(None, 36)
        a = fonts.render(country.name, True, (0, 0, 0))
        screen.blit(a, (30, start_y))

        pygame.draw.rect(screen, country.color, (200, start_y, 20, 20), 0)

        start_x = 400
        for img in country.ages[age]:
            img_load = pygame.image.load(img)
            screen.blit(img_load, (start_x, start_y))
            start_x += 150

        mygt(screen, 800, start_y, 215, 50, u'Keisti', gs)

        start_y += 100


    # Inputs
    events = pygame.event.get()
    for event in events:
        if event.type == MOUSEBUTTONUP and event.button == 1:
            x_m, y_m = event.pos

            if (x_m > 1140 and x_m < 1355):
                if (y_m > 30 and y_m < 80):
                    gs.set_stage('start')
                    pygame.mouse.set_cursor(*pygame.cursors.arrow)

                if (y_m > 90 and y_m < 130):
                    gs.set_stage('new_country')
                    pygame.mouse.set_cursor(*pygame.cursors.arrow)


def maps(screen, gs):
    bgcolor = pygame.Surface(screen.get_size())
    bgcolor = bgcolor.convert()
    bgcolor.fill((235, 235, 155))
    screen.blit(bgcolor, (0, 0))

    txt1 = u'Imperijų amžius!'
    fonts = pygame.font.Font(None, 72)
    a = fonts.render(txt1, True, (0, 0, 0))
    screen.blit(a, (470, 30))

    mygt(screen, 1140, 30, 215, 50, u'Atgal', gs)
    mygt(screen, 1140, 90, 215, 50, u'Naujas žemėlapis', gs)

    start_y = 100
    age = 'XIX'
    for map_name in gs.maps:
        fonts = pygame.font.Font(None, 36)
        a = fonts.render(map_name, True, (0, 0, 0))
        screen.blit(a, (30, start_y))

        mygt(screen, 800, start_y, 215, 50, u'Keisti', gs)

        start_y += 100

    # Inputs
    events = pygame.event.get()
    for event in events:
        if event.type == MOUSEBUTTONUP and event.button == 1:
            x_m, y_m = event.pos

            if (x_m > 1140 and x_m < 1355):
                if (y_m > 30 and y_m < 80):
                    gs.set_stage('start')
                    pygame.mouse.set_cursor(*pygame.cursors.arrow)

                if (y_m > 90 and y_m < 130):
                    gs.set_stage('new_map')
                    pygame.mouse.set_cursor(*pygame.cursors.arrow)



def new_map(screen, gs):
    fonts18 = pygame.font.Font(None, 18)
    fonts24 = pygame.font.Font(None, 24)

    bgcolor = pygame.Surface(screen.get_size())
    bgcolor = bgcolor.convert()
    bgcolor.fill((235, 235, 155))
    screen.blit(bgcolor, (0, 0))

    mygt(screen, 1140, 30, 215, 50, u'Atgal', gs)
    mygt(screen, 1140, 90, 215, 50, u'Saugoti', gs)

    pygame.draw.rect(screen, (250, 250, 250), (10, 10, 1120, 720), 0)
    for border in gs.new_map['borders']:
        pos_old = None
        for pos in border:
            if (pos_old):
                pygame.draw.aaline(screen, (0, 0, 0),
                        (pos_old[0], pos_old[1]),
                        (pos[0], pos[1]), 1)
            pos_old = pos

    if gs.map_editor['tool'] == 'border' and gs.map_editor['action'] == 'stroke':
        pos_old = None
        for pos in gs.map_editor['tmp']:
            if (pos_old):
                pygame.draw.aaline(screen, (0, 0, 0),
                        (pos_old[0], pos_old[1]),
                        (pos[0], pos[1]), 1)
            pos_old = pos

    for pos in gs.new_map['capitals']:
        pygame.draw.circle(screen, (0, 0, 0), pos, 10)

    for country_short in gs.new_map['countries']:
        country = gs.get_country(country_short)
        for i, land in enumerate(gs.new_map['countries'][country_short]):
            a = fonts18.render('%i: %s' % (i, country.name), True, country.color)
            screen.blit(a, (land[0]+12, land[1]+12))


    # editor tools
    start_y = 160
    for tool in gs.map_editor_tools:
        color = (0, 0, 0)
        if tool == gs.map_editor['tool']:
            color = (255, 0, 0)

        a = fonts24.render(gs.map_editor_tools[tool], True, color)
        screen.blit(a, (1140, start_y))
        start_y += 30
    
    start_y = 350
    for country_sh in gs.countries:
        country = gs.countries[country_sh]
        color = (0, 0, 0)
        if country_sh == gs.map_editor['country']:
            color = (255, 0, 0)

        a = fonts18.render(country.name, True, color)
        screen.blit(a, (1140, start_y))

        pygame.draw.rect(screen, country.color, (1230, start_y, 20, 20), 0)

        start_y += 30

    # Inputs
    events = pygame.event.get()
    for event in events:
        if event.type == MOUSEBUTTONUP and event.button == 1:
            x_m, y_m = event.pos

            if (x_m > 1140 and x_m < 1355):
                if (y_m > 30 and y_m < 80):
                    gs.set_stage('maps')
                    pygame.mouse.set_cursor(*pygame.cursors.arrow)

                if (y_m > 90 and y_m < 130):
                    gs.set_stage('save_map')
                    pygame.mouse.set_cursor(*pygame.cursors.arrow)

            # tools
            if (x_m > 1140 and x_m < 1350):
                start_y = 160
                for tool in gs.map_editor_tools:
                    if (y_m > start_y and y_m < start_y + 30):
                        if tool == 'undo':
                            if gs.map_editor['tool'] == 'border':
                                if len(gs.map_editor['tmp']) > 0:
                                    gs.map_editor['tmp'].pop()
                                elif len(gs.new_map['borders']) > 0:
                                    gs.new_map['borders'].pop()
                            elif gs.map_editor['tool'] == 'capital' and len(gs.new_map['capitals']) > 0:
                                gs.new_map['capitals'].pop()
                            elif gs.map_editor['tool'] == 'country' and len(gs.new_map['countries']) > 0:
                                if gs.map_editor['country'] in gs.new_map['countries']:
                                    if len(gs.new_map['countries'][gs.map_editor['country']]) > 0:
                                        gs.new_map['countries'][gs.map_editor['country']].pop()
                                         
                        else:
                            gs.map_editor['tool'] = tool
                    start_y += 30    

            # countries
            if (x_m > 1140 and x_m < 1350):
                start_y = 350
                for country in gs.countries:
                    if (y_m > start_y and y_m < start_y + 30):
                        gs.map_editor['country'] = country
                    start_y += 30    

            if (x_m > 10 and x_m < 1120 and y_m > 10 and y_m < 720):
                if gs.map_editor['tool'] == 'border' and gs.map_editor['action'] == 'stroke':
                    gs.map_editor['tmp'].append((x_m, y_m))

                    gs.map_editor['x'] = x_m
                    gs.map_editor['y'] = y_m

                if gs.map_editor['tool'] == 'border' and not gs.map_editor['action'] == 'stroke':
                    gs.map_editor['action'] = 'stroke'
                    gs.map_editor['tmp'] = []
                    gs.map_editor['tmp'].append((x_m, y_m))
                    gs.map_editor['x'] = x_m
                    gs.map_editor['y'] = y_m

            if (x_m > 10 and x_m < 1120 and y_m > 10 and y_m < 720):
                if gs.map_editor['tool'] == 'capital':
                    gs.new_map['capitals'].append((x_m, y_m))
                    if gs.map_editor['country']:
                        if not gs.map_editor['country'] in gs.new_map['countries']:
                            gs.new_map['countries'][gs.map_editor['country']] = []
                        gs.new_map['countries'][gs.map_editor['country']].append((x_m, y_m))
                        
            if (x_m > 10 and x_m < 1120 and y_m > 10 and y_m < 720):
                if gs.map_editor['tool'] == 'country':
                    pass # not implemented

        if event.type == MOUSEBUTTONUP and event.button == 3:
            x_m, y_m = event.pos

            if (x_m > 10 and x_m < 1120 and y_m > 10 and y_m < 720):
                if gs.map_editor['tool'] == 'border' and gs.map_editor['action'] == 'stroke':
                    gs.map_editor['action'] = None
                    gs.new_map['borders'].append(gs.map_editor['tmp'])
                    gs.map_editor['tmp'] = []

        if event.type == MOUSEMOTION:
            x_m, y_m = event.pos

            if (x_m > 10 and x_m < 1120 and y_m > 10 and y_m < 720):
                if gs.map_editor['tool'] == 'border' and gs.map_editor['action'] == 'stroke':

                    pygame.draw.aaline(screen, (0, 0, 0),
                            (gs.map_editor['x'], gs.map_editor['y']),
                            (x_m, y_m), 1)



def save_map(screen, gs):
    bgcolor = pygame.Surface(screen.get_size())
    bgcolor = bgcolor.convert()
    bgcolor.fill((235, 235, 155))
    screen.blit(bgcolor, (0, 0))

    txt1 = u'Imperijų amžius!'
    fonts = pygame.font.Font(None, 72)
    a = fonts.render(txt1, True, (0, 0, 0))
    screen.blit(a, (470, 30))

    mygt(screen, 1140, 30, 215, 50, u'Atgal', gs)
    mygt(screen, 1140, 90, 215, 50, u'Patvirtinti', gs)

    fonts36 = pygame.font.Font(None, 36)
    fonts24 = pygame.font.Font(None, 24)

    a = fonts36.render(u'Pavadinimas', True, (0, 0, 0))
    screen.blit(a, (30, 140))
    pygame.draw.rect(screen, (250, 250, 250), (30, 190, 400, 30), 0)
    if gs.editor['in_progress']:
        editor_word = gs.editor['word'][:gs.editor['cursor']]+'|'+gs.editor['word'][gs.editor['cursor']:]
    else:
        editor_word = gs.editor['word']

    a = fonts24.render(editor_word, True, (0, 0, 0))
    screen.blit(a, (35, 195))

    a = fonts36.render(u'Amžius', True, (0, 0, 0))
    screen.blit(a, (30, 240))
    start_x = 35
    for age in gs.ages:
        color = (0, 0, 0)
        if age == gs.settings['age']:
            color = (255, 0, 0)

        a = fonts24.render(age, True, color)
        screen.blit(a, (start_x, 290))
        start_x += 50

    if len(gs.errors) > 0:
        start_y = 400
        for error in gs.errors:
            a = fonts36.render(error, True, (255, 0, 0))
            screen.blit(a, (100, start_y))
            start_y += 50

    # Inputs
    events = pygame.event.get()
    for event in events:
        if event.type == MOUSEBUTTONUP and event.button == 1:
            x_m, y_m = event.pos

            if (x_m > 1140 and x_m < 1355):
                if (y_m > 30 and y_m < 80):
                    gs.set_stage('start')
                    pygame.mouse.set_cursor(*pygame.cursors.arrow)

                if (y_m > 90 and y_m < 130):
                    gs.errors = []
                    if len(gs.editor['word']) == 0:
                        gs.errors.append(u'Nenurodytas žemėlapio pavadinimas!!!')
                    else:
                        gs.save_new_map()
                        gs.set_stage('maps')
                        pygame.mouse.set_cursor(*pygame.cursors.arrow)

            # ages
            if (y_m > 290 and y_m < 335):
                start_x = 35
                for age in gs.ages:
                    if (x_m > start_x and x_m < start_x + 50):
                        gs.settings['age'] = age
                    start_x += 50    

            if (x_m > 30 and x_m < 430 and y_m > 190 and y_m < 220):
                gs.editor['in_progress'] = True


        if gs.editor['in_progress']:
            if event.type == KEYDOWN and event.key in [K_LEFT] and gs.editor['cursor'] > 0:
                gs.editor['cursor'] -= 1

            if event.type == KEYDOWN and event.key in [K_RIGHT] and gs.editor['cursor'] < len(gs.editor['word']):
                gs.editor['cursor'] += 1

            if event.type == KEYDOWN and event.key in [K_q]:
                gs.editor['word'] = gs.editor['word'][:gs.editor['cursor']]+'q'+gs.editor['word'][gs.editor['cursor']:]
                gs.editor['cursor'] += 1

            if event.type == KEYDOWN and event.key in [K_w]:
                gs.editor['word'] = gs.editor['word'][:gs.editor['cursor']]+'w'+gs.editor['word'][gs.editor['cursor']:]
                gs.editor['cursor'] += 1

            if event.type == KEYDOWN and event.key in [K_e]:
                gs.editor['word'] = gs.editor['word'][:gs.editor['cursor']]+'e'+gs.editor['word'][gs.editor['cursor']:]
                gs.editor['cursor'] += 1

            if event.type == KEYDOWN and event.key in [K_r]:
                gs.editor['word'] = gs.editor['word'][:gs.editor['cursor']]+'r'+gs.editor['word'][gs.editor['cursor']:]
                gs.editor['cursor'] += 1

            if event.type == KEYDOWN and event.key in [K_t]:
                gs.editor['word'] = gs.editor['word'][:gs.editor['cursor']]+'t'+gs.editor['word'][gs.editor['cursor']:]
                gs.editor['cursor'] += 1

            if event.type == KEYDOWN and event.key in [K_y]:
                gs.editor['word'] = gs.editor['word'][:gs.editor['cursor']]+'y'+gs.editor['word'][gs.editor['cursor']:]
                gs.editor['cursor'] += 1

            if event.type == KEYDOWN and event.key in [K_u]:
                gs.editor['word'] = gs.editor['word'][:gs.editor['cursor']]+'u'+gs.editor['word'][gs.editor['cursor']:]
                gs.editor['cursor'] += 1

            if event.type == KEYDOWN and event.key in [K_i]:
                gs.editor['word'] = gs.editor['word'][:gs.editor['cursor']]+'i'+gs.editor['word'][gs.editor['cursor']:]
                gs.editor['cursor'] += 1

            if event.type == KEYDOWN and event.key in [K_o]:
                gs.editor['word'] = gs.editor['word'][:gs.editor['cursor']]+'o'+gs.editor['word'][gs.editor['cursor']:]
                gs.editor['cursor'] += 1

            if event.type == KEYDOWN and event.key in [K_p]:
                gs.editor['word'] = gs.editor['word'][:gs.editor['cursor']]+'p'+gs.editor['word'][gs.editor['cursor']:]
                gs.editor['cursor'] += 1

            if event.type == KEYDOWN and event.key in [K_a]:
                gs.editor['word'] = gs.editor['word'][:gs.editor['cursor']]+'a'+gs.editor['word'][gs.editor['cursor']:]
                gs.editor['cursor'] += 1

            if event.type == KEYDOWN and event.key in [K_s]:
                gs.editor['word'] = gs.editor['word'][:gs.editor['cursor']]+'s'+gs.editor['word'][gs.editor['cursor']:]
                gs.editor['cursor'] += 1

            if event.type == KEYDOWN and event.key in [K_d]:
                gs.editor['word'] = gs.editor['word'][:gs.editor['cursor']]+'d'+gs.editor['word'][gs.editor['cursor']:]
                gs.editor['cursor'] += 1

            if event.type == KEYDOWN and event.key in [K_f]:
                gs.editor['word'] = gs.editor['word'][:gs.editor['cursor']]+'f'+gs.editor['word'][gs.editor['cursor']:]
                gs.editor['cursor'] += 1

            if event.type == KEYDOWN and event.key in [K_g]:
                gs.editor['word'] = gs.editor['word'][:gs.editor['cursor']]+'g'+gs.editor['word'][gs.editor['cursor']:]
                gs.editor['cursor'] += 1

            if event.type == KEYDOWN and event.key in [K_h]:
                gs.editor['word'] = gs.editor['word'][:gs.editor['cursor']]+'h'+gs.editor['word'][gs.editor['cursor']:]
                gs.editor['cursor'] += 1

            if event.type == KEYDOWN and event.key in [K_j]:
                gs.editor['word'] = gs.editor['word'][:gs.editor['cursor']]+'j'+gs.editor['word'][gs.editor['cursor']:]
                gs.editor['cursor'] += 1

            if event.type == KEYDOWN and event.key in [K_k]:
                gs.editor['word'] = gs.editor['word'][:gs.editor['cursor']]+'k'+gs.editor['word'][gs.editor['cursor']:]
                gs.editor['cursor'] += 1

            if event.type == KEYDOWN and event.key in [K_l]:
                gs.editor['word'] = gs.editor['word'][:gs.editor['cursor']]+'l'+gs.editor['word'][gs.editor['cursor']:]
                gs.editor['cursor'] += 1

            if event.type == KEYDOWN and event.key in [K_z]:
                gs.editor['word'] = gs.editor['word'][:gs.editor['cursor']]+'z'+gs.editor['word'][gs.editor['cursor']:]
                gs.editor['cursor'] += 1

            if event.type == KEYDOWN and event.key in [K_x]:
                gs.editor['word'] = gs.editor['word'][:gs.editor['cursor']]+'x'+gs.editor['word'][gs.editor['cursor']:]
                gs.editor['cursor'] += 1

            if event.type == KEYDOWN and event.key in [K_c]:
                gs.editor['word'] = gs.editor['word'][:gs.editor['cursor']]+'c'+gs.editor['word'][gs.editor['cursor']:]
                gs.editor['cursor'] += 1

            if event.type == KEYDOWN and event.key in [K_v]:
                gs.editor['word'] = gs.editor['word'][:gs.editor['cursor']]+'v'+gs.editor['word'][gs.editor['cursor']:]
                gs.editor['cursor'] += 1

            if event.type == KEYDOWN and event.key in [K_b]:
                gs.editor['word'] = gs.editor['word'][:gs.editor['cursor']]+'b'+gs.editor['word'][gs.editor['cursor']:]
                gs.editor['cursor'] += 1

            if event.type == KEYDOWN and event.key in [K_n]:
                gs.editor['word'] = gs.editor['word'][:gs.editor['cursor']]+'n'+gs.editor['word'][gs.editor['cursor']:]
                gs.editor['cursor'] += 1

            if event.type == KEYDOWN and event.key in [K_m]:
                gs.editor['word'] = gs.editor['word'][:gs.editor['cursor']]+'m'+gs.editor['word'][gs.editor['cursor']:]
                gs.editor['cursor'] += 1

            if event.type == KEYDOWN and event.key in [K_0]:
                gs.editor['word'] = gs.editor['word'][:gs.editor['cursor']]+'0'+gs.editor['word'][gs.editor['cursor']:]
                gs.editor['cursor'] += 1

            if event.type == KEYDOWN and event.key in [K_1]:
                gs.editor['word'] = gs.editor['word'][:gs.editor['cursor']]+'1'+gs.editor['word'][gs.editor['cursor']:]
                gs.editor['cursor'] += 1

            if event.type == KEYDOWN and event.key in [K_2]:
                gs.editor['word'] = gs.editor['word'][:gs.editor['cursor']]+'2'+gs.editor['word'][gs.editor['cursor']:]
                gs.editor['cursor'] += 1

            if event.type == KEYDOWN and event.key in [K_3]:
                gs.editor['word'] = gs.editor['word'][:gs.editor['cursor']]+'3'+gs.editor['word'][gs.editor['cursor']:]
                gs.editor['cursor'] += 1

            if event.type == KEYDOWN and event.key in [K_4]:
                gs.editor['word'] = gs.editor['word'][:gs.editor['cursor']]+'4'+gs.editor['word'][gs.editor['cursor']:]
                gs.editor['cursor'] += 1

            if event.type == KEYDOWN and event.key in [K_5]:
                gs.editor['word'] = gs.editor['word'][:gs.editor['cursor']]+'5'+gs.editor['word'][gs.editor['cursor']:]
                gs.editor['cursor'] += 1

            if event.type == KEYDOWN and event.key in [K_6]:
                gs.editor['word'] = gs.editor['word'][:gs.editor['cursor']]+'6'+gs.editor['word'][gs.editor['cursor']:]
                gs.editor['cursor'] += 1

            if event.type == KEYDOWN and event.key in [K_7]:
                gs.editor['word'] = gs.editor['word'][:gs.editor['cursor']]+'7'+gs.editor['word'][gs.editor['cursor']:]
                gs.editor['cursor'] += 1

            if event.type == KEYDOWN and event.key in [K_8]:
                gs.editor['word'] = gs.editor['word'][:gs.editor['cursor']]+'8'+gs.editor['word'][gs.editor['cursor']:]
                gs.editor['cursor'] += 1

            if event.type == KEYDOWN and event.key in [K_9]:
                gs.editor['word'] = gs.editor['word'][:gs.editor['cursor']]+'9'+gs.editor['word'][gs.editor['cursor']:]
                gs.editor['cursor'] += 1

            if event.type == KEYDOWN and event.key in [K_DELETE]:
                gs.editor['word'] = gs.editor['word'][:gs.editor['cursor']]+gs.editor['word'][gs.editor['cursor']+1:]

            if event.type == KEYDOWN and event.key in [K_SPACE]:
                gs.editor['word'] = gs.editor['word'][:gs.editor['cursor']]+' '+gs.editor['word'][gs.editor['cursor']:]
                gs.editor['cursor'] += 1

            if event.type == KEYDOWN and event.key in [K_BACKSPACE] and gs.editor['cursor'] > 0:
                gs.editor['word'] = gs.editor['word'][:gs.editor['cursor']-1]+gs.editor['word'][gs.editor['cursor']+1:]
                gs.editor['cursor'] -= 1


def new(screen, gs):
    bgcolor = pygame.Surface(screen.get_size())
    bgcolor = bgcolor.convert()
    bgcolor.fill((235, 235, 155))
    screen.blit(bgcolor, (0, 0))

    txt1 = u'Imperijų amžius!'
    fonts = pygame.font.Font(None, 72)
    a = fonts.render(txt1, True, (0, 0, 0))
    screen.blit(a, (470, 30))

    mygt(screen, 1140, 30, 215, 50, u'Atgal', gs)
    mygt(screen, 1140, 90, 215, 50, u'Pradėti', gs)

    fonts36 = pygame.font.Font(None, 36)
    fonts24 = pygame.font.Font(None, 24)

    a = fonts36.render(u'Amžius', True, (0, 0, 0))
    screen.blit(a, (30, 140))
    start_x = 35
    for age in gs.ages:
        color = (0, 0, 0)
        if age == gs.settings['age']:
            color = (255, 0, 0)

        a = fonts24.render(age, True, color)
        screen.blit(a, (start_x, 190))
        start_x += 50

    pygame.draw.aaline(screen, (0, 0, 0), (10, 230), (300, 230), 2)

    a = fonts36.render(u'Žemėlapis', True, (0, 0, 0))
    screen.blit(a, (30, 250))
    start_y = 290
    for map_name in gs.maps:
        color = (0, 0, 0)
        if map_name == gs.settings['map']:
            color = (255, 0, 0)

        a = fonts24.render(map_name, True, color)
        screen.blit(a, (30, start_y))
        start_y += 30

    pygame.draw.aaline(screen, (0, 0, 0), (10, 430), (300, 430), 2)

    a = fonts36.render(u'Šalis', True, (0, 0, 0))
    screen.blit(a, (30, 450))
    start_y = 490
    for country_sh in gs.countries:
        country = gs.countries[country_sh]
        color = (0, 0, 0)
        if country_sh == gs.settings['country']:
            color = (255, 0, 0)

        a = fonts24.render(country.name, True, color)
        screen.blit(a, (30, start_y))

        pygame.draw.rect(screen, country.color, (200, start_y, 20, 20), 0)

        start_y += 30

    if len(gs.errors) > 0:
        start_y = 400
        for error in gs.errors:
            a = fonts36.render(error, True, (255, 0, 0))
            screen.blit(a, (400, start_y))
            start_y += 50

    # Inputs
    events = pygame.event.get()
    for event in events:
        if event.type == MOUSEBUTTONUP and event.button == 1:
            x_m, y_m = event.pos

            if (x_m > 1140 and x_m < 1355):
                if (y_m > 30 and y_m < 80):
                    gs.set_stage('start')
                    pygame.mouse.set_cursor(*pygame.cursors.arrow)

                if (y_m > 90 and y_m < 130):
                    gs.errors = []
                    if not gs.settings['age'] or not gs.settings['country'] or not gs.settings['map']:
                        gs.errors.append(u'Amžius, žemėlapis ir šalis turi būti pasirinktas!!!')

                    else:
                        gs.game['age'] = gs.settings['age']
                        gs.game['map'] = gs.maps[gs.settings['map']].map
                        gs.game['turn'] += 1
                        gs.game['stage'] = 'get'
                        gs.game['users'].append(gs.settings['country']) #1st user is real
                        for country in gs.game['map']:
                            if not country in gs.game['users']:
                                gs.game['users'].append(country)

                        gs.set_stage('play')

                    pygame.mouse.set_cursor(*pygame.cursors.arrow)

            # ages
            if (y_m > 185 and y_m < 230):
                start_x = 35
                for age in gs.ages:
                    if (x_m > start_x and x_m < start_x + 50):
                        gs.settings['age'] = age
                    start_x += 50    

            # maps
            if (x_m > 30 and x_m < 290):
                start_y = 290
                for map_name in gs.maps:
                    if (y_m > start_y and y_m < start_y + 30):
                        gs.settings['map'] = map_name
                    start_y += 30    

            # countries
            if (x_m > 30 and x_m < 290):
                start_y = 490
                for country in gs.countries:
                    if (y_m > start_y and y_m < start_y + 30):
                        gs.settings['country'] = country
                    start_y += 30    


def play(screen, gs):
    fonts18 = pygame.font.Font(None, 18)
    fonts24 = pygame.font.Font(None, 24)
    fonts72 = pygame.font.Font(None, 72)

    if gs.game['stage'] == 'get':
        for country in gs.game['map']:
            for i, land in enumerate(gs.game['map'][country]):
                if not 'army' in land:
                    gs.game['map'][country][i]['army'] = {
                            'pst': 0,
                            'ark': 0,
                            'ptr': 0
                            }

                gs.game['map'][country][i]['army']['pst'] += 20
                gs.game['map'][country][i]['army']['ark'] += 5
                gs.game['map'][country][i]['army']['ptr'] += 1

        gs.game['stage'] = 0

    bgcolor = pygame.Surface(screen.get_size())
    bgcolor = bgcolor.convert()
    bgcolor.fill((235, 235, 155))
    screen.blit(bgcolor, (0, 0))

    mygt(screen, 1140, 30, 215, 50, u'Ėjimas baigtas', gs)
    mygt(screen, 1140, 90, 215, 50, u'Meniu', gs)

    pygame.draw.rect(screen, (63, 125, 143), (10, 10, 1120, 720), 0)

    lefts = dict()
    for country in gs.game['map']:
        for land in gs.game['map'][country]:
            lefts[country] = ''
            pygame.draw.polygon(screen, land['color'], land['border'])

            pos_old = None
            for pos in land['border']:
                if (pos_old):
                    pygame.draw.line(screen, (0, 0, 0),
                            (pos_old[0], pos_old[1]),
                            (pos[0], pos[1]), 5)
                pos_old = pos

            pygame.draw.circle(screen, (0, 0, 0), land['capital'], 10)

            army_text = '%i | %i | %i' % (land['army']['pst'], land['army']['ark'], land['army']['ptr'])
            a = fonts18.render(army_text, True, (0, 0, 0))
            screen.blit(a, (land['capital'][0]+12, land['capital'][1]+12))

    victory = False
    if (len(lefts) == 1):
        victory = True
        victory_country = gs.get_country(lefts.keys()[0])
        a = fonts72.render(u'%s laimėjo' % victory_country.name, True, (0, 0, 0))
        screen.blit(a, (300, 300))


    a = fonts24.render(u'Ėjimas: %i' % gs.game['turn'], True, (0, 0, 0))
    screen.blit(a, (1140, 160))

    start_y = 200
    for i, country_sh in enumerate(gs.game['users']):
        country = gs.countries[country_sh]
        color = (0, 0, 0)
        if i == gs.game['stage']:
            color = (255, 0, 0)

        a = fonts24.render(country.name, True, color)
        screen.blit(a, (1140, start_y))

        pygame.draw.rect(screen, country.color, (1230, start_y, 20, 20), 0)

        start_y += 30

    # Inputs
    events = pygame.event.get()
    for event in events:
        if event.type == MOUSEBUTTONUP and event.button == 1:
            x_m, y_m = event.pos

            if (x_m > 1140 and x_m < 1355):
                if not victory and (y_m > 30 and y_m < 80): # and gs.game['stage'] == 0):
                    if (len(gs.game['users']) == gs.game['stage'] + 1):
                        gs.game['stage'] = 'get'
                    else:
                        gs.game['stage'] += 1

                    pygame.mouse.set_cursor(*pygame.cursors.arrow)

                if (y_m > 90 and y_m < 130):
                    gs.set_stage('menu')
                    pygame.mouse.set_cursor(*pygame.cursors.arrow)

            if (x_m > 10 and x_m < 1120 and y_m > 10 and y_m < 720):
                country, land = gs.get_country_land_from_capital(x_m, y_m)
                if country and country == gs.game['users'][gs.game['stage']]:
                    gs.game['fight_from'] = land['capital']
                elif country and gs.game['fight_from']:
                    gs.game['fight_to'] = land['capital']
                    gs.set_stage('prepare_fight')

        if event.type == MOUSEMOTION:
            x_m, y_m = event.pos

            if (x_m > 10 and x_m < 1120 and y_m > 10 and y_m < 720):
                if gs.game['fight_from']:
                    pygame.draw.line(screen, (255, 0, 0), (gs.game['fight_from'][0], gs.game['fight_from'][1]), (x_m, y_m), 5)
                    pygame.draw.aaline(screen, (0, 0, 0), (gs.game['fight_from'][0], gs.game['fight_from'][1]), (x_m, y_m), 1)


def prepare_fight(screen, gs):
    fonts18 = pygame.font.Font(None, 18)
    fonts24 = pygame.font.Font(None, 24)
    fonts72 = pygame.font.Font(None, 72)

    bgcolor = pygame.Surface(screen.get_size())
    bgcolor = bgcolor.convert()
    bgcolor.fill((235, 235, 155))
    screen.blit(bgcolor, (0, 0))

    mygt(screen, 1140, 30, 215, 50, u'Kovoti', gs)
    mygt(screen, 1140, 90, 215, 50, u'Nutraukti puolimą', gs)

    country, land = gs.get_country_land_from_capital(gs.game['fight_from'][0], gs.game['fight_from'][1])
    country = gs.get_country(country)

    img = country.ages[gs.settings['age']][0]
    img_load = pygame.image.load(img)
    screen.blit(img_load, (50, 100))

    a = fonts72.render(str(land['army']['pst'] - gs.game['fight_pst']), True, (0, 0, 0))
    screen.blit(a, (250, 120))

    mygt(screen, 400, 120, 50, 50, '<<<', gs)
    mygt(screen, 500, 120, 50, 50, '>>>', gs)

    a = fonts72.render(str(gs.game['fight_pst']), True, (0, 0, 0))
    screen.blit(a, (650, 120))

    img = country.ages[gs.settings['age']][1]
    img_load = pygame.image.load(img)
    screen.blit(img_load, (50, 250))

    a = fonts72.render(str(land['army']['ark'] - gs.game['fight_ark']), True, (0, 0, 0))
    screen.blit(a, (250, 270))

    mygt(screen, 400, 270, 50, 50, '<<<', gs)
    mygt(screen, 500, 270, 50, 50, '>>>', gs)

    a = fonts72.render(str(gs.game['fight_ark']), True, (0, 0, 0))
    screen.blit(a, (650, 270))

    img = country.ages[gs.settings['age']][2]
    img_load = pygame.image.load(img)
    screen.blit(img_load, (50, 400))

    a = fonts72.render(str(land['army']['ptr'] - gs.game['fight_ptr']), True, (0, 0, 0))
    screen.blit(a, (250, 420))

    mygt(screen, 400, 420, 50, 50, '<<<', gs)
    mygt(screen, 500, 420, 50, 50, '>>>', gs)

    a = fonts72.render(str(gs.game['fight_ptr']), True, (0, 0, 0))
    screen.blit(a, (650, 420))

    # Inputs
    events = pygame.event.get()
    for event in events:
        if event.type == MOUSEBUTTONUP and event.button == 1:
            x_m, y_m = event.pos

            if (x_m > 1140 and x_m < 1355):
                if (y_m > 30 and y_m < 80): # and gs.game['stage'] == 0):
                    gs.set_stage('fight')
                    gs.fight['action'] = 'moving'
                    gs.fight['fields'] = []
                    for i in range(54):
                        gs.fight['fields'].append([])
                        for j in range(9):
                            gs.fight['fields'][i].append('')

                    gs.fight['units'] = []

                    land['army']['pst'] -= gs.game['fight_pst']
                    land['army']['ark'] -= gs.game['fight_ark']
                    land['army']['ptr'] -= gs.game['fight_ptr']
                    for i in range(gs.game['fight_pst']):
                        gs.fight['units'].append({
                            'id': len(gs.fight['units']),
                            'country': country.short_name,
                            'color': country.color,
                            'type': 'P',
                            'health': 10,
                            'pos': None,
                            'field': None,
                            'in_action': False,
                            'fortify': False
                            })
                    for i in range(gs.game['fight_ark']):
                        gs.fight['units'].append({
                            'id': len(gs.fight['units']),
                            'country': country.short_name,
                            'color': country.color,
                            'type': 'A',
                            'health': 50,
                            'pos': None,
                            'field': None,
                            'in_action': False,
                            'fortify': False
                            })
                    for i in range(gs.game['fight_ptr']):
                        gs.fight['units'].append({
                            'id': len(gs.fight['units']),
                            'country': country.short_name,
                            'color': country.color,
                            'type': 'C',
                            'health': 100,
                            'pos': None,
                            'field': None,
                            'in_action': False,
                            'fortify': False
                            })

                    country_b, land_b = gs.get_country_land_from_capital(gs.game['fight_to'][0], gs.game['fight_to'][1])
                    for i in range(land_b['army']['pst']):
                        gs.fight['units'].append({
                            'id': len(gs.fight['units']),
                            'country': country_b,
                            'color': land_b['color'],
                            'type': 'P',
                            'health': 10,
                            'pos': None,
                            'field': None,
                            'in_action': False,
                            'fortify': False
                            })
                    for i in range(land_b['army']['ark']):
                        gs.fight['units'].append({
                            'id': len(gs.fight['units']),
                            'country': country_b,
                            'color': land_b['color'],
                            'type': 'A',
                            'health': 50,
                            'pos': None,
                            'field': None,
                            'in_action': False,
                            'fortify': False
                            })
                    for i in range(land_b['army']['ptr']):
                        gs.fight['units'].append({
                            'id': len(gs.fight['units']),
                            'country': country_b,
                            'color': land_b['color'],
                            'type': 'C',
                            'health': 100,
                            'pos': None,
                            'field': None,
                            'in_action': False,
                            'fortify': False
                            })

                    a = 0
                    b = 0
                    for k, unit in enumerate(gs.fight['units']):
                        if unit['country'] == country.short_name:
                            i = a / 9
                            j = a % 9
                            gs.fight['fields'][i][j] = k
                            a += 1
                        else:
                            i = b / 9 + 1
                            j = b % 9
                            gs.fight['fields'][-i][j] = k
                            b += 1

                    pygame.mouse.set_cursor(*pygame.cursors.arrow)

                if (y_m > 90 and y_m < 130):
                    gs.set_stage('play')
                    gs.game['fight_from'] = None
                    gs.game['fight_to'] = None
                    pygame.mouse.set_cursor(*pygame.cursors.arrow)

            if (400 < x_m < 450):
                if (120 < y_m < 170 and gs.game['fight_pst'] > 0):
                    gs.game['fight_pst'] -= 1

                if (270 < y_m < 320 and gs.game['fight_ark'] > 0):
                    gs.game['fight_ark'] -= 1

                if (420 < y_m < 470 and gs.game['fight_ptr'] > 0):
                    gs.game['fight_ptr'] -= 1


            if (500 < x_m < 550):
                if (120 < y_m < 170 and gs.game['fight_pst'] < land['army']['pst']):
                    gs.game['fight_pst'] += 1

                if (270 < y_m < 320 and gs.game['fight_ark'] < land['army']['ark']):
                    gs.game['fight_ark'] += 1

                if (420 < y_m < 470 and gs.game['fight_ptr'] < land['army']['ptr']):
                    gs.game['fight_ptr'] += 1


def fight(screen, gs):
    fonts18 = pygame.font.Font(None, 18)
    fonts24 = pygame.font.Font(None, 24)
    fonts72 = pygame.font.Font(None, 72)

    bgcolor = pygame.Surface(screen.get_size())
    bgcolor = bgcolor.convert()
    bgcolor.fill((235, 235, 155))
    screen.blit(bgcolor, (0, 0))

    if gs.fight['action'] != 'victory':
        mygt(screen, 1140, 30, 215, 50, u'Ėjimo pabaiga', gs)
        mygt(screen, 1140, 90, 215, 50, u'Pabėgti iš mūšio', gs)

    country, land = gs.get_country_land_from_capital(gs.game['fight_from'][0], gs.game['fight_from'][1])
    country = gs.get_country(country)

    country_b, land_b = gs.get_country_land_from_capital(gs.game['fight_to'][0], gs.game['fight_to'][1])
    country_b = gs.get_country(country_b)

    army_text = '%i | %i | %i' % (gs.game['fight_pst'], gs.game['fight_ark'], gs.game['fight_ptr'])
    a = fonts72.render(army_text, True, country.color)
    screen.blit(a, (100, 30))

    army_text = '%i | %i | %i' % (land_b['army']['pst'], land_b['army']['ark'], land_b['army']['ptr'])
    a = fonts72.render(army_text, True, country_b.color)
    screen.blit(a, (800, 30))

    pygame.draw.rect(screen, (163, 225, 143), (50, 500, 1080, 180), 0)
    start_y = 500
    for i in range(10):
        pygame.draw.line(screen, (0, 0, 0), (50, start_y), (1130, start_y), 3)
        start_y += 20

    start_x = 50
    for i in range(55):
        pygame.draw.line(screen, (0, 0, 0), (start_x, 500), (start_x, 680), 3)
        start_x += 20
 
    #remove dead
    for unit in gs.fight['units']:
        if unit['health'] < 0 and unit['field'] != None:
            gs.fight['fields'][unit['field'][0]][unit['field'][1]] = ''
            unit['field'] = None
            unit['pos'] = (1000, 1000)

            if unit['country'] == country.short_name:
                if unit['type'] == 'P':
                    gs.game['fight_pst'] -= 1
                elif unit['type'] == 'A':
                    gs.game['fight_ark'] -= 1
                elif unit['type'] == 'C':
                    gs.game['fight_ptr'] -= 1
            else:
                if unit['type'] == 'P':
                    land_b['army']['pst'] -= 1
                elif unit['type'] == 'A':
                    land_b['army']['ark'] -= 1
                elif unit['type'] == 'C':
                    land_b['army']['ptr'] -= 1

    #may be victory?
    lefts = dict()
    for unit in gs.fight['units']:
        if unit['health'] > 0:
            lefts[unit['country']] = ''

    if (len(lefts) == 1):
        gs.fight['action'] = 'victory'

        victory_country = gs.get_country(lefts.keys()[0])
        a = fonts72.render(u'%s laimėjo' % victory_country.name, True, (0, 0, 0))
        screen.blit(a, (300, 300))

        mygt(screen, 500, 400, 215, 50, u'Grįžti į žemėlapį', gs)


    for i in range(54):
        for j in range(9):
            index = gs.fight['fields'][i][j]
            if isinstance(index, int):
                unit = gs.fight['units'][index]
                unit['pos'] = (52 + i * 20, 502 + j * 20)
                unit['field'] = (i, j)
                pygame.draw.rect(screen, unit['color'], (52 + i * 20, 502 + j * 20, 17, 17), 0)
                type_color = (0, 0, 0)
                if unit['in_action']:
                    type_color = (255, 255, 255)

                a = fonts18.render(unit['type'], True, type_color)
                screen.blit(a, (55 + i * 20, 505 + j * 20))
                if unit['fortify']:
                    pygame.draw.rect(screen, (255, 255, 255), (52 + i * 20, 502 + j * 20, 16, 16), 2)


    if gs.fight['action'] == 'selected':
        selected_unit = gs.fight['units'][gs.fight['selected_unit']]
        if selected_unit['type'] in ['P', 'C']:
            actions = ['X', 'F', 'G', 'S']
            longness = 80
        else:
            actions = ['X', 'F', 'G']
            longness = 60

        x, y = gs.fight['selected_pos']
        pygame.draw.rect(screen, (255, 255, 255), (x, y, longness, 20), 0)
        start_x = x + 5
        for letter in actions:
            a = fonts18.render(letter, True, (0, 0, 0))
            screen.blit(a, (start_x, y + 5))
            start_x += 20


    if gs.fight['action'] == 'selected_go':
        selected_unit = gs.fight['units'][gs.fight['selected_unit']]
        if selected_unit['type'] in ['P']:
            longness = 100
        elif selected_unit['type'] in ['C']:
            longness = 50
        else:
            longness = 200

        x, y = gs.fight['selected_pos']
        pygame.draw.circle(screen, (255, 0, 0), (x - 20, y + 20), longness, 5)


    if gs.fight['action'] in ['moving', 'shooting']:
        if len(gs.fight['user_log']) == 0:
            gs.fight['action'] = 'looking'
        else:
            action = gs.fight['user_log'][0]
            unit = gs.fight['units'][action['unit']]

            if not unit['health'] > 0:
                del gs.fight['user_log'][0]
            else:
                if action['action'] == 'F':
                    unit['fortify'] = True
                    unit['in_action'] = False
                    del gs.fight['user_log'][0]
                elif action['action'] == 'S':
                    pygame.draw.circle(screen, (0, 0, 0), (unit['pos'][0]+10, 300), 10)
                    pygame.draw.line(screen, (0, 0, 0), (50, 300), (1130, 300), 3)
                    gs.fight['action'] = 'shooting'
                elif action['action'] == 'G':

                    if unit['pos'] == action['target']:
                        i = (unit['pos'][0] - 52) / 20
                        j = (unit['pos'][1] - 502) / 20
                        unit['field'] = (i, j)
                        unit['in_action'] = False
                        gs.fight['fields'][i][j] = unit['id']

                        del gs.fight['user_log'][0]

                    else:
                        #check is field empty or enemy and empty field is near
                        moving_target = list(action['target'])
                        calculating_road = True
                        while calculating_road:
                            target_unit = gs.get_fight_unit_from_pos(moving_target)
                            if not target_unit:
                                calculating_road = False
                                break

                            if abs(moving_target[0] - unit['pos'][0]) > abs(moving_target[1] - unit['pos'][1]):
                                if moving_target[0] > unit['pos'][0]:
                                    moving_target[0] -= 20
                                elif moving_target[0] < unit['pos'][0]:
                                    moving_target[0] += 20
                            else:
                                if moving_target[1] > unit['pos'][1]:
                                    moving_target[1] -= 20
                                elif moving_target[1] < unit['pos'][1]:
                                    moving_target[1] += 20

                            recheck_unit = gs.get_fight_unit_from_pos(moving_target)
                            if not recheck_unit:
                                calculating_road = False

                            if target_unit['country'] != unit['country']:
                                #calculating damage
                                if target_unit['fortify']:
                                    fortify = 1
                                else:
                                    fortify = 2

                                if unit['type'] == 'P':
                                    if target_unit['type'] == 'P':
                                        target_unit['health'] -= unit['health'] / 4 * fortify
                                        unit['health'] -= target_unit['health'] / 4
                                    elif target_unit['type'] == 'A':
                                        target_unit['health'] -= unit['health'] / 8 * fortify
                                        unit['health'] -= target_unit['health'] / 4
                                    else:
                                        target_unit['health'] -= unit['health'] / 2 * fortify
                                        unit['health'] -= target_unit['health'] / 12
                                elif unit['type'] == 'A':
                                    if target_unit['type'] == 'P':
                                        target_unit['health'] -= unit['health'] / 4 * fortify
                                        unit['health'] -= target_unit['health'] / 8
                                    elif target_unit['type'] == 'A':
                                        target_unit['health'] -= unit['health'] / 4 * fortify
                                        unit['health'] -= target_unit['health'] / 4
                                    else:
                                        target_unit['health'] -= unit['health'] / 2 * fortify
                                        unit['health'] -= target_unit['health'] / 12
                                else:
                                    if target_unit['type'] == 'P':
                                        target_unit['health'] -= unit['health'] / 12 * fortify
                                        unit['health'] -= target_unit['health'] / 2
                                    elif target_unit['type'] == 'A':
                                        target_unit['health'] -= unit['health'] / 12 * fortify
                                        unit['health'] -= target_unit['health'] / 2
                                    else:
                                        target_unit['health'] -= unit['health'] / 4 * fortify
                                        unit['health'] -= target_unit['health'] / 4

                            if unit['pos'] == tuple(moving_target):
                                calculating_road = False

                            
                        if unit['pos'] == tuple(moving_target):
                            i = (unit['pos'][0] - 52) / 20
                            j = (unit['pos'][1] - 502) / 20
                            unit['field'] = (i, j)
                            unit['in_action'] = False
                            gs.fight['fields'][i][j] = unit['id']

                            del gs.fight['user_log'][0]
                        else:
                            gs.fight['fields'][unit['field'][0]][unit['field'][1]] = ''
                            pygame.draw.rect(screen, (0, 0, 0), (unit['pos'][0] - 1, unit['pos'][1] - 1, 19, 19), 5)
                            pygame.draw.rect(screen, unit['color'], (unit['pos'][0], unit['pos'][1], 17, 17), 0)
                            a = fonts18.render(unit['type'], True, (255, 255, 255))
                            screen.blit(a, (unit['pos'][0] + 3, unit['pos'][1] + 3))

                            x = unit['pos'][0]
                            y = unit['pos'][1]
                            if x < moving_target[0]:
                                x += 1
                            elif x > moving_target[0]:
                                x -= 1

                            if y < moving_target[1]:
                                y += 1
                            elif y > moving_target[1]:
                                y -= 1

                            unit['pos'] = (x, y)


    if gs.fight['action'] == 'selected_shoot':
        selected_unit = gs.fight['units'][gs.fight['selected_unit']]
        if selected_unit['type'] in ['P']:
            longness = 20
        elif selected_unit['type'] in ['C']:
            longness = 60
        else:
            longness = 0

        x, y = gs.fight['selected_pos']
        pygame.draw.circle(screen, (255, 0, 0), (x, y + 10), gs.fight['param_int'], 0)

        gs.fight['param_int'] += 1
        if (gs.fight['param_int'] > longness):
            # calculating damage
            for unit in gs.fight['units']:
                distance = int(math.sqrt((unit['pos'][0] - x)**2 + (unit['pos'][1] - y - 10)**2))
                if longness / distance:
                    fortify = 1
                    if unit['fortify']:
                        fortify = 2

                    unit['health'] -= (longness - distance) / fortify

            gs.fight['param_int'] = 0
            gs.fight['selected_unit'] = None
            gs.fight['selected_pos'] = None
            selected_unit['in_action'] = False
            del gs.fight['user_log'][0]
            gs.fight['action'] = 'moving'



    # Inputs
    events = pygame.event.get()
    for event in events:
        if event.type == MOUSEBUTTONUP and event.button == 1:
            x_m, y_m = event.pos

            if gs.fight['action'] != 'victory' and (x_m > 1140 and x_m < 1355):
                if (y_m > 30 and y_m < 80):
                    gs.fight['action'] = 'moving'
                    pygame.mouse.set_cursor(*pygame.cursors.arrow)

                if (y_m > 90 and y_m < 130):
                    gs.set_stage('play')
                    # we have logic here. If we retriet we lose half of canons,
                    # 1/5 simple and 1/10 cavalery
                    land['army']['pst'] += int(gs.game['fight_pst'] * 0.8)
                    land['army']['ark'] += int(gs.game['fight_ark'] * 0.9)
                    land['army']['ptr'] += int(gs.game['fight_ptr'] * 0.5)

                    gs.game['fight_from'] = None
                    gs.game['fight_to'] = None
                    pygame.mouse.set_cursor(*pygame.cursors.arrow)

            if gs.fight['action'] == 'victory' and (x_m > 500 and x_m < 715) and (400 < y_m < 450):
                gs.set_stage('play')

                #if aggressor wins - army should go to this land and land should got to him
                if country.short_name == lefts.keys()[0]:
                    land_b['army']['pst'] = gs.game['fight_pst']
                    land_b['army']['ark'] = gs.game['fight_ark']
                    land_b['army']['ptr'] = gs.game['fight_ptr']

                    gs.transfare_land()
                    

                gs.game['fight_from'] = None
                gs.game['fight_to'] = None
                pygame.mouse.set_cursor(*pygame.cursors.arrow)



            if gs.fight['action'] in ['looking', 'selected_go']:
                for i in range(54):
                    for j in range(9):
                        x = 52 + i * 20
                        y = 502 + j * 20
                        index = gs.fight['fields'][i][j]
                        if x < x_m < x + 17 and y < y_m < y + 17:
                            pygame.draw.rect(screen, (0, 0, 255), (x, y, 17, 17), 0)

                            if isinstance(index, int):
                                if gs.fight['action'] == 'looking':
                                    gs.fight['selected_unit'] = index
                                    gs.fight['selected_field'] = i, j
                                    gs.fight['selected_pos'] = x + 30, y - 10
                                    gs.fight['action'] = 'selected'

                            if gs.fight['action'] == 'selected_go':
                                selected_unit = gs.fight['units'][gs.fight['selected_unit']]
                                if selected_unit['type'] in ['P']:
                                    longness = 120
                                elif selected_unit['type'] in ['C']:
                                    longness = 40
                                else:
                                    longness = 220

                                x_, y_ = gs.fight['selected_pos']
                                distance = int(math.sqrt((x_ - 20 - x_m)**2 + (y_ + 20 - y_m)**2))

                                if distance <= longness:
                                    for i, log in enumerate(gs.fight['user_log']):
                                        if log['unit'] == gs.fight['selected_unit']:
                                            del gs.fight['user_log'][i]
                                            break

                                    gs.fight['user_log'].append({
                                        'unit': gs.fight['selected_unit'],
                                        'action': 'G',
                                        'target': (x, y)
                                        })

                                    selected_unit['in_action'] = True

                                    gs.fight['action'] = 'looking'
                                    gs.fight['selected_unit'] = None
                                    gs.fight['selected_field'] = None
                                    gs.fight['selected_pos'] = None


            if gs.fight['action'] == 'selected':
                selected_unit = gs.fight['units'][gs.fight['selected_unit']]
                if selected_unit['type'] in ['P', 'C']:
                    actions = ['X', 'F', 'G', 'S']
                else:
                    actions = ['X', 'F', 'G']

                x, y = gs.fight['selected_pos']
                # X - close
                if x < x_m < x + 20 and y < y_m < y + 20:
                    gs.fight['action'] = 'looking'
                    gs.fight['selected_unit'] = None
                    gs.fight['selected_field'] = None
                    gs.fight['selected_pos'] = None

                x += 20
                # F - fortify
                if x < x_m < x + 20 and y < y_m < y + 20:
                    for i, log in enumerate(gs.fight['user_log']):
                        if log['unit'] == gs.fight['selected_unit']:
                            del gs.fight['user_log'][i]
                            break

                    gs.fight['user_log'].append({
                        'unit': gs.fight['selected_unit'],
                        'action': 'F'
                        })

                    selected_unit['in_action'] = True

                    gs.fight['action'] = 'looking'
                    gs.fight['selected_unit'] = None
                    gs.fight['selected_field'] = None
                    gs.fight['selected_pos'] = None

                x += 20
                # G - go
                if x < x_m < x + 20 and y < y_m < y + 20:
                    gs.fight['action'] = 'selected_go'

                x += 20
                # S - shot
                if x < x_m < x + 20 and y < y_m < y + 20:
                    for i, log in enumerate(gs.fight['user_log']):
                        if log['unit'] == gs.fight['selected_unit']:
                            del gs.fight['user_log'][i]
                            break

                    gs.fight['user_log'].append({
                        'unit': gs.fight['selected_unit'],
                        'action': 'S'
                        })

                    selected_unit['in_action'] = True

                    gs.fight['action'] = 'looking'
                    gs.fight['selected_unit'] = None
                    gs.fight['selected_field'] = None
                    gs.fight['selected_pos'] = None

            # locking shooting target
            if (gs.fight['action'] == 'shooting' and 0 < x_m < 1180 and 300 < y_m < 500):
                action = gs.fight['user_log'][0]
                unit = gs.fight['units'][action['unit']]

                if unit['type'] == 'C':
                    potention = (y_m - 300) / 20.
                else:
                    potention = (y_m - 300) / 60.

                if  x_m > unit['pos'][0] + 10:
                    x_start = unit['pos'][0] + 10 - int((x_m - unit['pos'][0] - 10) * potention)
                else:
                    x_start = unit['pos'][0] + 10 + int((unit['pos'][0] + 10 - x_m) * potention)

                gs.fight['action'] = 'selected_shoot'
                gs.fight['selected_unit'] = unit['id']
                gs.fight['selected_field'] = None
                gs.fight['selected_pos'] = (x_start, unit['pos'][1])


        if event.type == MOUSEMOTION:
            x_m, y_m = event.pos

            if (gs.fight['action'] == 'shooting' and 0 < x_m < 1180 and 300 < y_m < 500):
                action = gs.fight['user_log'][0]
                unit = gs.fight['units'][action['unit']]
                pygame.draw.circle(screen, (0, 0, 0), (unit['pos'][0]+10, 300), 10)
                pygame.draw.line(screen, (255, 0, 0), (x_m, y_m), (unit['pos'][0]+10, 300), 3)

                if unit['type'] == 'C':
                    potention = (y_m - 300) / 20.
                else:
                    potention = (y_m - 300) / 60.

                y_diff = y_m - 300
                y_start = 300 - y_diff / 2

                if  x_m > unit['pos'][0] + 10:
                    x_start = unit['pos'][0] + 10 - int((x_m - unit['pos'][0] - 10) * potention)
                    x_diff = int((x_m - unit['pos'][0] - 10) * potention)
                else:
                    x_start = unit['pos'][0] + 10
                    x_diff = int((unit['pos'][0] + 10 - x_m) * potention)

                if x_diff > 5 and y_diff > 5:
                    pygame.draw.arc(screen, (255, 0, 0), (x_start, y_start, x_diff, y_diff),
                            0, 3.15, 3)

