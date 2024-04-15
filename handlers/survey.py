from aiogram import Router,F,types
from aiogram.fsm.state import State,StatesGroup
from aiogram.fsm.context import FSMContext


survey_router=Router()


class BookSurvey(StatesGroup):
    name=State()
    age=State()
    gender=State()
    genre =State()


@survey_router.callback_query(F.data=="survey")
async def start_survey(cb:types.CallbackQuery, state: FSMContext):
    await cb.answer()
    await state.set_state(BookSurvey.name)
    await cb.message.answer("Как вас зовут?")


@survey_router.message(BookSurvey.name)
async def process_name(message:types.Message,state:FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(BookSurvey.age)
    await message.answer(f"Сколько вам лет,{message.text}?")
    
  

@survey_router.message(BookSurvey.age)
async def process_name(message:types.Message,state:FSMContext):
    age=message.text
    if not age.isdigit():
        await message.answer("Пожалуйста , ведите число")
        return
    if int(age) < 10 or int(age)>100:
        await message.answer("Введите число от 10-100")
        return
    await state.update_data(age=int(age))
    await state.set_state(BookSurvey.gender)
    await message.answer("Укажите пол?")



@survey_router.message(BookSurvey.gender)
async def process_name(message:types.Message,state:FSMContext): 
    await state.update_data(gender=message.text)
    await state.set_state(BookSurvey.genre)
    await message.answer("Какой любимый ваш жанр?")


@survey_router.message(BookSurvey.genre)
async def process_name(message:types.Message,state:FSMContext):
    await state.update_data(genre=message.text)
    await message.answer("спасибо за пройденный опрос")

    