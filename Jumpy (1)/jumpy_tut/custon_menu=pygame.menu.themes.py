custon_menu=py_game.menu.themes.Theme(
        background_color=(255,240,245),
        widgetfont_color=(255,105,180),
        selection_color=(147,112,219),
        title_font_size=20,
        widget_font='dogicapixel.ttf'
        )
def main_menu():
    menu=pygame_menu.Menu('Main',WINDOWWIDTH, WIDOWHEIGHT,theme='custom_menu')
    menu.add.button('START',choose_character)
    menu.add.button('QUIT',pygame_menu.events.EXIT)
    menu.mainloop(DISPLAYSURF)


def main():
    while True:
       main_menu()
if __name__=='__main__':
    main()