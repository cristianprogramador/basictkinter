from tkinter import *
from tkinter import Tk, Canvas, Label, Frame, Entry, Button, W, E, Listbox
import psycopg2

root = Tk()
root.title('Python & PostgreSQL')

#definimos la funcion de guardado
def save_new_student(name, age, address):
    conn = psycopg2.connect(
        dbname='postgres', 
        user='postgres', 
        password='isa20', 
        host='localhost',
        port='5432'
    )
    cursor = conn.cursor()
    query = '''INSERT INTO students (name, age, address) VALUES (%s, %s, %s)'''
    cursor.execute(query, (name, age, address))
    print('guardado')
    conn.commit()
    conn.close()
    # refresh listbox students
    display_students()

#Funcion que muestra en pantalla los students
def display_students():
    conn = psycopg2.connect(
        dbname='postgres', 
        user='postgres', 
        password='isa20', 
        host='localhost',
        port='5432'
    )
    cursor = conn.cursor()
    query = '''SELECT * FROM students'''
    cursor.execute(query)
    rows = cursor.fetchall()
    listbox = Listbox(frame, width=20, height=10)
    listbox.grid(row=10, columnspan=4, sticky=W+E)

    for row in rows:
        listbox.insert(END, row)

    conn.commit()
    conn.close()

#definimos la funcion de search de students
def search(id):
    conn = psycopg2.connect(
        dbname='postgres', 
        user='postgres', 
        password='isa20', 
        host='localhost',
        port='5432'
    )
    cursor = conn.cursor()
    query = '''SELECT * FROM students WHERE id = %s'''
    cursor.execute(query, (id))
    rows = cursor.fetchone()
    display_search_result(rows)
    conn.commit()
    conn.close()

#funcion de resultado de la busqueda  
def display_search_result(rows):
    listbox = Listbox(frame, width=20, height=1)
    listbox.grid(row=9, columnspan=4, sticky=W+E)
    listbox.insert(END, rows)
    

#canvas o ventana
canvas = Canvas(root, height=380, width=400)
canvas.pack()

frame = Frame()
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

label = Label(frame, text='Add a Student')
label.grid(row=0, column=1,)

#Name input
label = Label(frame, text='Name')
label.grid(row=1, column=0,)

entry_name = Entry(frame)
entry_name.grid(row=1, column=1,)

#Age input
label = Label(frame, text='Age')
label.grid(row=2, column=0,)

entry_age = Entry(frame)
entry_age.grid(row=2, column=1,)

#Address Input
label = Label(frame, text='Address')
label.grid(row=3, column=0,)

entry_address = Entry(frame)
entry_address.grid(row=3, column=1,)

#button
button = Button(frame, text='Add', command=lambda: save_new_student(
    entry_name.get(),
    entry_age.get(),
    entry_address.get()
))
button.grid(row=4, column=1, sticky=W+E)

#search data
label = Label(frame, text='Search Data')
label.grid(row=5, column=1)

label = Label(frame, text='Search By Id')
label.grid(row=6, column=0)

id_search = Entry(frame)
id_search.grid(row=6, column=1)

button = Button(frame, text='Search', command=lambda: search(
    id_search.get()
))
button.grid(row=6, column=2)



display_students()

root.mainloop()