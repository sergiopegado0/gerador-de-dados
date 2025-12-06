import pandas as pd

def criartabelaClienteSQL(df: pd.DataFrame, tabela: str) -> str:
    sql_create = f"""
CREATE TABLE {tabela} (
    id_cliente INT PRIMARY KEY,
    nome VARCHAR(100),
    email VARCHAR(100),
    telefone VARCHAR(20),
    data_nascimento DATE,
    genero VARCHAR(10)
);
    """

        # 2. Gerar os INSERTs a partir do DataFrame
    linhas = []
    for _, row in df.iterrows():
            valores = f"({row['id_cliente']}, '{row['nome']}', '{row['email']}', '{row['telefone']}, '{row['data_nascimento']}, '{row['genero']}')"
            linhas.append(valores)

    sql_insert = f"INSERT INTO {tabela} (id_cliente, nome, email, data_nascimento, genero)\nVALUES\n" + ",\n".join(linhas) + ";"

    # 3. Combinar CREATE + INSERT em um único script
    sql_script = sql_create + "\n" + sql_insert

    return sql_script


def criarAgenciaSQL(df: pd.DataFrame, tabela: str) -> str:
    sql_create = f"""
CREATE TABLE {tabela} (
    id_cliente INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100),
    localizacao POINT NOT NULL,   -- coluna espacial
    SPATIAL INDEX(localizacao)
);
    """

        # 2. Gerar os INSERTs
    linhas = []
    for _, row in df.iterrows():
        valores = (
            f"({row['id_cliente']}, '{row['nome']}',  {row['localizacao']})"
            )
        linhas.append(valores)

    sql_insert = (
        f"INSERT INTO {tabela} (id_cliente, nome, localizacao)\nVALUES\n"
        + ",\n".join(linhas)
        + ";"
    )

    # 3. Combinar CREATE + INSERT
    return sql_create + "\n" + sql_insert
        


def criarContasSQL(df: pd.DataFrame, tabela: str) -> str:
    sql_create = f"""
CREATE TABLE {tabela} (
    id_conta INT PRIMARY KEY AUTO_INCREMENT,
    id_cliente INT NOT NULL,
    id_agencia INT NOT NULL,
    saldo DECIMAL(12,2),
    tipo_conta VARCHAR(50),
    numero_conta VARCHAR(30)
);
    """

        # 2. Gerar os INSERTs a partir do DataFrame
    linhas = []
    for _, row in df.iterrows():
            valores = f"({row['id_conta']}, '{row['id_cliente']}', '{row['id_agencia']}, '{row['saldo']}, '{row['numero_conta']})"
            linhas.append(valores)

    sql_insert = f"INSERT INTO {tabela} (id_conta, id_cliente, id_agencia, saldo, numero_conta)\nVALUES\n" + ",\n".join(linhas) + ";"

    # 3. Combinar CREATE + INSERT em um único script
    sql_script = sql_create + "\n" + sql_insert

    return sql_script

def criarTransacoesSQL(df: pd.DataFrame, tabela: str) -> str:
    sql_create = f"""
CREATE TABLE {tabela} (
    id_transacao INT PRIMARY KEY AUTO_INCREMENT,
    id_conta INT NOT NULL,
    data DATE,
    tipo VARCHAR(30),
    valor DECIMAL(12,2)
);
    """

        # 2. Gerar os INSERTs a partir do DataFrame
    linhas = []
    for _, row in df.iterrows():
            valores = f"({row['id_transacao']}, '{row['id_conta']}', '{row['data']}, '{row['tipo']}, '{row['valor']})"
            linhas.append(valores)

    sql_insert = f"INSERT INTO {tabela} (id_transacao, id_conta, data, tipo, valor)\nVALUES\n" + ",\n".join(linhas) + ";"

    # 3. Combinar CREATE + INSERT em um único script
    sql_script = sql_create + "\n" + sql_insert

    return sql_script


"""-----------------------------PARTE DA EDUCAÇÃO------------------------------"""


