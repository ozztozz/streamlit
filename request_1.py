import streamlit as st


col01,col02=st.columns(2)
with col01:
    NAME=st.text_input('NAME')
    TITLE=st.text_input('TITLE')
    Dept=st.text_input('Dept')
with col02:
    Position=st.text_input('Position')
    DATE=st.date_input('DATE')
    REVISION_SPECIAL_NOTES=st.text_area('REVISION/SPECIAL NOTES')
    

tab1, tab2,tab3 = st.tabs(["Transport", "Hotel",'Rental Cars'])
with tab1:
    col11,col12=st.columns(2)
    with col11:
        AIRLINE=st.text_input('AIRLINE')
        FLIGHT=st.text_input('FLIGHT')
        DEPARTURE_CITY=st.text_input('DEPARTURE CITY')
        TRANSPORT_FROM_AIRPORT=st.text_input('TRANSPORT FROM AIRPORT')
        DEPART_TIME=st.time_input('DEPART TIME')
       
       
    with col12:

        ARRIVAL_CITY=st.text_input('ARRIVAL CITY')
        ARRIVE_TIME=st.time_input('ARRIVE TIME')
        TRANSPORT_TO_AIRPORT=st.text_input('TRANSPORT TO AIRPORT')
        PICKUP_TIME=st.time_input('PICKUP TIME')

        
with tab2:
    col21,col22=st.columns(2)
    with col21:
        Hotel=st.text_input('Hotel')
        Conf=st.text_input('Conf Number')
        IN=st.date_input('IN')
        OUT=st.date_input('OUT')
        Nights=st.number_input('Number of Nights')
    with col22:
        Rate=st.number_input('Rate per Night')
        Subtotal=st.number_input('Subtotal')
        Tax=st.number_input('Tax 15.25%')
        Parking=st.number_input('Parking')
        Total_Cost=st.number_input('Total Cost')
    Notes=st.text_area('Notes')



with tab3:
    col31,col32,col33=st.columns(3)
    with col31:
        Type=st.text_input('Type')
        Rent=st.date_input('Rent')
        Return=st.date_input('Return')
        rateM=st.number_input('Rate/Month')
        rateW=st.number_input('Rate/Week')
        rateD=st.number_input('Rate/Date')

    with col32:
        Months=st.number_input('Months')
        Weeks=st.number_input('Weeks')
        Days=st.number_input('Days')   
        T=st.number_input('T')
        VLF=st.number_input('VLF (.50/day)')
    with col33:
        Base_Total=st.number_input('Base Total')
        Concession_Fee=st.number_input('Concession Fee (11.11%)')
        Facility_Fee=st.number_input('Facility Fee ($5/day)')
        TAX=st.number_input('TAX 17.95%')
        Total=st.number_input('Total')
