from flask import Flask, render_template, url_for, abort

app = Flask(__name__, static_folder="static", template_folder="templates")

products = [
    {
        "id": "combo-carinho",
        "title": "Combo Mini Pão de Queijo + Café Especial",
        "price": "R$ 27,90",
        "description": "Um clássico que dispensa apresentações e aquece o paladar.",
    },
    {
        "id": "bebida-quente",
        "title": "Bebida Quente + Comida",
        "price": "A partir de R$ 23,32",
        "description": "Sua opção de bebida quente com uma comida aconchegante.",
    },
    {
        "id": "misto-quente",
        "title": "Misto Quente da Cida + Café Especial",
        "price": "R$ 39,15",
        "description": "Um combo saboroso com café especial e lanche quentinho.",
    },
    {
        "id": "pao-milho",
        "title": "Pão de Milho na Chapa + Café",
        "price": "R$ 23,32",
        "description": "Pão de milho crocante com café para o momento perfeito.",
    },
]

@app.route("/")
def index():
    return render_template("index.html", products=products)

@app.route("/produto/<product_id>")
def product_page(product_id):
    product = next((item for item in products if item["id"] == product_id), None)
    if product is None:
        abort(404)
    return render_template("product.html", product=product)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
