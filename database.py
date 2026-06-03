import psycopg2

conn = psycopg2.connect(host='localhost',port='5432',user='postgres',password='7811',dbname='myduka')
print("connected successfully")
cur = conn.cursor()

conn=psycopg2.connect(host='localhost',port='5432',user='postgres',password='7811',dbname='myduka')
cur = conn.cursor()

cur.execute("SELECT * FROM products;")
products_data= cur.fetchall()
print (products_data)

cur.execute("insert into products(name,buying_price,selling_price)values('fridge',45000,55000)")
conn.commit()


product1=('DSTV',20000,50000)
product2=(z'LGTV',50000,80000)
insert_products2=(product1)
insert_products2=(product2)



def insert_products2(values):
    cur.execute("insert into products(name,buying_price,selling_price)values(%s,%s,%s)",values)
    conn.commit()

    product3=('book',1200,1800)
    insert_products2(product3)
    


    def get_products():
        cur.execute("SELECT * from PRODUCTS")
        products_data=cur.fetchall()
        return products_data

        
