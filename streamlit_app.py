import streamlit as st
st.session_state.role='Admin'
role=st.session_state.role
ROLES=[None,'Requester','Responder','Admin']


request_1=st.Page(
    'request_1.py',
    title='Master Movement',
    icon=":material/help:",
    default=(role == 'Requester')
)
request_2= st.Page(
    'request_2.py',
    title='Travelers',
    icon=":material/bug_report:"

)




admin_pages=[request_1,request_2]



st.title('Travel Logger')


page_dict={}
page_dict['Travel Log']=admin_pages


pg=st.navigation(page_dict)
pg.run()