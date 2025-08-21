import streamlit as st

st.title("Hello Streamlit 👋")
st.write("이건 정말 간단한 예시야!")

name = st.text_input("이름을 입력해봐")
age = st.slider("나이", 0, 100, 20)

if st.button("확인"):
    st.success(f"안녕 {name}, 너의 나이는 {age}살이구나!")

