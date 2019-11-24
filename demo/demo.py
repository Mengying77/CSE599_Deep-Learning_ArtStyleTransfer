import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import style_transfer
import base64  # REMOVE LATER

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

styles = {
    'van Gogh': 'Gogh',
    'Monet': 'Monet'
}

# REMOVE LATER
image_filename = '../images/style/Gogh-StarryNight.jpg' # replace with your own image
encoded_image = base64.b64encode(open(image_filename, 'rb').read())
#

app.layout = html.Div([
    html.H1('ArtNet', style={'textAlign': 'center'}),

    html.Hr(),

    # drag or upload input image
    html.Div(
        children=[
            dcc.Upload(
                id='input-image',
                children=html.Div(['Drag and Drop or ', html.Button('Select a File')]),
                style={
                    'width': '100%',
                    'height': '60px',
                    'lineHeight': '60px',
                    'borderWidth': '1px',
                    'borderStyle': 'dashed',
                    'borderRadius': '5px',
                    'textAlign': 'center',
                    'backgroundColor': '#F7F3E3'
                },
                accept='image/*'
            )
        ],
        style={'width': '48%', 'display': 'inline-block', 'verticalAlign': 'top'}
    ),

    # style options
    html.Div(
        children=[
            html.Label([
                "Choose a style",
                dcc.Dropdown(
                    id='choose-style',
                    options=[
                        {'label': label, 'value': value} for (label, value) in styles.items()
                    ],
                    value='Gogh',  # initial value
                )]
            )
        ],
        style={'width': '48%', 'display': 'inline-block', 'marginLeft': '30px', 'verticalAlign': 'top'}
    ),

    html.Hr(),

    # display input image
    html.Div(
        id='display-input-image',
        style={'width': '50%', 'display': 'inline-block'}
    ),

    # display output image
    html.Div(
        style={'width': '50%', 'display': 'inline-block', 'verticalAlign': 'top'},
        id='display-output-image'
    ),

], style={'padding': '10px'})


@app.callback(Output('display-input-image', 'children'),
              [Input('input-image', 'contents')],
              [State('input-image', 'filename')])
def display_input(contents, filename):
    if contents is not None:
        children = [
            html.H5('Input Image: ' + filename),
            html.Img(src=contents, style={'width': '100%'}),
        ]
        return children


@app.callback(Output('display-output-image', 'children'),
              [Input('input-image', 'filename')],
              [State('choose-style', 'value')])
def display_output(input_image_name, style):
    if input_image_name is not None:
        output_image = style_transfer.transfer(input_image_name, style)
        for key, value in styles.items():
            if value == style:
                style_name = key
        children = [
            html.H5('Output Image (' + style_name + ')'),
            html.Img(
                src='data:image/png;base64,{}'.format(output_image.decode()),
                style={'width': '100%'}
            ),
        ]
        return children


if __name__ == '__main__':
    app.run_server(debug=True)