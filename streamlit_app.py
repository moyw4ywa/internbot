import streamlit as st
from content_bot import ContentBot
from gemini_api import GeminiAPI

# Initialize the Content Bot and Gemini API
content_bot = ContentBot()
gemini_api = GeminiAPI()

def get_response(user_input):
    content = content_bot.generate_content(user_input)
    gemini_response = gemini_api.generate_response(user_input)
    return content, gemini_response

def main():
    st.set_page_config(page_title="ContentBot")

    st.markdown('<h1 style="text-align:center;">Chat with ContentBot 🤖</h1>', unsafe_allow_html=True)

    user_input = st.text_input('Enter your post or comment prompt:')

    if st.button('Generate Content'):
        if user_input:
            content, gemini_response = get_response(user_input)
            st.markdown('<h2 style="color:#228b22;font-style:italic;">Generated Content:</h2>', unsafe_allow_html=True)
            st.markdown(f'<p>{content}</p>', unsafe_allow_html=True)

            st.markdown('<h2 style="color:#228b22;font-style:italic;">Gemini Response:</h2>', unsafe_allow_html=True)
            st.markdown(f'<p>{gemini_response}</p>', unsafe_allow_html=True)
        else:
            st.error("Please enter a post or comment prompt.")

    st.sidebar.markdown('<h1 style="font-size: 30px;">Menu</h1>', unsafe_allow_html=True)
    
    st.sidebar.markdown("### Navigation")
    st.sidebar.write("Use the buttons below to navigate:")
    
    if st.sidebar.button("Back to Main App"):
        st.write('<meta http-equiv="refresh" content="0;url=https://project-frontend11.onrender.com/">', unsafe_allow_html=True)
    
    if st.sidebar.button("Join Mailing List"):
        st.write('<meta http-equiv="refresh" content="0;url=https://contentbot-signup.onrender.com/">', unsafe_allow_html=True)
    
    st.sidebar.markdown("### Resources")
    st.sidebar.markdown("[Meta Community Guidelines](https://www.facebook.com/communitystandards/)")
    st.sidebar.markdown("[Content Moderation Guide](https://www.humanrightscareers.com/guide/content-moderation/)")

if __name__ == '__main__':
    main()
