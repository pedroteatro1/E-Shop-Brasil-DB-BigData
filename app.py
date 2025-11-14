import streamlit as st
from pymongo import MongoClient
import pandas as pd
import json, os
from dotenv import load_dotenv

load_dotenv()
MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/eshop')
client = MongoClient(MONGO_URI)
db = client.get_database()

st.set_page_config(page_title='E-Shop Brasil - Data Manager', layout='wide')
st.title('🛒 E-Shop Brasil — Gerenciamento de Dados (MongoDB)')

#@st.cache_data
def get_collection_df(col_name, limit=1000):
    docs = list(db[col_name].find().limit(limit))
    if not docs:
        return pd.DataFrame()
    df = pd.DataFrame(docs)
    if '_id' in df.columns:
        df['_id'] = df['_id'].astype(str)
    return df

collections = db.list_collection_names()
col_sel = st.sidebar.selectbox('Coleção', options=collections if collections else ['produtos','vendas'])
st.sidebar.header('Inserir dados')

upload = st.sidebar.file_uploader('Enviar JSON/CSV', type=['json','csv'])
if upload:
    if upload.name.endswith('.json'):
        data = json.load(upload)
        data = data if isinstance(data, list) else [data]
        db[col_sel].insert_many(data)
        st.sidebar.success(f'Inseridos {len(data)} documentos em {col_sel}')
    else:
        df = pd.read_csv(upload)
        db[col_sel].insert_many(df.to_dict(orient='records'))
        st.sidebar.success(f'Inseridos {len(df)} documentos em {col_sel}')

if st.sidebar.button('Gerar 100 produtos falsos'):
    from faker import Faker
    fake = Faker('pt_BR')
    docs = []
    for _ in range(100):
        docs.append({
            'sku': f'FAKE-{fake.random_number(digits=6)}',
            'nome': fake.word().title(),
            'categoria': fake.random_element(elements=('Eletrônicos','Moda','Casa','Beleza','Esportes')),
            'preco': round(fake.random_number(digits=4)/10,2),
            'estoque': fake.random_int(min=0, max=500)
        })
    db['produtos'].insert_many(docs)
    st.sidebar.success('100 produtos adicionados!')

st.header('Visualizar e consultar dados')
df = get_collection_df(col_sel)
st.dataframe(df)

del_id = st.text_input('Excluir documento (_id)')
if st.button('Excluir'):
    from bson.objectid import ObjectId
    db[col_sel].delete_one({'_id': ObjectId(del_id)})
    st.success('Documento excluído!')

edit_id = st.text_input('Editar documento (_id)')
edit_json = st.text_area('Novo conteúdo (ex: {"preco": 99.9})')
if st.button('Editar'):
    from bson.objectid import ObjectId
    db[col_sel].update_one({'_id': ObjectId(edit_id)}, {'$set': json.loads(edit_json)})
    st.success('Documento atualizado!')

st.header('Consulta personalizada')
filtro = st.text_area('Filtro (JSON)', '{"categoria": "Moda"}')
if st.button('Buscar'):
    q = json.loads(filtro)
    docs = list(db[col_sel].find(q))
    if docs:
        df = pd.DataFrame(docs)
        df['_id'] = df['_id'].astype(str)
        st.dataframe(df)
    else:
        st.info('Nenhum resultado encontrado')


st.markdown("---")
st.subheader("🔗 Concatenação: Produtos + Vendas")

if st.button("Concatenar dados e exibir análise"):
    produtos = list(db["produtos"].find({}, {"_id": 0}))
    vendas = list(db["vendas"].find({}, {"_id": 0}))

    if not produtos or not vendas:
        st.warning("As coleções 'produtos' e 'vendas' precisam ter dados.")
    else:
        import pandas as pd

        df_prod = pd.DataFrame(produtos)
        df_vendas = pd.DataFrame(vendas)

        # Junta (join) pelo campo 'sku'
        df_merged = pd.merge(df_vendas, df_prod, on="sku", how="left")

        st.write("### Dados combinados:")
        st.dataframe(df_merged.head(10))

        # Agrupa por categoria e soma total
        df_cat = df_merged.groupby("categoria")["valor_total"].sum().reset_index()

        st.write("### Total de vendas por categoria:")
        st.dataframe(df_cat)

        # Gráfico de barras
        st.bar_chart(df_cat.set_index("categoria"))


st.markdown("---")
st.subheader("📊 Gráfico de vendas por canal")

if st.button("Gerar gráfico de canais"):
    vendas = list(db["vendas"].find({}, {"_id": 0}))
    if not vendas:
        st.warning("Nenhuma venda encontrada.")
    else:
        import pandas as pd

        df_vendas = pd.DataFrame(vendas)
        df_canal = df_vendas.groupby("canal")["valor_total"].sum().reset_index()

        st.write("### Total de vendas por canal:")
        st.dataframe(df_canal)

        st.bar_chart(df_canal.set_index("canal"))
