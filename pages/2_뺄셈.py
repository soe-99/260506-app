import streamlit as st

st.title("2. 뺄셈")
st.write("뺄셈은 하나의 수에서 다른 수를 빼서 차이를 구하는 계산이에요.")

st.header("뺄셈 공식")
st.latex(r"a - b = c")
st.write("여기서 `a`는 빼기할 첫 번째 수(피감수), `b`는 빼는 수(감수), `c`는 결과(차)입니다.")

st.header("기본 예시")
st.write("예: 8 - 3 = 5")
st.write("왜냐하면 8개 중에서 3개를 빼면 5개가 남기 때문이에요.")

st.markdown("- `5 - 2 = 3`")
st.markdown("- `12 - 7 = 5`")
st.markdown("- `20 - 15 = 5`")

st.header("뺄셈을 잘하는 팁")
st.write(
    "1. 큰 수에서 작은 수를 빼세요.\n"
    "2. 자리수가 있는 수라면 오른쪽에서 왼쪽으로 계산하세요.\n"
    "3. 필요하면 자릿값을 빌려서 계산하세요.\n"
)

st.header("간단한 연습")
a = st.number_input("첫 번째 수 (빼기할 수)", min_value=0, step=1, value=10)
b = st.number_input("두 번째 수 (뺄 수)", min_value=0, step=1, value=4)

result = a - b
st.write(f"### 계산 결과: {a} - {b} = {result}")

if result < 0:
    st.warning("결과가 음수입니다. 뺐을 수가 더 크면 음수가 될 수 있어요.")
