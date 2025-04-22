import streamlit as st  

# Configure the main page
st.set_page_config(
    page_title='Stress Level Detector',
    page_icon='',
    layout='wide',
    initial_sidebar_state='auto'
)

# Import necessary functions and modules
from web_functions import load_data
from Tabs import home, data, predict, visualise, chatbot

def main():
    # Dictionary for pages
    Tabs = {
        "Home": home,
        "Data Info": data,
        "Prediction": predict,
        "Visualisation": visualise,
        "Chatbot": chatbot
    }

    # Create a sidebar
    st.sidebar.title("Navigation")

    # Create radio option to select the page
    page = st.sidebar.radio("Pages", list(Tabs.keys()))

    # Loading the dataset
    df, X, y = load_data()

    # Main content area
    main_container = st.container()
    with main_container:
        if page in ["Prediction", "Visualisation"]:
            Tabs[page].app(df, X, y)
        elif page == "Data Info":
            Tabs[page].app(df)
        elif page == "Chatbot":
            Tabs[page].main()
        else:
            Tabs[page].app()

if __name__ == "__main__":
    main()