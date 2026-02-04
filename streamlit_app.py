import streamlit as st 
from streamlit_carousel_uui import uui_carousel

st.set_page_config(page_title="streamlit-carousel-uui demo", layout="centered", page_icon=":material/camera:")

st.image("images/header.png")

# Define your carousel items
slides = [
    {
        "image": "https://github.com/janduplessis883/demo-streamlit-carousel-uii/blob/master/images/fenced_court_dusk.png?raw=true",
        "title": "Berlin Court",
        "description": "Fenced dreams, urban, solitary game."
    },
    {
        "image": "https://github.com/janduplessis883/demo-streamlit-carousel-uii/blob/master/images/Sidewalk_Woman_Purse.png?raw=true",
        "title": "Morgenlicht",
        "description": "Purse held tight, daybreak transaction lingers."
    },
    {
        "image": "https://github.com/janduplessis883/demo-streamlit-carousel-uii/blob/master/images/night_view_of_living_room.png?raw=true",
        "title": "Studio Nocturne",
        "description": "Shadows, portraits, tools, silence, waiting."
    },
    {
        "image": "https://github.com/janduplessis883/demo-streamlit-carousel-uii/blob/master/images/speeding_bike.png?raw=true",
        "title": "De Zwarte Kat",
        "description": "Wet cobblestones, street art, hurried motion."
    },
]

# Display the carousel
uui_carousel(items=slides, variant="md")
with st.expander("About this demo", icon=":material/favorite:"):
    st.markdown(
        """
        :material/camera: **Streamlit-Carousel-UUI** is a custom Streamlit component you created to bring sophisticated, modern carousel functionality to Streamlit applications. Built on top of the elegant **Untitled UI** design system and powered by Embla Carousel with React, this component addresses a gap in Streamlit's native capabilities by offering a polished image showcase solution. The carousel features smooth transitions between slides, intuitive navigation arrows, and indicator dots—all wrapped in a clean, minimalist aesthetic that aligns with contemporary web design standards.  
        
        The component is remarkably straightforward to implement: `pip install streamlit-carousel-uui` and import with `from streamlit_carousel_uui import uui_carousel`, requiring only a simple list of dictionary items containing image URLs (or paths) and optional title and description fields. I designed it with flexibility in mind, offering two size variants **medium** and **large** to accommodate different layout needs. This simplicity doesn't sacrifice functionality; the responsive design ensures the carousel performs well across various screen sizes, making it suitable for both desktop dashboards and mobile presentations. No need to resize or crop images.  
        
        ```python
        from streamlit_carousel_uui import uui_carousel

        # Define your carousel items
        slides = [
            {
                "image": "https://github.com/janduplessis883/demo-streamlit-carousel-uii/blob/master/images/fenced_court_dusk.png?raw=true",
                "title": "Berlin Court",
                "description": "Fenced dreams, urban, solitary game."
            },
            {
                "image": "https://github.com/janduplessis883/demo-streamlit-carousel-uii/blob/master/images/Sidewalk_Woman_Purse.png?raw=true",
                "title": "Morgenlicht",
                "description": "Purse held tight, daybreak transaction lingers."
            },
            {
                "image": "https://github.com/janduplessis883/demo-streamlit-carousel-uii/blob/master/images/night_view_of_living_room.png?raw=true",
                "title": "Studio Nocturne",
                "description": "Shadows, portraits, tools, silence, waiting."
            },
            {
                "image": "https://github.com/janduplessis883/demo-streamlit-carousel-uii/blob/master/images/speeding_bike.png?raw=true",
                "title": "De Zwarte Kat",
                "description": "Wet cobblestones, street art, hurried motion."
            },
        ]

        # Display the carousel
        uui_carousel(items=slides, variant="md")
        
        ```
        :material/download: [Install via **PyPi**](https://pypi.org/project/streamlit-carousel-uui/)  
        :material/code: [View source on **GitHub**](https://github.com/janduplessis883/streamlit_carousel_uui)  
        :material/star: **janduplessis883** on GitHub if you like this component!
        """
    )