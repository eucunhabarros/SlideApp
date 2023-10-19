import xmltodict
import os
import pandas as pd
from datetime import datetime
from num2words import num2words

def pegar_infos(nome_arquivo, valores, dicionario):
    with open(f'nfe/{nome_arquivo}', "rb") as arquivo_xml:
        dic_arquivo = xmltodict.parse(arquivo_xml)
        
        if "NFe" in dic_arquivo:
            infos_nf = dic_arquivo['NFe']['infNFe']
        else:
            infos_nf = dic_arquivo['nfeProc']['NFe']['infNFe']
        DATAEMISSAO = infos_nf['ide']['dhEmi']
        DATAEMISSAO = datetime.fromisoformat(DATAEMISSAO).strftime("%d/%m/%Y")
        DATAVENC = infos_nf['cobr']['dup']['dVenc']
        DATAVENC = datetime.fromisoformat(DATAVENC).strftime("%d/%m/%Y")
        NUMNF = infos_nf['ide']['nNF']
        NUMNF = int(NUMNF)
        NOMECLIENTE = infos_nf['dest']['xNome']
        IDPRODUTO = " "
        PRODUTO = " "
        QTDE = " "
        VLRUN = " "
        VALORTOTAL = infos_nf['cobr']['dup']['vDup'].replace('.',',')
        VALORDANOTA = infos_nf['cobr']['dup']['vDup'].replace('.',',')
        VENCTO = infos_nf['cobr']['dup']['dVenc']
        VENCTO = datetime.fromisoformat(VENCTO).strftime("%d/%m/%Y")
        EMISSAO = DATAEMISSAO
        # Converte VALORTOTAL em extenso
        if VALORTOTAL:
            valor_extenso = num2words(float(VALORTOTAL.replace(',', '.')), lang='pt_BR', to='currency')
            EXTENSO = valor_extenso.capitalize()  # Converte a primeira letra em maiúscula
        else:
            EXTENSO = ""

        # ...
        CNPJ = infos_nf['dest']['CNPJ']
        
        # Verifica se o CNPJ está no dicionário
        if CNPJ in dicionario:
            IDCLIENTE = dicionario[CNPJ]
        else:
            IDCLIENTE = ""  # Ou qualquer valor padrão que você desejar
        
        CODCLIENTE = IDCLIENTE

        valores.append([DATAEMISSAO, DATAVENC, NUMNF, IDCLIENTE, NOMECLIENTE, IDPRODUTO, PRODUTO, QTDE, VLRUN, VALORTOTAL, VALORDANOTA, CODCLIENTE, VENCTO, EMISSAO, EXTENSO])

# Dicionário de mapeamento
LISTAIDCLIENTE = {"37422096000196" : "C00001","01369186000547" : "C00106", "01369186000113" : "C00068", "37422096000358" : "C00001", "37422096000358" : "C00002", "42813402000155" : "C00003", "42813402000317" : "C00004", "42813402000589" : "C00005", "42813402000660" : "C00006", "42813402000740" : "C00007", "42813402000821" : "C00008", "42813402000902" : "C00009", "42813402001046" : "C00010", "42813402001127" : "C00011", "00748437000108" : "C00012", "14077545000100" : "C00013", "14077545000291" : "C00014", "05787644000195" : "C00015", "05787644000276" : "C00016", "05787644000861" : "C00017", "05787644000942" : "C00018", "05787644001086" : "C00019", "01803846000122" : "C00020", "01803846000203" : "C00021", "01803846000394" : "C00022", "01803846000475" : "C00023", "01803846000556" : "C00024", "06994443000121" : "C00025", "03716882000184" : "C00026", "00535340000117" : "C00027", "00535340000540" : "C00028", "00535340000621" : "C00029", "00535340000702" : "C00030", "00535340001008" : "C00031", "00535340001199" : "C00032", "00808899000173" : "C00033", "00808899000840" : "C00034", "00808899000920" : "C00035", "00808899001064" : "C00036", "08505776000175" : "C00037", "08505776000337" : "C00038", "08505776000418" : "C00039", "02799365000153" : "C00040", "02799365000234" : "C00041", "02799365000315" : "C00042", "02531842000103" : "C00043", "02531842000286" : "C00044", "04894685000118" : "C00045", "04894685000207" : "C00046", "04894685000380" : "C00047", "04894685000460" : "C00048", "27003044000121" : "C00049", "27003044000202" : "C00050", "00616936000141" : "C00051", "46121588000132" : "C00052", "46121588000566" : "C00053", "14242802000112" : "C00054", "03633516000161" : "C00055", "03633516000323" : "C00056", "03633516000404" : "C00057", "03633516000595" : "C00058", "03633516000676" : "C00059", "03633516000757" : "C00060", "03633516000838" : "C00061", "03633516000919" : "C00062", "12302060000148" : "C00063", "12302060000300" : "C00064", "00680229000114" : "C00065", "00680229000203" : "C00066", "00680229000467" : "C00067", "01369186000113" : "C00068", "01369186000202" : "C00069", "01948356000114" : "C00070", "01948356000203" : "C00071", "01948356000467" : "C00072", "01948356000548" : "C00073", "87689402008370" : "C00074", "00599846000190" : "C00075", "04419281000172" : "C00076", "19063889000184" : "C00077", "06266492000148" : "C00078", "27912244000105" : "C00080", "37422096000277" : "C00081", "37422096000358" : "C00082", "01803846000807" : "C00083", "12248342000104" : "C00084", "45116253015" : "C00085", "38490153000" : "C00086", "38490153000" : "C00087", "28789709004" : "C00088", "87689402008884" : "C00089", "37422096000439" : "C00090", "37422096000510" : "C00091", "05787644001167" : "C00092", "35501099000190" : "C00093", "12302060000490" : "C00094", "37637139000665" : "C00095", "29907174000203" : "C00097", "29907174000467" : "C00098", "03633516001052" : "C00099", "03633516001133" : "C00100"}

lista_arquivos = os.listdir("nfe")

colunas = ["DATAEMISSAO", "DATAVENC", "NUMNF", "IDCLIENTE", "NOMECLIENTE", "IDPRODUTO", "PRODUTO", "QTDE", "VLRUN", "VALORTOTAL", "VALORDANOTA", "CODCLIENTE", "VENCTO", "EMISSAO", "EXTENSO"]
valores = []

for arquivo in lista_arquivos:
    pegar_infos(arquivo, valores, LISTAIDCLIENTE)

tabela = pd.DataFrame(columns=colunas, data=valores)
tabela.to_excel("NotasFiscais2.xlsx", index=False)
