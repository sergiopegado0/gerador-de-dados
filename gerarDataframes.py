import funcoes
import pandas as pd
import random

from faker import Faker

faker = Faker("pt_PT")

def gerarCliente(numero):
    generos = ["M", "F"]
    
    id = list(range(1,numero+1))
    nomes = funcoes.gerarNomes(numero)
    data = funcoes.data_aleatoria(numero)
    numeros_telefone = funcoes.gerar_telefones(numero)
    email =funcoes.gerar_emails(nomes)
    genero = random.choices(generos,k=numero)
    
    df = pd.DataFrame({
        "id_cliente":id,
        "nome": nomes,
        "telefone": numeros_telefone,        
        "email": email,
        "data_nascimento": data,
        "genero": genero
        
    })
    
    return df


"""----------------------------------A PARTE DO BANCO------------------------"""


def gerarAgencias(numero):
    id = list(range(1,numero+1))
    nomes = [faker.company() for _ in range(numero)]
    localizacao = [funcoes.gerar_localizacao_africa() for _ in range(numero)]
    
    df = pd.DataFrame({
        "id_cliente":id,
        "nome": nomes,
        "localizacao": localizacao,
        
    })
    
    return df



def gerarContas(numero):
    df = pd.DataFrame({    
        "id_conta": list(range(1,numero+1)),
        "id_cliente": [random.randint(1, numero) for _ in range(numero)],
        "id_agencia": [random.randint(1, numero) for _ in range(numero)],
        "saldo": [round(random.uniform(0, 50000), 2) for _ in range(numero)],
        "tipo_conta": [random.choice(["Corrente", "Poupança"]) for _ in range(numero)],       
        "numero_conta": [(faker.unique.random_int(500000, 99999999999)) for _ in range(numero)],
    })
    
    return df

def gerarTransacoes(numero):
    tipos_transacoes = [
    "Depósito",
    "Levantamento",
    "Transferência",
    "Pagamento",
    "Recebimento",
    "Empréstimo",
    "Juros",
    "Multa",
    "Estorno",
    "Compra",
    "Venda",
    "Investimento",
    "Dividendos",
    "Câmbio"
]
    
    df = pd.DataFrame({
        "id_transacao": list(range(1,numero+1)),
        "id_conta": [random.randint(1, numero) for _ in range(numero)],
        "data": funcoes.data_aleatoria(numero),
        "tipo": random.choices(tipos_transacoes,k=numero),
        "valor": [round(random.uniform(0, 50000), 2) for _ in range(numero)],
    })
    
    return df



"""-----------------------------PARTE DA EDUCAÇÃO------------------------------"""

def gerarInstrutor(numero):
    especialidades_professores = [
    "Matemática",
    "Física",
    "Química",
    "Estatística",
    "Computação",
    "Engenharia",
    "História",
    "Geografia",
    "Filosofia",
    "Sociologia",
    "Psicologia",
    "Antropologia",
    "Biologia",
    "Educação Física",
    "Medicina",
    "Enfermagem",
    "Farmácia",
    "Nutrição",
    "Português",
    "Literatura",
    "Línguas Estrangeiras",
    "Artes Visuais",
    "Música",
    "Teatro",
    "Direito",
    "Administração",
    "Economia",
    "Contabilidade",
    "Comunicação Social",
    "Pedagogia",
    "Informática",
    "Robótica",
    "Inteligência Artificial",
    "Ciência de Dados",
    "Design",
    "Arquitectura",
    "Banco de Dados",
    "Compiladores",
    "Economia"
]

    
    df = pd.DataFrame({
        "id_instrutor": list(range(1,numero+1)),
        "nome": funcoes.gerarNomes(numero),
        "especialidade": random.choices(especialidades_professores,k=numero),
    })
    
    return df

def gerarCurso(numero):
    
    
    df = pd.DataFrame({
        "id_curso": list(range(1,numero+1)),
        "nome_curso": [faker.word().capitalize() for _ in range(numero)],
        "duracao": [random.randint(20, 200) for _ in range(numero)],
        "preco": [round(random.uniform(0, 50000), 2) for _ in range(numero)],
        "id_instrutor": [random.randint(1, numero) for _ in range(numero)],
    })
    
    return df

def gerarInscricao(numero):
    
    df = pd.DataFrame({
        "id_inscricao": list(range(1,numero+1)),
        "id_cliente": [random.randint(1, numero) for _ in range(numero)],
        "id_curso": [random.randint(1, numero) for _ in range(numero)],
        "data": funcoes.data_aleatoria(numero),
    })
    
    return df

