# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 18:57:10 2020

@author: Jaimin Panchal
Project: QR Code
"""

import streamlit as st
import streamlit.components.v1 as components

import qrcode


html_code = """
        <div style="background-color: #3cba54 ; padding:  10px; border-radius: 10px">
          <h1 style="color:white; text-align: center">QR Code Generator</h1>
        </div>
        """
components.html(html_code)


# Add the data to QR
data = st.text_input("Enter the data you want to embed")
data_title = data.title()


# Number Inputs
box_size = st.number_input("Enter the box size")
border = st.number_input("Enter the border spacing value")

# Select Box Inputs
from matplotlib import colors as mcolors

colors = mcolors.CSS4_COLORS
colors_list = list(colors.keys())

fill = st.selectbox("Select the fill color", colors_list)
back = st.selectbox("Select the background color", colors_list)


# Create a QR Code

if(st.button("Generate QR Code")):
    qr = qrcode.QRCode(
        box_size=box_size,
        border=border
    )
    
    qr.add_data(data_title)
    qr.make()
    img = qr.make_image(fill_color = fill, back_color = back)
    img.save('myqr.png')
    
    
    # Display the QR Code
    img = Image.open("myqr.png")
    st.image(img)










