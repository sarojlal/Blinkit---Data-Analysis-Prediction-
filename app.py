import streamlit as st
import pandas as pd
import pickle

# Load the model
model = pickle.load(open('XGBClassifier_model.pkl', 'rb'))

# Load the columns used in training
columns = pickle.load(open('model_columns1.pkl', 'rb'))

# Set the page configuration
st.set_page_config(page_title='Item Fat Content Prediction', page_icon="🥤")

# Custom CSS for styling
st.markdown(
    """
    <style>
    .main {
        background-color: #f7f7f9;
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
        border: none;
    }
    .stTextInput input, .stNumberInput input, .stSelectbox select {
        background-color: #ffffff;
        color: #333333;
        border-radius: 5px;
        border: 1px solid #ccc;
    }
    .stMetric {
        font-size: 1.2em;
        color: #333333;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar for input fields
st.sidebar.header('Input Features')

item_identifier = st.sidebar.text_input('Item Identifier')
item_weight = st.sidebar.number_input('Item Weight', min_value=0.0, step=0.01)
item_type = st.sidebar.selectbox('Item Type', ['Dairy', 'Soft Drinks', 'Meat', 'Fruits and Vegetables', 'Others'])
item_mrp = st.sidebar.number_input('Item MRP', min_value=0.0, step=0.01)
item_visibility = st.sidebar.number_input('Item Visibility', min_value=0.0, step=0.01)

# Convert input into dataframe
input_data = pd.DataFrame({
    'Item_Identifier': [item_identifier],
    'Item_Weight': [item_weight],
    'Item_Type': [item_type],
    'Item_MRP': [item_mrp],
    'Item_Visibility': [item_visibility]
})

# Encode input data
input_data_encoded = pd.get_dummies(input_data, columns=['Item_Identifier', 'Item_Type'], drop_first=True)

# Ensure all necessary columns are present
for col in columns:
    if col not in input_data_encoded.columns:
        input_data_encoded[col] = 0

input_data_encoded = input_data_encoded[columns]

# Main title
st.title('Item Fat Content Prediction')

# Display all input metrics
col1, col2 = st.columns(2)

with col1:
    st.metric(label="Item Identifier", value=item_identifier)
    st.metric(label="Item Weight", value=f"{item_weight} kg")

with col2:
    st.metric(label="Item Type", value=item_type)
    st.metric(label="Item MRP", value=f"${item_mrp:.2f}")
    st.metric(label="Item Visibility", value=f"{item_visibility:.2f}")

# Predict button and result
if st.button('Predict'):
    prediction = model.predict(input_data_encoded)[0]
    if prediction == 0:
        st.success('The item is predicted to be **Low Fat**.')
    else:
        st.success('The item is predicted to be **Regular**.')

# Display feature importance (if available)
if hasattr(model, 'coef_'):
    st.write('### Feature Importance')
    coef_df = pd.DataFrame(model.coef_, columns=columns)
    st.write(coef_df)
