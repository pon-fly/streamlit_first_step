#マルチページ
#同じディレクトリにpyファイルがあると
#サイドバーを自動作成してくれる

import streamlit as st
from PIL import Image

st.title('pythonだけでサイト作成')
st.caption('これはテストサイトです')

image = Image.open('./images/image_1.jpg')
st.image(image,width=200)