"""PARTE DA LOGÍSTICA"""

def gerarMotorista(numero):
    idade, experiencia = funcoes.gerar_idade_experiencia(numero)
    df = pd.DataFrame({
        "id_motorista": list(range(1,numero+1)),
        "nome": funcoes.gerarNomes(numero),
        "idade": idade,
        "experiencia": experiencia,
        "eficiencia": [round(random.uniform(0.1, 1.0), 2) for _ in range(numero)]
    })
    
    return df 

def gerarVeiculo(numero):
    tipo, capacidade = funcoes.listas_veiculos_lugares(numero)
    
    df = pd.DataFrame({
        "id_veiculo": list(range(1,numero+1)),
        "tipo": tipo,
        "capacidade": capacidade,
        "ano_fabricacao": funcoes.data_aleatoria(numero),
        "matricula": funcoes.gerar_matricula_unica(numero),
    })
    
    return df

def gerarEntrega(numero):
    
    df = pd.DataFrame({
        "id_entrega": list(range(1,numero+1)),
        "id_veiculo": [random.randint(1, numero) for _ in range(numero)],
        "id_motorista": [random.randint(1, numero) for _ in range(numero)],
        "tempo_previsto": [random.randint(30, 300) for _ in range(numero)],
        "tempo_real": [random.randint(30, 400) for _ in range(numero)]
    })
    
    return df

def gerarRastreio(numero):
    
    df = pd.DataFrame({
        "id_rastreio": list(range(1,numero+1)),
        "id_entrega":  [random.randint(1, numero) for _ in range(numero)],
        "status": [random.choice(["Concluída", "Pendente"]) for _ in range(numero)],
        "data_status": funcoes.data_aleatoria(numero)
    })
    return df

"""PARTE DO RETALHO"""

def gerarLoja(numero):
    
    df = pd.DataFrame({
        "id_loja": list(range(1,numero+1)),
        "nome_loja": [faker.company() for _ in range(numero)],
        "localizacao": [funcoes.gerar_localizacao_africa() for _ in range(numero)]
    })
    return df

def gerarProduto(numero):
    df = pd.DataFrame({
        "id_produto": list(range(1,numero+1)),
        "nome_produto": [faker.word() for _ in range(numero)],
        "categoria": [random.choice(["Alimentos", "Bebidas", "Higiene", "Limpeza"]) for _ in range(numero)],
        "preco_unitario": [round(random.uniform(1, 100000), 2) for _ in range(numero)],
        "margem_bruta": [round(random.uniform(0.1, 0.5), 2) for _ in range(numero)]
    })
    return df

def gerarVendas(numero):
    
    df = pd.DataFrame({
        "id_venda": list(range(1,numero+1)),
        "id_produto": [random.randint(1, numero) for _ in range(numero)],
        "id_cliente": [random.randint(1, numero) for _ in range(numero)],
        "quantidade": [random.randint(1, 1000000) for _ in range(numero)],
        "id_loja": [random.randint(1, numero) for _ in range(numero)],
        "valor_total": [round(random.uniform(5, 100000000), 2) for _ in range(numero)],
        "data_venda": funcoes.data_aleatoria(numero),
    })
    return df

"""PARTE DA SAUDE"""
def gerarClinica(numero):
    df = pd.DataFrame({
        "id_clinica": list(range(1,numero+1)),
        "nome": [faker.company() for _ in range(numero)],
        "localizacao": [funcoes.gerar_localizacao_africa() for _ in range(numero)],
    })
    return df

