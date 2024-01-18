import plotly.graph_objs as go
import plotly.offline as pyo
from datetime import datetime

  
 
def create_plot_metrics_vara(values):
    # Verificar si estamos trabajando con 'count_txn' o 'fee_avg'
    if 'count_txn' in values[0]:
        # Extraer fechas y cantidad de transacciones
        fechas = [dato['time'] for dato in values]
        y_values = [dato['count_txn'] for dato in values]
        y_label = 'Number of transactions'
    elif 'fee_avg' in values[0]:
        # Extraer fechas y promedio de tarifas
        fechas = [dato['time'] for dato in values]
        y_values = [dato['fee_avg'] for dato in values]
        y_label = 'Average fee (Gas Limit)'

    # Crear el gráfico
    layout = go.Layout(
        title=y_label,
        height=560,
        yaxis=dict(title=y_label, side='right')
    )

    data = [go.Scatter(x=fechas, y=y_values, mode='lines', line=dict(width=1))]
    fig = go.Figure(data=data, layout=layout)

    # Configuraciones adicionales del gráfico
    fig.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1m", step="month", stepmode="backward"),
                dict(count=6, label="6m", step="month", stepmode="backward"),
                dict(count=1, label="YTD", step="year", stepmode="todate"),
                dict(count=1, label="1y", step="year", stepmode="backward"),
                dict(step="all")
            ])
        )
    )

    config = {
        'displayModeBar': True,
        'modeBarButtonsToRemove': ['sendDataToCloud'],
        'showLink': False,
        'displaylogo': False
    }

    plot = pyo.plot(fig, output_type='div', config=config)

    # Retornar el plot
    return plot