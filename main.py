# ------------------------------ Import -------------------------------- #
from dash import Dash, dcc, html, Input, Output, State
from dash_bootstrap_templates import ThemeSwitchAIO
from dash_bootstrap_components import Card, Col, Row, CardBody, Container, DropdownMenu, ButtonGroup, Button, Label, RadioItems
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from base import *


# ============== Links externos -> cdns de estilização / Tratamento de dados =========================#
FONT_AWESOME = ["http://use.fontawesome.com/releases/v6.4.2/css/all.css"]
link = "https://github.com/thercior"
bd = pd.read_csv("./assets/data/dataset_asimov.csv")
bd_base = bd.copy()
bd = trata_bd(bd)
# =============================== Instanciação da aplicação =======================================#

app = Dash(__name__, external_stylesheets=[FONT_AWESOME,dbc.themes.DARKLY, dbc.icons.BOOTSTRAP,])
app.scripts.config.serve_locally = True
server = app.server
# app = Dash(external_stylesheets=[dbc.themes.MINTY])

        # dbc.themes.TEMA ESCOLHIDO --> insere tema personalizado. ver na documentação DASH-BOOTSTRAP-COMPONENTs

# =============================== Estilos da aplicação ==============================================#
tab_card = {"height": "100%"}
main_config = {
    "hovermode": "x unified",
    "legend": {"yanchor": "top",
                "y":0.9,
                "xanchor": "left",
                "x":0.1,
                "title": {"text": None},
                "font": {"color": "white"},
                "bgcolor": "rgba(0,0,0,0.6 )"
            },
    "margin": {"l":10, "r":10, "t":10, "b":10}
}

config_graph = {"displayModeBar": False, "showTips": False}
style_graf = {"margin": {"l":10, "r":10, "t":20, "b":0}}

#criação de opções para listas
options_mes = [{"label": "Ano todo", "value":0}]
for i, j in zip(bd_base["Mês"].unique(), bd["Mês"].unique()):
    options_mes.append({"label": i, "value": j})
options_mes = sorted(options_mes, key=lambda x: x["value"])

options_time = [{"label": "Todas Equipes", "value": 0}]
for i in bd["Equipe"].unique():
    options_time.append({"label": i, "value": i})

# Funções de Filtro


#Opções de temas
Theme1, Theme2 = "darkly", "flatly", 
url_theme1, url_theme2 = dbc.themes.DARKLY, dbc.themes.FLATLY

