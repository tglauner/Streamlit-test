import streamlit as st
import pandas as pd
import numpy as np

snow = st.button('Snow!')
if snow:
    st.snow()

tab1, tab2, tab3, tab4 = st.tabs(["RFQ", "Hedge", "Playground", 'Market Data'])



with tab1:
    st.header("Advances RFQ")

    accepted_maturities = ['1Y','2Y','3Y']
    accepted_pay_freq = ['M','Q','S','A']
    with st.form(key='advance_rfq'):
        notional = st.number_input('Notional')
        maturity = st.selectbox('Maturity',accepted_maturities)         
        pay_freq = st.selectbox('Pay Frequency',accepted_pay_freq)
        submitted_rfq = st.form_submit_button('Request for Quote')
    if submitted_rfq:
        st.write('REST call to be implemented')
        st.write('Fixed Rate: 3.12%')

with tab2:
    st.header("Hedge with Asset Swap")
    with st.form(key='hedge'):
        submitted_hedge = st.form_submit_button("Execute Hedge")
    
        if submitted_hedge:
            st.write('REST call to be implemented')
            st.write('Generated Trade Id: 65234SU')

with tab3:
    df = pd.DataFrame(np.random.randn(50, 20), columns=('col %d' % i for i in range(20)))
    st.dataframe(df)

with tab4:
    st.header('Market Data')
    #Fill with REST call
    d = {'Date': ['1D','1W','2W','3W', '1M'], 
         'Instrument': ['Overnight', 'Swap', 'Swap', 'Swap', 'Swap'], 
         'Rate': [1,1,1,1,1]}
    mktData = pd.DataFrame(data=d)
    st.write(mktData)
