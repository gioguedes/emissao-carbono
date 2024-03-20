from enum import Enum

# Enumerado para os tipos de atividades que podem gerar emissões de carbono
class TipoAtividade(Enum):
    VIAGEM_CARRO = "viagem de carro"
    VIAGEM_AVIAO = "viagem de avião"
    CONSUMO_ENERGIA = "consumo de energia"

# Enumerado para os tipos de combustíveis que podem ser usados nas atividades
class TipoCombustivel(Enum):
    GASOLINA = "gasolina"
    ETANOL = "etanol"
    DIESEL = "diesel"
    ELETRICO = "elétrico"

# Dicionário que mapeia cada tipo de atividade e combustível para a quantidade de carbono que emite
EMISSORES_DE_CARBONO = {
    TipoAtividade.VIAGEM_CARRO: {
        TipoCombustivel.GASOLINA: 0.15,
        TipoCombustivel.ETANOL: 0.07,
        TipoCombustivel.DIESEL: 0.20,
        TipoCombustivel.ELETRICO: 0.0007,
    },
    TipoAtividade.VIAGEM_AVIAO: 0.20,
    TipoAtividade.CONSUMO_ENERGIA: 0.0007,
}

# Função para calcular as emissões de carbono com base no tipo de atividade, tipo de combustível, quantidade de energia, distância e número de passageiros
def calcular_emissoes_de_carbono(tipo_atividade: TipoAtividade, tipo_combustivel: TipoCombustivel,
                                 quantidade_energia: float, distancia: float, numero_passageiros: int) -> float:
    if tipo_atividade == TipoAtividade.VIAGEM_CARRO:
        emissoes_por_unidade_energia = EMISSORES_DE_CARBONO[tipo_atividade][tipo_combustivel]
    else:
        emissoes_por_unidade_energia = EMISSORES_DE_CARBONO[tipo_atividade]
    return emissoes_por_unidade_energia * quantidade_energia * distancia / 1000 / numero_passageiros

# Função para calcular a quantidade de créditos de carbono necessários para compensar as emissões de carbono
def calcular_quantidade_de_creditos_de_carbono(emissões_de_carbono: float) -> float:
    CARBONO_COMPENSADO_POR_CREDITO = 0.25
    return emissões_de_carbono / CARBONO_COMPENSADO_POR_CREDITO

# Função para calcular o lucro potencial com a venda de créditos de carbono excedentes
def calcular_lucro_potencial(quantidade_de_creditos_de_carbono: float, preco_do_credito: float) -> float:
    return quantidade_de_creditos_de_carbono * preco_do_credito

# Função principal que executa o programa
def main():
    while True:
        # Solicitando ao usuário o tipo de atividade
        tipo_atividade_str = input("Qual tipo de atividade está gerando as emissões de carbono? (viagem de carro, viagem de avião, consumo de energia): ")
        try:
            tipo_atividade = TipoAtividade(tipo_atividade_str.lower())
        except ValueError:
            print("Tipo de atividade inválido.")
            continue

        # Solicitando ao usuário o tipo de combustível utilizado
        tipo_combustivel_str = input("Qual tipo de combustivel foi utilizado? (gasolina, etanol, diesel, elétrico): ")
        try:
            tipo_combustivel = TipoCombustivel(tipo_combustivel_str.lower())
        except ValueError:
            print("Tipo de combustivel inválido.")
            continue

        # Solicitando ao usuário a quantidade de energia consumida, a distância percorrida e o número de passageiros
        quantidade_energia = float(input("Quanta energia foi consumida (kWh): "))
        distancia = float(input("Qual foi a distância percorrida (km): "))
        numero_passageiros = int(input("Quantos passageiros estavam presentes? "))

        # Verificando se o número de passageiros é válido
        if numero_passageiros < 1:
            print("Número de passageiros inválido.")
            return

        # Calculando as emissões de carbono, a quantidade de créditos de carbono e o lucro potencial
        emissões_de_carbono = calcular_emissoes_de_carbono(tipo_atividade, tipo_combustivel,
                                                           quantidade_energia, distancia, numero_passageiros)
        quantidade_de_creditos_de_carbono = calcular_quantidade_de_creditos_de_carbono(emissões_de_carbono)
        preco_do_credito = float(input("Qual é o preço do crédito de carbono?: "))
        lucro_potencial = calcular_lucro_potencial(quantidade_de_creditos_de_carbono, preco_do_credito)

        # Exibindo os resultados
        print(f"Emissões de carbono: {emissões_de_carbono:.2f} toneladas")
        print(f"Quantidade de créditos de carbono necessários: {quantidade_de_creditos_de_carbono:.2f}")
        print(f"Lucro potencial com a venda de excedentes de créditos: R${lucro_potencial:.2f}")

        # Perguntando ao usuário se ele deseja calcular novamente
        resposta = input("Deseja calcular novamente? (s/n): ")
        if resposta.lower() != "s":
            break

if __name__ == "__main__":
    main()
