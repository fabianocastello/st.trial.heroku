import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import time
import socket
st.title('My first app @ heroku 4')
st.write("socket:", socket.gethostname())

t1 = os.environ['teste']
t2 = os.environ['another']
t3 = os.environ['another2']
t4 = os.environ['another3']

st.write(t1)
st.write(t2)
st.write(t3)
st.write(t4)

st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(10):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'