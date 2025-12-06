import random
from faker import Faker
import datetime
import string
import names

def gerarNomes(numero):
    lista = []
    for i in range(numero):
        lista.append(names.get_first_name())
        
    return lista


def gerarBI(qtd):
    lista_bi = []
    for _ in range(qtd):
        # 9 dígitos
        numeros = str(random.randint(100000000, 999999999))
        # 2 letras maiúsculas
        letras = chr(random.randint(65, 90)) + chr(random.randint(65, 90))
        lista_bi.append(numeros + letras)
    return lista_bi



def gerar_telefones(qtd):
    return [
        f"+244 {random.randint(900, 999)} {random.randint(100, 999)} {random.randint(100, 999)}"
        for _ in range(qtd)
    ]
    
   

def data_aleatoria(qtd):
    inicio = datetime.date(2000, 1, 1)
    fim = datetime.date(2025, 12, 31)
    delta = (fim - inicio).days
    
    # gera várias datas diferentes
    lista_datas = [
        inicio + datetime.timedelta(days=random.randint(0, delta))
        for _ in range(qtd)
    ]
    return lista_datas


def data_nascimento1(qtd):
    inicio = datetime.date(2000, 1, 1)
    fim = datetime.date(2010, 12, 31)
    # diferença em dias entre as duas datas
    delta = (fim - inicio).days
    
    # gera número aleatório de dias
    dias_aleatorios = random.randint(0, delta)
    
    # soma ao início
    return inicio + datetime.timedelta(days=dias_aleatorios)


def gerar_emails(nomes, dominios=None):
    
    if dominios is None:
        dominios = ["gmail.com", "yahoo.com", "outlook.com", "empresa.com"]
    
    emails = []
    for nome in nomes:
        nome_base = nome.lower().replace(" ", ".")  # padroniza
        
        numero = random.randint(1, 9999)  # sufixo aleatório
        dominio = random.choice(dominios)
        email = f"{nome_base}{numero}@{dominio}"
        emails.append(email)
    
    return emails


def lista_generos_random(x: int) -> list:
    return [random.choice(["masculino", "feminino"]) for _ in range(x)]



def gerar_idade_experiencia(qtd: int, idade_min=21, idade_max=65, exp_min=0, exp_max=40):
    """
    Gera duas listas: uma de idades e outra de experiências.
    
    Parâmetros:
        qtd (int): número de elementos em cada lista
        idade_min (int): idade mínima
        idade_max (int): idade máxima
        exp_min (int): experiência mínima (anos)
        exp_max (int): experiência máxima (anos)
    
    Retorno:
        tuple: (lista_idades, lista_experiencias)
    """
    lista_idades = [random.randint(idade_min, idade_max) for _ in range(qtd)]
    lista_experiencias = [random.randint(exp_min, exp_max) for _ in range(qtd)]
    
    return lista_idades, lista_experiencias


"""
idades, experiencias = gerar_idade_experiencia(10)
print("Idades:", idades)
print("Experiências:", experiencias)
"""


def gerar_matricula_unica(qtd: int):
    matrículas = set()
    letras = string.ascii_uppercase
    numeros = string.digits
    
    while len(matrículas) < qtd:
        parte1 = ''.join(random.choice(letras) for _ in range(2))
        parte2 = ''.join(random.choice(numeros) for _ in range(4))
        parte3 = ''.join(random.choice(letras) for _ in range(2))
        matrículas.add(f"{parte1}-{parte2}-{parte3}")
    
    return list(matrículas)




def listas_veiculos_lugares(qtd: int):
    # Definição dos intervalos possíveis por categoria
    ranges = { 
        "motociclo": (1, 2),
        "ciclomotor": (1, 2),
        "ligeiro": (1, 9),
        "pesado_mercadorias": (1, 3),
        "pesado_passageiros": (1, 100),
        "minibus": (1, 16),
        "quadriciclo": (1, 2)
    }
    
    lista_categorias = []
    lista_lugares = []
    
    for _ in range(qtd):
        categoria = random.choice(list(ranges.keys()))
        lista_categorias.append(categoria)
        
        # gera um valor diferente a cada vez
        min_val, max_val = ranges[categoria]
        lugar = random.randint(min_val, max_val)
        lista_lugares.append(lugar)
    
    return lista_categorias, lista_lugares

"""# Exemplo de uso
cats, lugares = listas_veiculos_lugares(10)
print(cats)
print(lugares)
"""


def gerar_saldos(qtd: int):
    """
    Gera uma lista de saldos bancários aleatórios.
    Cada saldo tem no máximo 15 algarismos (parte inteira + decimais),
    com 2 casas decimais fixas.
    """
    lista_saldos = []
    
    for _ in range(qtd):
        # Gera número aleatório até 10^13 (13 dígitos inteiros) + 2 decimais = 15 algarismos
        saldo = random.uniform(0, 2**13)
        
        # Formata com 2 casas decimais
        saldo_formatado = round(saldo, 2)
        
        lista_saldos.append(saldo_formatado)
        
    return lista_saldos

def gerar_localizacao_africa():
    # Latitude da África: -35 a 37
    latitude = random.uniform(-35, 37)
    # Longitude da África: -17 a 51
    longitude = random.uniform(-17, 51)
    
    # Retorna no formato MySQL POINT
    return f"POINT({longitude}, {latitude})"





    
