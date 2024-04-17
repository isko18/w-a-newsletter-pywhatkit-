import pywhatkit
import json

with open('phones.json', encoding='utf-8') as file:
    list_of_number = json.load(file)

# with open('photo.png', 'rb') as r:
#     photo = r.read()
photo = 'photo.png'
def send_message_inst():
    # Shorten the message to prevent URL length error
    message = """
        Хакни свой мозг 🧠 💻 Ultra COURSE 9 в 1  Летний ИНТЕНСИВ  👨🏻‍💻 iT+ENGLISH 🇺🇸   Летом Вас ждёт :    
        🔸Программирование 3 раза в неделю    
        🔸Английский 2 раза в неделю    
        🔸Разбор ИИ (искусственный интеллект)   
        🔸Тренинги с Senior программистами    
        🔸Сертификат    
        🔸Походы 🏕️    
        🔸Турниры (футбол, теннис, шашки)    
        🔸Походы в кино 🍿    
        🔸Кибер спорт 🤩 И всё это 5000с за месяц 🔥  Компьютер предоставляется 👍🏼 Без домашних заданий 99%практики  
        Лучшие специалисты города Ош👨🏻‍💻  🔺Количество мест ОГРАНИЧЕНО 🔺     
        Тел: 0704000705 (WhatsApp) Инстаграм: itpark_osh Адрес: Баялинова 1, ориентир гостиница Ош НУРУ
        """

    for k, v in list_of_number.items():
        phone = v['phone']
        pywhatkit.sendwhats_image(phone, photo , message, tab_close=True)
        if k == 1600:
            break

def main():
    send_message_inst()

if __name__ == '__main__':
    main()
