# Все задания выполнялись в PostgreSQL.

## Этап 1
### Создание таблицы custoomers
```sql
CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);
```

### Создание таблицы orders
```sql
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    order_date DATE NOT NULL,
	FOREIGN KEY (customer_id) REFERENCES customers(id) ON DELETE CASCADE
);
```

### Создание таблицы order_items
```sql
CREATE TABLE order_items (
    id SERIAL PRIMARY KEY,
    order_id INTEGER NOT NULL,
    product_name VARCHAR(255) NOT NULL,
    quantity INTEGER NOT NULL,
    price NUMERIC(10, 2) NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(id) ON DELETE CASCADE
);
```


## Этап 2
### customers: минимум 3 клиента с уникальными email.
```sql
INSERT INTO customers (name, email) VALUES
('Иван Иванов', 'ivan@example.com'),
('Петр Петров', 'petr@example.com'),
('Сидор Сидоров', 'sidor@example.com');
```

### orders: минимум 3 заказа, распределённых между клиентами (один клиент должен иметь 2 заказа).
```sql
INSERT INTO orders (customer_id, order_date) VALUES
(1, '2025-06-15'),
(1, '2025-06-20'),
(2, '2025-06-21');
```

### order_items: минимум 5 товаров, с привязкой к разным заказам, с разными количествами и ценами.
```sql
INSERT INTO order_items (order_id, product_name, quantity, price) VALUES
(1, 'Ноутбук', 1, 60000.00),
(1, 'Мышь', 2, 3500.00),
(2, 'Клавиатура', 2, 8000.00),
(3, 'Монитор', 1, 15000.00),
(3, 'Коврик для мыши', 3, 1000.00);
```


## Этап 3
### Задание 1: Простая фильтрация
```sql
SELECT orders.id, orders.order_date
FROM orders
JOIN customers ON orders.customer_id = customers.id
WHERE customers.name = 'Иван Иванов';
```

### Задание 2: Фильтрация + сортировка
```sql
SELECT product_name, quantity, price
FROM order_items
WHERE order_id = 3
ORDER BY price DESC;
```

### Задание 3: Группировка + фильтрация
```sql
SELECT name, SUM(quantity * price) as total_spent
FROM customers
JOIN orders ON customers.id = orders.customer_id
JOIN order_items ON orders.id = order_items.id
GROUP BY customers.id
HAVING SUM(quantity * price) > 5000;
```
