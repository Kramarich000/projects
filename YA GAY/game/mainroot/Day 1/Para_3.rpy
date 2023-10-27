label D1P3:
    scene PARA_INFA
    with fade
    show GOGA_OUTSIDE at center
    g "Не опоздали даже"
    hide GOGA_OUTSIDE
    show kyperprizrak
    with dissolve
    k_p "Итак, давайте начнем"
    "Ебать киберпризрак сасная девочка сука АХХАХАХАХХАХАХАХ"
    k_p "Зовут меня Константин Алексеевич и в этом семестре я буду вести у вас дисциплину под названием пользовательский интерфейс"
    k_p "И я сразу скажу, что будут 2 лабораторные: первая создать сайт, а вторая игрушку на JavaScript "
    "~ Скрипт, интересно ~"
    g "{color=#808080}Ты на нем делал хоть раз что-то?"
    s "{color=#808080}Ты о чем?"
    g "{color=#808080}Про скрипт говорю, ты делал на нем что-либо?"
    "~ Он что мои мысли читать умеет? ~"
    s "{color=#808080}Не пробовал, но у меня был знакомый, он этим увлекался"
    g "{color=#808080}А почему был?"
    s "{color=#808080}Ну не общаюсь я с ним уже что поделать"
    k_p "Так и по итогам этого семестра у нас будет зачет"
    b "{color=#808080}Ребят, а почему он лысый?"
    g "{color=#808080}Я видел адрес его почты, там было написано киберпризрак"
    b "Ахахахаха"
    s "Ахахахаха"
    k_p "Что это за смех? Поделитесь с нами"
    g "Простите, этого больше не повторится"
    k_p "Уж очень надеюсь"
    k_p "Итак, вопросы есть?"
    stud "..."
    k_p "Прекрасно"
    k_p "Так как в прошлом семестре у вас была дисциплина под названием сети и телекоммуникации, то я бы хотел освежить вашу память и поговорить сегодня немного об интернете в целом"
    k_p "Итак, я начинаю"
    nvl_1 "Интернет - глобальная информационная сеть, части которой логически взаимосвязаны друг с другом посредством единого адресного пространства, основанного на протоколе TCP/IP. Интернет состоит из множества взаимосвязанных компьютерных сетей и обеспечивает удаленный доступ к сервисам сети Интернет." with dissolve
    nvl_1 "Сервисы Интернет - сервисы, предоставляемые в сети Интернет пользователям, программам, системам, уровням, функциональным блокам. В сети Интернет сервисы реализованы в виде сетевых служб, доступ к которым реализуется как из локальной, так и из глобальной сети."
    nvl_1 "Наиболее распространенными Интернет-сервисами являются:"
    nvl_1 "1) Cлужба WWW;"
    nvl_1 "2) Cлужба передачи файлов FTP;"
    nvl_1 "3) Передача электронных сообщений и блоков данных (e-mail);"
    nvl_1 "4) Интернет-телефония - частный случай IP-телефонии, когда в качестве линий передачи телефонного трафика используются каналы сети Интернета. IP-телефония - технология, позволяющая использовать Интернет или другую IP-сеть в качестве средства организации и ведения международных и междугородных телефонных разговоров и передачи факсов в режиме реального времени."
    nvl_1 "5) Интернет-вещание - динамическое изменение информации, передаваемой по каналам Интернета: новостные ленты, видео, аудио, сообщения о результатах выборов и т.д."
    nvl clear
    nvl_1 "Служба WWW"
    nvl_1 'Служба WWW (World Wide Web) - основная служба в сети Интернет, позволяющая получать доступ к информации на любых серверах, подключенных к сети. Служба WWW представляет собой множество независимых, но взаимосвязанных серверов и предназначена для обмена текстовой, графической, аудио и видео-информацией. Работая с Web, пользователь последовательно соединяется с Web-серверами и получает информацию. WWW построена по схеме "клиент-сервер". В качестве клиента выступает браузер, который является также и интерпретатором HTML. Как интерпретатор, браузер в зависимости от команд (тегов) выполняет различные функции: размещение текста на экране, обмен информацией с сервером по мере анализа полученного HTML-текста и др.'
    nvl_1 "Служба WWW организована на принципах гиперсреды. Гиперсреда - технология представления информации в виде относительно небольших блоков, ассоциативно связанных друг с другом. WWW – это глобальное информационное пространство, основанное на физической инфраструктуре Интернета и протоколе передачи данных HTTP. Его образуют миллионы веб-сeрверов сети Интернет, расположенных по всему миру. WWW неразрывно связана с понятиями гипертекста и гиперссылки."
    nvl clear
    nvl_1 "Web-сервер"
    nvl_1 "Web-сервер – это программное обеспечение, отвечающее за прием запросов браузеров, поиск указанных файлов и возвращение их содержимого. Web-cерверы хранят информацию в виде текстовых файлов, называемых страницами Web-сервера. Помимо текста, такие страницы могут содержать ссылки на другие страницы, ссылки на графические изображения, аудио- и видеоинформацию, различные объекты ввода данных (поля, кнопки, формы и т. д.), а также другие объекты. Страницы Web представляют собой некоторое связующее звено между объектами различных типов."
    nvl_1 "Web-сервер является программой, запускаемой на подключённом к сети компьютере и использующей протокол HTTP для передачи данных. В простейшем виде такая программа получает по сети HTTP-запрос на определённый ресурс, находит соответствующий файл на локальном жёстком диске и отправляет его по сети запросившему компьютеру. Более сложные web-серверы способны динамически формировать ресурсы в ответ на HTTP-запрос."
    nvl clear
    nvl_1 "Web-браузер"
    nvl_1 "Для доступа к информации, расположенной на web-серверах, пользователи применяют специальные клиентские программы — браузеры."
    nvl_1 "Web-браузер - это программное обеспечение для просмотра web-сайтов, то есть для запроса web-страниц из WWW, для их обработки и вывода, и для реализации перехода от одной страницы к другой. Браузер — комплексное приложение для обработки и вывода разных составляющих web-страницы, и для предоставления интерфейса между web-сайтом и его посетителем. Браузер способен предварительно обрабатывать данные, отправляемые на сервер, а также обрабатывать и представлять результаты, полученные от сервера, в удобном для пользователя виде."
    nvl clear
    nvl_1 "В настоящее время существует четыре наиболее популярных web-браузера. К ним относятся Internet Explorer (IE), Netscape, Opera и Firefox. Большинство браузеров основано на одном ядре. Например, Netscape и Firefox основаны на ядре, которое называется Gecko. Между браузерами существует ряд отличий, например:"
    nvl_1 "Некоторые HTML-теги по-разному обрабатываются IE и Firefox"
    nvl_1 "IE и Firefox имеют абсолютно разные модели сообщений"
    nvl_1 "IE, в отличие от Firefox, не в полной мере поддерживает каскадируемые таблицы стилей Cascading Style Sheets (CSS) 2.0 о чем мы будем говорить позже"
    nvl_1 "Firefox, в отличие от IE, не имеет возможности запускать элементы управления ActiveX"
    nvl_1 "Последовательность обработки HTML-тегов при визуализации страницы отличается в различных браузерах, что иногда приводит к отличиям в получаемых страницах"
    k_p "Так в принципе основу я вам рассказал и отпущу вас сегодня пораньше"
    stud "Спасибо! До свидания!"
    jump D1M_CHILL

