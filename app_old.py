from dash import Dash, html, callback, Input, Output, State
import dash_mantine_components as dmc

app = Dash(__name__)

app.layout = html.Div([

    dmc.NumberInput(
        id="input1",
        label="Prvni číslo",
        description="From 0 to infinity, in steps of 5"

    ),


    dmc.NumberInput(
        id="input2",
        label="Druhé číslo",
    ),

    dmc.Button(
        "Stiskni mně",
        id="tlacitko",
    ),

    dmc.Text(id="vystup")

])
@callback(
    Output(component_id="vystup" , component_property="children"),
    Input(component_id="tlacitko" , component_property="n_clicks"),
    State(component_id="input1" , component_property="value"),
    State(component_id="input2" , component_property="value"),
    prevent_initial_call= True,
)

def scitaj(n_click, hodnota1, hodnota2):
    return hodnota1+hodnota2

if __name__ == "__main__":
    app.run(debug=True)
