from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_invoice', methods=['POST'])
def generate_invoice():
    client_name = request.form.get('client_name')
    product_name = request.form.get('product_name')
    quantity = int(request.form.get('quantity'))
    price = float(request.form.get('price'))

    total_amount = quantity * price

    return render_template('invoice.html', client_name=client_name, product_name=product_name, quantity=quantity, price=price, total_amount=total_amount)

if __name__ == '__main__':
    app.run(debug=True)
