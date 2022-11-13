    
import sqlite3
conn = sqlite3.connect('Database/recipient.db')
c = conn.cursor()

def print_all_clients():

    # needed when startet from external file
    import sqlite3
    conn = sqlite3.connect('Database/recipient.db')
    c = conn.cursor()

    
    print('''
    Client Database:
    ''')
    try:
        c.execute('SELECT * FROM recipient')
        # list all clients in the database 
        for row in c.fetchall():
            print(row)
    except Exception as error:
        print(error)


def add_client():
    # needed when startet from external file
    import sqlite3
    conn = sqlite3.connect('Database/recipient.db')
    c = conn.cursor()



    print('''
    Add Client:
    ''')

    compname_input = input("Company Name: ")
    name_input = input("Name: ")
    street_input = input("Street: ")
    city_input = input("City: ")


    try: 
        # insert a client into the database with the given inputs
        c.execute(f'INSERT INTO recipient (company_name, name, street, city) VALUES ("{compname_input}", "{name_input}", "{street_input}", "{city_input}")')
        conn.commit()
    except Exception as error:
        print(error)


def delete_client():
    # needed when startet from external file
    import sqlite3
    conn = sqlite3.connect('Database/recipient.db')
    c = conn.cursor()


    print('''
    Delete Client:
    ''')
    try:
        # delete a client from the database
        c.execute(f'DELETE FROM recipient WHERE company_id = {input("Company ID: ")}')
        conn.commit()
    except Exception as error:
        print(error)


def update_client():
    # needed when startet from external file
    import sqlite3
    conn = sqlite3.connect('Database/recipient.db')
    c = conn.cursor()


    print('''
    Update Client:
    ''')
    try:
        compid_input = input("Company ID: ")
        # update a client in the database
        c.execute(f'UPDATE recipient SET company_name = {input("Company Name: ")}, name = {input("Name: ")}, street = {input("Street: ")}, city = {input("City: ")} WHERE company_id = {compid_input}')
        conn.commit()
    except Exception as error:
        print(error)


def search_client():
    # needed when startet from external file
    import sqlite3
    conn = sqlite3.connect('Database/recipient.db')
    c = conn.cursor()

    print('''
    Search Client:
    ''')
    try:
        # search for a client in the database
        c.execute(f'SELECT * FROM recipient WHERE company_id = {input("Company ID: ")}')
        print(c.fetchall())
    except Exception as error:
        print(error)


# not for the user only for the informations in the pdf
def pdf_input_get():

    

    # needed when startet from external file
    import sqlite3
    conn = sqlite3.connect('Database/recipient.db')
    c = conn.cursor()

    print('''
    Bill Client:
    ''')
    try:
        # search for a client in the database
        c.execute(f'SELECT company_name, name, street, city FROM recipient WHERE company_id = {input("Company ID: ")}')
        pdf_input_get.company_name, pdf_input_get.name, pdf_input_get.street, pdf_input_get.city = c.fetchone()
        
       
    except Exception as error:
        print(error)

def pdf_input_get_products():

    # needed when startet from external file
    import sqlite3
    conn = sqlite3.connect('Database/products.db')
    c = conn.cursor()

    print('''
    Bill Products:
    ''')
    try:
        # search for a client in the database
        c.execute(f'SELECT product_name, product_price FROM products WHERE id = {input("Product ID: ")}')
        pdf_input_get_products.product_name, pdf_input_get_products.product_price = c.fetchone()
        
       
    except Exception as error:
        print(error)

def add_product():
    # needed when startet from external file
    import sqlite3
    conn = sqlite3.connect('Database/products.db')
    c = conn.cursor()



    print('''
    Add Product:
    ''')

    productname_input = input("Product Name: ")
    productprice_input = input("Product Price: ")


    try: 
        # insert a client into the database with the given inputs
        c.execute(f'INSERT INTO products (product_name, product_price) VALUES ("{productname_input}", "{productprice_input}")')
        conn.commit()
    except Exception as error:
        print(error)

def delete_product():


    # needed when startet from external file
    import sqlite3
    conn = sqlite3.connect('Database/products.db')
    c = conn.cursor()


    print('''
    Delete Product:
    ''')
    try:
        # delete a client from the database
        c.execute(f'DELETE FROM products WHERE id = {input("Product ID: ")}')
        conn.commit()
    except Exception as error:
        print(error)


def update_product():
    # needed when startet from external file
    import sqlite3
    conn = sqlite3.connect('Database/products.db')
    c = conn.cursor()


    print('''
    Update Product:
    ''')
    try:
        compid_input = input("Product ID: ")
        # update a client in the database
        c.execute(f'UPDATE products SET product_name = {input("Product Name: ")}, product_price = {input("Product Price: ")} WHERE id = {compid_input}')
        conn.commit()
    except Exception as error:
        print(error)

    
conn.commit()
conn.close()