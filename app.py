from flask import Flask, render_template, abort
site = Flask(__name__, static_folder="estatico", template_folder="modelos")

produtos = [
    {
        "id": "combo-carinho",
        "titulo": "Combo Pão de Queijo + Café Especial",
        "preco": "R$ 16,90",
        "descricao": "Um clássico que dispensa apresentações e aquece o paladar.",
        "categoria": "Combos",
    },
    {
        "id": "Bebida-Quente",
        "titulo": "Bebida Quente + Comidinha",
        "preco": "A partir de R$ 15,32",
        "descricao": "Sua opção de bebida quente com uma comida aconchegante.",
        "categoria": "Combos",
    },
    {
        "id": "misto-quente",
        "titulo": "Misto Quente + Cappuccino",
        "preco": "R$ 21,15",
        "descricao": "Um combo saboroso com cappuccino e lanche quentinho.",
        "categoria": "Combos",
    },
    {
        "id": "pao-milho",
        "titulo": "Pão de Milho na Chapa + Café Mokaccino",
        "preco": "R$ 23,32",
        "descricao": "Pão de milho crocante com café para o momento perfeito.",
        "categoria": "Combos",
    },
    {
        "id": "pao-queijo",
        "titulo": "Pão de Queijo na Chapa + Café Espresso na Cafeteria Italiana",
        "preco": "R$ 23,32",
        "descricao": "Pão de queijo crocante com café Italiano para o momento perfeito.",
        "categoria": "Combos",
    },
    {
        "id": "pao-milho-queijo",
        "titulo": "Pão de Milho com Queijo + Chocolate quente cremoso",
        "preco": "R$ 27,90",
        "descricao": "Pão de milho crocante com queijo e Chocolate quente cremoso para alegra o dia.",
        "categoria": "Combos",
    },
    {
        "id": "Combo Imperador",
        "titulo": "Cappuccino com Chocolate + Empada de Frango + Croissant de Presunto e Queijo",
        "preco": "R$ 25,90",
        "descricao": "Cappuccino com Chocolate + Empada de Frango + Croissant de Presunto e Queijo para saborear o dia.",
        "categoria": "Combos",
    },
    {  
         "id": "Combo Segredo?",
        "titulo": "Combo Segredo?",
        "preco": "R$ 30,00",
        "descricao": "Um combo especial para os apreciadores de sabores exóticos.",
        "categoria": "Combos",
    },
    {
         "id": "Combo Doce Tentação",
        "titulo": "Mousse de Maracujá + Bolo de Chocolate + Cappuccino com Chocolate",
        "preco": "R$ 28,50",
        "descricao": "Um combo irresistível para os amantes de doces.",
        "categoria": "Combos",
    },
    {
        "id": "cafe-espresso",
        "titulo": "Café Espresso",
        "preco": "R$ 8,90",
        "descricao": "Café forte e intenso, preparado na hora.",
        "categoria": "Café",
    },
    {
        "id": "cappuccino",
        "titulo": "Cappuccino",
        "preco": "R$ 12,50",
        "descricao": "Cappuccino cremoso com chocolate em pó.",
        "categoria": "Café",
    },
    {
        "id": "cafe-latte",
        "titulo": "Café Latte",
        "preco": "R$ 13,90",
        "descricao": "Café suave com leite vaporizado.",
        "categoria": "Café",
    },
    {
        "id": "mokaccino",
        "titulo": "Mokaccino",
        "preco": "R$ 14,50",
        "descricao": "Café com chocolate e leite.",
        "categoria": "Café",
    },
    {
        "id": "chocolate-quente",
        "titulo": "Chocolate Quente",
        "preco": "R$ 11,90",
        "descricao": "Chocolate quente cremoso e delicioso.",
        "categoria": "Café",
    },
    {
        "id": "pao-queijo-simples",
        "titulo": "Pão de Queijo",
        "preco": "R$ 6,90",
        "descricao": "Pão de queijo mineiro tradicional.",
        "categoria": "Comidas",
    },
    {
        "id": "pao-queijo-chapa",
        "titulo": "Pão de Queijo na Chapa",
        "preco": "R$ 8,50",
        "descricao": "Pão de queijo quentinho e crocante.",
        "categoria": "Comidas",
    },
    {
        "id": "misto-quente-simples",
        "titulo": "Misto Quente",
        "preco": "R$ 12,90",
        "descricao": "Pão com queijo e presunto grelhado.",
        "categoria": "Comidas",
    },
    {
        "id": "croissant-presunto-queijo",
        "titulo": "Croissant de Presunto e Queijo",
        "preco": "R$ 14,90",
        "descricao": "Croissant amanteigado com presunto e queijo.",
        "categoria": "Comidas",
    },
    {
        "id": "empada-frango",
        "titulo": "Empada de Frango",
        "preco": "R$ 9,90",
        "descricao": "Empada de frango com massa crocante.",
        "categoria": "Comidas",
    },
    {
        "id": "bolo-chocolate",
        "titulo": "Bolo de Chocolate",
        "preco": "R$ 11,50",
        "descricao": "Fatia de bolo de chocolate fofinho.",
        "categoria": "Comidas",
    },
    {
        "id": "mousse-maracuja",
        "titulo": "Mousse de Maracujá",
        "preco": "R$ 10,90",
        "descricao": "Mousse cremosa de maracujá.",
        "categoria": "Comidas",
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
