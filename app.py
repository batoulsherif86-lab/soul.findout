import streamlit as st
import time

st.set_page_config(page_title="🔒 Locked Message")

st.title("🔒 Locked message waiting for you.")
st.write("")
st.write("**Hint:** what I call you when I wanna seduce you.")
st.write("")

if "attempts" not in st.session_state:
    st.session_state.attempts = 0
if "unlocked" not in st.session_state:
    st.session_state.unlocked = False

password = st.text_input("Enter the password", type="password")

if not st.session_state.unlocked and password:
    cleaned = password.strip().lower()

    if cleaned == "dollie":
        st.success("Good girl. Access granted.")
        st.session_state.unlocked = True
        time.sleep(1.5)
        st.rerun()
    else:
        st.session_state.attempts += 1
        if st.session_state.attempts == 1:
            st.error("Nah uh. Try again baby.")
        elif st.session_state.attempts == 2:
            st.error("Come on, I don’t have all day.")
        else:
            st.error("❌ Access denied.")

if st.session_state.unlocked:
    st.write("")
    message = [
        "I wanna love you in ways you can’t imagine.",
        "I wanna be your shelter.",
        "I wanna be your home,",
        "your shoulder to cry on,",
        "your pillow to snuggle into.",
        "My hands never wavered for you,",
        "and so will my heart."
    ]

    for line in message:
        st.write(line)
        time.sleep(1)

    st.write("")
    time.sleep(1.5)
    st.write("**I love you.**")
    st.write("")

    st.markdown(
        """
        <div style="color:red; font-size:20px; line-height:1.1; text-align:center;">
            ███       ███<br>
          ███████   ███████<br>
         ███████████████████<br>
          █████████████████<br>
            █████████████<br>
              █████████<br>
                █████<br>
                  █
        </div>
        """,
        unsafe_allow_html=True
    )
