import streamlit as st


tab1, tab2 = st.tabs(["RFQ", "Hedge"])

with tab1:
    st.header("Advances RFQ")

    accepted_maturities = ['1Y','2Y','3Y']
    accepted_pay_freq = ['M','Q','S','A']
    with st.form(key='advance_rfq'):
        maturity = st.text_input('Maturity','3Y')
        if maturity in accepted_maturities:
            st.write('ok')
        else:
            st.error('Invalid maturity:'+str(accepted_maturities))           
        pay_freq = st.text_input('Pay Frequency','Q')
        st.form_submit_button('Quote')
    st.write('Fixed Rate: ')

with tab2:
    st.header("Hedge with Asset Swap")
    with st.form(key='hedge'):
        st.form_submit_button("Execute Hedge")
    st.write('Generated Trade Id:')