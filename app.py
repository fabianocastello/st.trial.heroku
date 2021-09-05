import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import time
import socket
import os

st.title('My first app @ heroku 4')
st.write("socket:", socket.gethostname())

# The first entry in the list should be the client's IP.
 
################
# from flask import request
# x = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)

from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

@app.route("/get_my_ip", methods=["GET"])
def get_my_ip():
     return jsonify({'ip': request.remote_addr}), 200
     
@app.route('/q')
def query_example():
    return 'Query String Example'
# x = 'teste'#get_my_ip()
#provided_ips = request.headers.getlist("X-Forwarded-For")

@app.route('/q1')
def query_example1():
    if not request.headers.getlist("X-Forwarded-For"):
       ip = request.remote_addr
    else:
       ip = request.headers.getlist("X-Forwarded-For")[0]
    return ip


from werkzeug.contrib.fixers import ProxyFix
# [ ... ]
app.wsgi_app = ProxyFix(app.wsgi_app)

# (don't just copy/paste this -- keep reading)



###############

t1 = os.environ['teste']
t2 = os.environ['another']
t3 = os.environ['another2']
t4 = os.environ['another3']

st.write(t1)
st.write(t2)
st.write(t3)
st.write(t4)
# st.write(x)
# st.write(provided_ips)

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