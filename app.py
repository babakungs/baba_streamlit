import streamlit as st
import random

st.set_page_config(
    page_title="영어 학습장"
)

list_word = [
    ["aaa", "a1"], ["bbb", "b2"], ["ccc", "c3"], ["ddd", "d4"], ["eee", "e5"],
    ["fff", "f6"], ["ggg", "g7"], ["hhh", "h8"], ["iii", "i9"], ["jjj", "j10"],
    ["kkk", "k11"], ["lll", "l12"], ["mmm", "m13"], ["nnn", "n14"], ["ooo", "o15"],
    ["ppp", "p16"], ["qqq", "q17"], ["rrr", "r18"], ["sss", "s19"], ["ttt", "t20"],
    ["uuu", "u21"], ["vvv", "v22"], ["www", "w23"], ["xxx", "x24"], ["yyy", "y25"],
    ["zzz", "z26"], ["AAA", "a27"], ["BBB", "b28"], ["CCC", "c29"], ["DDD", "d30"],
    ["EEE", "e31"], ["FFF", "f32"], ["GGG", "g33"], ["HHH", "h34"], ["III", "i35"],
    ["JJJ", "j36"], ["KKK", "k37"], ["LLL", "l38"], ["MMM", "m39"], ["NNN", "n40"],
    ["OOO", "o41"], ["PPP", "p42"], ["QQQ", "q43"], ["RRR", "r44"], ["SSS", "s45"],
    ["TTT", "t46"], ["UUU", "u47"], ["VVV", "v48"], ["WWW", "w49"], ["XXX", "x50"]
]
def get_random_five(n: int) -> list: # n포함 무작위 5개 섞기기
    numbers = list(range(1, 51))
    fixed = numbers[n - 1]  # n번째 숫자 (1-based index)
    remaining = numbers[:n - 1] + numbers[n:]  # n번째 숫자를 뺀 나머지
    random_choices = random.sample(remaining, 4)  # 무작위 4개
    result = random_choices + [fixed]  # 고정된 숫자 포함
    random.shuffle(result)  # 순서 섞기
    return result

if 'all_random_sets' not in st.session_state:
    st.session_state.all_random_sets = {n: get_random_five(n) for n in range(1, 51)}

if 'selected_answers' not in st.session_state:
    st.session_state.selected_answers = {}

all_random_sets = st.session_state.all_random_sets
selected_answers = st.session_state.selected_answers

def get_button_style(state):
    if state == "correct":
        return "background-color: green; color: white;"
    elif state == "wrong":
        return "background-color: red; color: white;"
    elif state == "disabled":
        return "background-color: lightgray; color: white;"
    else:
        return "background-color: #1f77b4; color: white;"  # 기본 파랑

# 퀴즈 표시
for i in range(1, 51):
    st.write(f"문제 {i}. {list_word[i-1][0]}")
    options = all_random_sets[i]
    correct = i  # 1-based index
    chosen = selected_answers.get(i, None)

    cols = st.columns(5)
    for j in range(5):
        idx = options[j]
        word = list_word[idx - 1][1]
        key = f"quiz_{i}_{j}"

        if chosen is None:
            if cols[j].button(word, key=key):
                st.session_state.selected_answers[i] = idx
                st.rerun()  # 🚀 버튼 누른 즉시 다시 그려지게 함!
        else:
            # 버튼 상태 표시
            if idx == correct:
                style = get_button_style("correct")
            elif idx == chosen:
                style = get_button_style("wrong")
            else:
                style = get_button_style("disabled")

            cols[j].markdown(
                f"<button style='padding:10px; width:100%; border:none; border-radius:5px; {style}' disabled>{word}</button>",
                unsafe_allow_html=True
            )
