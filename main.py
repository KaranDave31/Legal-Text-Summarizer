import streamlit as st

# Page title
st.set_page_config(page_title="LEGAL TEXT SUMMARIZER", layout="wide")
st.title("Legal Text Summarizer")

# Sidebar for model selection
st.sidebar.header("Choose Model")
model_choice = st.sidebar.selectbox(
    "Select a model:",
    ("RNN", "LSTM", "BERT", "FinBERT + BART")
)

# Main content based on model selection
st.subheader(f"Using model: {model_choice}")

# Text input for legal text
legal_text = st.text_area("Enter your legal text here:", height=250)

# Buttons for generating summary and title
col1, col2 = st.columns(2)

with col1:
    if st.button("Generate Summary"):
        if legal_text.strip() != "":
            # Replace with your model inference code
            st.success(f"Summary generated using {model_choice}!")
        else:
            st.warning("Please enter legal text to summarize.")

with col2:
    if st.button("Generate Title"):
        if legal_text.strip() != "":
            # Replace with your model inference code
            st.success(f"Title generated using {model_choice}!")
        else:
            st.warning("Please enter legal text to generate title.")