def criarInscricoesSQL(df: pd.DataFrame, tabela: str) -> str:
    sql_create = f"""
CREATE TABLE {tabela} (
    id_inscricao INT PRIMARY KEY AUTO_INCREMENT,
    id_cliente INT NOT NULL,
    id_curso INT NOT NULL,
    data DATE
    
);
    """

        # 2. Gerar os INSERTs a partir do DataFrame
    linhas = []
    for _, row in df.iterrows():
            valores = f"({row['id_inscricao']}, '{row['id_cliente']}', '{row['id_curso']}, '{row['data']})"
            linhas.append(valores)

    sql_insert = f"INSERT INTO {tabela} (id_inscricao, id_cliente, id_curso, data)\nVALUES\n" + ",\n".join(linhas) + ";"

    # 3. Combinar CREATE + INSERT em um único script
    sql_script = sql_create + "\n" + sql_insert

    return sql_script


def criarInstrutoresSQL(df: pd.DataFrame, tabela: str) -> str:
    sql_create = f"""
CREATE TABLE {tabela} (
    id_instrutor INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100),
    especialidade VARCHAR(50)
    
);
    """

        # 2. Gerar os INSERTs a partir do DataFrame
    linhas = []
    for _, row in df.iterrows():
            valores = f"({row['id_instrutor']}, '{row['nome']}', '{row['especialidade']})"
            linhas.append(valores)

    sql_insert = f"INSERT INTO {tabela} (id_instrutor, nome, especialidade)\nVALUES\n" + ",\n".join(linhas) + ";"

    # 3. Combinar CREATE + INSERT em um único script
    sql_script = sql_create + "\n" + sql_insert

    return sql_script


def criarCursosSQL(df: pd.DataFrame, tabela: str) -> str:
    sql_create = f"""
CREATE TABLE {tabela} (
    id_curso INT PRIMARY KEY AUTO_INCREMENT,
    nome_curso VARCHAR(100),
    duracao INT,
    preco DECIMAL(10,2),
    id_instrutor INT
    
);
    """

        # 2. Gerar os INSERTs a partir do DataFrame
    linhas = []
    for _, row in df.iterrows():
            valores = f"({row['id_curso']}, '{row['nome_curso']}', '{row['duracao']}, '{row['preco']}, '{row['id_instrutor']})"
            linhas.append(valores)

    sql_insert = f"INSERT INTO {tabela} (id_curso, nome_curso, duracao, preco, id_instrutor)\nVALUES\n" + ",\n".join(linhas) + ";"

    # 3. Combinar CREATE + INSERT em um único script
    sql_script = sql_create + "\n" + sql_insert

    return sql_script


"""----------------------------- PARTE DA LOGISTICA ------------------------"""

def criarEntregasSQL(df: pd.DataFrame, tabela: str) -> str:
    sql_create = f"""
CREATE TABLE {tabela} (
    id_entrega INT PRIMARY KEY AUTO_INCREMENT,
    id_veiculo INT NOT NULL,
    id_motorista INT NOT NULL,
    tempo_previsto INT,
    tempo_real INT
    
);
    """

        # 2. Gerar os INSERTs a partir do DataFrame
    linhas = []
    for _, row in df.iterrows():
            valores = f"({row['id_entrega']}, '{row['id_veiculo']}', '{row['id_motorista']}, '{row['tempo_previsto']}, '{row['tempo_real']})"
            linhas.append(valores)

    sql_insert = f"INSERT INTO {tabela} (id_entrega, id_veiculo, id_motorista, tempo_previsto, tempo_real)\nVALUES\n" + ",\n".join(linhas) + ";"

    # 3. Combinar CREATE + INSERT em um único script
    sql_script = sql_create + "\n" + sql_insert

    return sql_script


def criarRastreioSQL(df: pd.DataFrame, tabela: str) -> str:
    sql_create = f"""
CREATE TABLE {tabela} (
    id_rastreio INT PRIMARY KEY AUTO_INCREMENT,
    id_entrega INT NOT NULL,
    status VARCHAR(20) NOT NULL,
    data_status DATE
    
);
    """

        # 2. Gerar os INSERTs a partir do DataFrame
    linhas = []
    for _, row in df.iterrows():
            valores = f"({row['id_rastreio']}, '{row['id_entrega']}', '{row['status']}, '{row['data_status']})"
            linhas.append(valores)

    sql_insert = f"INSERT INTO {tabela} (id_rastreio, id_entrega, status, data_status)\nVALUES\n" + ",\n".join(linhas) + ";"

    # 3. Combinar CREATE + INSERT em um único script
    sql_script = sql_create + "\n" + sql_insert

    return sql_script


