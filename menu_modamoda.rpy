#начало main_menu_modamoda
label main_menu_modamoda:
    play music menumus fadein 4
    play ambience hosam fadein 6
    $ was_in_menu = True
    scene bg fon_menu with dissolve    #заменить картинку
    call screen main_menu_modamoda

screen main_menu_modamoda:
    imagemap:
        ground "pg_menu_start.png"  #заменить картинку
        alpha True

        hotspot (622, 35, 1270, 68) action Jump("introduction")
        hotspot (622, 100, 1206, 144) action Jump("choose_label")
        hotspot (622, 166, 1205, 212) action Jump("aboutall")
        hotspot (622, 234, 1204, 280) action Quit("confirm")
#конец main_menu_modamoda

