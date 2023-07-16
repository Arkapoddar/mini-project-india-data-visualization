import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(layout="wide")

final_df=pd.read_csv("India (1).csv")
list_of_state=list(final_df["State"].unique())
list_of_state.insert(0,"Overall India")


st.sidebar.title("India-Data-Visualisation")
select_one=st.sidebar.selectbox("Select A State",list_of_state)
primary_one=st.sidebar.selectbox("Select primary parameter",sorted(final_df.columns[5:]))
secondary_one=st.sidebar.selectbox("Select secendory parameter",sorted(final_df.columns[5:]))
plot=st.sidebar.button('Plot Graph')
if plot:

    st.text("size Parameter => primary one")
    st.text("color Parameter => secondary one")


    if select_one=="Overall India":
        fig=px.scatter_mapbox(final_df, lat="Latitude", lon="Longitude", zoom=3.5,size=primary_one,color=secondary_one, mapbox_style='carto-positron',width=1600,height=700,hover_name="District")
        st.plotly_chart(fig,use_container_width=True)
    else:
        state_df=final_df[final_df["State"]==select_one]
        fig = px.scatter_mapbox(state_df, lat="Latitude", lon="Longitude", zoom=3.5, size=primary_one,
                                color=secondary_one, mapbox_style='carto-positron', width=1600, height=700,hover_name="District")
        st.plotly_chart(fig, use_container_width=True)


else:
    pass



