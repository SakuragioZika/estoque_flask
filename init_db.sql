CREATE DATABASE IF NOT EXISTS estoque_db;

USE estoque_db;

CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    quantity INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Inserir alguns dados de exemplo
INSERT INTO products (name, description, price, quantity) VALUES
('KIT SKALA SH', 'Shampoo + Condicionador', 19, 1),
('Amaciante e Calosidades', 'Amaciante de Cuticulas e Calosidades Repos', 15.70, 2),
('Botox', 'Botox Borabella Repositor', 59.40, 2),
('Aparelho de Barbear', 'Aparelho de Barbear Superbarba', 50, 8);