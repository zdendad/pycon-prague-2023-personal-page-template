from dash import Dash, html, callback, Input, Output, State, page_container
import dash_mantine_components as dmc
from utils import nerespoznivny_navigacny_panel

app = Dash(__name__, use_pages=True)

links = {
    "o-mne": {"label": "O mne"},
    "zkusenosti": {"label": "zkušenosti"},
    "projekty": {"label": "Projekty"},
    "kontakty": {"label": "Kontakty"},
    "analyza-scitanie": {"label": "Analyza scitanie"},
}
app.layout = html.Div([
   nerespoznivny_navigacny_panel(odkazy = links, logo = "tabler:square-rounded-letter-l"),
   html.Div(page_container, style={"margin-top":"40px"})

])


if __name__ == "__main__":
    app.run(debug=True)
