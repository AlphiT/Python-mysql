import pymysql.cursors

def insertProduct(name, price, imageURL, description):
    connection = pymysql.connect(
        host = "localhost",
        user = "root", 
        password = "alpalp5858",
        database = "node_app"
    )   
    cursor = connection.cursor()

    sql = "INSERT INTO product(name,price,imageURL,description) VALUES (%s,%s,%s,%s)"
    values = (name, price, imageURL, description)

    cursor.execute(sql, values)
    
    try:
        connection.commit()
        print(f'{cursor.rowcount} tane kayıt eklendi.')
        print(f'Son eklenen kayıt id: {cursor.lastrowid}')
    except pymysql.connect.Error as err:
        print("hata: ", err)
    finally:
        connection.close()
        print("Database bağlantısı kapandı.")

def insertProducts(list):
    connection = pymysql.connect(
        host = "localhost",
        user = "root", 
        password = "alpalp5858",
        database = "node_app"
    )   
    cursor = connection.cursor()

    sql = "INSERT INTO product(name,price,imageURL,description) VALUES (%s,%s,%s,%s)"
    values = list

    cursor.executemany(sql, values)
    
    try:
        connection.commit()
        print(f'{cursor.rowcount} tane kayıt eklendi.')
        print(f'Son eklenen kayıt id: {cursor.lastrowid}')
    except pymysql.connect.Error as err:
        print("hata: ", err)
    finally:
        connection.close()
        print("Database bağlantısı kapandı.")

list = []
while True:
    name = input("Ürün Adı: ")
    price = float(input("Ürünün Fiyatı: "))
    imageURL = input("Ürünün Resmi: ")
    description = input("Ürün Açıklaması: ")

    list.append((name, price, imageURL, description))
    
    result = input("devam etmek istiyor musunuz? (e/h)")
    if result == 'h':
        print('Kayıtlarınız veritabanına aktarılıyor...')
        print(list)
        insertProducts(list)
        break
#insertProduct(name, price, imageURL, description)