# ===============================           Layout          =======================================#
app.layout = Container(children=[
    
    # Row 1 
    Row([
        Col([
            Card([
                CardBody([
                    Row([
                        Col([
                            html.Legend("Análises de Vendas - CallCenter", style={"font-size": "95%"})
                        ], sm=8),
                        
                        Col([
                            html.I(className="fa fa-balance-scale", style={"font-size": "200%"})
                        ], sm=4, align="center"),
                        
                    ]),
                    
                    Row([
                        Col([
                            ThemeSwitchAIO(aio_id="theme", themes=[url_theme1, url_theme2]),
                            html.Legend("TR Soluções")
                        ], sm=8),
                    ], style={"margin-top": "10px"}),
                    
                    Row([
                        Col([
                            html.I(className="fa fa-github")
                        ],sm=3, md=3,lg=3),
                        
                        Col([
                            Button("Perfil dev", href=link,target="_blank")
                        ], sm=9, md=9, lg=9)
                        
                    ], style={"margin-top": "10px"}),
                    
                    
                ])
            ],style=tab_card)
        ],sm=4, md=2, lg=2),
        Col([
            Card([
                CardBody([
                    Row([
                        Col([
                            html.Legend("Melhores Consultores por Equipe")
                        ])
                    ]),
                    
                    Row([
                        Col([
                            dcc.Graph(id="graf1", className="dbc", config=config_graph)
                        ], sm=12, md=7),
                        
                        Col([
                            dcc.Graph(id="graf2", className="dbc", config=config_graph)
                        ], sm=12, md=5)
                    ])
                ])
            ],style=tab_card)
        ], sm=12, md=7, lg=7),
        
        Col([
            Card([
                CardBody([
                    Row([
                        Col([
                            html.H5("Escolha o Mês"),
                            RadioItems(
                                id="radio-mes",
                                options=options_mes,
                                value=0,
                                inline=True,
                                labelCheckedClassName="text-success",
                                inputCheckedClassName="border border-success bg-success",
                                
                            ),
                            html.Div(id="mes-selecionado", style={"text-align": "center", "margin-top": "30px"})
                        ])
                    ])
                ])
            ],style=tab_card)
        ], sm=12, md=3, lg=3),
    ], className="g-2 my-auto", style={"margin-top": "7px"}),
    
    # Row 2
    Row([
        Col([
            Row([
                Col([
                    Card([
                        CardBody([
                            dcc.Graph(id="graf3", className="dbc", config=config_graph)
                        ])
                    ],style=tab_card)
                ])
            ]),
            
            Row([
                Col([
                    Card([
                        CardBody([
                            dcc.Graph(id="graf4", className="dbc", config=config_graph)
                        ])
                    ],style=tab_card)
                ])
            ],className="g-2 my-auto", style={"margin-top": "7px"})
        ], sm=12, md=5, lg=5),
        
        Col([
            Row([
                Col([
                    Card([
                        CardBody([
                            dcc.Graph(id="graf5", className="dbc", config=config_graph)
                        ])
                    ],style=tab_card)
                ],sm=6),
                
                Col([
                    Card([
                        CardBody([
                            dcc.Graph(id="graf6", className="dbc", config=config_graph)
                        ])
                    ],style=tab_card)
                ],sm=6),
            ],className="g-2"),
            
            Row([
                Col([
                    Card([
                        dcc.Graph(id="graf7", className="dbc", config=config_graph)
                    ],style=tab_card)
                ])
            ], className="g-2 my-auto", style={"margin-top": "7px"}),
            
        ], sm=12, md=4, lg=4),
        
        Col([
            Card([
                dcc.Graph(id="graf8", className="dbc", config=config_graph)
            ],style=tab_card)
        ], sm=12, md=3, lg=3),
        
    ],className="g-2 my-auto", style={"margin-top": "7px"}),
    
    #Row 3
    Row([
        Col([
            Card([
                CardBody([
                    html.H4("Distribuição de propaganda"),
                    dcc.Graph(id="graf9", className="dbc", config=config_graph)
                ])
            ],style=tab_card)
        ],sm=12, md=2, lg=2),
        Col([
            Card([
                CardBody([
                    html.H4("Valores de Propaganda convertidos por mês"),
                    dcc.Graph(id="graf10", className="dbc", config=config_graph)
                ])
            ],style=tab_card)
        ], sm=12, md=5, lg=5),
        
        Col([
            Card([
                CardBody([
                    dcc.Graph(id="graf11", className="dbc", config=config_graph)
                ])
            ],style=tab_card)
        ],sm=12, md=3, lg=3),
        
        Col([
            Card([
                CardBody([
                    html.H5("Escolha a Equipe"),
                    RadioItems(
                        id="radio-time",
                        options=options_time,
                        value=0,
                        inline=True,
                        labelCheckedClassName="text-warning",
                        inputCheckedClassName="border border-warning bg-warning"
                    ),
                    html.Div(id="time-selecionado", style={"text-align": "center", "margin-top": "30px"})
                ])
            ],style=tab_card)
        ], sm=12, md=2, lg=2),
        
    ],className="g-2 my-auto", style={"margin-top": "7px"})
    
], fluid=True, style={"height": "100vh"})

