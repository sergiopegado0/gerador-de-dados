import streamlit as st
import gerarDataframes
import comandosSQL

st.title("Gerador de Dados")


qtd_dados = st.slider("Número de Dados para serem gerados",0,1000000,100)

#Eventos
def gerarBanco(qtd_dados):
    agenciasDF = gerarDataframes.gerarAgencias(qtd_dados)
    clientesDF = gerarDataframes.gerarCliente(qtd_dados)
    contasDF = gerarDataframes.gerarContas(qtd_dados)
    transacoesDF = gerarDataframes.gerarTransacoes(qtd_dados)
    
    return agenciasDF, clientesDF, contasDF, transacoesDF


def gerarEducacao(qtd_dados):
    cursosDF = gerarDataframes.gerarCurso(qtd_dados)
    clientesDF = gerarDataframes.gerarCliente(qtd_dados)
    instrutoresDF = gerarDataframes.gerarInstrutor(qtd_dados)
    inscricoesDF = gerarDataframes.gerarInscricao(qtd_dados)
    
    return cursosDF, clientesDF, inscricoesDF, instrutoresDF

def gerarLogistica(qtd_dados):
    entregasDF = gerarDataframes.gerarEntrega(qtd_dados)
    motoristasDF = gerarDataframes.gerarMotorista(qtd_dados)
    rastreioDF = gerarDataframes.gerarRastreio(qtd_dados)
    veiculosDF = gerarDataframes.gerarVeiculo(qtd_dados)
    
    return entregasDF, motoristasDF, rastreioDF, veiculosDF

def gerarRetalho(qtd_dados):
    produtosDF = gerarDataframes.gerarProduto(qtd_dados)
    lojasDF = gerarDataframes.gerarLoja(qtd_dados)
    clientesDF = gerarDataframes.gerarCliente(qtd_dados)
    vendasDF = gerarDataframes.gerarVendas(qtd_dados)
    
    return produtosDF, lojasDF, clientesDF, vendasDF

def gerarSaude(qtd_dados):
    clientesDF = gerarDataframes.gerarCliente(qtd_dados)
    clinica = gerarDataframes.gerarClinica(qtd_dados)
    consultas = gerarDataframes.gerarConsulta(qtd_dados)
    medicos = gerarDataframes.gerarMedico(qtd_dados)
    exames = gerarDataframes.gerarExame(qtd_dados)
    
    return clientesDF, clinica, consultas, medicos, exames

def gerarTelecom(qtd_dados):
    clientesDF = gerarDataframes.gerarCliente(qtd_dados)
    assinaturas = gerarDataframes.gerarAssinatura(qtd_dados)
    chamadas = gerarDataframes.gerarChamada(qtd_dados)
    consumo_internet = gerarDataframes.gerarConsumoInternet(qtd_dados)
    plano = gerarDataframes.gerarPlano(qtd_dados)
    
    return clientesDF, assinaturas, chamadas, consumo_internet, plano

# Inicializa no estado
if "dataframesBanco" not in st.session_state:
    st.session_state.dataframesBanco = None
    
if "dataframesEducacao" not in st.session_state:
    st.session_state.dataframesEducacao = None
    
if "dataframesLogistica" not in st.session_state:
    st.session_state.dataframesLogistica = None

if "dataframesRetalho" not in st.session_state:
    st.session_state.dataframesRetalho = None
    
if "dataframesSaude" not in st.session_state:
    st.session_state.dataframesSaude = None

if "dataframeTelecom" not in st.session_state:
    st.session_state.dataframeTelecom = None

tab1, tab2,tab3, tab4, tab5, tab6 = st.tabs(["Banco", "Educação", "Logística", "Retalho",
                                             "Saúde", "Telecom"])

