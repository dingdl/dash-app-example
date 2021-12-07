import dash
from dash import html


app = dash.Dash()
app.layout = html.Div(
    children=html.H1(
        children=['Your first Dash App!']
    )
)

app.title = 'Example'

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run_server(debug=True, host="0.0.0.0", port=8050)