# ===============================    Callback/Atualização   =======================================#
# Callback gráficos 1 e 2 - Melhores consultores de cada equipe
@app.callback(
        
        # Saída (dados atualizados)
        [   
            Output(component_id="graf1", component_property="figure"),
            Output(component_id="graf2", component_property="figure"),
            Output("mes-selecionado", "children"),
        ],
        
        # Entrada (dados que serão atualizados)
        [
            Input(component_id="radio-mes", component_property="value"),
            Input(component_id=ThemeSwitchAIO.ids.switch("theme"), component_property="value"),
            
        ]
        # State

)
def graf1_2(mes, toggle):
    # Função para criação do 
    template = Theme1 if toggle else Theme2
    
    mask = mes_filtro(bd, mes)
    bd1 = bd.loc[mask]
    
    bd1 = bd1.groupby(["Equipe", "Consultor"])["Valor Pago"].sum()
    bd1 = bd1.sort_values(ascending=False)
    bd1 = bd1.groupby("Equipe").head(1).reset_index()
    
    fig2 = go.Figure(go.Pie(labels=bd1["Consultor"] + " - " + bd1["Equipe"], values = bd1["Valor Pago"], hole=.6))
    fig1 = go.Figure(go.Bar(
        x=bd1["Consultor"], y=bd1["Valor Pago"],
        textposition="auto",
        text=bd1["Valor Pago"]
    ))
    fig1.update_layout(main_config, height=200, template=template)
    fig2.update_layout(main_config, height=200, template=template, showlegend=False)
    
    select = html.H3(convert_to_text(mes))
    
    return fig1, fig2, select

# Callbacks do gráfico 3 - Chamadas realizadas por equite/total por dia
@app.callback(
        
        # Saída (dados atualizados)
        Output(component_id="graf3", component_property="figure"),
        
        # Entrada (dados que serão atualizados)
        [
            Input(component_id="radio-time", component_property="value"),
            Input(component_id=ThemeSwitchAIO.ids.switch("theme"), component_property="value"),
        ]
        # State

)
def graf3(time, toggle):
    # Função para criação do 
    template = Theme1 if toggle else Theme2
    
    filtro = time_filtro(bd, time)
    bd3 = bd.loc[filtro]
    
    bd3 = bd3.groupby("Dia")["Chamadas Realizadas"].sum().reset_index()
    
    fig3 = go.Figure(go.Scatter(
        x=bd3["Dia"], y=bd3["Chamadas Realizadas"],
        mode = "lines", fill="tonexty"
    ))
    fig3.add_annotation(
        text="Chamadas Médias por dia do Mês",
        xref="paper", yref="paper",
        font=dict(size=17, color="gray"),
        align="center", bgcolor="rgba(0,0,0,0.8)",
        x=0.05, y=0.85, showarrow=False
    )
    fig3.add_annotation(
        text=f"Média : {round(bd3['Chamadas Realizadas'].mean(), 2)}",
        xref="paper", yref="paper",
        font=dict(size=20, color="gray"),
        align="center", bgcolor="rgba(0,0,0,0.8)",
        x=0.05, y=0.55, showarrow=False
    )
    fig3.update_layout(main_config, height=180, template=template)
    
    return fig3

# Callbacks do gráfico 4 - Chamadas realizadas de cada equipe e total por mês
@app.callback(
        
        # Saída (dados atualizados)
        Output(component_id="graf4", component_property="figure"),
        
        # Entrada (dados que serão atualizados)
        [
            Input(component_id="radio-time", component_property="value"),
            Input(component_id=ThemeSwitchAIO.ids.switch("theme"), component_property="value"),
        ]
        # State

)
def graf4(time, toggle):
    # Função para criação do 
    template = Theme1 if toggle else Theme2
    
    filtro = time_filtro(bd, time)
    bd4 = bd.loc[filtro]
    
    bd4 = bd4.groupby("Mês")["Chamadas Realizadas"].sum().reset_index()
    
    fig4 = go.Figure(go.Scatter(
        x=bd4["Mês"], y=bd4["Chamadas Realizadas"],
        mode = "lines", fill="tonexty"
    ))
    fig4.add_annotation(
        text="Chamadas Médias por Mês",
        xref="paper", yref="paper",
        font=dict(size=15, color="gray"),
        align="center", bgcolor="rgba(0,0,0,0.8)",
        x=0.05, y=0.85, showarrow=False
    )
    fig4.add_annotation(
        text=f"Média : {round(bd4['Chamadas Realizadas'].mean(), 2)}",
        xref="paper", yref="paper",
        font=dict(size=20, color="gray"),
        align="center", bgcolor="rgba(0,0,0,0.8)",
        x=0.05, y=0.55, showarrow=False
    )
    fig4.update_layout(main_config, height=180, template=template)
    
    return fig4

