import streamlit as st
import random
import time
from streamlit_option_menu import option_menu
import os
from configs import VERSION
from streamlit_chatbox import *
from typing import List, Dict
from datetime import datetime
# from webui_pages.utils import *

# api = ApiRequest(base_url="http://127.0.0.1:7861", no_remote_api=False)

# st.set_page_config(
#     page_title="知识库",
#     page_icon=None,
#     layout="wide",  # 如果你希望使用宽屏布局
#     initial_sidebar_state="collapsed",  # 这里设置侧边栏默认隐藏
#     menu_items=None,
# )

chat_box = ChatBox(
    assistant_avatar=os.path.join(
        "img",
        "chatchat_icon_blue_square_v2.png"
    )
)


def get_messages_history(history_len: int) -> List[Dict]:
    def filter(msg):
        '''
        针对当前简单文本对话，只返回每条消息的第一个element的内容
        '''
        content = [x._content for x in msg["elements"] if x._output_method in ["markdown", "text"]]
        return {
            "role": msg["role"],
            "content": content[0] if content else "",
        }

    history = chat_box.filter_history(100000, filter)  # workaround before upgrading streamlit-chatbox.
    user_count = 0
    i = 1
    for i in range(1, len(history) + 1):
        if history[-i]["role"] == "user":
            user_count += 1
            if user_count >= history_len:
                break
    return history[-i:]


chat_box.init_session()

mode = "知识库问答"
cur_kb = "科诺公司企业标准化文件"
selected_kb = "科诺公司企业标准化文件"
dialogue_mode = "知识库问答"
# 历史对话轮数
history_len = 3
# 匹配知识条数
kb_top_k = 5
# 知识匹配分数阈值
score_threshold = 1.0

chat_box.output_messages()

chat_input_placeholder = "请输入对话内容，换行请使用Ctrl+Enter "

if prompt := st.chat_input(chat_input_placeholder, key="prompt"):
    chat_box.user_say(prompt)
    history = get_messages_history(history_len)
    chat_box.ai_say([
        f"正在查询知识库 `{selected_kb}` ...",
        Markdown("...", in_expander=True, title="知识库匹配结果"),
    ])
    text = ""
    for d in api.knowledge_base_chat(prompt, selected_kb, kb_top_k, score_threshold, history):
        if error_msg := check_error_msg(d):  # check whether error occured
            st.error(error_msg)
        text += d["answer"]
        chat_box.update_msg(text, 0)
        chat_box.update_msg("\n\n".join(d["docs"]), 1, streaming=False)
    chat_box.update_msg(text, 0, streaming=False)

now = datetime.now()

# st.title("聊天标题")
#
# # Initialize chat history
# if "messages" not in st.session_state:
#     st.session_state.messages = []
#
# # Display chat messages from history on app rerun
# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])
#
# # Accept user input
# if prompt := st.chat_input("What is up?"):
#     # Display user message in chat message container
#     with st.chat_message("user"):
#         st.markdown(prompt)
#     # Add user message to chat history
#     st.session_state.messages.append({"role": "user", "content": prompt})
