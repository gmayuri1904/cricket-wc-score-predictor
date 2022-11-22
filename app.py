import streamlit as st
import pickle
import pandas as pd
import numpy as np
import sklearn

pipe=pickle.load(open('pipe.pkl','rb'))
teams=['Bangladesh',
    'Afghanistan',
    'England',
    'Australia',
    'West Indies',
    'Sri Lanka',
    'New Zealand',
    'India',
    'South Africa',
    'Pakistan']

cities=['Colombo',
 'Mirpur',
 'Johannesburg',
 'Dubai',
 'Auckland',
 'Cape Town',
 'London',
 'Pallekele',
 'Barbados',
 'Sydney',
 'Melbourne',
 'Durban',
 'St Lucia',
 'Wellington',
 'Lauderhill',
 'Hamilton',
 'Centurion',
 'Manchester',
 'Abu Dhabi',
 'Mumbai',
 'Nottingham',
 'Southampton',
 'Mount Maunganui',
 'Chittagong',
 'Kolkata',
 'Lahore',
 'Delhi',
 'Nagpur',
 'Chandigarh',
 'Adelaide',
 'Bangalore',
 'St Kitts',
 'Cardiff',
 'Christchurch',
 'Trinidad']

bteam=teams.copy()

st.title('Cricket T20 WC Score Predictor')
col1,col2=st.columns(2)
with col1:
    batting_team=st.selectbox('Select batting team',sorted(teams))
with col2:
    bteam.remove(batting_team)
    bowling_team=st.selectbox('Select bowling team',sorted(bteam))

city=st.selectbox('Select city',sorted(cities))

col3,col4,col5=st.columns(3)

with col3:
    current_score=st.number_input('Current Score',min_value=0,value=1,step=1)

with col4:
    overs_done=st.number_input('Over Played(>5)',min_value=5,max_value=20,value=5,step=1)

with col5:
    wickets=st.number_input('Wickets',min_value=0,max_value=9,value=0,step=1)

last_five=st.number_input('Runs scored in  last 5 overs',min_value=1,value=1,step=1)

if st.button('Predict Score'):
    balls_left=120-(overs_done*6)
    wickets_left=10-wickets
    crr=current_score/overs_done

    input_df=pd.DataFrame(
        {
            'batting_team':[batting_team],'bowling_team':[bowling_team],'city':city,
            'current_score':[current_score], 'balls_left':[balls_left],'wickets_left':[wickets],
            'crr':[crr],'last_five':[last_five]
        }
    )
    result=pipe.predict(input_df)
    st.header('Projected Score: '+ str(int(result[0])))