🛒 E-Shop Brasil — Sistema de Gestão e Análise de Dados (Big Data)
Plataforma completa para CRUD de produtos, geração de dados falsos, análise de vendas e dashboard interativo, utilizando:

MongoDB (NoSQL)
Docker
Python
Streamlit
Pandas
Este projeto simula um ambiente real de uma empresa de e-commerce, permitindo gerenciar dados, fazer consultas avançadas e visualizar gráficos analíticos.

# 💡 Objetivo
Simular a gestão de dados de uma empresa de e-commerce usando **MongoDB**, **Streamlit** e **Docker**.

## ⚙️ Como rodar o projeto

### 1️⃣ Clone ou baixe o repositório
```bash
git clone https://github.com/pedroteatro1/E-Shop-Brasil-DB-BigData.git
cd E-Shop-Brasil-DB-BigData

📂 Estrutura do Projeto
E-Shop-Brasil-DB-BigData/
├── README.md
├── docker-compose.yml           # Sobe MongoDB + interface (app)
├── Dockerfile                   # Ambiente do Streamlit
├── requirements.txt             # Dependências do Python
├── app.py                       # Interface Streamlit (CRUD + Análises)
├── data_gen.py                  # Gerador de dados falsos
├── init-mongo/
│   └── seed.js                  # Scripts de inicialização do MongoDB
└── exemplos/
    ├── demo_insert.gif          # Demonstração da inserção
    ├── demo_edit.gif            # Demonstração da edição
    └── demo_delete.gif          # Demonstração da exclusão

🛠️ Tecnologias utilizadas
Tecnologia	Função
MongoDB	Banco NoSQL principal
Docker / Docker Compose	Orquestração do ambiente
Streamlit	Interface web interativa
Pandas	Manipulação dos dados
Python	Lógica da aplicação

🚀 Como rodar o projeto
1️⃣ Clonar o repositório
git clone https://github.com/seu-usuario/E-Shop-Brasil-DB-BigData.git
cd E-Shop-Brasil-DB-BigData

2️⃣ Subir o ambiente Docker
docker-compose up --build
Isso irá:

✔ Criar o container do MongoDB
✔ Criar o container do Streamlit
✔ Disponibilizar o app em:
👉 http://localhost:8501
👉 MongoDB em mongodb://localhost:27017

🧩 Funcionalidades da Interface
🔹 1. Inserir dados (JSON / CSV)

Upload de arquivos .json ou .csv
Inserção direta no MongoDB
Exibição imediata na tabela
Exemplo:

{
  "sku": "ELEC-001",
  "nome": "Smartphone XYZ",
  "categoria": "Eletrônicos",
  "preco": 1999.90,
  "estoque": 120
}

🔹 2. Gerar dados falsos
O botão Gerar 100 produtos falsos usa o arquivo:

data_gen.py
Produz dados realistas de e-commerce com:
SKU automático
Categoria
Preço
Estoque
Marca
Data de cadastro

🔹 3. Consultar dados
Inclui busca por:
Categoria
Nome
Faixa de preço
Campos personalizados (JSON)

🔹 4. Editar documentos
Atualiza qualquer documento pelo _id:
{"preco": 149.90}

🔹 5. Excluir documentos
Remove qualquer registro pelo _id.

📊 6. Dashboard Analítico
Inclui:

✔ Gráfico — Vendas por categoria
✔ Gráfico — Vendas por canal (app/web/mobile)
✔ Tabela de vendas + produtos com merge automático
✔ Cálculo automático de:

valor_total
ticket médio
quantidade vendida

⚙️ Configuração do MongoDB (init/seed)
O arquivo init-mongo/seed.js insere coleções base:
db = db.getSiblingDB("ecomtech");
db.produtos.insertMany([
  { sku: "ELEC-0001", nome: "Smartphone XYZ", preco: 1999.9, categoria: "Eletrônicos", estoque: 120 },
]);

📦 Dependências (requirements.txt)
streamlit
pymongo
pandas
faker
plotly
python-dotenv

🎥 Demonstrações
Inserção
Edição
Exclusão

🧑‍💻 Autor

Pedro Henrique Araújo Silva
Projeto criado para estudos e portfólio na área de Dados / Big Data / Engenharia de Dados.

