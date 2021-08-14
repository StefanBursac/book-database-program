from models import Base, session, Book, engine
import datetime
import csv


def menu():
    while True:
        print("""
            \nPROGRAMMING BOOKS
            \r1)Add book
            \r2)View All Books      
            \r3)Search for Book
            \r4)Book Analaysis
            \r5)Exit""")
        choice = input("What would you like to do")   

        if choice in ["1","2","3","4","5"]:
            return choice    
        else: 
            input("Please choose one of the above options, A number beetwen 1 and 5, press any key to continue")


def clean_date(date_str):
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    split_date = date_str.split(" ")
    month = int(months.index(split_date[0]) + 1)
    day = int(split_date[1].split(",")[0])
    year = int(split_date[2])
    return datetime.date(year, month, day)

def clean_price(price_str):
    price_float = float(price_str)
    return int(price_float * 100)


def add_csv():
    with open("suggested_books.csv") as csvfile:
        data = csv.reader(csvfile)
        for row in data:
            book_in_db = session.query(Book).filter(Book.title == row[0]).one_or_none()
            if book_in_db == None:
                title = row[0]
                author = row[1]
                date = clean_date(row[2])
                price = clean_price(row[3])
                new_book = Book(title = title, author = author, published_date = date, price = price)
                session.add(new_book)
        session.commit()

def app():
    app_running = True
    while app_running:
        choice =  menu()
        if choice == "1":
            pass
        elif choice == "2":
            pass
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        else:
            print("Good by")
            app_running = False
            

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    add_csv()
    # clean_date("October 25, 2017")
    # clean_price("10.10")
    for book in session.query(Book):
        print(book)