def gerarMedico(numero):
    especialidade = ["Alergia e Imunologia",
    "Anestesiologia",
    "Angiologia",
    "Cancerologia (Oncologia)",
    "Cardiologia",
    "Cirurgia Cardiovascular",
    "Cirurgia da Mão",
    "Cirurgia de Cabeça e Pescoço",
    "Cirurgia do Aparelho Digestivo",
    "Cirurgia Geral",
    "Cirurgia Pediátrica",
    "Cirurgia Plástica",
    "Cirurgia Torácica",
    "Cirurgia Vascular",
    "Clínica Médica",
    "Coloproctologia",
    "Dermatologia",
    "Endocrinologia e Metabologia",
    "Gastroenterologia",
    "Genética Médica",
    "Geriatria",
    "Ginecologia e Obstetrícia",
    "Hematologia e Hemoterapia",
    "Infectologia",
    "Medicina de Família e Comunidade",
    "Medicina de Emergência",
    "Medicina de Tráfego",
    "Medicina do Trabalho",
    "Medicina Esportiva",
    "Medicina Física e Reabilitação",
    "Medicina Intensiva",
    "Medicina Legal e Perícia Médica",
    "Medicina Nuclear",
    "Medicina Preventiva e Social",
    "Nefrologia",
    "Neurocirurgia",
    "Neurologia",
    "Nutrologia",
    "Oftalmologia",
    "Ortopedia e Traumatologia",
    "Otorrinolaringologia",
    "Patologia",
    "Patologia Clínica/Medicina Laboratorial",
    "Pediatria",
    "Pneumologia",
    "Psiquiatria",
    "Radiologia e Diagnóstico por Imagem",
    "Radioterapia",
    "Reumatologia",
    "Urologia"] 
    nomes = funcoes.gerarNomes(numero)
    email = funcoes.gerar_emails(nomes)
    
    df = pd.DataFrame({
        "id_medico": list(range(1,numero+1)),
        "nome": nomes,
        "especialidade": random.choices(especialidade,k=numero),
        "telefone": funcoes.gerar_telefones(numero),
        "email": email
    })
    return df

def gerarConsulta(numero):
    
    df = pd.DataFrame({
        "id_consulta": list(range(1,numero+1)),
        "id_cliente": [random.randint(1, numero) for _ in range(numero)],
        "id_medico": [random.randint(1, numero) for _ in range(numero)],
        "id_clinica": [random.randint(1, numero) for _ in range(numero)],
        "data_agendamento": funcoes.data_aleatoria(numero),
        "data_atendimento": funcoes.data_aleatoria(numero),
    })
    return df

def gerarExame(numero):
    
    df = pd.DataFrame({
        "id_exame": list(range(1,numero+1)),
        "id_cliente": [random.randint(1, numero) for _ in range(numero)],
        "id_medico": [random.randint(1, numero) for _ in range(numero)],
        "resultado": [random.choice(["Normal", "Alterado"]) for _ in range(numero)],
        "custo": [round(random.uniform(5, 100000000), 2) for _ in range(numero)],
        "id_clinica": [random.randint(1, numero) for _ in range(numero)],
    })
    return df

"""------------------------------------PARTE DA TELECOM-------------------------------"""
def gerarPlano(numero):
    # Lista de nomes de planos de telefonia
    planos_nomes = [
    "Alçada Start",
    "Alçada Plus",
    "Alçada Família",
    "Alçada Premium",
    "Alçada Ilimitado",
    "Alçada Jovem",
    "Alçada Empresarial"
]

# Lista de tipos de planos de telefonia
    tipos_planos = [
    "Pré-pago",
    "Pós-pago",
    "Controle",
    "Familiar",
    "Empresarial",
    "Ilimitado",
    "Internet móvel"
]
    
    
    df = pd.DataFrame({
        "id_plano": list(range(1,numero+1)),
        "nome_plano": random.choices(planos_nomes,k=numero),
        "tipo": random.choices(tipos_planos,k=numero),
        "mensalidade": [round(random.uniform(100, 20000), 2) for _ in range(numero)]
    })
    return df

def gerarAssinatura(numero):
    df = pd.DataFrame({
        "id_assinatura": list(range(1,numero+1)),
        "id_cliente": [random.randint(1, numero) for _ in range(numero)],
        "id_plano": [random.randint(1, numero) for _ in range(numero)],
        "data_inicio": funcoes.data_aleatoria(numero),
        "data_fim": funcoes.data_aleatoria(numero),
        "status": [random.choice(["Ativo", "Cancelado"]) for _ in range(numero)]
    })
    return df

def gerarConsumoInternet(numero):
    df = pd.DataFrame({
        "id_consumo": list(range(1,numero+1)),
        "id_assinatura": [random.randint(1, numero) for _ in range(numero)],
        "mes": [random.randint(1, 12) for _ in range(numero)],
        "dados_consumidos": [round(random.uniform(100, 2000000), 2) for _ in range(numero)]
    })
    return df

def gerarChamada(numero):
    df = pd.DataFrame({
        "id_chamada": list(range(1,numero+1)),
        "id_assinatura": [random.randint(1, numero) for _ in range(numero)],
        "data_chamada": funcoes.data_aleatoria(numero),
        "duracao":[random.randint(1, 240) for _ in range(numero)], 
        "dados_consumidos": [round(random.uniform(100, 2000000), 2) for _ in range(numero)]
    })
    return df


    