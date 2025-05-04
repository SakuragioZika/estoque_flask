from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = app.config['SECRET_KEY']

def get_db_connection():
    conn = mysql.connector.connect(
        host=app.config['MYSQL_HOST'],
        user=app.config['MYSQL_USER'],
        password=app.config['MYSQL_PASSWORD'],
        database=app.config['MYSQL_DB'],
        port=app.config['MYSQL_PORT']
    )
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/products')
def products():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('products.html', products=products)

@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        price = float(request.form['price'])
        quantity = int(request.form['quantity'])
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO products (name, description, price, quantity) VALUES (%s, %s, %s, %s)',
            (name, description, price, quantity)
        )
        conn.commit()
        cursor.close()
        conn.close()
        
        flash('Produto adicionado com sucesso!', 'success')
        return redirect(url_for('products'))
    
    return render_template('add_product.html')

@app.route('/edit_product/<int:id>', methods=['GET', 'POST'])
def edit_product(id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        price = float(request.form['price'])
        quantity = int(request.form['quantity'])
        
        cursor.execute(
            'UPDATE products SET name = %s, description = %s, price = %s, quantity = %s WHERE id = %s',
            (name, description, price, quantity, id)
        )
        conn.commit()
        cursor.close()
        conn.close()
        
        flash('Produto atualizado com sucesso!', 'success')
        return redirect(url_for('products'))
    
    cursor.execute('SELECT * FROM products WHERE id = %s', (id,))
    product = cursor.fetchone()
    cursor.close()
    conn.close()
    
    if product is None:
        flash('Produto não encontrado!', 'danger')
        return redirect(url_for('products'))
    
    return render_template('edit_product.html', product=product)

@app.route('/delete_product/<int:id>')
def delete_product(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM products WHERE id = %s', (id,))
    conn.commit()
    cursor.close()
    conn.close()
    
    flash('Produto removido com sucesso!', 'success')
    return redirect(url_for('products'))

if __name__ == '__main__':
    app.run(debug=True)