def criarVeiculosSQL(df: pd.DataFrame, tabela: str) -> str:
    sql_create = f"""
CREATE TABLE {tabela} (
    id_veiculo INT PRIMARY KEY AUTO_INCREMENT,
    tipo VARCHAR(20) NOT NULL,
    capacidade INT NOT NULL,
    ano_fabricacao DATE,
    matricula VARCHAR(20)
    
);
    """

        # 2. Gerar os INSERTs a partir do DataFrame
    linhas = []
    for _, row in df.iterrows():
            valores = f"({row['id_veiculo']}, '{row['tipo']}', '{row['capacidade']}, '{row['ano_fabricacao']}, '{row['matricula']})"
            linhas.append(valores)

    sql_insert = f"INSERT INTO {tabela} (id_veiculo, tipo, capacidade, ano_fabricacao, matricula)\nVALUES\n" + ",\n".join(linhas) + ";"

    # 3. Combinar CREATE + INSERT em um único script
    sql_script = sql_create + "\n" + sql_insert

    return sql_script


def criarMotoristasSQL(df: pd.DataFrame, tabela: str) -> str:
    sql_create = f"""
CREATE TABLE {tabela} (
    id_motorista INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    idade INT NOT NULL,
    experiencia INT NOT NULL,
    eficiencia DECIMAL(3,2)
    
);
    """

        # 2. Gerar os INSERTs a partir do DataFrame
    linhas = []
    for _, row in df.iterrows():
            valores = f"({row['id_motorista']}, '{row['nome']}', '{row['idade']}, '{row['experiencia']}, '{row['eficiencia']})"
            linhas.append(valores)

    sql_insert = f"INSERT INTO {tabela} (id_motorista, nome, idade, experiencia, eficiencia)\nVALUES\n" + ",\n".join(linhas) + ";"

    # 3. Combinar CREATE + INSERT em um único script
    sql_script = sql_create + "\n" + sql_insert

    return sql_script



"""----------------------------- PARTE DO RETALHO ------------------------"""

def criarProdutosSQL(df: pd.DataFrame, tabela: str) -> str:
    sql_create = f"""
CREATE TABLE {tabela} (
    id_produto INT PRIMARY KEY AUTO_INCREMENT,
    nome_produto VARCHAR(100) NOT NULL,
    categoria VARCHAR(50),
    preco_unitario DECIMAL(10,2),
    margem_bruta DECIMAL(3,2)
    
);
    """

        # 2. Gerar os INSERTs a partir do DataFrame
    linhas = []
    for _, row in df.iterrows():
            valores = f"({row['id_produto']}, '{row['nome_produto']}', '{row['categoria']}, '{row['preco_unitario']}, '{row['margem_bruta']})"
            linhas.append(valores)

    sql_insert = f"INSERT INTO {tabela} (id_produto, nome_produto, categoria, preco_unitario, margem_bruta)\nVALUES\n" + ",\n".join(linhas) + ";"

    # 3. Combinar CREATE + INSERT em um único script
    sql_script = sql_create + "\n" + sql_insert

    return sql_script


def criarLojasSQL(df: pd.DataFrame, tabela: str) -> str:
    sql_create = f"""
CREATE TABLE {tabela} (
    id_loja INT PRIMARY KEY AUTO_INCREMENT,
    nome_loja VARCHAR(100) NOT NULL,
    localizacao POINT NOT NULL,   -- coluna espacial
    SPATIAL INDEX(localizacao) 
    
);
    """

        # 2. Gerar os INSERTs a partir do DataFrame
    linhas = []
    for _, row in df.iterrows():
            valores = f"({row['id_loja']}, '{row['nome_loja']}', '{row['localizacao']})"
            linhas.append(valores)

    sql_insert = f"INSERT INTO {tabela} (id_loja, nome_loja, localizacao)\nVALUES\n" + ",\n".join(linhas) + ";"

    # 3. Combinar CREATE + INSERT em um único script
    sql_script = sql_create + "\n" + sql_insert

    return sql_script


