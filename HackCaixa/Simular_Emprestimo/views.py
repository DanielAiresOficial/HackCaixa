from django.shortcuts import render
from azure.eventhub import EventHubProducerClient, EventData
from .models import Produto
import json
from django.http import JsonResponse

def envie_eventhub(request):
    # Verificação de Requisicao POST
    if request.method == 'POST':
        # Obter request
        mensagem = request.POST.get('mensagem')

        # Definição da conexão
        conn_str = "Endpoint=sb://eventhack.servicebus.windows.net/;SharedAccessKeyName=hack;SharedAccessKey=HeHeVaVqyVkntO2FnjQcs2Ilh/4MUDo4y+AEhKp8z+g=;EntityPath=simulacoes"

        # Instanciação do cliente EventHubProducerClient
        producer = EventHubProducerClient.from_connection_string(conn_str)

        # lote de eventos
        batch = producer.create_batch()

        # Add mensagem ao lote de eventos
        batch.add(EventData(mensagem))

        # Envie o lote de eventos para o Event Hub
        producer.send_batch(batch)

        # Feche a conexão com o Event Hub
        producer.close()

        # Renderize a resposta para o usuário
        return render(request, 'enviar_mensagem.html', {'mensagem_enviada': True})

    # Se não for uma requisição POST, renderize o formulário de envio de mensagem
    return render(request, 'enviar_mensagem.html')

def calcular_tabela_price(valor, prazo, taxa_juros):
    PMT = (valor * taxa_juros) / (1 - (1 + taxa_juros) ** -prazo)
    tabela_price = []
    saldo_devedor = valor
    for i in range(prazo):
        juros = saldo_devedor * taxa_juros
        amortizacao = PMT - juros
        saldo_devedor -= amortizacao
        tabela_price.append((PMT, juros, amortizacao, saldo_devedor))
    return tabela_price

def calcular_tabela_sac(valor, prazo, taxa_juros):
    saldo_devedor = valor
    amortizacao = valor / prazo
    tabela_sac = []
    for i in range(prazo):
        juros = saldo_devedor * taxa_juros
        parcela = amortizacao + juros
        saldo_devedor -= amortizacao
        tabela_sac.append((amortizacao, saldo_devedor, juros, parcela))
    return tabela_sac

def simular_emprestimo(request):
    if request.method == 'POST':
        valor = request.POST['valor']
        prazo = request.POST['prazo']
        
        # Consultar o banco de dados para encontrar o produto com a menor taxa de juros
        produto = Produto.objects.filter(VR_MINIMO__lt=valor, VR_MAXIMO__gt=valor).order_by('PC_TAXA_JUROS').first()

        if produto:
            # Calcular a tabela Price
            tabela_price = calcular_tabela_price(valor, prazo, produto.PC_TAXA_JUROS)
    
            # Calcular a tabela SAC
            tabela_sac = calcular_tabela_sac(valor, prazo, produto.PC_TAXA_JUROS)
    
              # Criar o dicionário de contexto com os dados do resultado
            context = {
                'produto': produto,
                'valor': valor,
                'prazo': prazo,
                'tabela_price': tabela_price,
                'tabela_sac': tabela_sac
            }
    
            # Renderizar o template de resultado com o contexto
            return render(request, 'Simular_Emprestimo/resultado.html', context=context)
    return render(request, 'Simular_Emprestimo/index.html')
def index(request):
    return render(request, 'Simular_Emprestimo/index.html')
