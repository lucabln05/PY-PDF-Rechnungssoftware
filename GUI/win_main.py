def main_window():
    from tkinter import ttk
    import tkinter as tk
    import sqlite3


    # get conntent from database and return it as a list
   
    def View():

            con1 = sqlite3.connect("Database/recipient.db")

            cur1 = con1.cursor()

            cur1.execute("SELECT * FROM recipient")
            rows = cur1.fetchall()    
            for row in rows:

                print(row) 

                tree.insert("", tk.END, values=row)        

            con1.close()

    def View_products():

        con1 = sqlite3.connect("Database/products.db")

        cur1 = con1.cursor()

        cur1.execute("SELECT * FROM products")
        rows = cur1.fetchall()    
        for row in rows:

            print(row) 

            tree2.insert("", tk.END, values=row)        

        con1.close()


    root = tk.Tk()


    # create Treeview with 5 columns that will be display data from database
    tree = ttk.Treeview(root, column=("c1", "c2", "c3", "c4", 'c5'), show='headings')

    tree.column("#1", anchor=tk.CENTER)
    tree.heading("#1", text="ID")

    tree.column("#2", anchor=tk.CENTER)
    tree.heading("#2", text="Company")

    tree.column("#3", anchor=tk.CENTER)
    tree.heading("#3", text="Name")

    tree.column("#4", anchor=tk.CENTER)
    tree.heading("#4", text="Street")

    tree.column("#5", anchor=tk.CENTER)
    tree.heading("#5", text="City")

    tree.pack()
    View()
        
    # add secound list that will display data from database products
    tree2 = ttk.Treeview(root, column=("c1", "c2", "c3"), show='headings')

    tree2.column("#1", anchor=tk.CENTER)
    tree2.heading("#1", text="ID")

    tree2.column("#2", anchor=tk.CENTER)
    tree2.heading("#2", text="Product")

    tree2.column("#3", anchor=tk.CENTER)
    tree2.heading("#3", text="Price")

    tree2.pack()
    View_products()


    # delete a client with pressing it in the treeview
    def delete():

        x = tree.selection()[0]
        tree.delete(x)
        # remove I000 from  x and convert it to int
        x = int(x[1:])
        print(x)
        # remove client from the treeview
        

        con1 = sqlite3.connect("Database/recipient.db")
        cur1 = con1.cursor()
        #remove client from the database
        cur1.execute(f"DELETE FROM recipient WHERE company_id = {x}")
        con1.commit()
        con1.close()




    # add 3 textboxes with title for the user to input data for a new client
    def add():
        
            # create a new window
            add_window = tk.Toplevel(root)
            add_window.title("Add Client")
            add_window.geometry("300x200")
        
            # create a label and a textbox for the company name
            compname_label = tk.Label(add_window, text="Company Name: ")
            compname_label.grid(row=0, column=0)
            compname_entry = tk.Entry(add_window)
            compname_entry.grid(row=0, column=1)
        
            # create a label and a textbox for the name
            name_label = tk.Label(add_window, text="Name: ")
            name_label.grid(row=1, column=0)
            name_entry = tk.Entry(add_window)
            name_entry.grid(row=1, column=1)
        
            # create a label and a textbox for the street
            street_label = tk.Label(add_window, text="Street: ")
            street_label.grid(row=2, column=0)
            street_entry = tk.Entry(add_window)
            street_entry.grid(row=2, column=1)
        
            # create a label and a textbox for the city
            city_label = tk.Label(add_window, text="City: ")
            city_label.grid(row=3, column=0)
            city_entry = tk.Entry(add_window)
            city_entry.grid(row=3, column=1)
        
            # create a button to add the client to the database and the treeview
            add_button = tk.Button(add_window, text="Add", command=lambda: add_client(compname_entry.get(), name_entry.get(), street_entry.get(), city_entry.get()))
            add_button.grid(row=4, column=1)
        
            # add the client to the database and the treeview
            def add_client(compname, name, street, city):
        
                con1 = sqlite3.connect("Database/recipient.db")
                cur1 = con1.cursor()
        
                # insert a client into the database
                cur1.execute(f"INSERT INTO recipient (company_name, name, street, city) VALUES ('{compname}', '{name}', '{street}', '{city}')")
                con1.commit()
        
                # get the last inserted client from the database
                cur1.execute("SELECT * FROM recipient ORDER BY company_id DESC LIMIT 1")
                rows = cur1.fetchall()    
                for row in rows:
        
                    print(row) 
        
                    # insert the last inserted client into the treeview
                    tree.insert("", tk.END, values=row)
                
                con1.close()



    # create a button to delete a client
    delete_button = tk.Button(root, text="Delete", command=delete)
    delete_button.pack()

    # create a button to add a client
    add_button = tk.Button(root, text="Add", command=add)
    add_button.pack()


    root.title("Client List")
    root.mainloop()