def criarVendas_RetailSQL(df: pd.DataFrame, tabela: str) -> str:
    sql_create = f"""
CREATE TABLE {tabela} (
    id_venda INT PRIMARY KEY AUTO_INCREMENT,
    id_produto INT NOT NULL,
    id_cliente INT NOT NULL,   
    quantidade INT
    id_loja INT,
    valor_total DECIMAL(10,2),
    data_venda DATE
    
);
    """

        # 2. Gerar os INSERTs a partir do DataFrame
    linhas = []
    for _, row in df.iterrows():
            valores = f"({row['id_venda']}, '{row['id_produto']}', '{row['id_cliente']}, '{row['quantidade']}, '{row['id_loja']}, '{row['valor_total']}, '{row['data_venda']})"
            linhas.append(valores)

    sql_insert = f"INSERT INTO {tabela} (id_venda, id_produto, id_cliente, quantidade, id_loja, valor_total, data_venda)\nVALUES\n" + ",\n".join(linhas) + ";"

    # 3. Combinar CREATE + INSERT em um único script
    sql_script = sql_create + "\n" + sql_insert

    return sql_script

        
        
"""----------------------------- PARTE DA SAUDE ------------------------"""

def criarClinicaSQL(df: pd.DataFrame, tabela: str) -> str:
    sql_create = f"""
CREATE TABLE {tabela} (
    id_clinica INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100),
    localizacao POINT NOT NULL,   -- coluna espacial
    SPATIAL INDEX(localizacao)
);
    """

        # 2. Gerar os INSERTs
    linhas = []
    for _, row in df.iterrows():
        valores = (
            f"({row['id_clinica']}, '{row['nome']}',  {row['localizacao']})"
            )
        linhas.append(valores)

    sql_insert = (
        f"INSERT INTO {tabela} (id_clinica, nome, localizacao)\nVALUES\n"
        + ",\n".join(linhas)
        + ";"
    )

    # 3. Combinar CREATE + INSERT
    return sql_create + "\n" + sql_insert


def criarConsultaSQL(df: pd.DataFrame, tabela: str) -> str:
    sql_create = f"""
CREATE TABLE {tabela} (
    id_consulta INT PRIMARY KEY AUTO_INCREMENT,
    id_cliente INT NOT NULL,  
    id_medico INT NOT NULL, 
    id_clinica INT NOT NULL,
    data_agendamento DATE,
    data_atendimento DATE
    
);
    """

        # 2. Gerar os INSERTs a partir do DataFrame
    linhas = []
    for _, row in df.iterrows():
            valores = f"({row['id_consulta']}, '{row['id_cliente']}', '{row['id_medico']}, '{row['id_clinica']}, '{row['data_agendamento']}, '{row['data_atendimento']})"
            linhas.append(valores)

    sql_insert = f"INSERT INTO {tabela} (id_consulta, id_cliente, id_medico, id_clinica, data_agendamento, data_atendimento)\nVALUES\n" + ",\n".join(linhas) + ";"

    # 3. Combinar CREATE + INSERT em um único script
    sql_script = sql_create + "\n" + sql_insert

    return sql_script


def criarExameSQL(df: pd.DataFrame, tabela: str) -> str:
    sql_create = f"""
CREATE TABLE {tabela} (
    id_exame INT PRIMARY KEY AUTO_INCREMENT,
    id_cliente INT NOT NULL,  
    id_medico INT NOT NULL, 
    resultado VARCHAR(100) NOT NULL,
    custo DECIMAL(10,2),
    id_clinica INT NOT NULL
    
);
    """

        # 2. Gerar os INSERTs a partir do DataFrame
    linhas = []
    for _, row in df.iterrows():
            valores = f"({row['id_exame']}, '{row['id_cliente']}', '{row['id_medico']}, '{row['resultado']}, '{row['custo']}, '{row['id_clinica']})"
            linhas.append(valores)

    sql_insert = f"INSERT INTO {tabela} (id_exame, id_cliente, id_medico, resultado, custo, id_clinica)\nVALUES\n" + ",\n".join(linhas) + ";"

    # 3. Combinar CREATE + INSERT em um único script
    sql_script = sql_create + "\n" + sql_insert

    return sql_script


def criarMedicosSQL(df: pd.DataFrame, tabela: str) -> str:
    sql_create = f"""
CREATE TABLE {tabela} (
    id_medico INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,  
    especialidade VARCHAR(100), 
    telefone VARCHAR(100) NOT NULL,
    email VARCHAR(100)
    
    
);
    """

        # 2. Gerar os INSERTs a partir do DataFrame
    linhas = []
    for _, row in df.iterrows():
            valores = f"({row['id_medico']}, '{row['nome']}', '{row['especialidade']}, '{row['telefone']}, '{row['email']})"
            linhas.append(valores)

    sql_insert = f"INSERT INTO {tabela} (id_medico, nome, especialidade, telefone, email)\nVALUES\n" + ",\n".join(linhas) + ";"

    # 3. Combinar CREATE + INSERT em um único script
    sql_script = sql_create + "\n" + sql_insert

    return sql_script


