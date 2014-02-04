# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
import json
import os
import re
import time
from math import fabs


HAND_CURSOR_STRING = (
    "     XX         ",
    "    X..X        ",
    "    X..X        ",
    "    X..X        ",
    "    X..XXXXX    ",
    "    X..X..X.XX  ",
    " XX X..X..X.X.X ",
    "X..XX.........X ",
    "X...X.........X ",
    " X.....X.X.X..X ",
    "  X....X.X.X..X ",
    "  X....X.X.X.X  ",
    "   X...X.X.X.X  ",
    "    X.......X   ",
    "     X....X.X   ",
    "     XXXXX XX   ")
CURSOR_HAND, MASK = pygame.cursors.compile(HAND_CURSOR_STRING, black='X',
        white='.', xor='o')


def mygt(screen, x, y, x_sz, y_sz, txt, gs):
    """Drawing button."""

    x_m, y_m = pygame.mouse.get_pos()

    # if mouse is under button
    if (x_m < (x + x_sz) and x_m > x) and (y_m < (y + y_sz) and y_m > y):
        pygame.draw.rect(screen, (200, 160, 60), (x, y, x_sz, y_sz), 0)
        pygame.mouse.set_cursor((16, 16), (8, 1), CURSOR_HAND, MASK)
        gs.register_button(x, y, x_sz, y_sz)
    else:
        pygame.draw.rect(screen, (255, 200, 80), (x, y, x_sz, y_sz), 0)
        if not gs.check_button(x, y, x_sz, y_sz):
            pygame.mouse.set_cursor(*pygame.cursors.arrow)

    pygame.draw.rect(screen, (0, 0, 0), (x, y, x_sz, y_sz), 2)

    fonts = pygame.font.Font(None, 24)
    a = fonts.render(txt, True, (0, 0, 0))
    screen.blit(a, (x + 8, y + (y_sz / 2) - 8))


