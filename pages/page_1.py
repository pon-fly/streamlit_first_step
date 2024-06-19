import streamlit as st


code = '''
コードをそのまま表示できる
import streamlit as st

st.title('アプリ')
'''

st.code(code, language='python')
