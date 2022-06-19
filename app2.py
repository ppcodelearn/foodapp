import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner
import time
import requests
import random

from sendmessage import list
from sendmessage import producttype

from itertools import cycle
from PIL import Image

# def load_lottieurl(url: str):
#     r = requests.get(url)
#     if r.status_code != 200:
#         return None
#     return r.json()


# lottie_url_hello = "https://assets5.lottiefiles.com/packages/lf20_V9t630.json"
# lottie_url_download = "https://assets4.lottiefiles.com/private_files/lf30_t26law.json"
# lottie_hello = load_lottieurl(lottie_url_hello)
# lottie_download = load_lottieurl(lottie_url_download)


# horizontal menu
selected2 = option_menu(None, ["Home", "Upload", "Tasks", 'Settings'], 
    icons=['house', 'cloud-upload', "list-task", 'gear'], 
    menu_icon="cast", default_index=0, orientation="horizontal")
# selected2

banana = Image.open(r'C:\Users\LIQWV\Project\streamlit\banana.jpg')
grape = Image.open(r'C:\Users\LIQWV\Project\streamlit\grape.jpg')
orange = Image.open(r'C:\Users\LIQWV\Project\streamlit\orange.jpg')
apple = Image.open(r'C:\Users\LIQWV\Project\streamlit\apple.jpg')

filteredImages = [banana,grape,orange,apple] # your images here

if producttype == 'apple':
    saveimage = filteredImages[0]
    filteredImages[0] = apple
    indexC = 0
    while indexC <= len(filteredImages)-1:
        if indexC > 0:
            if filteredImages[indexC] == apple:
                filteredImages[indexC] = saveimage
        indexC += 1
            

#price with discount or just price
caption = list
# caption = ['2 EUR','3 EUR','4 EUR','3 EUR'] # your caption here
# cols = cycle(st.columns(4)) # st.columns here since it is out of beta at the time I'm writing this
# for idx, filteredImage in enumerate(filteredImages):
#     next(cols).image(filteredImage, width=150, caption=caption[idx])


idx = 0 
for _ in range(len(filteredImages)-1): 
    cols = st.columns(4) 
    
    if idx < len(filteredImages): 
        cols[0].image(filteredImages[idx], width=150, caption=caption[idx])
    idx+=1
    
    if idx < len(filteredImages):
        cols[1].image(filteredImages[idx], width=150, caption=caption[idx])
    idx+=1

    if idx < len(filteredImages):
        cols[2].image(filteredImages[idx], width=150, caption=caption[idx])
    idx+=1 
    if idx < len(filteredImages): 
        cols[3].image(filteredImages[idx], width=150, caption=caption[idx])
        idx = idx + 1
    else:
        break