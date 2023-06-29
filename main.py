from models import *
from database import session


def get_purchases_by_publisher(publisher_name):
    publisher = session.query(Publisher).filter_by(name=publisher_name).first()
    if publisher:
        books = session.query(Book).join(Stock).join(Shop).join(Sale). \
            filter(Book.id_publisher == publisher.id). \
            with_entities(
            Book.title,
            Shop.name,
            Sale.price,
            Sale.date_sale
        ).all()

        if books:
            for book in books:
                title, shop_name, price, date_sale = book
                print(
                    f"Название книги: {title} | Название магазина: {shop_name} | Стоимость покупки: {price} | Дата покупки: {date_sale}")
        else:
            print(f"Нет доступных фактов покупок для издателя '{publisher_name}'")
    else:
        print(f"Издатель с именем '{publisher_name}' не найден")


# Запрос имени издателя у пользователя
publisher_name = input("Введите имя издателя: ")

# Вызов функции для получения фактов покупок
get_purchases_by_publisher(publisher_name)
