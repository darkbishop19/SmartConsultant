import sqlite3

connection = sqlite3.connect('shop.db')
cursos = connection.cursor()


def create_tables():
    cursos.execute('''
    CREATE TABLE IF NOT EXISTS Goods(
    good_id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT not null,
    name TEXT not null,
    description TEXT,
    price FLOAT not null,
    max_duration INTEGER,
    country TEXT,
    available BOOLEAN not null
    )
    ''')

    cursos.execute('''
    CREATE TABLE IF NOT EXISTS Classification(
    class_id INTEGER PRIMARY KEY AUTOINCREMENT,
    service_name TEXT not null,
    weight FLOAT not null,
    good_id INTEGER not null,
    FOREIGN KEY (good_id) REFERENCES  Goods (good_id)
    )
    ''')


def add_goods_data():
    cursos.execute('''
    INSERT INTO Goods VALUES
    (2, 'vpn', 'VPN Москва', 'Подключение осуществляется к дата центрам расположенным в Москве', '10000.0', NULL, 'Russia', 'True' ),
    (3, 'vpn', 'VPN Санкт-Петербург', 'Подключение осуществляется к дата центрам расположенным в Санкт-Петербурге', '9000.0', NULL, 'Russia', 'True' )

    ''')

def add_classification_data():
    cursos.execute('''
    INSERT INTO Classification VALUES
    (1, 'chat gpt', '0.8', 1),
    (2, 'chat gpt', '0.0', 2),
    (3, 'chat gpt', '0.0', 3),
    (4, 'Битрикс', '0.2', 1),
    (5, 'Битрикс', '0.9', 2),
    (6, 'Битрикс', '0.9', 1),
    (7, 'Госуслуги Москвы', '0.0', 1),
    (8, 'Госуслуги Москвы', '1.0', 2),
    (9, 'Госуслуги Москвы', '0.8', 3);

    ''')

add_classification_data()
connection.commit()
connection.close()
