from aiogram import Router, F
from aiogram.types import FSInputFile
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from random import randint

router = Router()

bullshit = ["Ой какая ты глупая.", "Ты вообще умеешь головой пользоваться?", "Ты уверенна, что тебе вообще это надо?",
            "Это даже жалко.", "Да у меня мать лучше решает, чем ты.", "Знай своё место!", "Какой от тебя прок?"
            "Просто встань уже на колени и сдайся!", "Мирская пыль!", "...Смешно.", "И это всё?",
            "Надеялся, что ты не будешь отвлекать меня по пустякам."]

import asyncio


async def send_with_typing(message, text: str, delay: float = 2.0):
    await message.bot.send_chat_action(message.chat.id, action="typing")
    await asyncio.sleep(delay)
    await message.answer(text)


# ---- Состояния ----
class Quest(StatesGroup):
    taskE = State()
    task0 = State()
    task1 = State()
    task2 = State()
    task3 = State()
    task4 = State()
    task5 = State()
    finish = State()


@router.message(CommandStart())
async def cmd_start(message: Message, state=FSMContext):
    await send_with_typing(message, "…Наконец-то.\n"
                                    "Ты догадалась открыть эту жалкую коробку и пришла сюда.\n"
                                    "Неужели ты думала, что твой праздник пройдёт спокойно?\n"
                                    "Я подготовил испытания — и если сможешь пройти их, тогда, "
                                    "может быть… я признаю твою сообразительность.\n\n"
                                    "Пример чтоб понимала: `flag<task0_flag>`\n\n"
                                    "Можно уже хоть что то написать ☝️😒 ")
    await state.set_state(Quest.taskE)


@router.message(F.text.in_(["жопа", "Жопа", "ЖОПА"]))
async def jopa(message: Message):
    text = "ЖО" + "O" * randint(0, 5) + "П" + "A" * randint(1, 10)
    await message.answer(text)


# ---- TASK E ----
@router.message(Quest.taskE)
async def taskE(message: Message, state: FSMContext):
    text = ("Я — кукла, лишённая сердца, но стремящаяся стать богом.\n"
            "Моё прошлое было стёрто из мирового древа, но осталось в нулях и единицах.\n\n"
            "`01010011 01001011 01010010 01001101 01000011 01001000`\n\n"
            "Расшифруй моё имя, чтобы узнать ключ.\n")
    if message.text.strip().lower() == "flag<task0_flag>":
        await send_with_typing(message, text)
        await state.set_state(Quest.task0)
    else:
        await send_with_typing(bullshit[randint(0, len(bullshit) - 1)])


# ---- TASK 0 ----
@router.message(Quest.task0)
async def task0(message: Message, state: FSMContext):
    if message.text.strip().lower() == "flag<scrmch>":
        await send_with_typing(message,
                               "Хм. Так ты всё же догадалась… Ты действительно рассекретила меня.\n\n"
                               "Но это только начало. Один из моих слуг ждет тебя в библиотеке для образованных.\n"
                               "Не таких как ты, разумеется.\n"
                               "Первое испытание:\n"
                               "Я отправил письмо. Хочу убедиться, что оно дошло в целости и сохранности.\n"
                               "Введи отправленное мной сообщение"
                               )
        await state.set_state(Quest.task1)
    else:
        await send_with_typing(message, bullshit[randint(0, len(bullshit) - 1)])


# ---- TASK 1 ----
@router.message(Quest.task1)
async def task1(message: Message, state: FSMContext):
    # ожидаемый ответ (например «HAPPYBIRTHDAY»)
    if message.text.strip().lower() == "flag<happybirthday>":
        await send_with_typing(message,
                               "Вижу, что базовые шифры для тебя не проблема. Но не обольщайся.\n\n"
                               "Теперь тащи своё тело как можно выше к небесам.\n"
                               "Второе испытание:\n"
                               "Я сыграл мелодию на небесной арфе. Каждая нота соответствует букве на клавиатуре.\n"
                               "Собери порядок букв и получи слово. Введи его.\n\n"
                               "Это может тебе помочь.\n"
                               "https://specy.github.io/genshinMusic"
                               )
        voice = FSInputFile("arpha.ogg")
        await message.answer_voice(voice)
        await state.set_state(Quest.task2)
    else:
        await send_with_typing(message, "Неверно. Ты уверена, что правильно поняла ключ?")


# ---- TASK 2 ----
@router.message(Quest.task2)
async def task2(message: Message, state: FSMContext):
    if message.text.strip().lower() == "flag<trash>":
        await send_with_typing(message,
                               "Так-так… у тебя получается быстрее, чем я ожидал.\n\n"
                               "Как говорится, чем выше заберешься, тем дольше падать. Пора отправляться под землю.\n"
                               "Третье испытание:\n"
                               "Посмотри на силуэты и назови героев. Из имен возьми первую букву — это и будет ответ."
                               )
        await state.set_state(Quest.task3)
    else:
        await send_with_typing(message, bullshit[randint(0, len(bullshit) - 1)])


# ---- TASK 3 ----
@router.message(Quest.task3)
async def task3(message: Message, state: FSMContext):
    if message.text.strip().lower() == "flag<jopa>":
        await send_with_typing(message,
                               "Верно. Ты начинаешь узнавать Тейват не хуже меня.\n\n"
                               "Теперь иди туда, где варят бодрящие зелья. Заведение, что за сторожевой башней\n"
                               "Четвёртое испытание:\n"
                               "Отсканируй QR-код. Найди слово и введи его здесь."
                               )
        await state.set_state(Quest.task4)
    else:
        await send_with_typing(message, "Ха. Разуй глаза." + bullshit[randint(0, len(bullshit) - 1)])


# ---- TASK 4 ----
@router.message(Quest.task4)
async def task4(message: Message, state: FSMContext):
    if message.text.strip().lower() == "flag<каноэ>":
        await send_with_typing(message,
                               "Ты и здесь справилась… Последний шаг — и мы закончим это представление.\n\n"
                               "Заключительное испытание:\n"
                               )
        photo = FSInputFile("integral.png")  # путь к картинке
        await message.answer_photo(photo, caption = "Сиди решай, может, хоть чему-то научишься. Ответом должно быть "
                                                   "число.\n")
        await state.set_state(Quest.task5)
    else:
        await send_with_typing(message, bullshit[randint(0, len(bullshit) - 1)])


# ---- TASK 5 ----
@router.message(Quest.task5)
async def task5(message: Message, state: FSMContext):
    if message.text.strip() == "flag<314>":
        # await send_with_typing(
        #     "314… Верно.\nНеужели ты действительно прошла всё?\n"
        #     "Что ж. Возможно, в этот раз я позволю себе сказать…\n\n"
        #     "🎉 С днём рождения! 🎉\n\n"
        #     "Пусть этот мир, каким бы жалким он ни был, хотя бы сегодня подарит тебе немного радости.\n"
        #     "…Не обольщайся. В следующий раз всё будет сложнее."
        # )
        video_note = FSInputFile("vv.mp4")
        await message.answer_video_note(video_note, length=640) 
        voice = FSInputFile("scaramouche-voicemessage.ogg")
        await message.answer_voice(voice)
        # await state.set_state(Quest.finish)
    else:
        await send_with_typing(message,
                               "Ха! Даже с математикой справиться не можешь?" + bullshit[randint(0, len(bullshit) - 1)])


# ---- FINISH ----
# @router.message(Quest.finish)
# async def finish(message: Message):
#     voice = FSInputFile("scaramouche-voicemessage.ogg")
#     await message.answer_voice(voice)
