db = db.getSiblingDB('eshop');

db.produtos.insertMany([
  { sku: 'ELEC-0001', nome: 'Smartphone XYZ', categoria: 'Eletrônicos', preco: 1999.9, estoque: 120 },
  { sku: 'FASH-0001', nome: 'Camiseta ABC', categoria: 'Moda', preco: 59.9, estoque: 450 }
]);

db.vendas.insertMany([
  { pedido_id: 'PED-10001', sku: 'ELEC-0001', cliente_id: 'C-100', data: new Date(), quantidade: 1, valor: 1999.9, canal: 'web' }
]);
