import streamlit as st

# 更丰富的双语语料库
faq = {
    "中文": {
        "过境签如何办理？": "办理过境签，您需要准备有效护照、目的地签证（如有）、过境机票，然后前往对应国家的使领馆或在指定口岸办理。",
        "健康申明卡在哪里领取？": "健康申明卡可以在口岸指定的柜台或者自助领取机处领取。",
        "充电宝可以带上飞机吗？": "一般情况下，额定能量不超过100Wh的充电宝可以随身携带，但每人限带两个，且不能托运；超过100Wh但不超过160Wh的，经航空公司批准后可以随身携带一个，严禁托运；超过160Wh的严禁携带。",
        "入境需要填写什么表格？": "通常需要填写入境卡和海关申报单，具体表格内容可在飞机上向乘务员索取，或在口岸的相关区域获取。"
    },
    "英文": {
        "How to apply for a transit visa?": "To apply for a transit visa, you need to prepare a valid passport, a destination visa (if required), and a transit flight ticket. Then, go to the embassy or consulate of the corresponding country or apply at the designated port.",
        "Where can I get the health declaration form?": "You can get the health declaration form at the designated counter or self - service machine at the port.",
        "Can I take a power bank on the plane?": "Generally, power banks with a rated energy of no more than 100Wh can be carried on board, but each person is limited to two and cannot be checked in. For power banks with a rated energy between 100Wh and 160Wh, one can be carried on board after being approved by the airline, and they are strictly prohibited from being checked in. Power banks with a rated energy exceeding 160Wh are strictly prohibited from being carried.",
        "What forms do I need to fill in when entering the country?": "You usually need to fill in an arrival card and a customs declaration form. You can get the specific forms from the flight attendants on the plane or in the relevant area at the port."
    }
}

def get_answer(question, language):
    # 先尝试精确匹配
    answer = faq[language].get(question)
    if answer:
        return answer
    # 若精确匹配失败，进行模糊匹配
    for q, a in faq[language].items():
        if question in q:
            return a
    return "未找到相关答案，请换个问题试试。" if language == "中文" else "No relevant answer found. Please try another question."

st.title("AI通关问答员 - 中英双语边检FAQ问答系统")
language = st.radio("选择语言", ["中文", "英文"])
question = st.text_input(f"请输入{language}问题" if language == "中文" else f"Please enter your {language.lower()} question")

if st.button("提问" if language == "中文" else "Ask"):
    answer = get_answer(question, language)
    st.write(answer)
    
