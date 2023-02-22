from creat import dp
from aiogram import Bot, Dispatcher, executor, types

total = 150

@dp.message_handler(commands=['start'])
async def mes_start(message: types.Message):
    await message.answer(f'''Привет, {message.from_user.first_name}. Давай сыграем в игру "Конфеты".\n
    На столе сейчас 150 конфет.
    Выбери максимальное колличество конфет с помощью команды "/set" и через пробел введи максимальное колличество конфет.
    \nНаример: "/set 200". Максимальное число конфет не должно превышать 1000 и не должно быть меньше 100.
    За один ход можно взять не больше 28ми конфет. Победит тот, кто последний заберет конфеты.
    Введите колличество конфет, которое хотите забрать:''')

@dp.message_handler(commands=['set'])
async def mes_settings(message: types.Message):
    global total
    count = int(message.text.split()[1])
    total = count
    if count < 1000 and count > 100:
        await message.answer(f'Максимальное колличество конфет {total}. Бери конфеты')
    else:
        await message.answer(f'Максимальное колличество конфет не может привышать 1000 конфет и не может быть меньше 100. Попробуй ввести другое число')

        

@dp.message_handler()
async def mes_all(message: types.Message):
    global total
    if message.text.isdigit():
        numbers = int(message.text)
        if numbers <= 28:
            total -= int(message.text)
            await message.answer(f'На столе осталось {total} конфет.')
            if total == 0:
                await message.answer('''Вы победили.
                На столе снова 150 конфет.
                Можешь поменять колличество конфет с помощью команды '/set "число" или сразу взять конфеты со стола''')
                total = 150
            else:    
                if total >= 57 or total == 29:
                    num = 28
                elif total > 29 and total < 57:
                    temp = 29
                    num = total - temp
                else:
                    num = total
                
                total -= num

                await message.answer(f'''Бот взял {num} конфет.
                На столе осталось {total} конфет.''')

                if total == 0:
                    await message.answer('''Бот победил.
                    На столе снова 150 конфет.
                    Можешь поменять колличество конфет с помощью команды '/set "число"' или сразу взять конфеты со стола''')
                    total = 150
        else:
            await message.answer(f'''Чтобы играть в игру, Вам нужно вводить числа. Числа положительные, которые не больше 28ми.\n
        Для ознакомления с игрой введите команду /start.''')
    else:
        await message.answer(f'''Чтобы играть в игру, Вам нужно вводить числа. Числа положительные, которые не больше 28ми.\n
    Для ознакомления с игрой введите команду /start.''')