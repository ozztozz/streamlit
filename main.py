import streamlit as st
import sqlite3

def init_db():
    conn=sqlite3.connect('names.db')
    cursor=conn.cursor()
    cursor.execute('create table if not exists people(id integer primary key autoincrement ,name text)')
    conn.commit()
    conn.close()

def insert_name(name):
    conn=sqlite3.connect('names.db')
    cursor=conn.cursor()
    cursor.execute('insert into people (name) values (?)',(name,))
    conn.commit()
    conn.close()

def get_all_names():
    conn=sqlite3.connect('names.db')
    cursor=conn.cursor()
    cursor.execute('select id, name from people')
    rows=cursor.fetchall()
    conn.close()
    return rows

def delete_name(id):
    conn=sqlite3.connect('names.db')
    cursor=conn.cursor()
    cursor.execute('delete from people where id= ?',(id,))
    conn.commit()
    conn.close()

def update_name(id,new_name):
    conn=sqlite3.connect('names.db')
    cursor=conn.cursor()
    cursor.execute('update people set name= ? where id= ?',(new_name,id))
    conn.commit()
    conn.close()

def search_name(keyword):
    conn=sqlite3.connect('names.db')
    cursor=conn.cursor()
    cursor.execute('select id, name from people where name like ?',(f'%{keyword}%',))
    rows=cursor.fetchall()
    conn.close()
    return rows


st.title('Add Name to Database')

init_db()
name=st.text_input('Enter a name')
if st.button('Save'):
    if name.strip():
        insert_name(name.strip())
        st.success('Name saved successfullly.')

st.title('Search Names')
query=st.text_input('Enter Name')
if query:
    results=search_name(query)
    for row in results:
        st.write(f'{row[0]}. {row[1]} ')

st.title('Update Name')
names=get_all_names()
id_list=[row[0] for row in names]
selected_id=st.selectbox('Select for update',id_list)
new_name=st.text_input('Enter new name')
if st.button('Update'):
    if new_name.strip():
        update_name(selected_id,new_name.strip())
        st.success('Updated successfully.')


st.title('Delete a name')
names=get_all_names()
id_list=[row[0] for row in names]
selected_id=st.selectbox('Select Id to delete',id_list)
if st.button('Delete'):
    delete_name(selected_id)
    st.success('Deleted successfully')


names=get_all_names()
st.title('Saved Names')
st.subheader('Name List')
for row in names:
    st.write(f'{row[0]}. {row[1]}')

