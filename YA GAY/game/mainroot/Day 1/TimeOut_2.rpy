label D1T2:
    scene KORIDOR
    play music "sounds/Universitet.mp3"
    with dissolve 
    "~ Интересно, какая там следующая пара? ~"
    "..."
    "~ Вроде сегодня их всего 3... ~"
    "~ Не многовато ли для понедельника? ~"
    "~ Ну, как говорится терпи, что еще тут поделаешь ~"
    show GOGA_OUTSIDE at left
    show BORYA_OUTSIDE at right
    show DIVAN_SMILE at center
    with dissolve
    g "Эй, Стас! Ау!?"
    s "М?"
    g "Что, опять в облаках витаешь?"
    s "А-а...да, так задумался просто, а в какой аудитории следующая пара?"
    b "1-492"
    d "Прости, мы с тобой еще не познакомились, так?"
    s "Все так"
    g "Давайте, я..."
    g "Стас, это Ваня"
    g "Ваня, это Стас"
    "Стас и Ваня пожимают руки"
    d "Ну, раз уж познакомились, тогда погнали в аудиторию"
    stop music
    g "Что ты сейчас сказал?"
    d "Эм..."
    d "Ну, идем в аудиторию. {w}Что-то не так?"
    g "И даже покурить не сходишь?"
    show DIVAN_SERIOUS at center
    d "Слушай, если я курящий, то это не значит, что я должен это делать при каждой удобной возможности"
    g "Все-все, не заводись, мы тебя поняли"
    d "Я пытался дать аргументированный ответ"
    b "Вы сегодня пойдете на пару или так и будете друг друга грызть?"
    b "Стас, ну же, скажи им"
    menu:
        "Вмешаться":
            $ karma += 1
            $ sociofob -= 1
            s "Эй ребят, не стоит ссориться по таким мелочам!"
            s "Все-таки, вы одногруппники и так грызетесь по пустякам"
            s "Давайте жить дружно, что-ли"
            "~ Я это вслух сказал сейчас? ~"
            hide DIVAN_SERIOUS
            show DIVAN_SMILE at center
            d "Да ладно, не переживай, у нас постоянно так"
            g "Грыземся, а потом на следующий день уже как братья."
            b "Чудаки..."
            s "А... Ну тогда мне не о чем беспокоиться?"
            g "Определенно."
            "~ Может все-таки не стоило вмешиваться? ~"
            "~ Я же не знаю, какие у них отношения. Может, они так шутят... ~"
            "~ ...и у них так заведено. ~"
            "~ Я же мало о них знаю на данный момент, и, возможно, мне не стоило лезть не в свое дело. ~"
            "~ Ладно, что сделано, то сделано. ~"
            g "Он вообще тут или нет?"
            s "А?"
            b "Стас, ты нас не пугай, хорошо?"
            g "Да, а то стоишь и пялишься в одну точку с минуту."
            d "А потом, будто током дернуло. Все в порядке?"
            s "Да, я просто думаю, нам нужно идти в аудиторию...{w}все хорошо."
            g "В таком случае пойдем, ребята, посмотрим, что там расскажут."
            d "Вперед."
            
        "Это не мое дело":
            $ karma -= 1
            $ sociofob += 1
            s "Я-я не знаю..." 
            s "Наверное это ваши проблемы"
            b "Стас, ну..."
            g "Да ладно мы шутим так, не волнуйтесь"
            hide DIVAN_SERIOUS
            show DIVAN_SMILE at center
            d "У нас постоянно такое"
            s "А-а...это всего лишь ш-шутка?"
            b "Да они снова разыгрывают цирк, даже я повелся"
            g "Ничего себе вы раздули"
            d "Это же шутка"
            "~ Ш-шутка? ~"
            "~ ... ~"
            "~ Я думал они это всерьез ~"
            "~ Но все же не стоит совать свой нос не в свои дела, так что.. ~"
            s "Думаю нам нужно идти в аудиторию...{w} все х-хорошо"
    hide GOGA_OUTSIDE
    hide BORYA_OUTSIDE
    hide DIVAN_SMILE
    with dissolve
    "~ Все в полном порядке, я уверен, что поступил правильно ~"
    jump D1P3