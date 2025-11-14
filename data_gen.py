from faker import Faker
import random, json

fake = Faker('pt_BR')

def gen_produto(i):
    sku = f"PRD-{i:05d}"
    return {
        'sku': sku,
        'nome': fake.word().title() + ' ' + fake.word().title(),
        'categoria': random.choice(['Eletrônicos','Moda','Casa','Beleza','Esportes']),
        'preco': round(random.uniform(10, 5000),2),
        'estoque': random.randint(0,1000)
    }

if __name__ == '__main__':
    produtos = [gen_produto(i) for i in range(1,501)]
    with open('produtos_fake.json','w',encoding='utf-8') as f:
        json.dump(produtos,f,ensure_ascii=False,indent=2)
    print('Gerado produtos_fake.json com 500 produtos')
