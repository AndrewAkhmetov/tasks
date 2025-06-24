# Все задания выполнялись в PostgreSQL. Использовались таблицы из предыдущего задания `sql`.

## Этап 1: Массовое наполнение базы
### Заполнить таблицу orders на 50 000 строк
```sql
INSERT INTO orders (customer_id, order_date)
SELECT 
    (random() * 2 + 1)::int, 
    (DATE '2025-01-01' + (random() * 900)::int)
FROM generate_series(1, 50000);
```

### Заполнить таблицу order_items минимум 1 000 000 строк
```sql
INSERT INTO order_items (order_id, product_name, quantity, price)
SELECT 
    (random() * 49999 + 1)::int,
    'Товар ' || (random() * 499 + 1)::int,
    (random() * 9 + 1)::int,
    (random() * 99000 + 100)::numeric(10,2)
FROM generate_series(1, 1000000);
```


## Этап 2: Установка индексов
### Создать индекс по полю customer_id в таблице orders
```sql
CREATE INDEX idx_orders_customer_id ON orders(customer_id);
```

### Создать композитный индекс по (order_id, price) в таблице order_items
```sql
CREATE INDEX idx_order_items_order_id_price ON order_items(order_id, price);
```

### Создать индекс по product_name в таблице order_items
```sql
CREATE INDEX idx_order_items_product_name ON order_items(product_name);
```


## Этап 3: Анализ использования индексов
### Задание 1: Написать EXPLAIN ANALYZE для запроса, который ищет все товары с price > 10000 из заказа с ID = 123
```sql
EXPLAIN ANALYZE
SELECT *
FROM order_items
WHERE order_id = 123 AND price > 10000;
```
#### Результат:
```sql
"Bitmap Heap Scan on order_items  (cost=4.62..78.18 rows=19 width=34) (actual time=16.136..16.197 rows=21 loops=1)"
"  Recheck Cond: ((order_id = 123) AND (price > '10000'::numeric))"
"  Heap Blocks: exact=21"
"  ->  Bitmap Index Scan on idx_order_items_order_id_price  (cost=0.00..4.62 rows=19 width=0) (actual time=16.113..16.113 rows=21 loops=1)"
"        Index Cond: ((order_id = 123) AND (price > '10000'::numeric))"
"Planning Time: 2.019 ms"
"Execution Time: 16.264 ms"
```
### Написать EXPLAIN ANALYZE для запроса, который ищет все заказы клиента с customer_id = 1
```sql
SELECT orders.id, order_items.product_name, order_items.quantity, order_items.price
FROM orders
JOIN order_items ON orders.id = order_items.order_id
WHERE orders.customer_id = 1;
```
#### Результат:
```sql
"Hash Join  (cost=727.91..21687.20 rows=249526 width=30) (actual time=8.976..537.626 rows=246801 loops=1)"
"  Hash Cond: (order_items.order_id = orders.id)"
"  ->  Seq Scan on order_items  (cost=0.00..18334.05 rows=1000005 width=30) (actual time=0.019..123.267 rows=1000005 loops=1)"
"  ->  Hash  (cost=571.95..571.95 rows=12477 width=4) (actual time=8.843..8.847 rows=12351 loops=1)"
"        Buckets: 16384  Batches: 1  Memory Usage: 563kB"
"        ->  Bitmap Heap Scan on orders  (cost=144.99..571.95 rows=12477 width=4) (actual time=0.780..5.408 rows=12351 loops=1)"
"              Recheck Cond: (customer_id = 1)"
"              Heap Blocks: exact=271"
"              ->  Bitmap Index Scan on idx_orders_customer_id  (cost=0.00..141.87 rows=12477 width=0) (actual time=0.704..0.704 rows=12351 loops=1)"
"                    Index Cond: (customer_id = 1)"
"Planning Time: 0.734 ms"
"Execution Time: 552.417 ms"
```
#### Примечание
Используется Seq Scan в order_items, судя по всему, из-за большого количество строк для возврата: (почти 25% таблицы). Была попытка добавить индекс по order_id, но это не помогло. Индекс по customer_id отрабатывается.


