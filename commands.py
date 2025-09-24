from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from random import randint

router = Router()

bulshit = ["ой какая ты глупая", "ты вообще умеешь головой пользоваться", "ты уверенна что тебе вообще это надо?", "Это даже жалко.", "да у меня бабуля лучше решает чем ты", "Знай свое место.", "Просто встань уже на калени и сдайся. "]


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
    await message.answer("""…Наконец-то.  
Ты догадалась открыть эту жалкую коробку и пришла сюда.  
Неужели ты думала, что твой праздник пройдёт спокойно?  
Я подготовил испытания — и если сможешь пройти их, тогда, может быть… я признаю твою сообразительность.  

Но сначала — докажи, что ты знаешь, кто я.  
                         
example: flag<task0_flag>
                         
Можно уже хоть что то написать ☝️😒 """)
    await state.set_state(Quest.taskE)




@router.message(F.text.in_(["жопа", "Жопа", "ЖОПА"]))
async def jopa(message: Message):
    text = "ЖО" + "O" * randint(0, 5) + "П" + "A" * randint(1, 10)
    await message.answer(text)

# ---- TASK E ----
@router.message(Quest.taskE) 
async def taskE(message: Message, state: FSMContext): 
    text = """Я — кукла, лишённая сердца, 
    но стремящаяся стать богом. 
    Моё прошлое было стёрто из мирового древа, но осталось в нулях и единицах. 
    01010011 01001011 01010010 01001101 01000011 01001000 Расшифруй мое имя, 
    чтобы узнать ключ."""
    if message.text.strip().lower() == "flag<task0_flag>":
        await message.answer(text)
        await state.set_state(Quest.task0)
    else:
        await message.answer(bulshit[randint(0, len(bulshit)-1)])



# ---- TASK 0 ----
@router.message(Quest.task0)
async def task0(message: Message, state: FSMContext):
    if message.text.strip().lower() == "flag<scaramouche>":
        await message.answer(
            "Хм. Так ты всё же догадалась… Ты действительно рассекретила меня. И это только начало.\n"
            "Первое испытание:\n"
            "Я зашифровал послание шифром Виженера. Ключ — моё имя.\n"
            "Введи расшифровку."
        )
        await state.set_state(Quest.task1)
    else:
        await message.answer("Это даже жалко. Попробуй ещё раз.")


# ---- TASK 1 ----
@router.message(Quest.task1)
async def task1(message: Message, state: FSMContext):
    # ожидаемый ответ (например «HAPPYBIRTHDAY»)
    if message.text.strip().lower() == "flag<happybirthday>":
        await message.answer(
            "Вижу, что базовые шифры для тебя не проблема. Но не обольщайся.\n\n"
            "Второе испытание:\n"
            "Я сыграл мелодию на небесной арфе. Каждая нота соответствует букве на клавиатуре.\n"
            "Собери порядок букв и получи слово. Введи его."
        )
        await state.set_state(Quest.task2)
    else:
        await message.answer("Неверно. Ты уверена, что правильно поняла ключ?")


# ---- TASK 2 ----
@router.message(Quest.task2)
async def task2(message: Message, state: FSMContext):
    if message.text.strip().lower() == "flag<vision>":
        await message.answer(
            "Так-так… у тебя получается быстрее, чем я ожидал.\n\n"
            "Третье испытание:\n"
            "Посмотри на силуэт и назови героя. Из имени возьми первую букву — это и будет ответ."
        )
        await state.set_state(Quest.task3)
    else:
        await message.answer(bulshit[randint(0, len(bulshit)-1)])


# ---- TASK 3 ----
@router.message(Quest.task3)
async def task3(message: Message, state: FSMContext):
    if message.text.strip().lower() == "flag<k>":
        await message.answer(
            "Верно. Ты начинаешь узнавать Тейват не хуже меня.\n\n"
            "Четвёртое испытание:\n"
            "Отсканируй QR-код. Найди слово и введи его здесь."
        )
        await state.set_state(Quest.task4)
    else:
        await message.answer("Ха. Разуй глаза." + bulshit[randint(0, len(bulshit)-1)])


# ---- TASK 4 ----
@router.message(Quest.task4)
async def task4(message: Message, state: FSMContext):
    if message.text.strip().lower() == "flag<world>":
        await message.answer(
            "Ты и здесь справилась… Последний шаг — и мы закончим это представление.\n\n"
            "Заключительное испытание:\n"
            "Реши интеграл. Ответом должно быть число.\n"
            "Подсказка: результат должен дать 314."
        )
        await state.set_state(Quest.task5)
    else:
        await message.answer(bulshit[randint(0, len(bulshit)-1)])


# ---- TASK 5 ----
@router.message(Quest.task5)
async def task5(message: Message, state: FSMContext):
    if message.text.strip() == "flag<314>":
        await message.answer(
            "314… Верно.\nНеужели ты действительно прошла всё?\n"
            "Что ж. Возможно, в этот раз я позволю себе сказать…\n\n"
            "🎉 С днём рождения! 🎉\n\n"
            "Пусть этот мир, каким бы жалким он ни был, хотя бы сегодня подарит тебе немного радости.\n"
            "…Не обольщайся. В следующий раз всё будет сложнее."
        )
        await state.set_state(Quest.finish)
    else:
        await message.answer("Ха! Даже с математикой справиться не можешь?" + bulshit[randint(0, len(bulshit)-1)])


# ---- FINISH ----
@router.message(Quest.finish)
async def finish(message: Message):
    await message.answer("Испытания закончены. Наслаждайся праздником… пока можешь.")