# Callbacks do gráfico 5 e 6 (indicadores 1 e 2) - Melhor consultor e melhor equipe
@app.callback(
        
        # Saída (dados atualizados)
        [
            Output(component_id="graf5", component_property="figure"),
            Output(component_id="graf6", component_property="figure"),
        ],
        # Entrada (dados que serão atualizados)
        [
            Input(component_id="radio-mes", component_property="value"),
            Input(component_id=ThemeSwitchAIO.ids.switch("theme"), component_property="value"),
        ]
        # State

)
def graf5_6(mes, toggle):
    
    template = Theme1 if toggle else Theme2
    
    filtro = mes_filtro(bd, mes)
    bd5 = bd6 = bd.loc[filtro]
    
    bd5 = bd5.groupby(["Consultor", "Equipe"])["Valor Pago"].sum()
    bd5.sort_values(ascending=False, inplace=True)
    bd5 = bd5.reset_index()
    
    fig5 = go.Figure()
    fig5.add_trace(go.Indicator(
        mode="number+delta",
        title={"text": f"<span style='font-size:80%'>{bd5['Consultor'].iloc[0]} - Melhor Consultor</span><br><span style='font-size:65%'>Em vendas - em relação a média</span>"},
        value=bd5["Valor Pago"].iloc[0],
        number={"prefix": "R$"},
        delta={"relative": True, "valueformat": ".1%", "reference": bd5["Valor Pago"].mean()}
    ))
    fig5.update_layout(main_config, height=200, template=template)
    
    bd6 = bd6.groupby("Equipe")["Valor Pago"].sum()
    bd6.sort_values(ascending=False, inplace=True)
    bd6 = bd6.reset_index()
    
    fig6 = go.Figure()
    fig6.add_trace(go.Indicator(
        mode="number+delta",
        title={"text": f"<span style='font-size:80%'>{bd6['Equipe'].iloc[0]} - Melhor Equipe</span><br><span style='font-size:65%'>Em vendas - em relação a média</span>"},
        value=bd6["Valor Pago"].iloc[0],
        number={"prefix": "R$"},
        delta={"relative": True, "valueformat": ".1%", "reference": bd6["Valor Pago"].mean()}
    ))
    fig6.update_layout(main_config, height=200, template=template)
    
    fig5.update_layout(style_graf)
    fig6.update_layout(style_graf)
    
    return fig5, fig6

#Callback Gráfico 7 - Valor de venda por equipe e total ao longo dos meses
@app.callback(
        
        # Saída (dados atualizados)
        Output(component_id="graf7", component_property="figure"),
        
        # Entrada (dados que serão atualizados)
        [
            Input(component_id=ThemeSwitchAIO.ids.switch("theme"), component_property="value"),
        ]
        # State

)
def graf7(toggle):
    
    template = Theme1 if toggle else Theme2
    
    bd7= bd.groupby(["Mês", "Equipe"])["Valor Pago"].sum().reset_index()
    bd7_group = bd.groupby("Mês")["Valor Pago"].sum().reset_index()
    
    fig7 = px.line(bd7, y="Valor Pago", x="Mês", color="Equipe")
    fig7.add_trace(go.Scatter(
        y=bd7_group["Valor Pago"], x=bd7_group["Mês"],
        mode="lines+markers", fill="tonexty", name="Total de vendas"
    ))
    fig7.update_layout(main_config, yaxis={"title": None}, xaxis={"title": None}, height=190, template=template)
    fig7.update_layout({"legend": {"yanchor": "top", "y": 0.99, "font": {"color": "white", "size": 10}}})
    
    return fig7

# Callback gráfico 8 - Valor Pago por Equipe
@app.callback(
        
        # Saída (dados atualizados)
        Output(component_id="graf8", component_property="figure"),
        
        # Entrada (dados que serão atualizados)
        [
            Input(component_id="radio-mes", component_property="value"),
            Input(component_id=ThemeSwitchAIO.ids.switch("theme"), component_property="value"),
        ]
        # State

)
def graf8(mes, toggle):
    
    template = Theme1 if toggle else Theme2
    
    filtro = mes_filtro(bd, mes)
    bd8 = bd.loc[filtro]
    
    bd8 = bd8.groupby("Equipe")["Valor Pago"].sum().reset_index()
    
    
    fig8 = go.Figure(go.Bar(
        x=bd8["Valor Pago"], y=bd8["Equipe"],
        orientation="h", textposition="auto", text=bd8["Valor Pago"],
        insidetextfont=dict(family="Verdana, Sans-serif, Arial, Helvetica", size=12),
    ))
    
    fig8.update_layout(main_config, height=360, template=template)
    
    return fig8