with tab1:
    st.write("Vamos gerar dados do segmento do banco")
    if st.button("Gerar Dados",key="banco"):
        df_agencias, df_clientes, df_contas, df_trans = gerarBanco(qtd_dados)

        st.session_state.dataframesBanco = {
            "Agencias": df_agencias,
            "Clientes": df_clientes,
            "Contas": df_contas,
            "Transações": df_trans
        }
        
    # Só mostra selectbox se já gerou
    if st.session_state.dataframesBanco is not None:
        opc1 = st.selectbox(
            "Selecione a tabela que deseja visualizar",
            list(st.session_state.dataframesBanco.keys()),
            key="opc1"
        )
        st.dataframe(st.session_state.dataframesBanco[opc1])
        
        df_selecionado = st.session_state.dataframesBanco[opc1]

        # Botão para exportar o DataFrame selecionado
        #Onde vão aparecer os botões para salvar os arquivos    
        coluna1, coluna2, coluna3 = st.columns(3)

#---------------------------------------------------------------------------------------

        with coluna1:
            #st.button("Salvar SQL",key="saveSQL")
            # Botão para baixar arquivo .sql
            if opc1 == "Agencias":
                script = comandosSQL.criarAgenciaSQL(st.session_state.dataframesBanco["Agencias"], "agencia")
            elif opc1 == "Clientes":
                script = comandosSQL.criartabelaClienteSQL(st.session_state.dataframesBanco["Clientes"], "clientes_banco")
            elif opc1 == "Contas":
                script = comandosSQL.criarContasSQL(st.session_state.dataframesBanco["Contas"], "contas")
            elif opc1 == "Transações":
                script = comandosSQL.criarTransacoesSQL(st.session_state.dataframesBanco["Transações"], "transacoes")
            st.download_button(
                label=f"📥 Baixar {opc1} SQL",
                data=script,
                file_name=f"{opc1}.sql",
                mime="text/sql"
            )
        with coluna2:
            csv = df_selecionado.to_csv(index=False, sep=";", encoding="utf-8")
            st.download_button(
            label=f"📥 Baixar {opc1} em CSV",
            data=csv,
            file_name=f"{opc1}.csv",
            mime="text/csv"
        )
        with coluna3:
            # Exportar para JSON
            json_data = df_selecionado.to_json(orient="records", force_ascii=False, indent=4)
            st.download_button(
                label=f"📥 Baixar {opc1} em JSON",
                data=json_data,
                file_name=f"{opc1}.json",
                mime="application/json"
            )
        
    else:
        st.info("Clique em 'Gerar Dados' para carregar as tabelas.")
      
#---------------------------------------------------------------------------------------  
    
with tab2:
    st.write("Vamos gerar dados do segmento Educação")
    if st.button("Gerar Dados",key="educacao"):
        cursosDF, df_clientes, inscricoesDF, instrutoresDF = gerarEducacao(qtd_dados)

        st.session_state.dataframesEducacao = {
            "Clientes": df_clientes,
            "Cursos": cursosDF,
            "Instrutores": instrutoresDF,
            "Inscricoes": inscricoesDF
        }
        
    # Só mostra selectbox se já gerou
    if st.session_state.dataframesEducacao is not None:
        opc2 = st.selectbox(
            "Selecione a tabela que deseja visualizar",
            list(st.session_state.dataframesEducacao.keys()),
            key="opc2"
        )
        st.dataframe(st.session_state.dataframesEducacao[opc2])
        
        df_selecionado2 = st.session_state.dataframesEducacao[opc2]

        # Botão para exportar o DataFrame selecionado
        #Onde vão aparecer os botões para salvar os arquivos    
        coluna1, coluna2, coluna3 = st.columns(3)

        with coluna1:
            #st.button("Salvar SQL",key="saveSQL")
            # Botão para baixar arquivo .sql
            if opc2 == "Clientes":
                script = comandosSQL.criartabelaClienteSQL(st.session_state.dataframesEducacao["Clientes"], "clientes")
            elif opc2 == "Cursos":
                script = comandosSQL.criarCursosSQL(st.session_state.dataframesEducacao["Cursos"], "cursos")
            elif opc2 == "Instrutores":
                script = comandosSQL.criarInstrutoresSQL(st.session_state.dataframesEducacao["Instrutores"], "instrutores")
            elif opc2 == "Inscricoes":
                script = comandosSQL.criarInscricoesSQL(st.session_state.dataframesEducacao["Inscricoes"], "inscricoes")
            st.download_button(
                label=f"📥 Baixar {opc2} SQL",
                data=script,
                file_name=f"{opc2}.sql",
                mime="text/sql"
            )
        with coluna2:
            csv = df_selecionado2.to_csv(index=False, sep=";", encoding="utf-8")
            st.download_button(
            label=f"📥 Baixar {opc2} em CSV",
            data=csv,
            file_name=f"{opc2}.csv",
            mime="text/csv"
        )
        with coluna3:
            # Exportar para JSON
            json_data = df_selecionado2.to_json(orient="records", force_ascii=False, indent=4)
            st.download_button(
                label=f"📥 Baixar {opc2} em JSON",
                data=json_data,
                file_name=f"{opc2}.json",
                mime="application/json"
            )
        
    else:
        st.info("Clique em 'Gerar Dados' para carregar as tabelas.")

