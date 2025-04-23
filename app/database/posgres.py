import psycopg2
import uuid
import os

class posgres:
    def __init__(self):
        self.conn = psycopg2.connect(dbname=os.getenv("dbname"), user=os.getenv("user"), password=os.getenv("password"), host=os.getenv("host"))
        curs = self.conn.cursor()
        curs.execute(
            'CREATE TABLE IF NOT EXISTS records( \
                id uuid default gen_random_uuid(), \
                name varchar(20) not null, \
                created_at TIMESTAMP default NOW(), \
                marked boolean default false, \
                content text \
            )',
        )
        self.conn.commit()
        curs.close()

    def create(self, name: str , content: str) -> id:
        cursor = self.conn.cursor()
        cursor.execute(
            'INSERT INTO records (name, content) values(%s, %s) RETURNING id',
            (name, content),
        )
        new_uuid = cursor.fetchone()[0]
        self.conn.commit()
        cursor.close()
        return new_uuid

    def update(self, id: uuid.UUID, new_content: str):
        cursor = self.conn.cursor()
        cursor.execute(
            'UPDATE records SET content = %s WHERE id = %s', 
            (new_content, str(id))
        )
        self.conn.commit()
        cursor.close()

    def delete(self, id: uuid.UUID):
        cursor = self.conn.cursor()
        cursor.execute(
            'DELETE from records WHERE id = %s', 
            (str(id), )
        )
        self.conn.commit()
        cursor.close()

    def read(self, id: uuid.UUID) -> str:
        cursor = self.conn.cursor()
        cursor.execute(
            'SELECT content FROM records WHERE id = %s', 
            (str(id), ),
        )
        content = cursor.fetchone()[0]
        cursor.close()          
        return content
    
    def show_records(self):
        cursor = self.conn.cursor()
        cursor.execute(
            'SELECT id, name, created_at, marked FROM records', 
        )
        records = cursor.fetchall()
        cursor.close()          
        return records
    
    def mark(self, id: uuid.UUID)-> bool:
        cursor = self.conn.cursor()
        cursor.execute(
            'select marked from records WHERE id = %s',
            (str(id), ),
        )
        flag = cursor.fetchone()[0]
        if flag:
            return False
        cursor.execute(
            'UPDATE records SET marked = true WHERE id = %s',
            (str(id), ),
        )
        cursor.close()
        return True
