import streamlit as st
from PIL import Image
import datetime

#withはボタンが押されたタイミングで読み込む
#with区の中に書けばいちいちロードされない
with st.form(key='profile_form'):

    #テキストボックス
    name = st.text_input('名前')
    adress = st.text_input('住所')

    #セレクトボックスかラジオボックス
    age_category = st.radio(
        '年齢',
        ('18歳以上','18未満'))
    
    #複数　
    hobby = st.multiselect(
        '趣味',
        ('読書','スポーツ','昼ね','映画','釣'))
    
    #チェックボックス
    mail_subscribe = st.checkbox('メール購読する')

    #スライダー
    height = st.slider('身長(cm単位)',min_value=110,max_value=200)

    #日付カレンダー機能もつく
    start_data = st.date_input(
        '開始日',
          datetime.date(2024, 1, 1))
    
    #カラーピッカー
    color = st.color_picker('テーマカラー','#00f900')
    


    #ボタン
    submit_btn = st.form_submit_button('送信')
    cancel_btn = st.form_submit_button('キャンセル')

    #submitが押されtrueになったら実行
    if submit_btn:
        st.text(f'ようこそ{name}さん、{adress}に書類を送ります')
        st.text(f'年齢層: {age_category}')
        st.text(f'趣味: {",".join(hobby)}')
        st.text(f'開始日は: {start_data}')
        st.text(f'身長は: {height}cm')


