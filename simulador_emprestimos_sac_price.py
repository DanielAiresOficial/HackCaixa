from flask import Flask, request, jsonify
import json

app = Flask(__name__)

def calculate_price(principal, rate, periods):
    rate = rate / 100 / 12
    payment = principal * rate / (1 - (1 + rate) ** -periods)
    schedule = []

    for period in range(1, periods + 1):
        interest = principal * rate
        amortization = payment - interest
        principal -= amortization
        schedule.append({
            'period': period,
            'payment': round(payment, 2),
            'interest': round(interest, 2),
            'amortization': round(amortization, 2),
            'balance': round(principal, 2)
        })

    return schedule

def calculate_sac(principal, rate, periods):
    rate = rate / 100 / 12
    amortization = principal / periods
    schedule = []

    for period in range(1, periods + 1):
        interest = principal * rate
        payment = amortization + interest
        principal -= amortization
        schedule.append({
            'period': period,
            'payment': round(payment, 2),
            'interest': round(interest, 2),
            'amortization': round(amortization, 2),
            'balance': round(principal, 2)
        })

    return schedule

def calculate_amortization(principal, periods, terms, amortization_type):
    rate = terms['taxa']
    modality = terms['modalidade'].lower()

    if amortization_type.lower() == 'price':
        return calculate_price(principal, rate, periods)
    elif amortization_type.lower() == 'sac':
        return calculate_sac(principal, rate, periods)
    else:
        return {'error': 'Invalid amortization type. Use "price" or "sac".'}

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    principal = data['valor_solicitado']
    periods = data['periodo']
    terms = data['modalidade']
    amortization_type = data['tipo_amortizacao']
    
    schedule = calculate_amortization(principal, periods, terms, amortization_type)
    return jsonify(schedule)

if __name__ == '__main__':
    import sys

    modalities = {
        "emprestimo": {"modalidade": "emprestimo", "taxa": 5},
        "consignado": {"modalidade": "consignado", "taxa": 2},
        "financiamento": {"modalidade": "financiamento", "taxa": 1}
    }

    # Solicitar entradas ao usuário
    principal = float(input("Qual o valor do empréstimo que deseja? "))
    periods = int(input("Qual o prazo que deseja para pagar? (Max 60x) "))
    
    if periods > 60:
        print("O prazo máximo é de 60 meses.")
        sys.exit(1)

    print("Modalidades disponíveis:")
    for key in modalities.keys():
        print(key)

    modality_key = input("Qual modalidade deseja? ")

    if modality_key not in modalities:
        print("Modalidade inválida.")
        sys.exit(1)
    
    amortization_type = input("Sistema de amortização preferido (price/sac): ").lower()

    if amortization_type not in ["price", "sac"]:
        print("Sistema de amortização inválido.")
        sys.exit(1)

    terms = modalities[modality_key]

    # Calcular e exibir a tabela de amortização
    result = calculate_amortization(principal, periods, terms, amortization_type)
    print(json.dumps(result, indent=4))

    # Executar a API Flask
    app.run(debug=True)
