from datetime import datetime
from pathlib import Path

import streamlit as st

from models import Base, Task, User
from streamlit_sqlalchemy import StreamlitAlchemyMixin



def _display_inline():
    """
    Make the columns inline.
    (https://stackoverflow.com/questions/69492406/streamlit-how-to-display-buttons-in-a-single-line)
    """
    st.markdown(
        """
        <style>
            div[data-testid="column"] {
                width: fit-content !important;
                flex: unset;
            }
            div[data-testid="column"] * {
                width: fit-content !important;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


def show_single_task(task):
    col1, col2, col3 = st.columns([1, 1, 1])
    if task.done:
        col1.write(f" - ~~{task.task}~~")
        with col2:
            task.st_delete_button()
    else:
        if task.due_date:
            date_color = "red" if task.due_date < datetime.today().date() else "green"
            col1.write(
                f" - {task.task} (:{date_color}[{task.due_date.strftime('%d.%m.%Y')}])"
            )
        else:
            col1.write(f" - {task.description}")
        with col2:
            task.st_edit_button("Done", {"done": True})
        with col3:
            task.st_delete_button()

def user_info(user):
    st.session_state.ogrenci=user.id
               
def app():
    
    with CONNECTION.session as db_session:
        for user in db_session.query(User).all():
            with st.sidebar:
               
                st.button(user.name,key=user.id,on_click=user_info,args=[user])
                

@st.dialog("Ders Ekle")
def add_task(user_id):
    form_ders=Task.st_create_form(defaults={"user_id":user_id, "done": False,'hata':0})
    if form_ders:
        st.rerun()

                        


def main():
    if not Path("example.db").exists():
        Base.metadata.create_all(CONNECTION.engine)

    # initialize the StreamlitAlchemyMixin
    StreamlitAlchemyMixin.st_initialize(connection=CONNECTION)
    if 'ogrenci'not in st.session_state:
        st.session_state.ogrenci=None
        st.title('Ogrenci Seciniz')

    if st.session_state.ogrenci:
        user_id=st.session_state.ogrenci
        if st.button('Ders Ekle'):
            add_task(user_id)
        user=CONNECTION.session.query(User).get(user_id)
        st.subheader(f'{user.name} Program')
        #Task.st_create_form(defaults={"user_id":user_id, "done": False})
        c = st.container()

        with c:
            if not user.tasks:
                st.caption("No tasks yet.")

            for task in user.tasks:
                show_single_task(task)

    

    # make the columns inline
    _display_inline()

    # use the logs as toasts in the app
    #_configure_logging()

    # the actual app
    app()


if __name__ == "__main__":
    # initialize the database connection
    # (see https://docs.streamlit.io/library/api-reference/connections/st.connection)
    CONNECTION = st.connection("example_db", type="sql")
    main()