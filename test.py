import streamlit as st
import leafmap.foliumap as leafmap
from pygmtsar import S1, Stack, tqdm_dask, ASF, Tiles, XYZTiles

st.title('SAR Processing with pyGMTSAR and Streamlit')

SCENE1 = st.text_input(label='Copy paste the first scene ID')
SCENE2 = st.text_input(label='Copy paste the second scene ID')

ORBIT = st.selectbox('Choose Orbit', ('A', 'D'),
                    #placeholder='A for Ascending. D for Descending',
                    index=None)

SUBSWATH = 1

POLARIZATION = st.selectbox('Choose Polarization',
                            ('VV', 'HH', 'HV'),
                            index=None)