#---------------------------------------------------------------------------------------
    
with tab3:
    st.write("Vamos gerar dados do segmento Logística")
    
    if st.button("Gerar Dados",key="logistica"):
        entregasDF, motoristasDF, rastreioDF, veiculosDF = gerarLogistica(qtd_dados)

        st.session_state.dataframesLogistica = {
            "Entregas": entregasDF,
            "Motoristas": motoristasDF,
            "Rastreio": rastreioDF,
            "Veiculos": veiculosDF
        }
        
    # Só mostra selectbox se já gerou
    if st.session_state.dataframesLogistica is not None:
        opc3 = st.selectbox(
            "Selecione a tabela que deseja visualizar",
            list(st.session_state.dataframesLogistica.keys()),
            key="opc3"
        )
        st.dataframe(st.session_state.dataframesLogistica[opc3])
        
        df_selecionado2 = st.session_state.dataframesLogistica[opc3]

        # Botão para exportar o DataFrame selecionado
        #Onde vão aparecer os botões para salvar os arquivos    
        coluna1, coluna2, coluna3 = st.columns(3)

        with coluna1:
            #st.button("Salvar SQL",key="saveSQL")
            # Botão para baixar arquivo .sql
            if opc3 == "Entregas":
                script = comandosSQL.criarEntregasSQL(st.session_state.dataframesLogistica["Entregas"], "entregas")
            elif opc3 == "Motoristas":
                script = comandosSQL.criarMotoristasSQL(st.session_state.dataframesLogistica["Motoristas"], "motoristas")
            elif opc3 == "Rastreio":
                script = comandosSQL.criarRastreioSQL(st.session_state.dataframesLogistica["Rastreio"], "rastreio")
            elif opc3 == "Veiculos":
                script = comandosSQL.criarVeiculosSQL(st.session_state.dataframesLogistica["Veiculos"], "veiculos")
            st.download_button(
                label=f"📥 Baixar {opc3} SQL",
                data=script,
                file_name=f"{opc3}.sql",
                mime="text/sql"
            )
        with coluna2:
            csv = df_selecionado2.to_csv(index=False, sep=";", encoding="utf-8")
            st.download_button(
            label=f"📥 Baixar {opc3} em CSV",
            data=csv,
            file_name=f"{opc3}.csv",
            mime="text/csv"
        )
        with coluna3:
            # Exportar para JSON
            json_data = df_selecionado2.to_json(orient="records", force_ascii=False, indent=4)
            st.download_button(
                label=f"📥 Baixar {opc3} em JSON",
                data=json_data,
                file_name=f"{opc3}.json",
                mime="application/json"
            )
        
    else:
        st.info("Clique em 'Gerar Dados' para carregar as tabelas.")
    
#____________________________________________________________________________    

