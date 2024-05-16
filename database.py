import sqlite3
import pandas as pd


class Database:
    def __init__(self):
        self.conn = sqlite3.connect('plants')
        self.cursor = self.conn.cursor()
        self.table_columns = ["рослина", "ціна", "кількість", "опис"]

    def add_data(self):
        id = input("ID: ")
        name = input("Назва: ")
        price = input("Ціна: ")
        description = input("Опис: ")
        quantity = input("Кількість: ")
        self.cursor.execute("INSERT INTO data (id, name, price, description, quantity) VALUES (?, ?, ?, ?, ?)", 
                            (id, name, price, description, quantity))
        self.conn.commit()
        

    def delete_data(self):
        id = input("ID: ")
        self.cursor.execute("DELETE FROM data WHERE id LIKE '%{id}%'", (id))
        self.conn.commit()

    def see_all_data(self):
        self.cursor.execute("SELECT * FROM data")
        data = self.cursor.fetchall()
        if(data):
            return pd.DataFrame(data)
        else:
            return None

    def see_all_plant_quantity(self):
        data = self.see_all_data()
        if data is not None:
            return len(data)
        else:
            return None


    def build_select_query(self, entities, actions):
        query_start = 'SELECT name'
        if actions['наявність рослини']:
            query_start += " , quantity"
        if actions['опис рослини']:
            query_start += ", description"
        if actions['ціна рослини']:
            query_start += ", price "
        if actions['кількість рослини']:
            query_start += ", quantity "


        if query_start == 'SELECT name':
            query_start = "SELECT * FROM DATA"
        else:
            query_end = ' FROM DATA'
            if query_start != "SELECT * FROM DATA":
                if(len(entities)):
                    query_end += ' WHERE '
                    for i in range (len(entities)):
                        query_end += f"name LIKE '%{entities[i].lemma_}%'"
                        # print(entities[i].lemma_)
                        if i < len(entities) - 1:
                            query_end += " OR " 
                    query = query_start + query_end
                else:
                    query = "SELECT * FROM DATA"
        return query

    def see_plant_data(self, entities, actions):
        query = self.build_select_query(entities, actions)
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        if result:
            return pd.DataFrame(result)
        else:
            return None


    
