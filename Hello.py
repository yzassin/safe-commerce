import streamlit as st
from streamlit.logger import get_logger
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn import svm
import pickle

LOGGER = get_logger(__name__)
loaded_model = pickle.load(open('best_svm_model.sav','rb'))


def fraud_predction(input_data):

    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    fraud = loaded_model.predict(input_data_reshaped)
    print(fraud)

def run():
    st.set_page_config(
        page_title="SafE-commerce",
        page_icon="💰",
    )

    st.write("# Welcome to SafE-Commerce!")

    st.markdown(
    """
        A web platform designed to track fraudulent activity within e-commerce transactions.
    """
    )

    No_Transactions = st.slider("Number of Transactions", min_value=1, max_value=10, value=1)
    No_Orders = st.slider("Number of orders ", min_value=1, max_value=10, value=1)
    No_Payments = st.slider("Payments Attempt", min_value=1, max_value=10, value=1)
    Total_transaction_amt = st.text_input("Transaction Amount")
    Transaction_fail = st.radio("Transaction Fail?", 
                                ('Yes', 'No'))


    if Transaction_fail == 'yes':
        Transaction_fail = 1
    else:
        Transaction_fail = 0

    Payment_method_fail = st.radio("Payment Method Fail?",
                                  ('Yes', 'No'))

    if Payment_method_fail == 'yes':
        Payment_method_fail = 1
    else:
        Payment_method_fail = 0

    Payment_method = st.selectbox("Method Payment", 
                                  ["Apple Pay", "Bitcoin", "PayPal", "Card"])
    
    apple_pay = 0
    bitcoin = 0
    paypal = 0
    card = 0
    if Payment_method == 'apple_pay':
        apple_pay = 1
    elif Payment_method == 'bitcoin':
        bitcoin = 1
    elif Payment_method == 'paypal':
        paypal = 1
    elif Payment_method == 'card':
        card = 1
    
    Order_status = st.radio("Current status of the order", 
                            ["Failed", "Fulfilled", "Pending"])
    
    failed_satus = 0
    fulfilled_status = 0
    pending_status = 0

    if Order_status == 'Failed':
        failed_satus = 1
    elif Order_status == 'Fulfilled':
        fulfilled_status = 1
    elif Order_status == 'Pending':
        pending_status = 1

    Payment_provider = st.selectbox("Method Payment", 
                                  ["American Express", "Diners Club", "Discover", "JCB 15", "JCB 16", "Maestro", "Mastercard", "Visa 13", "Visa 16", "Voyager"])
    
    american_express = 0
    diners_club = 0
    discover = 0
    jcb_15 = 0
    jcb_16 = 0
    Maestro = 0
    Mastercard = 0
    visa_13 = 0
    visa_16 = 0
    voyager = 0

    if Payment_provider == 'american_express':
        apple_pay = 1
    elif Payment_provider == 'diners_club':
        bitcoin = 1
    elif Payment_provider == 'discover':
        paypal = 1
    elif Payment_provider == 'jcb_15':
        card = 1
    elif Payment_provider == 'jcb_16':
        bitcoin = 1
    elif Payment_provider == 'Maestro':
        paypal = 1
    elif Payment_provider == 'Mastercard':
        card = 1
    elif Payment_provider == 'visa_13':
        bitcoin = 1
    elif Payment_provider == 'visa_16':
        paypal = 1
    elif Payment_provider == 'voyager':
        card = 1

    transaction_result = ''
    if st.button('Check if transaction is Fraud'):
        transaction_result = fraud_predction([No_Transactions, No_Orders, No_Payments, float(Total_transaction_amt), Transaction_fail, Payment_method_fail, apple_pay, bitcoin, card, paypal, failed_satus, fulfilled_status, pending_status, american_express, diners_club, discover, jcb_15, jcb_16, Maestro, Mastercard, visa_13, visa_16, voyager])
        if transaction_result == 0:
            #st.success("IT'S A VALID TRANSACTION")
            html_temp = """
            <div style="background:#08A04B ;padding:10px ; border-radius:10px ">
            <h3 style="color:white;text-align:center;">IT'S A VALID TRANSACTION</h3>
            </div>
            """
            st.markdown(html_temp, unsafe_allow_html = True)
        else:
            #st.success("IT'S A FRAUD TRANSACTION")
            html_temp = """
            <div style="background:#FF0000 ;padding:10px ; border-radius:10px">
            <h3 style="color:white;text-align:center;">IT'S A FRAUD TRANSACTION</h3>
            </div>
            """
            st.markdown(html_temp, unsafe_allow_html = True)

if __name__ == "__main__":
    run()
