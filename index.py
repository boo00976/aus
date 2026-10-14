# python -m streamlit run index.py
import streamlit as st
from google import genai  # 記得先 pip install google-generativeai

st.title("Hello Streamlit-er 👋")


if "GEMINI_API_KEY" not in st.session_state:
    st.session_state["GEMINI_API_KEY"] = "api輸入在這" # api輸入在這


client = None
if st.session_state["GEMINI_API_KEY"]:
    try:
        client = genai.Client(api_key=st.session_state["GEMINI_API_KEY"])
    except Exception as e:
        st.error(f"初始化 Client 失敗: {e}")
else:
    st.warning(" 重新整理一次 歐內該")

tab1, tab2 = st.tabs(["數據總覽", "詳細清單"])

with tab1:
    col_input, col_select, col_btn = st.columns([6, 1, 1])
    
    with col_input:
        user_input = st.text_input("輸入啦", placeholder="輸入想問 Gemini 的問題...")
    
    with col_select:
        options = st.selectbox("選擇模式", ["local", "auto", "online"])

    with col_btn:
        st.markdown("<div style='height: 28px;'></div>", unsafe_allow_html=True)
        submit_clicked = st.button("確認", use_container_width=True)
        if submit_clicked:
                if not st.session_state["GEMINI_API_KEY"]:
                    st.error(" 無法執行：尚未設定 API Key！")
                elif not user_input.strip():
                    st.warning(" 請先輸入內容再點擊確認。")
                elif client is None:
                    st.error(" API Client 尚未初始化！")
                else:
                    prompt = f"使用模式【{options}】來處理以下內容：\n\n{user_input}"
                    
                    with st.spinner("Gemini 正在思考中，請稍候..."):
                        try:
                            response = client.models.generate_content(
                                model="gemini-3.8-flash",
                                contents=prompt,
                            )
                            
                            st.markdown("###回覆：")
                            st.write(response.text)
                            
                        except Exception as e:
                            st.error(f" 呼叫 API 時發生錯誤: {e}")

with tab2:
    st.write("這是分頁二的內容")
