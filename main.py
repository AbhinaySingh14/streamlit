import streamlit as st
import pandas as pd
d={'name':['abhi','sunil','naman'],'marks':[100,77,87]}
df=pd.DataFrame(d)
st.title('First Streamlit App')

st.subheader('Introducing My first webApp')
st.write(''' welcome everyone this is my first web app
         enjoy it!''')
st.write(df)
st.line_chart(df)

#run by typing (streamlit run main.py) in terminal
#to deploy it connect to fithub using version controll and push it
# then go to 