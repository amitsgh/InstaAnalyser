
import streamlit as st
import requests
import numpy as np
import pandas as pd
import os
import json
import pandas as pd
import numpy as np
import re
import string

from datetime import datetime

class UserData:
    
    def getUserInfo():
        st.title('Instagram Dashboard')

        with st.form(key='my_form'):
            
            #gets a text input
            username = st.text_input(label='Enter User Name')

            #creates a submit button
            submit_button = st.form_submit_button(label='Submit')

if __name__ == '__main__':
    UserData.getUserInfo()