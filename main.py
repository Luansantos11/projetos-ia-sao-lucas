# previsao_demanda.py

def prever_demanda(vendas_passadas):
    media = sum(vendas_passadas) / len(vendas_passadas)
    return media

def main():
    vendas = [100, 150, 120, 130, 160]  # Vendas nos últimos 5 dias
    demanda_prevista = prever_demanda(vendas)
    print(f"Demanda prevista para o próximo dia: {demanda_prevista:.2f}")

if __name__ == "__main__":
    main()
