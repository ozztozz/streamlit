
import streamlit as st
from sqlalchemy import create_engine,ForeignKey, Column, String, Date,Integer,Enum
from sqlalchemy.ext.declarative import declarative_base
from streamlit_sqlalchemy import StreamlitAlchemyMixin
from datetime import date

Base = declarative_base()

class UserModel(Base, StreamlitAlchemyMixin):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String)

DERSLER=('FEN','SOSYAL','TURKCE','MATEMATIK')
class TodoModel(Base, StreamlitAlchemyMixin):
    __tablename__ = "todo"

    id = Column(Integer, primary_key=True)
    user_id= ForeignKey(UserModel.id)
    task = Column(String)
    TARIH = Column(Date)

    __st_input_meta__={
        'task':  lambda *a, **kw: st.selectbox('DERS', DERSLER ),

    }



# Initialize the connection
CONNECTION = st.connection("todo_db", type="sql")   
Base.metadata.create_all(CONNECTION.engine)
StreamlitAlchemyMixin.st_initialize(CONNECTION)

# Create CRUD tabs
UserModel.st_crud_tabs()
TodoModel.st_crud_tabs()