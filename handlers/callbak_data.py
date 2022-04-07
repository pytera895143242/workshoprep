from aiogram import types
from misc import dp, bot
import asyncio
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from .sqlit import update_country,cheak_traf,reg_user,cheak_chat_id,get_country,update_status
import random

reg_user(0,0)
content_chat = -1001631961913

markup = types.InlineKeyboardMarkup()
bat_a = types.InlineKeyboardButton(text='Далее', callback_data='next')
markup.add(bat_a)

markup_goo = types.InlineKeyboardMarkup()
bat_a = types.InlineKeyboardButton(text='💥Гоооо💥', callback_data='goo')
markup_goo.add(bat_a)

markup_forward = types.InlineKeyboardMarkup()
bat_a = types.InlineKeyboardButton(text='💥Вперёд💥', callback_data='forward')
markup_forward.add(bat_a)

markup_two = types.InlineKeyboardMarkup()
bat_a = types.InlineKeyboardButton(text='💥Вторая часть💥', callback_data='two_part')
markup_two.add(bat_a)

markup_dalee = types.InlineKeyboardMarkup()
bat_a = types.InlineKeyboardButton(text='Далее', callback_data='dalee')
markup_dalee.add(bat_a)

markup_dalee2 = types.InlineKeyboardMarkup()
bat_a = types.InlineKeyboardButton(text='Далее', callback_data='dalee2')
markup_dalee2.add(bat_a)

markup_dalee3 = types.InlineKeyboardMarkup()
bat_a = types.InlineKeyboardButton(text='Далее', callback_data='dalee3')
markup_dalee3.add(bat_a)


markup_dalee4 = types.InlineKeyboardMarkup()
bat_a = types.InlineKeyboardButton(text='Далее', callback_data='dalee4')
markup_dalee4.add(bat_a)


markup_pognali = types.InlineKeyboardMarkup()
bat_a = types.InlineKeyboardButton(text='💥Погнали💥', callback_data='pognali')
markup_pognali.add(bat_a)

markup_aga = types.InlineKeyboardMarkup()
bat_a = types.InlineKeyboardButton(text='💥Ага💥', callback_data='aga')
markup_aga.add(bat_a)

markup_bonus = types.InlineKeyboardMarkup()
bat_a = types.InlineKeyboardButton(text='💥Забрать бонус💥', callback_data='get_bonus')
markup_bonus.add(bat_a)

markup_go_next= types.InlineKeyboardMarkup()
bat_a = types.InlineKeyboardButton(text='🔥Двигаемся дальше🔥', callback_data='go_next')
markup_go_next.add(bat_a)


markup_tgstart= types.InlineKeyboardMarkup()
bat_a = types.InlineKeyboardButton(text='💥Tgstart💥', callback_data='tgstart')
markup_tgstart.add(bat_a)


text_stop = """Ах шалунишка 😈 сначала смотри видос, потом тыкай)"""

BIGTEXT1 = """Такс, давай зафиксируем:

1) Создаём тг канал 
2) Придумываем название 
3) Делаем аватарку 
4) Придумываем красивую ссылку канала 

Советую сделать от души 🤗

Двигаемся дальше?"""

BIGTEXT2 = """Такс, давай зафиксируем:

1) Создаём бота для публикации 
2) Делаем 10 четких постов в канал 

1 бот из видео: @BotFather
2 бот из видео: @ControllerBot

Сайт балансер из видео: videocdn.tv

Советую делать от души 🤗

Двигаемся дальше?"""


BIGTEXT3 = """Такс, давай зафиксируем:

Тик ток даёт бесплатных подписчиков в канал, на данный момент это топовая площадка, которая позволяет получать большие объёмы.

Бот из видео, для скачки роликов с ютуба: @SaveYoutubeBot

Двигаемся дальше?"""


TEXTBONUS = """Смотри, это не просто бонус, которым можно подтереться и выкинуть!

Это реальный инструмент, где находятся твои деньги!

Вопрос, как ты это будешь использовать!

Сохраняй - https://telegra.ph/Tut-ssylki-na-reklamnye-birzhi-04-01

<code>Ну а мы двигаемся дальше, тыкай на кнопку👇</code>"""

PRICE_KZ = """<b>1 тариф:</b> стоимость - 2802 тенге
<b>2 тариф:</b> стоимость - 4708 тенге

Купить можно написав нам)
Сюда 👉 @TGstart_info

Обязательно пиши:
1) Tgstart 
2) Какой тариф?
3) С какой ты страны?

Пример сообщения:
Tgstart/ 2 тариф/ Казахстан 

Если нужно, мы тебя проконсультируем, расскажем, как оплатить и дадим доступ на программу."""