"""----------------------------- PARTE DA SAUDE ------------------------"""
        
def criarPlanoSQL(df: pd.DataFrame, tabela: str) -> str:
    sql_create = f"""
CREATE TABLE {tabela} (
    id_plano INT PRIMARY KEY AUTO_INCREMENT,
    nome_plano VARCHAR(100) NOT NULL,
    tipo VARCHAR(50) NOT NULL,
    mensalidade DECIMAL(10,2)
    
);
    """

        # 2. Gerar os INSERTs a partir do DataFrame
    linhas = []
    for _, row in df.iterrows():
            valores = f"({row['id_plano']}, '{row['nome_plano']}', '{row['tipo']}, '{row['mensalidade']})"
            linhas.append(valores)

    sql_insert = f"INSERT INTO {tabela} (id_plano, nome_plano, tipo, mensalidade)\nVALUES\n" + ",\n".join(linhas) + ";"

    # 3. Combinar CREATE + INSERT em um único script
    sql_script = sql_create + "\n" + sql_insert

    return sql_script


def criarChamadasSQL(df: pd.DataFrame, tabela: str) -> str:
    sql_create = f"""
CREATE TABLE {tabela} (
    id_chamada INT PRIMARY KEY AUTO_INCREMENT,
    id_assinatura INT NOT NULL,  
    data_chamada DATE, 
    duracao INT NOT NULL,
    dados_consumidos DECIMAL(10,2)
    
    
);
    """

        # 2. Gerar os INSERTs a partir do DataFrame
    linhas = []
    for _, row in df.iterrows():
            valores = f"({row['id_chamada']}, '{row['id_assinatura']}', '{row['data_chamada']}, '{row['duracao']}, '{row['dados_consumidos']})"
            linhas.append(valores)

    sql_insert = f"INSERT INTO {tabela} (id_chamada, id_assinatura, data_chamada, duracao, dados_consumidos)\nVALUES\n" + ",\n".join(linhas) + ";"

    # 3. Combinar CREATE + INSERT em um único script
    sql_script = sql_create + "\n" + sql_insert

    return sql_script


def criarConsumo_internetSQL(df: pd.DataFrame, tabela: str) -> str:
    sql_create = f"""
CREATE TABLE {tabela} (
    id_consumo INT PRIMARY KEY AUTO_INCREMENT,
    id_assinatura INT NOT NULL,
    mes INT NOT NULL,
    dados_consumidos DECIMAL(10,2)
    
);
    """

        # 2. Gerar os INSERTs a partir do DataFrame
    linhas = []
    for _, row in df.iterrows():
            valores = f"({row['id_consumo']}, '{row['id_assinatura']}', '{row['mes']}, '{row['dados_consumidos']})"
            linhas.append(valores)

    sql_insert = f"INSERT INTO {tabela} (id_consumo, id_assinatura, mes, dados_consumidos)\nVALUES\n" + ",\n".join(linhas) + ";"

    # 3. Combinar CREATE + INSERT em um único script
    sql_script = sql_create + "\n" + sql_insert

    return sql_script


def criarAssinaturasSQL(df: pd.DataFrame, tabela: str) -> str:
    sql_create = f"""
CREATE TABLE {tabela} (
    id_assinatura INT PRIMARY KEY AUTO_INCREMENT,
    id_cliente INT,  
    id_plano INT, 
    data_inicio DATE,
    data_fim DATE,
    status VARCHAR(20)
    
    
);
    """

        # 2. Gerar os INSERTs a partir do DataFrame
    linhas = []
    for _, row in df.iterrows():
            valores = f"({row['id_assinatura']}, '{row['id_cliente']}', '{row['id_plano']}, '{row['data_inicio']}, '{row['data_fim']}, '{row['status']})"
            linhas.append(valores)

    sql_insert = f"INSERT INTO {tabela} (id_assinatura, id_cliente, id_plano, data_inicio, data_fim, status)\nVALUES\n" + ",\n".join(linhas) + ";"

    # 3. Combinar CREATE + INSERT em um único script
    sql_script = sql_create + "\n" + sql_insert

    return sql_script
