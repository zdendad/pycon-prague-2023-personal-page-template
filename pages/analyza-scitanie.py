from utils import priprava_dat
from dash import register_page, html, dcc, Input, Output, callback
import dash_mantine_components as dmc
from plotly.express import bar
register_page(__name__)

df = priprava_dat()


layout = dmc.Stack([
    dmc.Select(
        id="vyber-uzemi",
        value="Česká republika", # předvyplněná hodnota
        label="vyberte oblast:",
        data=[
            {"value": moznost, "label": moznost}
            for moznost in df["uzemi_txt"].drop_duplicates()


        ]

    ),
    dcc.Graph(id="graf-vzdelanie")
])

@callback(
    Output(component_id="graf-vzdelanie" , component_property="figur"),
    Input(component_id="vyber-uzemi" , component_property="value"),
    prevent_initial_call= True,
)

def data_do_grafu(uzemie):
    w_df = df.copy()
    w_df = w_df[w_df["uzemi_txt"] == uzemie]
    w_df = w_df.groupby(by=["vzdelani_txt"])["hodnota"].sum().reset_index()

    fig = bar(w_df, x="vzdelani_txt", y = "hodnota")
    return fig
