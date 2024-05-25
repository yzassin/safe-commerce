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


    if (fraud[0] == 0):
       return 'VALID'
    else:
        return 'FRAUD'

def run():
    st.set_page_config(
        page_title="SafE-commerce",
        page_icon="💰",
    )

    st.write("# 💰 Welcome to SafE-Commerce!")

    st.markdown(
    """
        A web platform designed to track fraudulent activity within e-commerce transactions
    """
    )
    st.markdown("---")

    
    No_Transactions = st.slider("Number of Transactions", min_value=1, max_value=10, value=1)
    Transaction_fail = st.slider("How many time Transaction Fail?", min_value=0, max_value=10, value=0)
    Total_transaction_amt = st.text_input("Transaction Amount")

    st.markdown("---")
    No_Orders = st.slider("Number of orders ", min_value=1, max_value=10, value=1)
    Order_status = st.multiselect("Status of the order", 
                            ["Failed", "Fulfilled", "Pending"])

    failed_satus = 0
    fulfilled_status = 0
    pending_status = 0

    for status in Order_status:
        if status == "Failed":
            failed_satus = st.number_input(f"How many times did the order status '{status}' occur?", min_value=0)
        elif status == "Fulfilled":
             fulfilled_status = st.number_input(f"How many times did the order status '{status}' occur?", min_value=0)
        elif status == "Pending":
            pending_status = st.number_input(f"How many times did the order status '{status}' occur?", min_value=0)

    st.markdown("---")
    No_Payments = st.slider("Payments Attempt", min_value=1, max_value=10, value=1)
    Payment_method_fail = st.slider("Payment Method Fail?", min_value=0, max_value=10, value=0)

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


    Payment_provider = st.multiselect("Payment Provider", 
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

    for status in Payment_provider:
        if status == "American Express":
            american_express = st.number_input(f"How many times '{status}' was used?", min_value=0)

        elif status == "Diners Club":
             diners_club = st.number_input(f"How many times '{status}' was used?", min_value=0)

        elif status == "Discover":
            discover = st.number_input(f"How many times '{status}' was used?", min_value=0)

        elif status == "JCB 15":
             jcb_15 = st.number_input(f"How many times '{status}' was used?", min_value=0)
            
        elif status == "JCB 16":
            jcb_16 = st.number_input(f"How many times '{status}' was used?", min_value=0)

        elif status == "Maestro":
             Maestro = st.number_input(f"How many times '{status}' was used?", min_value=0)
            
        elif status == "Mastercard":
            Mastercard = st.number_input(f"How many times '{status}' was used?", min_value=0)

        elif status == "Visa 13":
             visa_13 = st.number_input(f"How many times '{status}' was used?", min_value=0)
            
        elif status == "Visa 16":
            visa_16 = st.number_input(f"How many times '{status}' was used?", min_value=0)

        elif status == "Voyager":
             voyager = st.number_input(f"How many times '{status}' was used?", min_value=0)

    

    transaction_result = ''
    if st.button('Check if Transaction is Fraudulent'):
        transaction_result = fraud_predction(
            [No_Transactions, No_Orders, No_Payments, float(Total_transaction_amt), Transaction_fail,
             Payment_method_fail, apple_pay, bitcoin, card, paypal, failed_satus, fulfilled_status,
             pending_status, american_express, diners_club, discover, jcb_15, jcb_16, Maestro, Mastercard,
             visa_13, visa_16, voyager])
            # Styling based on transaction result
    if transaction_result == "FRAUD":
        st.error(f"Transaction is {transaction_result}")
    else:
        st.success(f"Transaction is {transaction_result}")


if __name__ == "__main__":
    run()
