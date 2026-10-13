import streamlit as st

st.title("Hello Streamlit-er 👋")
st.markdown(
    """ 
    
    """
)

tab1, tab2 = st.tabs(["數據總覽", "詳細清單"])
with tab1:
    user_input = st.text_input("輸入你爹啦")

    options = st.selectbox(" ", ["local", "歐頭", "on賴"])

    if st.button("確認"):
        st.write("您輸入的內容是：", user_input, "，您選擇的選項是：", options)
with tab2:
  st.write("這是分頁二的內容")

