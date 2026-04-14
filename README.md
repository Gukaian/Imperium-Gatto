# Imperium Gatto Designer

Este projeto agora inclui um site Python com design inspirado na imagem do café felino.

## Como usar

1. Copie a imagem que você enviou para `static/background.jpeg`.
2. Abra o terminal neste diretório.
3. Instale Flask:

```bash
pip install flask
```

4. Execute o servidor:

```bash
python app.py
```
5. O terminal mostrará que o servidor está rodando na porta 8080.

## Acesso local (mesma rede)

- No computador: `http://127.0.0.1:8080`
- No celular/outro dispositivo na mesma rede: `http://192.168.1.6:8080`

## Acesso externo via ngrok

O jeito mais simples de expor seu site sem mexer no roteador é usar o ngrok.

1. Instale o ngrok em https://ngrok.com/
2. Abra o terminal na pasta do projeto.
3. Execute:

```bash
gnrok http 8080
```

4. Use a URL gerada pelo ngrok, por exemplo:

```
https://xxxxxxxxxxxx.ngrok.io
```

> ⚠️ **Atenção:** ngrok cria um túnel temporário. Sempre encerre o ngrok quando não estiver usando o site.

## O que está incluído

- `app.py` — servidor Flask que exibe o site.
- `templates/index.html` — página principal com produtos clicáveis.
- `templates/product.html` — página de detalhe do produto que informa que não é possível comprar.
- `static/style.css` — estilo visual inspirado no design.

## Observação

Os itens são clicáveis, mas o site é apenas demonstrativo e não processa compras.
