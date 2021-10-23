import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from Connection import Connection
import covidSQL as sql

external_stylesheets = ["https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css"]

# Inicializacion app dash
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


# Casos por pais
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.totalCasesByCountry(), con.connection)
con.closeConnection()
dfCases = pd.DataFrame(query, columns=["country_code", "country", "amount"])

# Grafico barras
figBarCases = px.bar(dfCases.head(25), x="country", y="amount",
                     )

figBarCasesH = px.bar(dfCases.head(25), y="country", 
                     x="amount", orientation = 'h',
                     )
# Grafico pie
figPieCases = px.pie(dfCases.head(25), values="amount", names="country",
                     title='Pie')

# Grafico mapa
figMapCases = px.choropleth(dfCases, locations="country",
                            locationmode="country names",
                            color="amount",
                            hover_name="country",
                            color_continuous_scale = ["#99ccff","#ff3333"] )

# Casos para America
con.openConnection()
query = pd.read_sql_query(sql.totalCasesAmericas(), con.connection)
con.closeConnection()
dfCases = pd.DataFrame(query, columns=["country_code", "country", "amount"])

# Grafico barras
figBarCasesRegion = px.bar(dfCases.head(56), y="country", 
                     x="amount", orientation = 'h',
                     title = 'Barras verticales región',
                     height=1000)

# Casos por Region
con.openConnection()
query = pd.read_sql_query(sql.totalCasesByRegion(), con.connection)
con.closeConnection()
dfCases = pd.DataFrame(query, columns=["region", "amount"])
# Grafico pie
figPieCasesRegions = px.pie(dfCases.head(25), values="amount", names="region",
                     title='Regions Pie')


# Layout 
app.layout = html.Div(children=[
    html.H1(children='Dashboard Covid 19 '),
    
    # Grid-Container ancho completo
    html.Div(className="container-fluid", children=[
        # Row for cases
         html.Div(className="row", children=[
             #Col for bar graph
             html.Div(className="col-12 col-xl-5", children=[
                 # Card bar graph
                   html.Div(className="card", children=[
                       html.Div(className="card-header", children=[
                           html.H2(children='Casos por país barras verticales'),
                       ]),
                   html.Div(className="card-body", children=[
                            dcc.Graph(
                                id='barCasesByCountry',
                                figure=figBarCases
                                ),
                       ]),
                   ]),
             ]),
             #Col for bar_h graph
             html.Div(className="col-12 col-xl-5", children=[
                 # Card bar graph
                   html.Div(className="card", children=[
                       html.Div(className="card-header", children=[
                           html.H2(children='Casos por país barras horizontales'),
                       ]),
                   html.Div(className="card-body", children=[
                                dcc.Graph(
                                    id='barHCasesByCountry',
                                    figure=figBarCasesH
                                    ),
                       ]),
                   ]),
             ]),
             #Col for pie graph
             html.Div(className="col-12 col-xl-5", children=[
                 # Card bar graph
                   html.Div(className="card", children=[
                       html.Div(className="card-header", children=[
                           html.H2(children='Casos por país pie'),
                       ]),
                   html.Div(className="card-body", children=[
                           dcc.Graph(
                               id='pieCasesByCountry',
                               figure=figPieCases
                               ), 
                       ]),
                   ]),
             ]),
        ]),
          # Row for cases
         html.Div(className="row", children=[
             #Col for pie graph
             html.Div(className="col", children=[
                 # Card bar graph
                   html.Div(className="card", children=[
                       html.Div(className="card-header", children=[
                           html.H2(children='Casos por país map'),
                       ]),
                   html.Div(className="card-body", children=[
                               
                           dcc.Graph(
                               id='mapCasesByCountry',
                               figure=figMapCases
                               ), 
                       ]),
                   ]),
             ]),
        ]),
    ]),

    html.H3(children='Casos para América'),
    dcc.Graph(
        id='barCasesAmerica',
        figure=figBarCasesRegion
    ), 
    html.H3(children='Casos por Región'),
    dcc.Graph(
        id='pieCasesRegions',
        figure=figPieCasesRegions
    ), 
])

if __name__ == '__main__':
    app.run_server(debug=True)
