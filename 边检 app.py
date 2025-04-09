import streamlit as st

# 定义中英双语语料库
chinese_corpus = {
    "过境签如何办理？": {
        "answer": "办理过境签，您需要准备有效护照、目的地签证（如有）、过境机票，然后前往对应国家的使领馆或在指定口岸办理。",
        "law_reference": "《中华人民共和国出境入境管理法》相关规定"
    },
    "健康申明卡在哪里领取？": {
        "answer": "健康申明卡可以在口岸指定的柜台或者自助领取机处领取。",
        "law_reference": "海关总署相关公告要求"
    },
    "充电宝可以带上飞机吗？": {
        "answer": "一般情况下，额定能量不超过100Wh的充电宝可以随身携带，但每人限带两个，且不能托运；超过100Wh但不超过160Wh的，经航空公司批准后可以随身携带一个，严禁托运；超过160Wh的严禁携带。",
        "law_reference": "民航局《关于民航旅客携带“充电宝”乘机规定的公告》"
    },
    "入境需要填写什么表格？": {
        "answer": "通常需要填写入境卡和海关申报单，具体表格内容可在飞机上向乘务员索取，或在口岸的相关区域获取。",
        "law_reference": "《中华人民共和国海关对进出境旅客行李物品监管办法》"
    },
    "是否可以携带宠物入境？": {
        "answer": "携带宠物入境需要满足一定条件，如提供宠物的健康证明、疫苗接种记录等，具体要求可咨询口岸工作人员。",
        "law_reference": "《中华人民共和国进出境动植物检疫法》"
    },
    "海关申报的限额是多少？": {
        "answer": "不同物品的海关申报限额不同，例如，携带现金超过一定金额需要申报，具体金额可参考海关相关规定。",
        "law_reference": "《中华人民共和国海关对进出境旅客行李物品监管办法》"
    },
    # 可继续添加更多中文问题及相关信息
    "携带烟酒有什么限制？": {
        "answer": "一般来说，每位成年旅客可以免税携带一定数量的香烟和酒，具体数量因国家和地区而异。",
        "law_reference": "《中华人民共和国海关对进出境旅客行李物品监管办法》"
    },
    "能否携带中药材入境？": {
        "answer": "部分中药材可以携带入境，但有数量和品种限制，一些受保护的中药材禁止携带。",
        "law_reference": "《中华人民共和国禁止携带、邮寄进境的动植物及其产品名录》"
    }
}

english_corpus = {
    "How to apply for a transit visa?": {
        "answer": "To apply for a transit visa, you need to prepare a valid passport, a destination visa (if required), and a transit flight ticket. Then, go to the embassy or consulate of the corresponding country or apply at the designated port.",
        "law_reference": "Relevant provisions of the Exit - Entry Administration Law of the People's Republic of China"
    },
    "Where can I get the health declaration form?": {
        "answer": "You can get the health declaration form at the designated counter or self - service machine at the port.",
        "law_reference": "Requirements of relevant announcements of the General Administration of Customs"
    },
    "Can I take a power bank on the plane?": {
        "answer": "Generally, power banks with a rated energy of no more than 100Wh can be carried on board, but each person is limited to two and cannot be checked in. For power banks with a rated energy between 100Wh and 160Wh, one can be carried on board after being approved by the airline, and they are strictly prohibited from being checked in. Power banks with a rated energy exceeding 160Wh are strictly prohibited from being carried.",
        "law_reference": "Announcement of the Civil Aviation Administration of China on the Regulations for Passengers Carrying 'Power Banks' on Flights"
    },
    "What forms do I need to fill in when entering the country?": {
        "answer": "You usually need to fill in an arrival card and a customs declaration form. You can get the specific forms from the flight attendants on the plane or in the relevant area at the port.",
        "law_reference": "Measures of the Customs of the People's Republic of China for the Supervision of Baggage and Articles of Inward and Outward Passengers"
    },
    "Can I bring my pet into the country?": {
        "answer": "Bringing a pet into the country requires meeting certain conditions, such as providing the pet's health certificate and vaccination records. For specific requirements, please consult the port staff.",
        "law_reference": "Law of the People's Republic of China on the Entry and Exit Animal and Plant Quarantine"
    },
    "What is the customs declaration limit?": {
        "answer": "The customs declaration limits vary for different items. For example, you need to declare if you carry cash exceeding a certain amount. Please refer to the relevant customs regulations.",
        "law_reference": "Measures of the Customs of the People's Republic of China for the Supervision of Baggage and Articles of Inward and Outward Passengers"
    },
    # 可继续添加更多英文问题及相关信息
    "What are the restrictions on carrying cigarettes and alcohol?": {
        "answer": "Generally, each adult passenger can carry a certain amount of cigarettes and alcohol duty - free. The specific quantity varies by country and region.",
        "law_reference": "Measures of the Customs of the People's Republic of China for the Supervision of Baggage and Articles of Inward and Outward Passengers"
    },
    "Can I bring Chinese herbal medicines into the country?": {
        "answer": "Some Chinese herbal medicines can be brought into the country, but there are quantity and variety restrictions. Some protected Chinese herbal medicines are prohibited from being carried.",
        "law_reference": "List of Animals, Plants and Their Products Prohibited from Being Carried or Mailed into the People's Republic of China"
    }
}

def get_answer(question, language):
    try:
        if language == "中文":
            corpus = chinese_corpus
        else:
            corpus = english_corpus

        # 先尝试精确匹配
        if question in corpus:
            answer = corpus[question]["answer"]
            law_reference = corpus[question]["law_reference"]
            return f"{answer}\n法律依据: {law_reference}" if language == "中文" else f"{answer}\nLegal reference: {law_reference}"

        # 若精确匹配失败，进行模糊匹配
        for q, data in corpus.items():
            if question in q:
                answer = data["answer"]
                law_reference = data["law_reference"]
                return f"{answer}\n法律依据: {law_reference}" if language == "中文" else f"{answer}\nLegal reference: {law_reference}"

        return "未找到相关答案，请换个问题试试。" if language == "中文" else "No relevant answer found. Please try another question."
    except Exception as e:
        return f"发生错误: {str(e)}" if language == "中文" else f"An error occurred: {str(e)}"

st.title("AI通关问答员 - 中英双语边检FAQ问答系统")
language = st.radio("选择语言", ["中文", "英文"])
question = st.text_input(f"请输入{language}问题" if language == "中文" else f"Please enter your {language.lower()} question")

if st.button("提问" if language == "中文" else "Ask"):
    answer = get_answer(question, language)
    st.write(answer)
    
