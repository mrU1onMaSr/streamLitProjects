from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

#Page Config
st.set_page_config(page_title="My Website",page_icon = ":blue_book:", layout = "wide")

#import assets

def lottieLoad(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json() 

lottie1 = lottieLoad("https://assets5.lottiefiles.com/private_files/lf30_5u6A5U.json")
Img1 = Image.open("images/PlaceHolder.png")
contactHTML = """<form action="https://formsubmit.co/94602719f004194f29566314c80fb907" method="POST">
    <input type="text" name="name" placeholder = "Your Name" required>
    <input type="email" name="email" placeholder = "Email" required>
    <textarea name="message" placeholder="Your Message" required></textarea>
    <button type="submit">Send</button>
</form>"""

def localcss(filename):
    with open(filename) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

localcss("style/style.css")

#Main Head
with st.container():
    st.subheader("Hi I'm Yuvan And This Is My First StreamLit Website!! :wave: ")
    st.title("A Computer Enthusiast From India :v: ")
    st.write("I Love Coding! :D You have to be a good place  ")
    st.write("[My Github >](https://github.com/mrU1onMaSr)")
    
#More Information
with st.container():
    st.write("---")
    leftColumn , rightColumn = st.columns(2)
    with leftColumn:
        st.subheader("What I Do")
        st.write("##")
        st.write(""" I am Yuvan Srisai Dutta,
        I a web developer afrom Hyderbad India. I have good experience in building and customizing websites and apps,
        I also have a decent of experience in 3D designing.
        I also Have a lot of experience in python and have created small and big apps which are mention below.
        """)
    with rightColumn:
        st_lottie(lottie1,height = 500,width = 500)

#projects
with st.container():
    st.write("---")
    st.write("###")
    leftColumn , rightColumn = st.columns((1,2))
    with leftColumn:
        st.image(Img1)
    with rightColumn:
        st.write("PlaceHolder 1")

with st.container():
    st.write("---")
    st.write("###")
    leftColumn , rightColumn = st.columns((1,2))
    with leftColumn:
        st.image(Img1)
    with rightColumn:
        st.write("PlaceHolder 2")

#contact Form
with st.container():
    st.write("---")
    st.write("##")
    leftColumn,rightColumn = st.columns(2)
    with leftColumn:
        st.markdown(contactHTML,unsafe_allow_html=True)
    with rightColumn:
        st.empty()

