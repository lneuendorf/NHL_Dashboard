# import dash-core, dash-html, dash io, bootstrap
# import dash_core_components as dcc
from dash import dcc
# import dash_html_components as html
from dash import html
from dash.dependencies import Input, Output

# Dash Bootstrap components
import dash_bootstrap_components as dbc

# Navbar, layouts, custom callbacks
from layouts import appMenu, menuSlider, playerMenu, teamLayout, battingLayout
from layouts import fieldingLayout, projMenu, projLayout, team_menu, teamLayout_old
import callbacks

# Import from other files under same folder
from app_setup import app
# Import server for deployment
from app_setup import app_srv as server

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "right": 0,
    "height": "12rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
    "zIndex": 100,
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-top": "14rem",
    "margin-left": "2rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

topbar = html.Div(
    [
        html.H2("National Hockey League - Data Explorer", className="display-5"),
        html.Hr(), # horizontal rule, a thematic break between paragraph-level elements 
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("Team Information", href="/team", active="exact"),
                dbc.NavLink("Player Information", href="/player", active="exact"),
                dbc.NavLink("Update Player Data", href="/update", active="exact"),
            ],
            # horizontal="End",
            pills=True,
        ),
        html.Hr(),
        # html.H2("Historical Analysis", className="lead"),
        # html.Hr(),
        # html.H2("Machine Learning Analysis", className="lead"),
        # dbc.Nav(
        #     [
        #         dbc.NavLink("Projections and Regression", href="/projection", active="exact"),
        #         # dbc.NavLink("Batting Analysis", href="/player", active="exact"),
        #         # dbc.NavLink("Pitching/Feilding Analysis", href="/field", active="exact"),
        #     ],
        #     vertical=True,
        #     pills=True,
        # ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

# Sidebar layout
app.layout = html.Div([dcc.Location(id="url"), topbar, content])


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == '/':
        return html.Div([dcc.Markdown('''
            ### Applicaiton Introduction
            This application is a portfolio project built by [Matt Parra](https://devparra.github.io/) using Plotly's Dash,
            faculty.ai's Dash Bootstrap Components, Pandas, SKlearn's Linear Regression algorithm, and custom functions. 
            Using historical MLB (Major League Baseball) data, this application provides visualizations for team and player 
            statistics dating from 1903 to 2020. This application also provides player projections and regression analysis.

            The data used in this application was retrieved from [Seanlahman.com](http://www.seanlahman.com/baseball-archive/statistics/).
            Provided by [Chadwick Baseball Bureau's GitHub](https://github.com/chadwickbureau/baseballdatabank/) .
            This database is copyright 1996-2021 by Sean Lahman. This data is licensed under a Creative Commons Attribution-ShareAlike
            3.0 Unported License. For details see: [CreativeCommons](http://creativecommons.org/licenses/by-sa/3.0/)
        ''')], className='home')
    elif pathname == '/team':
        return team_menu, teamLayout
        # return appMenu, menuSlider, teamLayout
    elif pathname == '/player':
        return appMenu, menuSlider, playerMenu, battingLayout
    elif pathname == '/update':
        return appMenu, menuSlider, fieldingLayout
    # elif pathname == '/projection':
    #     return projMenu, projLayout
    else:
        # If the user tries to reach a different page, return a 404 message
        return dbc.Jumbotron(
            [
                html.H1("404: Not found", className="text-danger"),
                html.Hr(),
                html.P(f"The pathname {pathname} was not recognized..."),
            ]
        )


# Call app server
if __name__ == '__main__':
    # set debug to false when deploying app
    app.run_server(debug=True)
