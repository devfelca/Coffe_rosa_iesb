from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Dados em memória pré-setado
produtos = [
    {"id": 1, "nome": "Café Expresso", "preco": 5.0, "quantidade": "50ml"},
    {"id": 2, "nome": "Cappuccino", "preco": 7.0, "quantidade": "120ml"},
    {"id": 3, "nome": "Pão de Queijo", "preco": 4.0, "quantidade": "60g"},
    {"id": 4, "nome": "Chocolate Quente", "preco": 6.5, "quantidade": "100ml"},
    {"id": 5, "nome": "Torrada com Manteiga", "preco": 3.5, "quantidade": "2 unidades"},
    {"id": 6, "nome": "Suco de Laranja", "preco": 6.0, "quantidade": "300ml"},
    {"id": 7, "nome": "Croissant", "preco": 5.5, "quantidade": "1 unidade"},
    {"id": 8, "nome": "Bolo de Cenoura", "preco": 4.5, "quantidade": "100g"},
]

clientes = [
    {"id": 1, "nome": "Maria Silva"},
    {"id": 2, "nome": "João Souza"},
    {"id": 3, "nome": "Ana Paula"},
    {"id": 4, "nome": "Carlos Alberto"},
    {"id": 5, "nome": "Fernanda Lima"},
    {"id": 6, "nome": "Ricardo Gomes"},
    {"id": 7, "nome": "Beatriz Rocha"},
    {"id": 8, "nome": "Tiago Mendes"},
]

pedidos = [
    {"id": 1, "cliente": "Maria Silva", "produto": "Café Expresso"},
    {"id": 2, "cliente": "João Souza", "produto": "Cappuccino"},
    {"id": 3, "cliente": "Ana Paula", "produto": "Pão de Queijo"},
    {"id": 4, "cliente": "Carlos Alberto", "produto": "Chocolate Quente"},
    {"id": 5, "cliente": "Fernanda Lima", "produto": "Croissant"},
    {"id": 6, "cliente": "Ricardo Gomes", "produto": "Torrada com Manteiga"},
    {"id": 7, "cliente": "Beatriz Rocha", "produto": "Suco de Laranja"},
    {"id": 8, "cliente": "Tiago Mendes", "produto": "Bolo de Cenoura"},
    {"id": 9, "cliente": "Maria Silva", "produto": "Pão de Queijo"},
    {"id": 10, "cliente": "João Souza", "produto": "Café Expresso"},
]


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/sistema")
def sistema():
    return render_template("sistema.html")
    
""" 
Aqui estão as rotas utilizando o método POST e o processamento lógico para os itens do sistema, basicamente mockei tudo no mesmo lugar, não condiz com as boas
práticas, como é para fim acadêmico e de exemplificação optei por fazer assim.

A rota pede o caminho hmlt e retorna a função para determinada solicitação
ex: sistema > prodtuos > adionar produto > chama a função > adionar < retorna o produto para a lista armazenada em memo.

Em case real as rotas estariam protegidas via autenticação e o processamento da regra de negócio separado.

""" 
# Produtos
@app.route("/produtos", methods=["GET"])
def listar_produtos():
    return render_template("gerenciar_produtos.html", produtos=produtos)

@app.route("/produtos/adicionar", methods=["POST"])
def adicionar_produto():
    nome = request.form["nome"]
    preco = float(request.form["preco"])
    quantidade = request.form["quantidade"]
    novo_id = max([p["id"] for p in produtos], default=0) + 1
    produtos.append({"id": novo_id, "nome": nome, "preco": preco, "quantidade": quantidade})
    return redirect("/produtos")

@app.route("/produtos/editar/<int:id>", methods=["POST"])
def editar_produto(id):
    nome = request.form["nome"]
    preco = float(request.form["preco"])
    quantidade = request.form["quantidade"]
    for p in produtos:
        if p["id"] == id:
            p["nome"] = nome
            p["preco"] = preco
            p["quantidade"] = quantidade
    return redirect("/produtos")

@app.route("/produtos/excluir/<int:id>", methods=["POST"])
def excluir_produto(id):
    global produtos
    produtos = [p for p in produtos if p["id"] != id]
    return redirect("/produtos")

# Clientes
@app.route("/clientes", methods=["GET"])
def listar_clientes():
    return render_template("gerenciar_clientes.html", clientes=clientes)

@app.route("/clientes/adicionar", methods=["POST"])
def adicionar_cliente():
    nome = request.form["nome"]
    novo_id = max([c["id"] for c in clientes], default=0) + 1
    clientes.append({"id": novo_id, "nome": nome})
    return redirect("/clientes")

@app.route("/clientes/editar/<int:id>", methods=["POST"])
def editar_cliente(id):
    nome = request.form["nome"]
    for c in clientes:
        if c["id"] == id:
            c["nome"] = nome
    return redirect("/clientes")

@app.route("/clientes/excluir/<int:id>", methods=["POST"])
def excluir_cliente(id):
    global clientes
    clientes = [c for c in clientes if c["id"] != id]
    return redirect("/clientes")

# Pedidos
@app.route("/pedidos", methods=["GET"])
def listar_pedidos():
    return render_template("gerenciar_pedidos.html", pedidos=pedidos)

@app.route("/pedidos/adicionar", methods=["POST"])
def adicionar_pedido():
    cliente = request.form["cliente"]
    produto = request.form["produto"]
    novo_id = max([p["id"] for p in pedidos], default=0) + 1
    pedidos.append({"id": novo_id, "cliente": cliente, "produto": produto})
    return redirect("/pedidos")

@app.route("/pedidos/editar/<int:id>", methods=["POST"])
def editar_pedido(id):
    cliente = request.form["cliente"]
    produto = request.form["produto"]
    for p in pedidos:
        if p["id"] == id:
            p["cliente"] = cliente
            p["produto"] = produto
    return redirect("/pedidos")

@app.route("/pedidos/excluir/<int:id>", methods=["POST"])
def excluir_pedido(id):
    global pedidos
    pedidos = [p for p in pedidos if p["id"] != id]
    return redirect("/pedidos")

@app.route("/cardapio")
def cardapio():
    return render_template("cardapio.html", produtos=produtos)

if __name__ == "__main__":
    app.run(debug=True)
