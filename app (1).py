
import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

Diamond_price = pickle.load(open('diamond_model.sav', 'rb'))

# sidebar for navigation
# with st.sidebar:
#     st.image('bot.jpg', width=250)
#     selected = option_menu('Disease Prediction System',
                          
#                           ['Diabetes Prediction',
#                            'Heart Disease Prediction',
#                            'Parkinsons Prediction'],
#                           icons=['activity','heart','person'],
#                           default_index=0)
    
    
# Diabetes Prediction Page
    # page title

st.title('Diamond Price Prediction using ML')
      
    # getting the input data from the user
col1, col2, col3,col4,col5,col6,col7,col8,col9 = st.columns(9)
    
with col1:
  carat = st.text_input('carat_value')
        
with col2:
    cut= st.text_input('cut_level')
    
with col3:
    color = st.text_input('Diamond color')
    
with col4:
    clarity = st.text_input('Skin Thickness value')
    
with col5:
    depth = st.text_input('depth_value of diamond')
    
with col6:
    table = st.text_input('width of top of diamond')
    
with col7:
    x = st.text_input('value of x_dimension ')
    
with col8:
    y = st.text_input('value of y_dimension')
with col8:
    z = st.text_input('value of z_dimension')    
    
    
    # code for Prediction
price = ''
    
    # creating a button for Prediction
    
if st.button('Diamond Price Test Result'):
  price_prediction = model.predict([[carat, cut, color, clarity, depth, table, x, y,z]])
        
        
st.success(price_prediction)


