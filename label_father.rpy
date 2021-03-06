label father:
    $ renpy.pause (0.8)
    scene bg hrysh with dissolve
    play ambience gorod fadein 2
    play music zima fadein 6
    "Взору предстали усталые хрущевки, так органично вписывающиеся в понятие «окраина города»."
    "Место, некогда будучи очень родным и личным, не вызывало сейчас какой-либо приятной ностальгии, а, скорее, будило в памяти беспокойную череду детских обид и юношеских разочарований."
    "Двор, бывший сокровенным реликтом далеких лет, ныне ясно указывал на мою неуместность."
    "Не желая более задерживаться, я отправился к нужной мне квартире."
    stop music fadeout 5
    stop ambience
    scene bg kv with dissolve
    play ambience sk
    bt "Ну, здорово, Сем."
    play music kvar fadein 4
    show bt smile with dissolve
    "Я попытался ответить, но тщетно – отец уже успел пленить в крепкие объятия. Короткий кивок ознаменовал мое приветствие."
    bt "Ты, это, проходи на кухню, там все готово уже."
    "Очередной кивок - поддерживаю внезапный имидж человека-дела."
    "Отделка квартиры практически не изменилась с самых давних пор: ей заметно не хватало лоска и какого-то намека на свежесть, но, в целом, она все еще смотрелась неплохо."
    th "Жить можно. Если ты, конечно, не советский диссидент. Здесь явно удалось построить светлое коммунистическое будущее."
    "На кухонном столе, в трепетном ожидании гостей, расположился аккуратно разлитый коньяк и две тарелки с сочным бифштексом."
    th "Почему не пельмени со `Столичной`? Происки капиталистов, не иначе."
    show bt norm
    bt "Присаживайся, чего стоишь."
    me "Ты пригласил меня на ланч? Если так, то я пас - не голоден."
    bt "Нет, не для этого."
    show bt evil
    "Он залпом осушил увесистую рюмку."
    show bt norm
    bt "Сколько лет-то прошло, а? Ох, какой же я был дурак, Семка, какой дурак...Ты как сам по жизни? Учишься, работаешь?"
    me "Работаю."
    bt "Кем? Я, вон, до сих пор в школе горбачусь. Тебе бы, кстати, тоже спортом не помешало заняться. Тушка-то совсем дохлая."
    show bt smile
    th "Так, отсталый совок уже раздавал советы, осталось теперь на мастер-классы к местным пропойцам записаться. Заживу!"
    "Происходящее начинало порядком раздражать. Я не ощущал ни родственной, ни ментальной, не какой-либо еще связи со стоящим передо мной человеком."
    "Мы были бесконечно далеки от понимания и мировосприятия друг друга."
    me "Интернет-проект. Которому я уделяю ровно столько времени, сколько посчитаю нужным. Позволяет полностью себя обеспечивать, не разменивая свободу на звонкие монеты."
    "Выдержав театральную паузу."
    play music depra fadein 2
    stop ambience
    me "Звонкую грош, в твоем, отец, случае."
    show bt evil
    "Я никогда не был большим знатоком человеческой мимики, однако же, заметил, что мои слова его определенно задели."
    bt "С тобой по-людски нельзя что ли?"
    me "На что ты рассчитывал? У нас немного общих тем. И вообще - немного. По крайней мере, я пытаюсь лишиться всякой схожести."
    bt "Так мы долго еще можем препираться..."
    show bt norm
    me "На самом деле, нет. Я уже собираюсь уходить. Мне действительно нечего здесь делать, и сейчас осознаю это вполне отчетливо. Неясно лишь, на что я рассчитывал."
    bt "Сем, пойми, я хочу наладить контакт между нами, но ты ж из меня врага народа делаешь, честное слово."
    me "Мне. Не нужен. Никакой. Контакт."
    bt "С отцом-то родным не нужен?"
    me "Со старым, никчемным аутсайдером вроде тебя. Ты мне просто противен."
    show bt evil
    bt "Извинись, Семен. Извинись за то, что ты сейчас сказал."

    menu:
        "Я действительно перегнул":
            $ paragon += 1
            $ finka += 1
            stop music fadeout 5
            me "Да...Наверное, я погорячился. Не стоило так."
            play music bgood fadein 2
            "Раскаяние было неумолимо. От стыда ярко вспыхнули щеки и, конечно, это прекрасным образом ощущалось."
            "Лицо горело так сильно, что я чувствовал себя жертвой охотников на ведьм."
            me "Это было лишним."
            show bt norm
            bt "Да понимаю тебя, Семка, понимаю. Козел, подлец, подонок – заслуживаю все это, что уж. Дал заднюю, когда нужно было, наверно, рядом оставаться."
            bt "Но смерть Тамары, храни ее Господь, выбила она меня из колеи. Место себе не находил. А потом нашел…Со стаканом в руках."
            bt "Бабушка сама предложила тебя оставить у себя, видя, что со мной происходило. А что мне? Все в один миг рухнуло: стал, как у этого, у Горького – на дне."
            show bt smile
            "Я внимательно слушал своеобразную исповедь."
            show bt norm
            bt "И в один момент начал понимать: или берусь за голову, или за Тамаркой следом. Тогда и родился простой план, как все исправить можно. Или попытаться, хотя бы."
            th "Исправить? О чем он говорит? О некромантии что ли?"
            bt "Время непростое было, сам знаешь, с работой тоже сложности возникали. Пришлось уезжать на заработки за шестьсот километров. Ох, Семка, знал бы ты, сколько дерьма я повидал…"
            show bt evil
            "Он замолчал, словно размышляя, стоит ли продолжать, очевидно, неприятную тему."
            bt "Но…Получилось, сына. Трудности они же, знаешь, только закаляют мужика. В любую подработку, в любой калым зубами вцеплялся и крепко так!"
            show bt norm
            "Отец продемонстрировал многозначительный жест руками."
            bt "Много встречал неприятностей, людей, женщин...Короче говоря, своего я добился. И…Вот это все - твое теперь."
            "Он показал пальцем куда-то в сторону кухни."
            th "Холодильник, неужели?"
            me "Не совсем понимаю, что именно."
            bt "Квартира твоя. Чего в бабушкиной однушке-то ютиться."
            "Все это с трудом укладывалось в голове, как бы я не пытался упорядочить поступающую информацию."
            me "Подожди, ну, а ты как же?"
            bt "За меня ты не беспокойся. Это я за тебя должен. А кроме этого…"
            show bt smile
            "Батя хитро прищурился."
            bt "И кроме этого, у меня еще презент есть небольшой. Вон, в том белом пакете на комоде, ровно один миллион рублей. Тебя дожидается."
            th "Миллион?!"
            me "Это какой-то розыгрыш? Не очень удачный..."
            show bt norm
            bt "Не получилось принять участия в юности твоей, так хоть становление на ноги обеспечу."
            bt "Ты парень неглупый, Семка, тут уж в мать пошел…В дело пустишь какое-нибудь. Вот, про этот проект говорил же? Да хотя бы и в него. Или машину купишь себе."
            "Я все еще не мог поверить в происходящее. Реальность, кажется, подводила меня, нагло заигрывая с сюрреализмом."
            me "Машину?...Да у меня и прав даже нет…"
            bt "Одни обязанности, небось?"
            show bt smile
            "Он негромко усмехнулся."
            bt "Ну, чего такой потерянный, садись – отметим семейное воссоединение."
            show blink with dissolve



        "Но я не чувствую себя виноватым":
            stop music fadeout 5
            $ renegat += 1
            me "Могу лишь повторить."
            play music bbad fadein 2
            $ renpy.pause (0.4)
            bt "Жаль, что ты так думаешь насчет меня. Я ведь не плохой человек, Семен. И никогда им не был."
            me "Единственное, с чем я соглашусь, так это с тем, что ты никогда не был. {i}Не был в моей жизни{/i}."
            bt "Я понимаю твою обиду, но и ты…"
            me "Да ничего ты, черт возьми, не понимаешь!"
            "Я с удовольствием отдался слабости."
            "Слабые люди, в частности, отличаются от волевых лишь одним непременным атрибутом: {i}они всегда потакают собственным желаниям{/i}."
            "Эмоции обычно через какое-то время проходят. Но то, что они сделали — остается."
            "Безусловно, я знал об этом, но жаждал расплаты. Отмщения. Ненависть приятно разливалась по телу: она чувствовалась покалыванием в пальцах и в неожиданном всплеске энергии."
            me "У тебя все так просто, серьезно? Наплевал на меня, развлекался {i}годами{/i} непонятно с кем, а сейчас, значит, отцовский инстинкт проснулся, а? Нельзя просто вдруг похлопать по плечу, со словами: `Привет, малой, папка вернулся!`"
            "Сейчас я решительно перешел точку невозврата."
            me "Ты, попусту, {i}эгоистичный кусок дерьма{/i}. Ведь если бы ты хоть {i}чуть{/i} уважал меня, считался со мной, ты бы никогда больше не появился в моей жизни. Не стал бы обнажать старые раны и ворошить болезненное прошлое одним своим видом."
            bt "Я не смог. Мы друг другу не чужие люди, Сема."
            me "Таковым ты для меня и являешься. Последнего родного человека я потерял с уходом бабушки. Тебя же никогда и не было в списке близких людей. И он уж точно никак не корректируется."
            "Склонив голову, отец собирался с последними силами, кажется, все еще веря в возможный реванш. Глаза его предательски слезились."
            bt "Значит, вот так вот мы прощаемся?"
            me "Всякая ответственность за сложившуюся ситуацию принадлежит тебе. Я не желаю общаться с лицемерным предателем."
            $ renpy.pause (0.4)
            bt "Знаешь, Сем… Я ведь приглашал тебя для совсем других разговоров. У меня есть кое-что для тебя..."
            me "Но у меня для тебя нет {i}ничего{/i}!"
            "Последние слова прозвучали наподобие хлесткого приговора. В диалоге, как и во всей пренеприятной и запутанной истории взаимоотношений, была поставлена точка. Жирная и безапелляционная."
            show blink with dissolve
