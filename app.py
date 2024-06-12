import streamlit as st

page_title="짱구는 못말려 도감",
page_icon="./images/신짱구.png"


st.markdown("""
<style>
img { 
    max-height: 300px;
}
.streamlit-expanderContent div {
    display: flex;
    justify-content: center;
    font-size: 20px;
}
[data-testid="stExpanderToggleIcon"] {
    visibility: hidden;
}
.streamlit-expanderHeader {
    pointer-events: none;
}
[data-testid="StyledFullScreenButton"] {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)


st.title("streamlit 짱구는 못말려 도감")
st.markdown("**캐릭터들**을(를) 하나씩 추가해서 도감을 채워보세요!")

type_emoji_dict = {"익살스러운 성격":"😂",
"장난끼 많음":"😜",
"강아지":"🐶",
"공부잘함":"📚",
"겁이많음":"😟",
"돌을 좋아함":"🪨",
"귀여운 걸 좋아함":"🧸",
"마음씨가 고움":"😇"}
    


initial_character = [
    {
        "name": "신짱구",
        "types": ["장난끼 많음"],
        "image_url": "https://i.namu.wiki/i/g39mX6YMajoi9H_jj-PdnoUETKhcW6kOzZDlEetSbN4QabcmhO7J8YO5lUts1xBIqIDr7oCu-rSFjDwh-cT8mehdno0UwCMigtNOoCQuW4mxw5pS6wBU9nrcuWYdIfclvggWKUgpriRUEpOU5NjmdA.webp"
    },
    {
        "name": "흰둥이",
        "types": ["강아지"],
        "image_url": "https://i.namu.wiki/i/kF8Z-s_PqeC5lp97kAdg0WgS0nPFFJjogra5StfKajhSndOxcxax2jHigMsUw61fwUG8OVX_xSLeuIe1gDbzTRdWisdzAIHWjhykwH9bZTcw3tWzM72AYa2ijOnZK693lIsMlnynZqEDVL2Pa7bqzA.webp",
    },
    {
        "name": "김철수",
        "types": ["공부잘함"],
        "image_url": "https://i.namu.wiki/i/1RSsmo4o8SybCapX6r50-2b9t573Jr9YjTO2Bjrp3zMuJ_MSQTxAF5nH-IjMnK1rEPtR3oHeCR4FbSljXop6bdG5hye4TlnZejQPlz71TWJ34_OGiY2tCEwfH6KRx9OXyXAJttGA_cUh-XWsfU3gxQ.webp",
    },
    {
        "name": "맹구",
        "types": ["돌을 좋아함"],
        "image_url": "https://i.namu.wiki/i/jq-OIaShvJ6jgfzsq_B4T3dLauuqHCEhcReZeZJ2DdvWLnm-3_r_tZARZ6LoVQqPq-uIcoMlySkI6w5pvqWPLX6OTYETlWlrSonQTww7x7-86RyU30fDJUKBlAcC9njdPv0Ug1l5-rlRqG9SEC4Xyg.webp"
    },
    {
        "name": "한유리",
        "types": ["귀여운 걸 좋아함"],
        "image_url": "https://i.namu.wiki/i/l43I3G_THNTPjPHN2gc8XvPpMgHowm_jqudMFBpcgO6wlQJg8FcQ0r6V51uhNokfkYKkk6om7oCfSzIN50-Dveurc9Slex-SuGDJTIf5ZDUjSq-R8V2MZpFWwsm-lwLZ00yWynze-KQHSY5OZ-08dg.webp"
    },
    {
        "name": "한수지",
        "types": ["마음씨가 고움"],
        "image_url": "https://i.namu.wiki/i/OLQI2yIj4tPUVwI17GYG1m5vLiRVkxujELETfOvH-aKawNW4dn3VtPR7fQL8UgmcN6tG2pPIH8YhB0sMUnPI4gQVUAqWDLDPkmFTd67_5fzlDooyWGUxw4Ql2QC4chi8diwIKBV4AiR0XhQNvYVaYA.webp"
    },
]

example_character = {
    "name": "신짱구",
    "types": ["장난끼 많음"],
    "image_url": "https://i.namu.wiki/i/g39mX6YMajoi9H_jj-PdnoUETKhcW6kOzZDlEetSbN4QabcmhO7J8YO5lUts1xBIqIDr7oCu-rSFjDwh-cT8mehdno0UwCMigtNOoCQuW4mxw5pS6wBU9nrcuWYdIfclvggWKUgpriRUEpOU5NjmdA.webp"
}

if "characters" not in st.session_state:
    st.session_state.characters = initial_character

auto_complete = st.toggle("예시 데이터로 채우기")
with st.form(key="form"):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input(
            label="캐릭터 이름",
            value=example_character["name"] if auto_complete else ""
        )
    with col2:
        types = st.multiselect(
            label="캐릭터 특징",
            options=list(type_emoji_dict.keys()),
            max_selections=2,
            default=example_character["types"] if auto_complete else []
        )
    image_url = st.text_input(
        label="캐릭터 이미지 URL",
        value=example_character["image_url"] if auto_complete else ""
    )
    submit = st.form_submit_button(label="Submit")
    if submit:
        if not name:
            st.error("캐릭터의 이름을 입력해주세요.")
        elif len(types) == 0:
            st.error("캐릭터의 특징을 적어도 한개 선택해주세요.")
        else:
            st.success("캐릭터를 추가할 수 있습니다.")
            st.session_state.character.append({
                "name": name,
                "types": types,
                "image_url": image_url if image_url else "./images/default.png"
            })

for i in range(0, len(st.session_state.characters), 3):
    row_characters = st.session_state.characters[i:i+3]
    cols = st.columns(3)
    for j in range(len(row_characters)):
        with cols[j]:
            character = row_characters[j]
            with st.expander(label=f"**{i+j+1}. {character['name']}**", expanded=True):
                st.image(character["image_url"])
                emoji_types = [f"{type_emoji_dict[x]} {x}" for x in character["types"]]
                st.text(" / ".join(emoji_types))
                delete_button = st.button(label="삭제", key=i+j, use_container_width=True)
                if delete_button:
                    del st.session_state.character[i+j]
                    st.rerun()