site = Flask(__name__, static_folder="estatico", template_folder="modelos")

produtos = [
    {
        "id": "combo-carinho",
        "titulo": "Combo Mini Pão de Queijo + Café Especial",
        "preco": "R$ 27,90",
        "descricao": "Um clássico que dispensa apresentações e aquece o paladar.",
    },
    {
        "id": "bebida-quente",
        "titulo": "Bebida Quente + Comida",
        "preco": "A partir de R$ 23,32",
        "descricao": "Sua opção de bebida quente com uma comida aconchegante.",
    },
    {
        "id": "misto-quente",
        "titulo": "Misto Quente da Cida + Café Especial",
        "preco": "R$ 39,15",
        "descricao": "Um combo saboroso com café especial e lanche quentinho.",
    },
    {
        "id": "pao-milho",
        "titulo": "Pão de Milho na Chapa + Café",
        "preco": "R$ 23,32",
        "descricao": "Pão de milho crocante com café para o momento perfeito.",
    },
]

@site.route("/")
def pagina_inicial():
    return render_template("index.html", produtos=produtos)

@site.route("/produto/<produto_id>")
def pagina_produto(produto_id):
    produto = next((item for item in produtos if item["id"] == produto_id), None)
    if produto is None:
        abort(404)
    return render_template("product.html", produto=produto)

if __name__ == "__main__":
    site.run(debug=True, host="0.0.0.0", port=8080)
