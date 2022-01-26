label at_work:
    play music fan fadein 3
    show anim prologue_keyboard_1
    play sound sfx_keyboard_mouse_computer_noise
    anon "Так тебе еще повезло, чувак. Могли бы и закрыть, чего им стоит. Ты вообще знаешь, какой у нас процент оправдательных приговоров?"
    me "Слышал, слышал, что-то крайне незначительное и печальное."
    anon "Да. А куда тебя определили?"
    me "В хоспис. Даже не знаю, чего ожидать от такой работы. Завтра первый день. Мой {i}первый полноценный рабочий день в жизни, в общем-то."
    "Отныне в хаотичные и беспорядочные будни вмешивался порядок. Это пугало и угнетало одновременно."
    th "Что ж, придется вспомнить о будильнике."
    th "Не представляю, как справлюсь с нарастающей нервозностью."
    anon "Ха. Пиши, если что. И сразу в петлю не лезь - привыкнешь со временем, как и все мы."
    th "Надеюсь."
    scene bg black with dissolve
    $ renpy.pause(1.0)
    stop music fadeout 4
    stop sound
    scene bg hos with dissolve
    play sound steps fadein 2
    "Дорога заняла продолжительное время. Искомое место располагалась в доселе незнакомом районе. С непривычки, я даже умудрился немного заплутать."
    play music zima fadein 6
    "Снег падал увесистыми хлопьями и мягко ложился на крыши домов, деревья, асфальт. Зима уже уверенно утвердилась в правах."
    "Душа просит весну. А ее встречает декабрьский холод, приглашая в объятья."
    "Нет, друг, мы живем надеждой. Воспрянем, когда станем уходящую зиму оплакивать."
    $ renpy.pause(2.0)
    "Я бесцельно бродил возле хосписа, не решаясь зайти. Пятый круг сомнений."
    th "Что мне им сказать? Здравствуйте, я Семен, что никогда ранее нигде не работал; у меня нет образования, каких-либо навыков или талантов."
    th "Физический труд? Не про меня песня. Интеллект? Средний, не более. Средний, средний, средний я. Двадцать лет сплошной заурядности."
    "Предстояло связать себя с этим местом, как минимум, на год, но я никак не решался начать новую главу своей жизни."
    th "Не готов...Еще нет. Можно купить больничный, например, на пару недель, чтобы выиграть время."
    zs "Прекрати. Там тебя ждут такие же люди, со своими страхами и особенностями. Или лучше, по-твоему, в тюрьме оказаться?"
    th "Нет."
    th "Ух, в самом деле. Пора немного расширять зону комфорта."
    "Маленький шаг для человечества и..."
    stop sound fadeout 2
    stop music fadeout 4
    scene bg hoshol with dissolve
    th "Ремонт? Видимо, все же что-то перепутал..."
    play music kvar fadein 6
    "Вместо ожидаемого и привычного ресепшена, меня встречала теплая, приятная, но не оконченная работа."
    "В помещении отсутствовала не только большая часть необходимой мебели, но также и живые существа, по крайней мере, различимые человеческим глазом."
    th "Не удивлюсь, если окажусь единственным сотрудником."
    play sound shd
    "Недалекие размышления нарушил нарастающий звук шагов."
    show mt smile at right
    stop sound
    nezna "Добрый день! Вы к родственнику?"
    "Передо мной предстала очаровательная зеленоглазая девушка. В комнате, к слову, нас было уже трое: я, красавица-незнакомка и огромное смущение. Редко удавалась вербально взаимодействовать с такими привлекательным людьми."
    "Мой привычный удел - незаметно любоваться на подобную красоту в стороне, довольствуясь своим жалким положением."
    me "Эм-м, нет. Здесь, как бы, по работе, ну. То есть, меня сюда направили. В суде."
    th "Наконец, я осознал, какую глупость явил на свет."
    show mt norm at right
    nezna "Так вы тот самый Семен, стало быть."
    "Она хитро прищурилась. Ничего хорошего это не предвещало."
    show mt norm at right
    nezna "Сами понимаете, что работа у нас непростая."
    "Я кивнул в знак согласия. Но что я знал о подобном?"
    nezna "Меня зовут Ольга Дмитриевна, я заведующая хосписом. Штат здесь небольшой, но неравнодушных помощников много: недавно, например, приняли очередное пополнение волонтеров."
    mt "Постояльцы, в основном, - онкобольные. К {i}каждому стараемся найти подход, обеспечить теплотой и заботой. Воссоздаем, как можем, семейный уют."
    mt "Что касается вашей, Семен, работы: постепенно введем в курс дела, но потребуем ответственности и человечности."
    mt "Достойно трудитесь, и, в свою очередь, обещаю, что никаких проблем с органами надзора не будет."
    show mt laugh at right
    "Ольга широко улыбнулась. А ведь я уже почти отвык от девичьих улыбок."
    show mt smile at right
    mt "Еще какие-нибудь вопросы?"
    jump at_work_questions

label at_work_questions:
    menu:
        "Тяжело работать в хосписе?":
            me "Насколько тяжело здесь?"
            mt "В плане?"
            me "Душевного равновесия, прежде всего. Ведь...Этих ваших людей никак не спасти, они обречены."
            show mt angry at right
            mt "{i}Наших людей!"
            mt "Мы обеспечиваем им покой, приятное времяпрепровождение, качественный медицинский контроль."
            show mt norm at right
            mt "А насчет обреченности: с таким настроем здесь долго не задерживаются. Я лично провожала из хосписа нескольких счастливцев, которые смогли укротить болезнь. {i}Всегда есть место для чуда{/i}."
            mt "Даже здесь."
            jump at_work_questions

        "Почему вы выбрали это место?":
            me "Почему вы работаете в хосписе? Ведь есть множество лучших, по объективным показателям, вакансий."
            show mt smile at right
            mt "Кто-то же должен помогать людям. Я и не вижу себя в какой-то другой роли."
            th "Тут все болеют альтруизмом что ли? Хорошо, что у меня иммунитет."
            me "В обычной больнице, мне кажется, можно оказывать более значимую помощь."
            mt "Не буду спорить."
            show mt norm at right
            "Что-то она явно не договаривает касательно мотивов."
            jump at_work_questions


        "Что за волонтеры?":
            me "А что за волонтеры? Я так понимаю, это простые обыватели, что решили заглянуть разок-другой?"
            mt "Есть и такие, конечно. Но я имела в виду несколько более стабильных товарищей."
            mt "Кстати, они примерно твои одногодки, ну, чуть младше, возможно. Прекрасная троица: энергичные, веселые - такие нам нужны."
            th "Одногодки? Сколько же ей самой лет? Двадцать пять? Больше?"
            show mt norm at right
            jump at_work_questions

        "Вопросов нет":
            me "В общих чертах, мне все понятно..."
            stop music fadeout 2
            mt "И хорошо. Тогда приступим!"
            "Формальные вопросы по поводу трудоустройства, видимо, несильно волновали Ольгу."
            jump podari_zizn_vstrecha
