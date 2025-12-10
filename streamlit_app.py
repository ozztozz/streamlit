import streamlit as st

if 'role' not in st.session_state:
    st.session_state.role=None
ROLES=[None,'Requester','Responder','Admin']


def login():
    st.header('Log in')
    user_name=st.text_input('User Name' )
    st.write('Hint: Admin')
    password=st.text_input('Password ',type='password')
    st.write('Hint: 12345')
    if st.button('Log İn'):
        if user_name =='Admin' and password=='12345':
            st.session_state.role='Admin'
            st.rerun()
        else:
            st.session_state.role='Admin'
            st.error('Login failed')
            st.rerun()

def logout():
    st.session_state.role=None
    st.rerun()

role=st.session_state.role

logout_page=st.Page(logout,title='Log out',icon=":material/logout:")
settings=st.Page('settings.py', title='Settings',icon=":material/settings:")

request_1=st.Page(
    'request/request_1.py',
    title='Master Movement',
    icon=":material/help:",
    default=(role == 'Requester')
)
request_2= st.Page(
    'request/request_2.py',
    title='Travelers',
    icon=":material/bug_report:"

)



acount_pages=[logout_page,settings]
admin_pages=[request_1,request_2]



st.title('Travel Logger')
st.logo(
    "images/horizontal_blue.png",
    icon_image="images/icon_blue.png"
)

page_dict={}

if st.session_state.role in ['Requester','Admin']:
    page_dict['Request']=admin_pages
if st.session_state.role == "Admin":
    page_dict['Request']=admin_pages


print(page_dict)
if len(page_dict)>0:
    pg=st.navigation({'Account':acount_pages} | page_dict)
else:
    pg=st.navigation([st.Page(login)])

pg.run()