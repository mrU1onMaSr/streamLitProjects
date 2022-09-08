import streamlit as st

#Page Config
st.set_page_config(page_title="My Website",page_icon = ":blue_book:", layout = "wide")

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