with tab4:
    st.write("Vamos gerar dados do segmento Retalho")
    
    if st.button("Gerar Dados",key="retalho"):
        produtosDF, lojasDF, clientesDF, vendasDF = gerarRetalho(qtd_dados)

        st.session_state.dataframesRetalho = {
            "Produtos": produtosDF,
            "Lojas": lojasDF,
            "Clientes": clientesDF,
            "Vendas": vendasDF
        }
        
    # Só mostra selectbox se já gerou
    if st.session_state.dataframesRetalho is not None:
        opc4 = st.selectbox(
            "Selecione a tabela que deseja visualizar",
            list(st.session_state.dataframesRetalho.keys()),
            key="opc4"
        )
        st.dataframe(st.session_state.dataframesRetalho[opc4])
        
        df_selecionado2 = st.session_state.dataframesRetalho[opc4]

        # Botão para exportar o DataFrame selecionado
        #Onde vão aparecer os botões para salvar os arquivos    
        coluna1, coluna2, coluna3 = st.columns(3)

        with coluna1:
            #st.button("Salvar SQL",key="saveSQL")
            # Botão para baixar arquivo .sql
            if opc4 == "Produtos":
                script = comandosSQL.criarProdutosSQL(st.session_state.dataframesRetalho["Produtos"], "produtos")
            elif opc4 == "Lojas":
                script = comandosSQL.criarLojasSQL(st.session_state.dataframesRetalho["Lojas"], "lojas")
            elif opc4 == "Clientes":
                script = comandosSQL.criartabelaClienteSQL(st.session_state.dataframesRetalho["Clientes"], "clientes")
            elif opc4 == "Vendas":
                script = comandosSQL.criarVendas_RetailSQL(st.session_state.dataframesRetalho["Vendas"], "vendas")
            st.download_button(
                label=f"📥 Baixar {opc4} SQL",
                data=script,
                file_name=f"{opc4}.sql",
                mime="text/sql"
            )
        with coluna2:
            csv = df_selecionado2.to_csv(index=False, sep=";", encoding="utf-8")
            st.download_button(
            label=f"📥 Baixar {opc4} em CSV",
            data=csv,
            file_name=f"{opc4}.csv",
            mime="text/csv"
        )
        with coluna3:
            # Exportar para JSON
            json_data = df_selecionado2.to_json(orient="records", force_ascii=False, indent=4)
            st.download_button(
                label=f"📥 Baixar {opc4} em JSON",
                data=json_data,
                file_name=f"{opc4}.json",
                mime="application/json"
            )
        
    else:
        st.info("Clique em 'Gerar Dados' para carregar as tabelas.")
    
#-------------------------------------------------------------------------------------
    
with tab5:
    st.write("Vamos gerar dados do segmento Saúde")
    if st.button("Gerar Dados",key="saude"):
        clientesDF, clinica, consultas, medicos, exames = gerarSaude(qtd_dados)

        st.session_state.dataframesSaude = {
            "Clientes": clientesDF,
            "Clinica": clinica,
            "Consultas": consultas,
            "Médicos": medicos,
            "Exames": exames
        }
        
    # Só mostra selectbox se já gerou
    if st.session_state.dataframesSaude is not None:
        opc5 = st.selectbox(
            "Selecione a tabela que deseja visualizar",
            list(st.session_state.dataframesSaude.keys()),
            key="opc5"
        )
        st.dataframe(st.session_state.dataframesSaude[opc5])
        
        df_selecionado5 = st.session_state.dataframesSaude[opc5]

        # Botão para exportar o DataFrame selecionado
        #Onde vão aparecer os botões para salvar os arquivos    
        coluna1, coluna2, coluna3 = st.columns(3)

        with coluna1:
            #st.button("Salvar SQL",key="saveSQL")
            # Botão para baixar arquivo .sql
            if opc5 == "Clientes":
                script = comandosSQL.criartabelaClienteSQL(st.session_state.dataframesSaude["Clientes"], "clientes")
            elif opc5 == "Clinica":
                script = comandosSQL.criarClinicaSQL(st.session_state.dataframesSaude["Clinica"], "clinica")
            elif opc5 == "Consultas":
                script = comandosSQL.criarConsultaSQL(st.session_state.dataframesSaude["Consultas"], "consultas")
            elif opc5 == "Médicos":
                script = comandosSQL.criarMedicosSQL(st.session_state.dataframesSaude["Médicos"], "medicos")
            elif opc5 == "Exames":
                script = comandosSQL.criarExameSQL(st.session_state.dataframesSaude["Exames"], "exames")
            st.download_button(
                label=f"📥 Baixar {opc5} SQL",
                data=script,
                file_name=f"{opc5}.sql",
                mime="text/sql"
            )
        with coluna2:
            csv = df_selecionado5.to_csv(index=False, sep=";", encoding="utf-8")
            st.download_button(
            label=f"📥 Baixar {opc5} em CSV",
            data=csv,
            file_name=f"{opc5}.csv",
            mime="text/csv"
        )
        with coluna3:
            # Exportar para JSON
            json_data = df_selecionado5.to_json(orient="records", force_ascii=False, indent=4)
            st.download_button(
                label=f"📥 Baixar {opc5} em JSON",
                data=json_data,
                file_name=f"{opc5}.json",
                mime="application/json"
            )
        
    else:
        st.info("Clique em 'Gerar Dados' para carregar as tabelas.")
    
    
