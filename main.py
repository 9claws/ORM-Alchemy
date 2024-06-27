import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models import create_tables, Publisher, Book, Stock, Shop, Sale

DSN = "postgresql://postgres:Pderfhm86@localhost:5432/ORM_db"
engine = sqlalchemy.create_engine(DSN)
create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()


pub_1 = Publisher(id=1, name='Пушкин')
pub_2 = Publisher(id=2, name='Гоголь')
pub_3 = Publisher(id=3, name='Толстой')

session.add(pub_1)
session.add(pub_2)
session.add(pub_3)
session.commit()

book_1 = Book(id=1, title='Капитанская дочь', publisher_id=1)
book_2 = Book(id=2, title='Руслан и людмила', publisher_id=1)
book_3 = Book(id=3, title='Мёртвые души', publisher_id=2)
book_4 = Book(id=4, title='Война и Мир', publisher_id=3)
book_5 = Book(id=5, title='Ревизор', publisher_id=2)

session.add(book_1)
session.add(book_2)
session.add(book_3)
session.add(book_4)
session.add(book_5)
session.commit()

shop_1 = Shop(name='Буквоед')
shop_2 = Shop(name='Книжный дом')

session.add(shop_1)
session.add(shop_2)
session.commit()

stock_1 = Stock(id=1, book_id=1, shop_id=1, count=10)
stock_2 = Stock(id=2, book_id=2, shop_id=2, count=10)
stock_3 = Stock(id=3, book_id=3, shop_id=1, count=20)
stock_4 = Stock(id=4, book_id=4, shop_id=2, count=10)
stock_5 = Stock(id=5, book_id=5, shop_id=1, count=20)

session.add(stock_1)
session.add(stock_2)
session.add(stock_3)
session.add(stock_4)
session.add(stock_5)
session.commit()

sale_1 = Sale(id=1, price=750.00, date_sale='27.05.2023', id_stock=1, count=3)
sale_2 = Sale(id=2, price=450.00, date_sale='10.04.2023', id_stock=2, count=5)
sale_3 = Sale(id=3, price=340.00, date_sale='15.08.2023', id_stock=3, count=7)
sale_4 = Sale(id=4, price=330.00, date_sale='11.06.2023', id_stock=4, count=2)
sale_5 = Sale(id=5, price=800.00, date_sale='14.09.2023', id_stock=5, count=1)
sale_6 = Sale(id=6, price=750.00, date_sale='16.06.2023', id_stock=1, count=7)

session.add(sale_1)
session.add(sale_2)
session.add(sale_3)
session.add(sale_4)
session.add(sale_5)
session.add(sale_6)
session.commit()


request = input('Input Publisher.name or Publisher.id: ')
query = session.query(Book.title, Shop.name, Sale.price, Sale.date_sale).join(Publisher).join(Stock).join(Shop).join(Sale)
if request.isdigit():
    query = query.filter(Publisher.id == request).all()
else:
    query = query.filter(Publisher.name == request).all()

for title, name, price, date_sale in query:
    print(f"{title:<20} | {name:<10} | {price:<8} | {date_sale}")

session.commit()
session.close()