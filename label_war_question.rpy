label war_question:
    menu:
        "Где мы?":
            me "Так, а что это за место?"
            "Я бестолково огляделся."
            sl "Конкретно это? Подвал."
            me "Нет, хот..."
            "Блондинка, впрочем, не собиралась дожидаться резонного уточнения, а стремительно продолжила."
            sl "Где-то в районе Краснодара, точнее не скажу. При всем желании. Извини."
            "Ее нетерпеливый взгляд точно впился в меня; смелости для большего уточнения отыскать не получилось."
            me "Есть еще вопрос…"
            $question+=1
            if question==2:
                jump after_war
            sl "Ну же!"
            jump war_question

        "Меня интересует дата…":
            me "Какой сегодня день?"
            sl "Паршивый, в самом деле, паршивый."
            th "Неужели она не понимает?"
            me "Нет, я говорил о…"
            sl "Слушай, я не знаю. Могу сказать приблизительно: это что-то между 10 и 14 июня 2018 года."
            me "Подожди, 2018?!"
            sl "Именно."
            "Нет, это точно не являлось розыгрышем. Славяна абсолютно четко вычеканивала каждое слово: вне всякого сомнения, без малейшего намека на иронию или еще какую странную шутку."
            me "Есть еще вопрос…"
            $question+=1
            if question==2:
                jump after_war
            sl "Ну же!"
            jump war_question

        "Как ты оказалась рядом?":
            me "А как так вышло, что мы оказались вместе?"
            sl "А, твоя идея."
            "Девица небрежно бросила фразу куда-то в сторону, а затем безразлично пожала плечами."
            me "Не понимаю, в каком смысле?"
            sl "Ты старательно уговаривал меня покинуть перевал. Тебя, якобы, посещали нехорошие…видения."
            th "Твою же мать!"
            me "Видения, серьезно?"
            sl "Так и есть. Остальные не послушали, а я, вот, видишь, доверилась на свою голову."
            me "Какой-то бред…"
            sl "Выдвигаемся?"
            me "Есть еще вопрос…"
            $question+=1
            if question==2:
                jump after_war
            sl "Ну же!"
            jump war_question

        "Так ты говоришь, что со мной уже случалась амнезия?":
            me "Ты упомянула о том, что я уже терял…память."
            sl "Да. Сочувствую."
            th "Что толку от твоего сочувствия…"
            me "А как давно, если уч.."
            "Собеседница живо осадила набирающий обороты монолог."
            sl "С месяц назад, плюс-минус."
            "Мне лишь оставалось высказать свое наблюдение."
            me "А ты заметно огрубела, Славя."
            sl "Да ты что? И с чего бы только."
            me "Извини.."
            sl "Ты закончил?"
            me "Есть еще вопрос…"
            $question+=1
            if question==2:
                jump after_war
            sl "Ну же!"
            jump war_question

        "Что вообще тут происходит?":
            me "Что вообще происходит? От чего мы скрываемся?"
            "Славяна раздосадовано покачала головой."
            sl "Ох, сложно сказать. Натовцы, мародеры, сектанты…Тебе что ближе?"
            "Вот теперь я абсолютно точно отказывался принимать происходящее вокруг в качестве достоверной реальности."
            "Нужно приложить небольшое усилие, и я тотчас проснусь в теплой, уютной, заботливой кроватке."
            show blink with dissolve
            scene bg black
            "И…"
            $ renpy.pause (1.0)
            scene bg chart2 with dissolve
            show sl para
            "Видимо, все же не проснусь…"
            me "Ты ведь шутишь, да?"
            sl "Нет. Война заканчивается, но далеко не в нашу пользу."
            me "И, получается, было что-то вроде крупного конфликта?"
            sl "Что-то вроде. Центрального региона, по крайней мере, больше не существует."
            me "Но…Как это же такое вообще могло произойти?!"
            sl "У нас нет времени на такие разговоры."
            me "Есть еще вопрос…"
            $question+=1
            if question==2:
                jump after_war
            sl "Ну же!"
            jump war_question