
import streamlit as st
from sqlalchemy import Boolean, Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base, relationship
from streamlit_sqlalchemy import StreamlitAlchemyMixin

Base = declarative_base()



class User(Base, StreamlitAlchemyMixin):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String)
   

DERSLER=('FEN','SOSYAL','TURKCE','MATEMATIK')

class Task(Base, StreamlitAlchemyMixin):
    __tablename__ = "task"

    id = Column(Integer, primary_key=True)
    task = Column(String)
    done = Column(Boolean, default=False)
    soru=Column(Integer)
    hata=Column(Integer)
    due_date = Column(Date)

    user_id = Column(Integer, ForeignKey("user.id"))

    user = relationship("User", backref="tasks")

    __st_input_meta__ = {
        
        'task':  lambda *a, **kw: st.selectbox('DERS', DERSLER ),
        'due_date':  lambda *a, **kw: st.date_input('Tarih'),
        
    }