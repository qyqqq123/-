import streamlit as st

# 双语语料库（直接写在代码中）
faq = {
    "中文": {
        "过境签如何办理？": "1. 准备材料：有效护照...",
        "健康申明卡在哪里领取？": "在口岸指定柜台领取。"
    },
    "英文": {
        "How to apply for a transit visa?": "1. Prepare documents: Valid passport...",
        "Where can I get the health declaration form?": "At the designated counter at the port."
    }
}

st.title("边检问答系统")
language = st.radio("选择语言", ["中文", "英文"])
question = st.text_input(f"请输入{language}问题")

if st.button("获取答案"):
    answer = faq[language].get(question, "未找到答案")
    st.success(answer)