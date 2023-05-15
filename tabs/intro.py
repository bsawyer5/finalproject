from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app import app

layout = [dcc.Markdown("""
### Intro

This project uses data from the Cleveland Clinic Heart Disease dataset, collated by Dr Robert Detrano, M.D., Ph.D.
It was collected in response to the need for noninvasive coronary heart disease diagnostics, an alternative the gold stanard coronary angiogram. The original dataset contains 303 observations and 76 attributes, however for the purposes of this project a subset of 14 attributes(13 observable features and 1 taget variable) is used. The features include scores for alternative non-invasive diagnostics tests for heart disease, as well as some patient information. As there were no missing values, the dataset did not need much pre-processing. I only renamed some column heads just for ease of comprehension, prior to commencing exploratory work. It is also worth noting that the last column denotes the presence and severity of heart disease ie 0= no coronary disease, and 1-4 representing progressive severity of the occlusion. Prior work with this dataset has investigated purely the presence or absence of heart disease, ie 0 for no disease and 1 otherwise (values 1-4).

"""),
         
         
html.Img(src='data/chd.png
         https://raw.githubusercontent.com/bsawyer5/finalproject/main/data/chd.png'')
         
         
         
dcc.Markdown(""" _By Beryl Sawyerr_ """)]