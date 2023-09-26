import pandas as pd

# Funções de filtro
def mes_filtro(bd, mes):
    if mes == 0:
        mask= bd["Mês"].isin(bd["Mês"].unique())
    else:
        mask= bd["Mês"].isin([mes])
    
    return mask

def time_filtro(bd, time):
    if time == 0:
        filtro = bd["Equipe"].isin(bd["Equipe"].unique())
    else:
        filtro = bd["Equipe"].isin([time])
    
    return filtro

# Funções de conversão
def convert_to_text(mes):
    lista = ["Ano Todo", "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    
    return lista[mes]

# Funções de tratamento de base de dados
def trata_bd(bd):
    #Transforma os meses para seu respectivo número
    bd.loc[ bd["Mês"] == "Jan", "Mês" ] = 1
    bd.loc[ bd["Mês"] == "Fev", "Mês" ] = 2
    bd.loc[ bd["Mês"] == "Mar", "Mês" ] = 3
    bd.loc[ bd["Mês"] == "Abr", "Mês" ] = 4
    bd.loc[ bd["Mês"] == "Mai", "Mês" ] = 5
    bd.loc[ bd["Mês"] == "Jun", "Mês" ] = 6
    bd.loc[ bd["Mês"] == "Jul", "Mês" ] = 7
    bd.loc[ bd["Mês"] == "Ago", "Mês" ] = 8
    bd.loc[ bd["Mês"] == "Set", "Mês" ] = 9
    bd.loc[ bd["Mês"] == "Out", "Mês" ] = 10
    bd.loc[ bd["Mês"] == "Nov", "Mês" ] = 11
    bd.loc[ bd["Mês"] == "Dez", "Mês" ] = 12

    # Transformar Chamadas realizadas, meses e dia para variável tipo inteiro
    bd["Chamadas Realizadas"] = bd["Chamadas Realizadas"].astype(int)
    bd["Dia"] = bd["Dia"].astype(int)
    bd["Mês"] = bd["Mês"].astype(int)

    #Remove o R$ do campo e transforma para tipo inteiro
    bd["Valor Pago"] = bd["Valor Pago"].str.lstrip('R$ ') #lsstrip pega o que tá dentro do parêntesa no bd e exclui
    bd["Valor Pago"] = bd["Valor Pago"].astype(int)

    # Identifica as strings Pago/Não pago com número e transforma o campo para tipo inteiro
    bd.loc[bd["Status de Pagamento"] == "Pago", "Status de Pagamento"] = 1
    bd.loc[bd["Status de Pagamento"] == "Não pago", "Status de Pagamento"] = 0
    bd["Status de Pagamento"] = bd["Status de Pagamento"].astype(int)
    
    return bd