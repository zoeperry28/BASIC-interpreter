import os.path

import pygame
import pygame.locals as pl
import GUI_Link as lnk
pygame.font.init()

class TextInput:
    """
    This class lets the user input a piece of text, e.g. a name or a message.
    This class let's the user input a short, one-lines piece of text at a blinking cursor
    that can be moved using the arrow-keys. Delete, home and end work as well.
    """
    def __init__(
            self,
            initial_string="",
            font_family="",
            font_size=35,
            antialias=True,
            text_color=(0, 136, 255),
            cursor_color=(0, 136, 255),
            repeat_keys_initial_ms=400,
            repeat_keys_interval_ms=35,
            max_string_length=-1):
        """
        :param initial_string: Initial text to be displayed
        :param font_family: name or list of names for font (see pygame.font.match_font for precise format)
        :param font_size:  Size of font in pixels
        :param antialias: Determines if antialias is applied to font (uses more processing power)
        :param text_color: Color of text (duh)
        :param cursor_color: Color of cursor
        :param repeat_keys_initial_ms: Time in ms before keys are repeated when held
        :param repeat_keys_interval_ms: Interval between key press repetition when held
        :param max_string_length: Allowed length of text
        """

        # Text related vars:
        self.antialias = antialias
        self.text_color = text_color
        self.font_size = font_size
        self.max_string_length = max_string_length
        self.input_string = initial_string  # Inputted text

        if not os.path.isfile(font_family):
            font_family = pygame.font.match_font(font_family)

        self.font_object = pygame.font.Font(font_family, font_size)

        # Text-surface will be created during the first update call:
        self.surface = pygame.Surface((1, 1))
        self.surface.set_alpha(0)

        # Vars to make keydowns repeat after user pressed a key for some time:
        self.keyrepeat_counters = {}  # {event.key: (counter_int, event.unicode)} (look for "***")
        self.keyrepeat_intial_interval_ms = repeat_keys_initial_ms
        self.keyrepeat_interval_ms = repeat_keys_interval_ms

        # Things cursor:
        self.cursor_surface = pygame.Surface((int(self.font_size / 20 + 1), self.font_size))
        self.cursor_surface.fill(cursor_color)
        self.cursor_position = len(initial_string)  # Inside text
        self.cursor_visible = True  # Switches every self.cursor_switch_ms ms
        self.cursor_switch_ms = 500  # /|\
        self.cursor_ms_counter = 0

        self.clock = pygame.time.Clock()

    def update(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                self.cursor_visible = True  # So the user sees where he writes

                # If none exist, create counter for that key:
                if event.key not in self.keyrepeat_counters:
                    self.keyrepeat_counters[event.key] = [0, event.unicode]


                #if event.type == KEYDOWN:
                #    if event.key == K_BACKSPACE:
                #        if len(text)>0:
                #            text = text[:-1]
                #    else:
                #        text += event.unicode
                        
                if event.key == pl.K_BACKSPACE:
                    self.input_string = (
                        self.input_string[:-1]
                    )
                    return 3

                if event.key == pl.K_RETURN:
                    self.input_string = self.input_string + "\n"                  
                    # Subtract one from cursor_pos, but do not go below zero:
                    self.cursor_position = max((self.cursor_position+1), 0)
                    return 1;
                if event.key == pl.K_UP:
                    return 2;
                
                elif event.key == pl.K_DELETE:
                    self.input_string = (
                        self.input_string[:self.cursor_position]
                        + self.input_string[self.cursor_position + 1:]
                    )

                elif event.key == pl.K_RETURN:
                    return True

                elif event.key == pl.K_RIGHT:
                    # Add one to cursor_pos, but do not exceed len(input_string)
                    self.cursor_position = min(self.cursor_position + 1, len(self.input_string))

                elif event.key == pl.K_LEFT:
                    # Subtract one from cursor_pos, but do not go below zero:
                    self.cursor_position = max(self.cursor_position - 1, 0)

                elif event.key == pl.K_END:
                    self.cursor_position = len(self.input_string)

                elif event.key == pl.K_HOME:
                    self.cursor_position = 0

                elif len(self.input_string) < self.max_string_length or self.max_string_length == -1:
                    # If no special key is pressed, add unicode of key to input_string
                    self.input_string = (
                        self.input_string[:self.cursor_position]
                        + event.unicode
                        + self.input_string[self.cursor_position:]
                    )
                    self.cursor_position += len(event.unicode)  # Some are empty, e.g. K_UP

            elif event.type == pl.KEYUP:
                # *** Because KEYUP doesn't include event.unicode, this dict is stored in such a weird way
                if event.key in self.keyrepeat_counters:
                    del self.keyrepeat_counters[event.key]
            
        # Update key counters:
        for key in self.keyrepeat_counters:
            self.keyrepeat_counters[key][0] += self.clock.get_time()  # Update clock

            # Generate new key events if enough time has passed:
            if self.keyrepeat_counters[key][0] >= self.keyrepeat_intial_interval_ms:
                self.keyrepeat_counters[key][0] = (
                    self.keyrepeat_intial_interval_ms
                    - self.keyrepeat_interval_ms
                )

                event_key, event_unicode = key, self.keyrepeat_counters[key][1]
                pygame.event.post(pygame.event.Event(pl.KEYDOWN, key=event_key, unicode=event_unicode))

        # Re-render text surface:
        self.surface = self.font_object.render(self.input_string, self.antialias, self.text_color)

        # Update self.cursor_visible
        self.cursor_ms_counter += self.clock.get_time()
        if self.cursor_ms_counter >= self.cursor_switch_ms:
            self.cursor_ms_counter %= self.cursor_switch_ms
            self.cursor_visible = not self.cursor_visible

        if self.cursor_visible:
            cursor_y_pos = self.font_object.size(self.input_string[:self.cursor_position])[0]
            # Without this, the cursor is invisible when self.cursor_position > 0:
            if self.cursor_position > 0:
                cursor_y_pos -= self.cursor_surface.get_width()
            self.surface.blit(self.cursor_surface, (cursor_y_pos, 0))

        self.clock.tick()
        return False

    def get_surface(self):
        return self.surface

    def get_text(self):
        return self.input_string

    def get_cursor_position(self):
        return self.cursor_position

    def set_text_color(self, color):
        self.text_color = color

    def set_cursor_color(self, color):
        self.cursor_surface.fill(color)

    def clear_text(self):
        self.input_string = ""
        self.cursor_position = 0

class New_Output:
    
    OUT = ""
    ACTIVE_OUT = False
    def __init__(self, OUT_TEXT, start):
        self.OUT_TEXT = OUT_TEXT    # instance variable unique to each instance
        self.OUT = OUT_TEXT
        self.ACTIVE_OUT = start
        
if __name__ == "__main__":
    pygame.init()
    # Create TextInput-object
    textinput = TextInput()
    X_TEXT = 20
    Y_TEXT = 80
    LINE_COUNT = 0 
    screen = pygame.display.set_mode((700, 700))
    clock = pygame.time.Clock()
    ALL_LINES = []
    TEXT_LINES_TO_SHOW = []
    PREVIOUS = ""
    BLUE = (0, 0, 170)
    LBLUE = (0, 136, 255)
    
    """
    Set the default text
    """
    C64_BSC = " **** COMMODORE 64 BASIC V2 **** "
    C64_BYTES_FREE = "64K RAM SYSTEM   38911 BASIC BYTES FREE"
    C64_RDY = "READY."

    y = New_Output("", False)
    
    while True:
    
        screen.fill(LBLUE)
        pygame.draw.rect(screen,BLUE,(20,20,660,660))
        
        basicfont = pygame.font.SysFont(None, 32)
        text = basicfont.render(C64_BSC, True, LBLUE)
        screen.blit(text, (160,20))
        
        text = basicfont.render(C64_BYTES_FREE, True,  LBLUE)
        screen.blit(text, (100,50))
                    
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()
        # Feed it with events every frame
        res = textinput.update(events)
        # Blit it1s surface onto the screen
        font = pygame.font.SysFont("",32)

        if(res == 1):
            if((textinput.input_string == "RUN\n")):
                x = lnk.LINK(ALL_LINES)
                object_from_exe = x.run_all_lines(y)
                if(object_from_exe.ACTIVE_OUT == True):
                    TEXT_LINES_TO_SHOW.append([font.render(object_from_exe.OUT, True, (LBLUE)), X_TEXT, Y_TEXT+20])
            try:
                ALL_LINES[LINE_COUNT] = textinput.input_string
            except: 
                ALL_LINES.insert(LINE_COUNT, textinput.input_string)
                
            LINE_COUNT = LINE_COUNT + 1
            TEXT_LINES_TO_SHOW.append([font.render((ALL_LINES[LINE_COUNT-1][0:(len(ALL_LINES[LINE_COUNT-1])-1)]), True, (LBLUE)), X_TEXT, Y_TEXT])
            textinput.input_string = ""
            X_TEXT = X_TEXT + 0
            Y_TEXT = Y_TEXT + 20
            
        elif(res == 2):
            print("yeet")
            textinput.input_string = ALL_LINES[LINE_COUNT-1][0:(len(ALL_LINES[LINE_COUNT-1])-1)]
            LINE_COUNT = LINE_COUNT - 1
            Y_TEXT = Y_TEXT - 20
        elif(res == 3):
            textinput.input_string = textinput.input_string[0:(len(textinput.input_string))]
        else:
            screen.blit(textinput.get_surface(), (X_TEXT, Y_TEXT))
            temp = Y_TEXT - 20    

        for i in range(0, len(TEXT_LINES_TO_SHOW)):
            screen.blit((TEXT_LINES_TO_SHOW[i][0]), (TEXT_LINES_TO_SHOW[i][1], TEXT_LINES_TO_SHOW[i][2]))
        pygame.display.update()
        clock.tick(30)        
        
