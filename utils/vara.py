from utils.db_manager.db_manager_vara import VaraDBManager
from .helper import convert_to_datetime
from dashboard.plot import create_plot_metrics_vara

def get_fees_avg(blockDetails):
    # Crear una lista para almacenar los resultados
    data = []
    for value in blockDetails:
        
        timestamp = value['blockDetails']['block']['extrinsics'][0]['method']['args']['now']
        datatime = convert_to_datetime(timestamp)
        blockDetails = value['blockDetails']['block']['extrinsics'][1:]
        data_fee = []
        for block in blockDetails:
            # Usando el método get para evitar KeyError
            gas_limit = block['method']['args'].get('gas_limit')
            if gas_limit:
                # Eliminar las comas y convertir a entero
                gas_limit = int(gas_limit.replace(',', ''))
                data_fee.append(gas_limit)
       
        # Calcular el promedio si hay datos disponibles
        if data_fee:
            avg_gas_limit = sum(data_fee) / len(data_fee)
        else:
            avg_gas_limit = 0

        data.append({'time': datatime, 'fee_avg':avg_gas_limit})
       
    return data

def get_count_tnx_events(blockDetails):
        # Crear una lista para almacenar los resultados
    data = []
    for value in blockDetails:
        timestamp = value['blockDetails']['block']['extrinsics'][0]['method']['args']['now']
        datatime = convert_to_datetime(timestamp)
        count_txn = len(value['events'])
        data.append({'time': datatime, 'count_txn': count_txn})
    
    return data

def get_last_three_blocks():
    db_manager = VaraDBManager()
    values = db_manager.get_last_three_documents()
    values_blocks=[]
    for value in values:
        data_fee = []
        number_block = value['blockNumber']
        number_txns = len(value['events'])
        for block in value['blockDetails']['block']['extrinsics'][1:]:
            # # Usando el método get para evitar KeyError
            gas_limit = block['method']['args'].get('gas_limit')
            if gas_limit:
                # Eliminar las comas y convertir a entero
                gas_limit = int(gas_limit.replace(',', ''))
                data_fee.append(gas_limit)
        # Calcular el promedio si hay datos disponibles
        if data_fee:
            avg_gas_limit = sum(data_fee) / len(data_fee)
        else:
            avg_gas_limit = 0

        values_blocks.append({ 'number_block': number_block,'number_txns': number_txns, 'fees_avg': avg_gas_limit})
    return values_blocks
    

def plots_vara():
    db_manager = VaraDBManager()
    getvalues = db_manager.get_blockDetails_events()
    
    get_fees_prom = get_fees_avg(getvalues)
    get_count_tnx = get_count_tnx_events(getvalues)

    get_fees_prom.sort(key=lambda x: x['time'])
    get_count_tnx.sort(key=lambda x: x['time'])

    plot = create_plot_metrics_vara(get_count_tnx)
    plot2 = create_plot_metrics_vara(get_fees_prom)

    context={
        'plot': plot,
        'plot2': plot2
    }


    return context

