import pandas as pd
import tslumen
import pandas as pd

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def multiple_time_series():
    st.set_page_config(
        page_title="Multiple Time Series",
        page_icon="👋",
        layout="wide",
        # initial_sidebar_state="expanded",
    )

    st.write("## Multiple Time Series Analysis")

    with st.expander("Upload your file here for analysis!"):
        uploaded_file = st.file_uploader('Upload a CSV file')

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file, parse_dates=[0], index_col=0)
        df = df[(df.index >= '1990-01-01') & (df.index < '2015-01-01')]
        meta = {
            'frame': {
                'Description': '''S&P 500 index data including level, dividend, earnings and P/E ratio on
        a monthly basis since 1870. The S&P 500 (Standard and Poor’s 500) is a free-float,
        capitalization-weighted index of the top 500 publicly listed stocks in the US (top 500 by market cap)''',
                'Source': '<a href="https://datahub.io/core/s-and-p-500">DataHub</a>',
            },
            'series': {
                'SP500': "Level ('price') of the S&P 500 index",
                'Dividend': 'Dividend',
                'Earnings': 'Earnings',
                'Consumer Price Index': 'Consumer Price Index',
                'Long Interest Rate': '10 year interest rate (gov bonds)',
                'Real Price': 'Real Price',
                'Real Dividend': 'Real Dividend',
                'Real Earnings': 'Real Earnings',
                'PE10': 'Cyclically Adjusted Price Earnings Ratio P/E10 or CAPE',
            }
        }

        report = tslumen.HtmlReport(df, meta)

        #save report to local html file
        html_file = './01_Multiple_Series.html'
        report.save(html_file)

        # Read html file and keep in variable
        with open(html_file,'r') as f: 
            html_data = f.read()

        st.components.v1.html(html_data,height=8000, scrolling=False)

    
multiple_time_series()