# Callback gráfico 9 - valor pago de acordo com o meio de propaganda
@app.callback(
        
        # Saída (dados atualizados)
        Output(component_id="graf9", component_property="figure"),
        
        # Entrada (dados que serão atualizados)
        [
            Input(component_id="radio-mes", component_property="value"),
            Input(component_id="radio-time", component_property="value"),
            Input(component_id=ThemeSwitchAIO.ids.switch("theme"), component_property="value"),
        ]
        # State

)
def graf9(mes, time, toggle):
    # Função para criação do 
    template = Theme1 if toggle else Theme2
    
    filtro_mes, filtro_time = mes_filtro(bd, mes), time_filtro(bd, time)
    bd9 = bd.loc[filtro_mes].loc[filtro_time]
    
    bd9 = bd9.groupby("Meio de Propaganda")["Valor Pago"].sum().reset_index()
    
    
    fig9 = go.Figure()
    fig9.add_trace(go.Pie(labels=bd9["Meio de Propaganda"], values=bd9["Valor Pago"], hole=.7))
    
    fig9.update_layout(main_config, height=150, template=template, showlegend=False)
    
    return fig9

# Callback gráfico 10 - valor pago convetidos de propaganda por mês
@app.callback(
        
        # Saída (dados atualizados)
        Output(component_id="graf10", component_property="figure"),
        
        # Entrada (dados que serão atualizados)
        [
            Input(component_id="radio-time", component_property="value"),
            Input(component_id=ThemeSwitchAIO.ids.switch("theme"), component_property="value"),
        ]
        # State

)
def graf10(time, toggle):
    # Função para criação do 
    template = Theme1 if toggle else Theme2
    
    filtro_time = time_filtro(bd, time)
    bd10 = bd.loc[filtro_time]
    
    bd10 = bd10.groupby(["Meio de Propaganda", "Mês"])["Valor Pago"].sum().reset_index()
    
    fig10 = px.line(bd10, y="Valor Pago", x="Mês", color="Meio de Propaganda")
    
    fig10.update_layout(main_config, height=200, template=template, showlegend=False)
    
    return fig10


# Callback gráfico 11 - Indicador de valor total de vendas por equipe/total e ao longo do ano
@app.callback(
        
        # Saída (dados atualizados)
        [
            Output(component_id="graf11", component_property="figure"),
            Output(component_id="time-selecionado", component_property="children"),
        ],
        # Entrada (dados que serão atualizados)
        [
            Input(component_id="radio-mes", component_property="value"),
            Input(component_id="radio-time", component_property="value"),
            Input(component_id=ThemeSwitchAIO.ids.switch("theme"), component_property="value"),
        ]
        # State

)
def graf11(mes, time, toggle):
    # Função para criação do 
    template = Theme1 if toggle else Theme2
    
    filtro_mes, filtro_time = mes_filtro(bd, mes), time_filtro(bd, time)
    
    bd11 = bd.loc[filtro_mes].loc[filtro_time]
    
    fig11 = go.Figure()
    fig11.add_trace(go.Indicator(
        mode="number", 
        title={"text": f"<span style='font-size:150%'>Valor Total</span><br><span style='font-size:70%'>Em Reais</span><br>"},
        value=bd11["Valor Pago"].sum(),
        number={"prefix": "R$"}
    ))
    
    fig11.update_layout(main_config, height=300, template=template, showlegend=False)
    
    select = html.H4("Todas Equipes") if time == 0 else html.H1(time)
    
    return fig11, select

# ===============================          Execução         =======================================#
if __name__ == '__main__':
    app.run_server(debug=False, port=9000, host='0.0.0.0')

# debug false => coloca projeto para produção
# port => define a porta do servidor que o projeto vai rodar
# host => definir o host como '0.0.0.0' deixa o projeto disponível para ser acesado por qualquer dispositivo da mesma rede wi-fi
# do dispositivo em que o projeto está sendo executado