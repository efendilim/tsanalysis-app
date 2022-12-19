import pandas as pd
import tslumen
import streamlit as st


def single_time_series():
    st.set_page_config(
        page_title="Single Time Series",
        page_icon="👋",
        layout="wide",
        # initial_sidebar_state="expanded",
    )

    st.write("## Single Time Series Analysis")

    with st.expander("Upload your file here for analysis!"):
        uploaded_file = st.file_uploader('Upload a CSV file')
        
    if uploaded_file is not None:
        df = pd.read_csv(
            uploaded_file,
            parse_dates=[2],
            date_parser=lambda dt: pd.to_datetime(f'{dt}-12-31'),
        )

        df = df[df['Country Code'].isin(['WLD', 'EUU', 'USA', 'HIC', 'MIC', 'LIC'])]\
            .set_index(['Year', 'Country Code'])['Value'].unstack(1)

        meta = {
            'frame': {
                'Description': 'Country, regional and world GDP in current US Dollars ($).',
                'Source': 'User upload file.',
            },
            'series': {
                'WLD': 'World GDP in current USD',
                'EUU': 'European Union GDP in current USD',
                'USA': 'United States GDP in current USD',
                'HIC': 'High income GDP in current USD',
                'MIC': 'Middle income GDP in current USD',
                'LIC': 'Low income GDP in current USD',
            }
        }

        report = tslumen.HtmlReport(df, meta)
        report.SECTIONS = report.SECTIONS[1:2]

        #save report to local html file
        html_file = './03_Tune_Profilers.html'
        report.save(html_file)

        # Read html file and keep in variable
        with open(html_file,'r') as f: 
            html_data = f.read()

        st.components.v1.html(html_data,height=8000, scrolling=False)


single_time_series()