## Этап 4: Удаление неэффективных индексов
1. Был удален индекс по order_id в таблице order_items из-за неэффективности (предыдущее задание).
2. Был удален индекс product_name, т.к. не использовался в запросах.


## Этап 5: Бизнес-логика с использованием транзакций
### Проверка количества заказов до транзакции
```sql
SELECT 'Количество заказов ДО транзакций:' as info, COUNT(*) as count FROM orders;
```
#### Результат:
```sql
"Количество заказов ДО транзакций:"	50004
```

### Проверка количества товаров до транзакции
```sql
SELECT 'Количество товаров ДО транзакций:' as info, COUNT(*) as count FROM order_items;

```
#### Результат:
```sql
"Количество товаров ДО транзакций:"	1000008
```

### Создание заказа с товарами
```sql
DO $$
DECLARE
    new_order_id INT;
BEGIN    
    -- 1. Создаем заказ
    INSERT INTO orders (customer_id, order_date)
    VALUES (1, CURRENT_DATE)
    RETURNING id INTO new_order_id;
    
    RAISE NOTICE '1. Создан заказ #%', new_order_id;
    
    -- 2. Добавляем товары в заказ
    INSERT INTO order_items (order_id, product_name, quantity, price) VALUES
    (new_order_id, 'Ноутбук Pro', 1, 89900.00),
    (new_order_id, 'Беспроводная мышь', 2, 2490.50),
    (new_order_id, 'Чехол для ноутбука', 1, 3590.00);
    
    RAISE NOTICE '2. Добавлено 3 товара в заказ #%', new_order_id;
    RAISE NOTICE '3. Все операции выполнены успешно';

EXCEPTION WHEN OTHERS THEN
    RAISE NOTICE 'ОШИБКА в успешной транзакции: %', SQLERRM;    
END $$;
```

### Проверка количества заказов после транзакции
```sql
SELECT 'Количество заказов ПОСЛЕ транзакций:' as info, COUNT(*) as count FROM orders;
```
#### Результат:
```sql
"Количество заказов ПОСЛЕ транзакций:"	50005
```

### Проверка количества товаров после транзакции
```sql
SELECT 'Количество товаров ПОСЛЕ транзакций:' as info, COUNT(*) as count FROM order_items;
```
#### Результат:
```sql
"Количество товаров ПОСЛЕ транзакций:"	1000011
```


### Создание заказа с товарами с невалидными данными
```sql
DO $$
DECLARE
    new_order_id INT;
BEGIN    
    -- 1. Создаем заказ
    INSERT INTO orders (customer_id, order_date)
    VALUES (1, CURRENT_DATE)
    RETURNING id INTO new_order_id;
    
    RAISE NOTICE '1. Создан заказ #%', new_order_id;
    
    -- 2. Добавляем товары в заказ, один из которых невалиден
    INSERT INTO order_items (order_id, product_name, quantity, price) VALUES
    (new_order_id, 'Ноутбук Pro', 1, 89900.00),
    (new_order_id, 'Беспроводная мышь', 2, 2490.50),
    (new_order_id, 'Чехол для ноутбука', NULL, NULL);
    
    RAISE NOTICE '2. Добавлено 3 товара в заказ #%', new_order_id;
    RAISE NOTICE '3. Все операции выполнены успешно';

EXCEPTION WHEN OTHERS THEN
    RAISE NOTICE 'ОШИБКА в успешной транзакции: %', SQLERRM;
END $$;
```

### Проверка количества заказов после транзакции
```sql
SELECT 'Количество заказов ПОСЛЕ транзакций:' as info, COUNT(*) as count FROM orders;
```
#### Результат:
```sql
"Количество заказов ПОСЛЕ транзакций:"	50005
```

### Проверка количества товаров после транзакции
```sql
SELECT 'Количество товаров ПОСЛЕ транзакций:' as info, COUNT(*) as count FROM order_items;
```
#### Результат:
```sql
"Количество товаров ПОСЛЕ транзакций:"	1000011
```