class GameSettings:
    """Object to save all game parameters during game."""
    een = True          # Game loop
    stage = 'start'     # display stage of game (start, map, settings etc.)

    countries = {}      # Countries
    maps = {}           # Maps
    ages = ['XIII', 'XIX']

    HOME = os.path.expanduser("~")
    HOME = os.path.join(HOME, '.rc_maumataskis')
    try:
        f = open(HOME, 'r')
        HOME = f.readline()
        f.close()
        try:
            HOME = HOME[:-1]
            os.listdir(HOME)
        except OSError:
            HOME = os.path.expanduser("~")
            HOME = os.path.join(HOME, '.rc_maumataskis')
            f = open(HOME, 'w')
            ent = '\n'
            f.write(os.path.expanduser("~"))
            f.write(ent)
            f.close()
            HOME = os.path.expanduser("~")
    except IOError:
        f = open(HOME, 'w')
        ent = '\n'
        f.write(os.path.expanduser("~"))
        f.write(ent)
        f.close()
        HOME = os.path.expanduser("~")


    # FIXME: rewrite opt and flagai
    opt = {'kursor_pos' : 0, 't_raidie' : '', 'zaid' : '',
            's_dir_cur' : HOME, 's_dir_pos' : 0, 'HOME' : HOME}     # varies options
    flagai = {'SAVE_DIR' : 0, 'new_dir' : 0, 'KNIST_DIR' : 0, 'new_file' : 0,
            'new_file_err' : 0, 'load_err' : 0, 'SAUGOM' : 0, 'KRAUNAM' : 0,
            'PRINTINAM' : 0, 'KNIST_OK' : 0}    # varies flags

    buttons_stack = {}
    errors = []

    editor = {
            'in_progress': False,
            'word': '',
            'cursor': 0
            }
    settings = {
            'age' : 'XIX',
            'map' : '',
            'country' : ''
            }

    map_editor = {
            'tool' : 'border',
            'action' : None,
            'x': None,
            'y': None,
            'tmp' : None,
            'country' : None
            }

    map_editor_tools = {
            'border': u'Sienos',
            'undo': u'Atšaukti',
            'capital': u'Sostinė',
            'countries': u'Šalys',
            'connect': u'Ribojasi'
            }

    new_map = {
            'borders': [],
            'capitals': [],
            'countries': {}            
            }

    game = {
            'age': '',
            'map': '',
            'users': [],
            'turn': 0,
            'stage': '',
            'fight_from': None,
            'fight_to': None,
            'fight_pst': 0,
            'fight_ark': 0,
            'fight_ptr': 0
            }

    fight = {
            'fields': [],
            'units': [],
            'selected_unit': None,
            'selected_field': None,
            'selected_pos': None,
            'action': 'looking',
            'user_log': []
            }

    def __init__(self):
        self.load_countries()
        self.load_maps()

        self.fight['fields'] = []
        for i in range(54):
            self.fight['fields'].append([])
            for j in range(9):
                self.fight['fields'][i].append('')


    def get_stage(self):
        return self.stage


    def set_stage(self, stage):
        self.stage = stage


    def load_countries(self):
        countries = os.listdir('countries')
        for country_short in countries:
            country = Country(country_short)

            f = open('countries/'+country_short, 'r')
            country.name = f.readline()[0:-1]
            r = int(f.readline())
            g = int(f.readline())
            b = int(f.readline())
            country.color = (r, g, b)

            # reading players by ages
            ages = {}
            age = None
            line = f.readline()
            while line:
                line = line[0:-1]
                b = re.match('\[(\w+)\]', line)
                if b:
                    age = b.groups()[0]
                    ages[age] = []
                    line = f.readline()
                    continue

                if line:
                    ages[age].append(line)

                line = f.readline()


            f.close()
            country.ages = ages

            self.add_country(country_short, country)


    def add_country(self, country_short, country):
        self.countries[country_short] = country


    def get_country(self, short_name):
        if short_name in self.countries:
            return self.countries[short_name]

    def get_country_land_from_capital(self, x, y):
        for country in self.game['map']:
            for land in self.game['map'][country]:
                if x - 10 < land['capital'][0] < x + 10 and y - 10 < land['capital'][1] < y + 10:
                    return country, land

        return None, None
        

    def save_new_map(self):
        # prepare content
        structure ={}
        for country in self.new_map['countries']:
            structure[country] = []
            country_data = self.get_country(country)
            print(country_data)
            for capital in self.new_map['countries'][country]:
                border = self.get_capital_border(self.new_map['borders'], capital)
                if border:
                    structure[country].append({
                        'capital': capital,
                        'border': border,
                        'color': country_data.color
                        })

        filename = self.editor['word'].replace(' ', '_')+'.ia.map'
        f = open('maps/'+filename, 'w')
        f.write(self.editor['word']+"\n")
        f.write(self.settings['age']+"\n")
        f.write(json.dumps(structure)+"\n")
        f.close()

        self.maps = {}
        self.load_maps()


    def load_maps(self):
        maps = os.listdir('maps')
        for filename in maps:
            map_ = Map()

            f = open('maps/'+filename, 'r')
            map_.name = f.readline()[0:-1]
            map_.age = f.readline()[0:-1]
            map_.file = 'maps/'+filename
            map_.map = json.loads(f.readline()[0:-1])
            f.close()

            self.add_map(map_.name, map_)


    def add_map(self, map_name, map_object):
        self.maps[map_name] = map_object


    def clear_menu(self):
        """Clear menu and set flag."""
        self.menu = False
        self.menu_flag = 0
        self.buttons_stack = {}     # Make empty for renew situation


    def register_button(self, x, y, x_sz, y_sz):
        self.buttons_stack['%i_%i_%i_%i' % (x, y, x_sz, y_sz)] = True


    def check_button(self, x, y, x_sz, y_sz):
        self.buttons_stack['%i_%i_%i_%i' % (x, y, x_sz, y_sz)] = False
        return True in self.buttons_stack.values()


    def clear_log(text=None):
        self.log = []
        if text:
            self.log.append(text)


    def add_log(text):
        self.log.insert(0, text)


    def quit_game(self):
        """Quit aplication."""
        self.een = 0

    def get_extremums(self, border):
        """Returns extremums of border."""
        min_x = min([p[0] for p in border])
        max_x = max([p[0] for p in border])
        min_y = min([p[1] for p in border])
        max_y = max([p[1] for p in border])
        return min_x, max_x, min_y, max_y


    def extend_border(self, border):
        extended = [border[0]]
        pos_old = None
        tmp_border = border
        tmp_border.append(border[0])
        for pos in tmp_border:
            if pos_old:
                if not pos[1] - pos_old[1] == 0:
                    k = (pos[0] - pos_old[0]) * 1. / (pos[1] - pos_old[1])
                    c = -1 * (pos[1] * k - pos[0])
                    if (pos[1] > pos_old[1]):
                        step = 1
                    else:
                        step = -1

                    for y in range(pos_old[1], pos[1], step):
                        x_ = int(y * k + c)

                        if (extended[-1][0] <= x_):
                            step_x = 1
                        else:
                            step_x = -1

                        for x in range(extended[-1][0], x_, step_x): 
                            extended.append((x, y))

                else:
                    if (pos[0] > pos_old[0]):
                        step = 1
                    else:
                        step = -1

                    for x in range(pos_old[0], pos[0], step):
                        extended.append((x, pos[1]))


            pos_old = pos

        return extended


    def get_capital_border(self, borders, capital):
        for border in borders:
            min_x, max_x, min_y, max_y = self.get_extremums(border)
            FOUND = False
            border_extended = self.extend_border(border)
            if min_x < capital[0] < max_x and min_y < capital[1] < max_y:
                # this algoritm counts how many time it passes contur
                # border. If it is < 0 and is odd it meens what point is
                # inside contur
                y = capital[1]
                count = 0
                while y > min_y - 1:
                    y -= 1
                    for p in border_extended:
                        if p[0] == capital[0] and p[1] == y:
                            count += 1
                            print(count)

                if count > 0 and count % 2 == 1:
                    return border


class Country:
    """Main class for country."""

    def __init__(self, short_name):
        self.short_name = short_name
        self.ages = {}
        self.name = ''
        self.color = None


class Map:
    """Main class for map."""

    def __init__(self):
        self.name = ''
        self.age = ''
        self.file = ''
        self.map = None

