label zaharchenko_1:
    th "Не стоит осложнять и без того шаткое положение. Еще и возьмут на карандаш, если ударюсь в откровения."
    $ renegat = +1
    me "Все очень просто: мой никчемный вид – последствия пышного торжества. Друг недавно отмечал юбилей, вот и…"
    "Виола строго нахмурилась, и то стало вполне ожидаемой реакцией."
    cs "Сколько же вы выпили, чтобы…так?"
    me "Вспомнил свои шесть, так скажем."
    $ renpy.pause (1.0)
    cs "По-вашему, это смешно?"
    me "Казалось забавным в тот момент."
    "Я совершенно невинно пожал плечами."
    cs "Знаете, все-таки прихожу к вполне конкретным выводам на ваш счет."
    me "Если не секрет, то в чем заклю…"
    cs "Вам здесь не место."
    "Резко перебила доктор."
    me "Извините, пожалуйста."
    cs "Вы в состоянии доделать работу?"
    th "Стальную интонацию вызывали?"
    me "Да."
    cs "Так приступайте. "
    hide cs with dissolve
    "Неловкая попытка пошутить привела к подлинной дипломатической катастрофе. И зачем я только ляпнул ту глупость…"
    play sound sfx_keyboard_mouse_computer_noise
    $ renpy.pause (1.0)
    "Очередная порция тягостных обязательств под монотонный стук клавиш... Минуты тянутся столь медленно…"
    $ renpy.pause (1.0)
    "Сменяющие друг друга фамилии только навевают скуку…"
    $ renpy.pause (1.0)
    "Я откровенно скучал…"
    $ renpy.pause (1.0)
    th "Подайте, пожалуйста, веревку.."
    $ renpy.pause (1.0)
    "И наконец..."
    stop sound
    me "Закончил!!"
    "Эмоции вновь выставили меня дураком."
    th "Вот, в самом деле, интересно: как меня воспринимают в хосписе? В качестве потешного юродивого, не иначе."
    show cs normal with dissolve
    cs "Здорово, но совсем необязательно кричать."
    "Я лишь кивнул."
    cs "Семен, более поручений не имею."
    "Если в начале знакомства Виола показалась мне доброжелательным персонажем, то сейчас она заметно изменила манеру общения – она стала куда суше, формальнее и безразличнее."
    "Быть может, так сказывается усталость? Доктор выглядела заметно подавленной."
    stop music fadeout 8
    "Так или иначе, идея окончательного вырождения в офисного клерка нисколько не прельщала, а потому я бросился к кабинету заведующей."
    scene bg olk with dissolve
    show sl norm at left with dissolve
    show mt norm with dissolve
    play music kvar fadein 4
    "Девушки, увлеченные живым разговором, даже и не заметили моего появления. Немного обидно, если честно."
    mt "Будет здорово. Жаль, что область не выделяет деньги на праздники, поэтому придется экономить."
    show sl evil
    sl "Как же так! Все-таки Новый Год, неужели не могли найти средств хоть на коробку конфет?!"
    mt "Да что с них…"
    "В сердцах, Ольга махнула рукой."
    show sl smile
    me "К-хм."
    sl  "Ой, привет!"
    me "Добрый вечер."
    "Славяне сегодня достается учтивое приветствие. Впрочем, я здесь не за пустыми беседами и обменом любезностями."
    show sl norm
    me "Ольга Дмитриевна, с электронной картотекой покончено."
    show mt angry
    mt "В каком смысле?"
    me "Ну, я перенес все данные пациентов…"
    show mt norm
    mt "А, ты об этом. Ну, что, молодец."
    "Искренняя похвала – и эго уже раздувает от важности."
    me "Могу ли я… Отправиться домой?"
    show mt angry
    mt "Это с чего еще?"
    me "Я ведь работаю до 18-ти часов, если не ошибаюсь. Не скостите часок в знак скверного самочувствия?"
    show mt smile
    mt "Ах, вот оно что. Без проблем. Только, напоследок, уберись в детской. Швабра в соседнем кабинете, как обычно."
    me "Вас понял. Разрешите унижаться?"
    show sl smile
    mt "Иди уже. Хотя, подожди-ка."
    me "Что-то еще?"
    mt "Завтра приходи ко второй смене, в 18 часов."
    th "Вторая смена? Что-то необычное."
    scene bg hoskom with dissolve
    "Лишь я, швабра и грязь… Странно, но после побега из плена монотонности даже подобная работенка воспринималась доброжелательно. Взгляд зацепился за детские рисунки, пробуждая в памяти недавние события."
    th "Я уж точно последний человек, кто готов признать правоту Мику. Но хоспис - явно последнее место, куда нужно приводить ребенка."
    show sl norm at right with dissolve
    sl "Семен, не отвлекаю?"
    "Я мотнул головой, но вышло как-то по-особенному глупо, отчего Славя немного смутилась."
    sl "Как твои дела?"
    me "Все отлично, спасибо."
    sl "Да? А по тебе и не скажешь…"
    me "Тогда лучше промолчать, не находишь?"
    show sl syrp
    "Девушка, очевидно, замялась; по крайней мере, воцарившиеся молчание свидетельствовало именно об этом."
    show sl sad
    sl "Знаешь, если у тебя проблемы, то это еще не повод грубить другим."
    me "Ты права. Но я в самом деле чувствую себя неважно."
    show sl norm
    sl "А что тогда случилось? Мику подробностями не делится, только все твердит о том, что ты чем-то отравился."
    th "Тебе мои проблемы точно ни к чему."
    me "Да, так и было. Попался вчерашний хлеб, вот все и завертелось…"
    show sl evil
    "Блондинка забавно нахмурила брови."
    sl "Ох, паршивую ты компанию выбрал."
    th "Вау, зачатки ревности? Повысим ставку."
    me "А как по мне, так она очень даже милая."
    sl "Да причем тут это?! Мику к окружающим серьезно не относится, мы для нее – подопытные кролики."
    th "Я уже успел в этом убедиться, да."
    me "И на таких горе-манипуляторов найдется управа, будь уверена."
    show sl norm
    sl "Семен, я не настраиваю тебя против Мику…"
    th "А по-моему, именно этим ты и занимаешься сейчас."
    sl "Просто я хочу, чтобы ты был осторожен. Вот и все."
    show sl smile
    me "Спасибо за заботу, Славя, в самом деле, спасибо, но мне уже чуть больше одиннадцати."
    "A собеседница все никак не унималась."
    show sl norm
    sl "В хосписе она явно не по своей воле, более того, родители не стесняются ее прикрывать, чуть что. Понимаешь?"
    me "Ага. Подожди, а как происходит, ну, этот процесс…Прикрытия?"
    show sl evil
    sl "Сложный вопрос…Наверное, отец Мику давит на Ольгу своим авторитетом."
    me "Скорее всего. Бестия, к слову, сегодня к нам не заявится?"
    show sl norm
    sl "Не знаю, извини. Мы ведь не подруги, чтобы она мне докладывала."
    me "Ясно. Слушай, я приступлю к работе, хорошо? Сама понимаешь: для мытья пола необходима полная концентрация."
    sl "Конечно."
    hide sl with dissolve
    "Настало время взяться на настоящее дело!"
    stop music fadeout 8
    $ renpy.pause (1.5)
    jump one_step_to_war