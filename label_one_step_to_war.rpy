label one_step_to_war:
    scene bg semen_room
    "Домой я заявился по-особенному усталый и утомленный."
    if bezum == -1:
        "Внимательно изучив презент Виолы и ознакомившись с немногочисленными отзывами в сети, я, в свойственной себе нерешительной манере, принял таблетку."
        "И до чего же она горькая! Усталость, вскоре, заботливо донесла меня до кровати…"
        scene bg black with dissolve
        $ renpy.pause (1.0)
        play music yaziv
        scene bg semen_room with dissolve
        th "Ну, здравствуй, мир!"
        "Подобно фениксу, я переродился. И новый Семен, свободный от бесчисленных «багов» старого разума, обнаружил себя самым счастливым человеком."
        "На здравый рассудок вновь можно опереться. Ночью встречал глубокий сон без намеков на психоделические зарисовки, а утром – прекрасное настроение."
        "Глупо, банально, вторично, согласен, но лишь лишившись чего-либо, начинаешь это ценить."
        "И, черт возьми, душевное здоровье – это точно именно то, без чего внятно существовать невозможно."
        "Я окинул взором лекарство, столь небрежно брошенное на компьютерном столе."
        th "Спасибо, дружище. Я верю, что ты еще можешь меня вытащить."
        "И после незначительных дел и бытовых забот, меня ожидал хоспис.."
    else:
        show anim prologue_keyboard_1
        anon "Эй, чувак, куда пропал?"
        th "Прости, приятель, нет настроения для бесед."
        "Оставив сообщение без какого-либо ответа, я кое-как дополз до кровати, после чего всесильный демиург нажал на кнопку «сон»."
        scene bg black with dissolve
        $ renpy.pause (1.5)
        scene bg semen_room with dissolve
        play music yaziv
        "Внезапно ночь закончилась, забрав с собой подругу бессонницу."
        "Противный писк будильника беспощадно растаптывает последнюю надежду выспаться."
        "Я, в свою очередь, робко накрываюсь одеялом, оттягивая неизбежное."
        "Когда же до меня дотянулся бойкий солнечный луч, не оставалось ничего, кроме как принять постыдную капитуляцию."
        "И после незначительных дел и бытовых забот, меня ожидал хоспис.."

    jump third_day