PRICE_KR = """<b>1 тариф:</b> стоимость - 480 сом
<b>2 тариф:</b> стоимость - 806 сом

Купить можно написав нам)
Сюда 👉 @TGstart_info

Обязательно пиши:
1) Tgstart 
2) Какой тариф?
3) С какой ты страны?

Пример сообщения:
Tgstart/ 2 тариф/ Кыргызстан 

Если нужно, мы тебя проконсультируем, расскажем, как оплатить и дадим доступ на программу."""

PRICE_UZB = """<b>1 тариф:</b> стоимость - 67 200 сум 
<b>2 тариф:</b> стоимость - 112 900 сум

Купить можно написав нам)
Сюда 👉 @TGstart_info

Обязательно пиши:
1) Tgstart 
2) Какой тариф?
3) С какой ты страны?

Пример сообщения:
Tgstart/ 2 тариф/ Узбекистан 

Если нужно, мы тебя проконсультируем, расскажем, как оплатить и дадим доступ на программу."""

class st(StatesGroup):
    step1 = State()
    step2 = State()
    step3 = State()
    step4 = State()
    step5 = State()


country = 'kz' #kz / kr / uzb

@dp.callback_query_handler(lambda call: True, state='*')
async def answer_push_inline_button(call, state: FSMContext):
    country = get_country(call.message.chat.id)[0]


    if call.data == 'crazy' or call.data == 'bad' or call.data == 'good':
        if call.data == 'crazy':
            await call.message.answer("Заебись) сейчас будет ещё лучше 😉")
        if call.data == 'bad':
            await call.message.answer("""Ничего, сейчас исправим 💪""")
        if call.data == 'good':
            await call.message.answer("""Хорошо, что не хренова. 
Сейчас поднимем настрой))""")

        await state.update_data(video1 = 'stop')
        await asyncio.sleep(3)
        await call.message.answer("""Не буду тянуть, начнём""")
        await asyncio.sleep(2)
        if country == 'kz':
            await bot.copy_message(chat_id=call.message.chat.id, from_chat_id=content_chat, message_id=21,caption = """<b>Как создать телеграм канал?
Какую нишу выбрать новичку?</b>
    
<code>После просмотра жми на кнопку👇</code>""",reply_markup=markup)
        if country == 'uzb':
            await bot.copy_message(chat_id=call.message.chat.id, from_chat_id=content_chat, message_id=296, caption="""<b>Как создать телеграм канал?
Какую нишу выбрать новичку?</b>

<code>После просмотра жми на кнопку👇</code>""", reply_markup=markup)
        if country == 'kr':
            await bot.copy_message(chat_id=call.message.chat.id, from_chat_id=content_chat, message_id=235, caption="""<b>Как создать телеграм канал?
Какую нишу выбрать новичку?</b>

<code>После просмотра жми на кнопку👇</code>""", reply_markup=markup)




        await asyncio.sleep(210) #210 секунд
        await state.update_data(video1 = 'start')


    if call.data == 'next':
        try:
            if ((await state.get_data())['video1']) == 'start':
                flag = True
            else:
                flag = False

        except:
            flag = True

        if flag == False:
            await call.message.answer(text_stop)

        else:
            await bot.send_message(text= BIGTEXT1, chat_id=call.message.chat.id, reply_markup=markup_forward)


    if call.data == 'forward':
        await state.update_data(video2='stop')
        await bot.copy_message(chat_id=call.message.chat.id, from_chat_id=content_chat, message_id=27, caption="""<b>Делаем контент в канал (1 часть)

Создаём своего бота для постов</b>""", reply_markup=markup_two)
        await asyncio.sleep(120) #120
        await state.update_data(video2='start')


    if call.data == 'two_part':
        try:
            if ((await state.get_data())['video2']) == 'start':
                flag = True
            else:
                flag = False

        except:
            flag = True

        if flag == False:
            await call.message.answer(text_stop)

        else:
            await state.update_data(video3='stop')
            await bot.copy_message(chat_id=call.message.chat.id, from_chat_id=content_chat, message_id=31, caption="""<b>Делаем контент в канал (2 часть)

Грузим посты</b>

<code>После просмотра жми на кнопку👇</code>""", reply_markup=markup_dalee)
            await asyncio.sleep(150)#150
            await state.update_data(video3='start')

    if call.data == 'dalee':
        try:
            if ((await state.get_data())['video3']) == 'start':
                flag = True
            else:
                flag = False

        except:
            flag = True

        if flag == False:
            await call.message.answer(text_stop)
        else:
            await bot.send_message(chat_id= call.message.chat.id, text=BIGTEXT2,reply_markup=markup_pognali)

    if call.data == 'pognali':
        await state.update_data(video4='stop')
        await bot.copy_message(chat_id=call.message.chat.id, from_chat_id=content_chat, message_id=37, caption="""<b>Как прокачать канал без вложений</b>""", reply_markup=markup_dalee2)
        await asyncio.sleep(120)#120
        await state.update_data(video4='start')

    if call.data == 'dalee2':
        try:
            if ((await state.get_data())['video4']) == 'start':
                flag = True
            else:
                flag = False

        except:
            flag = True

        if flag == False:
            await call.message.answer(text_stop)
        else:
            await bot.send_message(chat_id=call.message.chat.id,text=BIGTEXT3, reply_markup= markup_aga)


    if call.data == 'aga':
        await state.update_data(video5='stop')
        await bot.copy_message(chat_id=call.message.chat.id, from_chat_id=content_chat, message_id=47,
                               caption="""<b>Информативный ролик 

План работы в киношке 1234567

+ <tg-spoiler>ахуенный</tg-spoiler>  бонус 👌</b>""", reply_markup=markup_bonus)

        await asyncio.sleep(60)  # 60
        await state.update_data(video5='start')


    if call.data == 'get_bonus':
        try:
            if ((await state.get_data())['video5']) == 'start':
                flag = True
            else:
                flag = False

        except:
            flag = True

        if flag == False:
            await call.message.answer(text_stop)
        else:
            await bot.send_message(chat_id=call.message.chat.id, text=TEXTBONUS, reply_markup=markup_goo,disable_web_page_preview=True)



    if call.data == 'goo':
        await state.update_data(video6='stop')
        if country == 'kz':
            await bot.copy_message(chat_id=call.message.chat.id, from_chat_id=content_chat, message_id=53,
                                   caption="""<b>Декомпозиция 
    
Какой доход в кино тематике нам даёт рынок телеграма</b>""", reply_markup=markup_dalee3)

        if country == 'kr':
            await bot.copy_message(chat_id=call.message.chat.id, from_chat_id=content_chat, message_id=263,
                                   caption="""<b>Декомпозиция 

Какой доход в кино тематике нам даёт рынок телеграма</b>""", reply_markup=markup_dalee3)
        if country == 'uzb':
            await bot.copy_message(chat_id=call.message.chat.id, from_chat_id=content_chat, message_id=324,
                                   caption="""<b>Декомпозиция 

Какой доход в кино тематике нам даёт рынок телеграма</b>""", reply_markup=markup_dalee3)


        await asyncio.sleep(180)  #180
        await state.update_data(video6='start')


    if call.data == 'dalee3':
        try:
            if ((await state.get_data())['video6']) == 'start':
                flag = True
            else:
                flag = False

        except:
            flag = True

        if flag == False:
            await call.message.answer(text_stop)
        else:
            await state.update_data(golos='stop')
            await bot.copy_message(chat_id=call.message.chat.id, from_chat_id=content_chat, message_id=64,caption="""Такс, давай зафиксируем:""", reply_markup=markup_go_next)
            await state.update_data(golos='start')


    if call.data == 'go_next':
        try:
            if ((await state.get_data())['golos']) == 'start':
                flag = True
            else:
                flag = False

        except:
            flag = True

        if flag == False:
            await call.message.answer("Ах шалунишка 😈 сначала послушай подкаст, потом тыкай)")

        else:
            await state.update_data(video7='stop')
            await bot.copy_message(chat_id=call.message.chat.id, from_chat_id=content_chat, message_id=66, reply_markup=markup_dalee4)
            await asyncio.sleep(180)  # 180
            await state.update_data(video7='start')

    if call.data == 'dalee4':
        try:
            if ((await state.get_data())['video7']) == 'start':
                flag = True
            else:
                flag = False

        except:
            flag = True

        if flag == False:
            await call.message.answer(text_stop)

        else:
            await state.update_data(video8='stop')
            await bot.copy_message(chat_id=call.message.chat.id, from_chat_id=content_chat, message_id=70,reply_markup=markup_tgstart)
            await asyncio.sleep(120)#120
            await state.update_data(video8='start')


    if call.data == 'tgstart':
        try:
            if ((await state.get_data())['video8']) == 'start':
                flag = True
            else:
                flag = False

        except:
            flag = True

        if flag == False:
            await call.message.answer(text_stop)

        else:
            await types.ChatActions.upload_photo()
            media_kz = types.MediaGroup()
            if country == 'kz':
                media_kz.attach_photo(types.InputFile('kz1.jpg'), PRICE_KZ)
            if country == 'kr':
                media_kz.attach_photo(types.InputFile('kz1.jpg'), PRICE_KR)
            if country == 'uzb':
                media_kz.attach_photo(types.InputFile('kz1.jpg'), PRICE_UZB)
            media_kz.attach_photo(types.InputFile('kz2.jpg'))
            await bot.send_media_group(chat_id= call.message.chat.id, media=media_kz)


            await bot.copy_message(chat_id=call.message.chat.id, from_chat_id= content_chat, message_id=93,caption="""Как всё будет происходить, какой формат.

Послушай ☝️

@TGstart_info""")
            update_status(call.message.chat.id)



    await bot.answer_callback_query(callback_query_id=call.id)


