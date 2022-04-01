
import streamlit as st



st.sidebar.header('แบบประเมินความเสี่ยงโรคถุงน้ำรังไข่หลายใบ')
st.sidebar.subheader('กรอกข้อมูล')
st.sidebar.write('--------------------------------------------------------------------')


with st.sidebar:
    with st.echo():
        st.write("This code will be printed to the sidebar.")

    with st.spinner("Loading..."):
        time.sleep(5)
    st.success("Done!")