with tab6:
    st.write("Vamos gerar dados do segmento Telecom")
    if st.button("Gerar Dados",key="telecom"):
        clientesDF, assinaturas, chamadas, consumo_internet, plano = gerarTelecom(qtd_dados)

        st.session_state.dataframeTelecom = {
            "Clientes": clientesDF,
            "Assinaturas": assinaturas,
            "Chamadas": chamadas,
            "Consumo Internet": consumo_internet,
            "Plano": plano
        }
        
    # Só mostra selectbox se já gerou
    if st.session_state.dataframeTelecom is not None:
        opc6 = st.selectbox(
            "Selecione a tabela que deseja visualizar",
            list(st.session_state.dataframeTelecom.keys()),
            key="opc6"
        )
        st.dataframe(st.session_state.dataframeTelecom[opc6])
        
        df_selecionado5 = st.session_state.dataframeTelecom[opc6]

        # Botão para exportar o DataFrame selecionado
        #Onde vão aparecer os botões para salvar os arquivos    
        coluna1, coluna2, coluna3 = st.columns(3)

        with coluna1:
            #st.button("Salvar SQL",key="saveSQL")
            # Botão para baixar arquivo .sql
            if opc6 == "Clientes":
                script = comandosSQL.criartabelaClienteSQL(st.session_state.dataframeTelecom["Clientes"], "clientes")
            elif opc6 == "Assinaturas":
                script = comandosSQL.criarAssinaturasSQL(st.session_state.dataframeTelecom["Assinaturas"], "assinaturas")
            elif opc6 == "Chamadas":
                script = comandosSQL.criarChamadasSQL(st.session_state.dataframeTelecom["Chamadas"], "chamadas")
            elif opc6 == "Consumo Internet":
                script = comandosSQL.criarConsumo_internetSQL(st.session_state.dataframeTelecom["Consumo Internet"], "consumo_internet")
            elif opc6 == "Plano":
                script = comandosSQL.criarPlanoSQL(st.session_state.dataframeTelecom["Plano"], "plano")
            st.download_button(
                label=f"📥 Baixar {opc6} SQL",
                data=script,
                file_name=f"{opc6}.sql",
                mime="text/sql"
            )
        with coluna2:
            csv = df_selecionado5.to_csv(index=False, sep=";", encoding="utf-8")
            st.download_button(
            label=f"📥 Baixar {opc6} em CSV",
            data=csv,
            file_name=f"{opc6}.csv",
            mime="text/csv"
        )
        with coluna3:
            # Exportar para JSON
            json_data = df_selecionado5.to_json(orient="records", force_ascii=False, indent=4)
            st.download_button(
                label=f"📥 Baixar {opc6} em JSON",
                data=json_data,
                file_name=f"{opc6}.json",
                mime="application/json"
            )
        
    else:
        st.info("Clique em 'Gerar Dados' para carregar as tabelas.")
    
    
    
    
    

    