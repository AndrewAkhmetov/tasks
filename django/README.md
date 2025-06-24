# Задачи по Django

## Базовые фильтры
### Найди всех авторов с именем «John».
```python
Author.objects.filter(first_name='John') 
```

### Найди всех авторов, кроме тех, у кого фамилия «Doe»
```python
Author.objects.exclude(last_name='Doe')
```


## Числовые сравнения
### Найди все книги, цена которых меньше 500
```python
Book.objects.filter(price__lt=500)
```

### Найди все книги с ценой не более 300
```python
Book.objects.filter(price__lte=300)
```

### Найди все книги дороже 1000
```python
Book.objects.filter(price__gt=1000)
```

### Найди все книги с ценой от 750 и выше
```python
Book.objects.filter(price__gte=750)
```


## Поиск текста
### Найди все книги, содержащие слово «django» в названии
```python
Book.objects.filter(title__contains='django')
```

### Найди книги, в названии которых есть «python» (без учёта регистра)
```python
Book.objects.filter(title__icontains='python')
```

### Найди книги, название которых начинается со слова «Advanced»
```python
Book.objects.filter(title__startswith='Advanced')
```

### Найди книги, название которых начинается с «pro» (игнорируя регистр)
```python
Book.objects.filter(title__istartswith='pro')
```

### Найди книги, название которых заканчивается на слово «Guide»
```python
Book.objects.filter(title__endswith='Guide')
```

### Найди книги, название которых заканчивается на «tutorial» (без учёта регистра)
```python
Book.objects.filter(title__iendswith='tutorial')
```


## Проверка на null
### Найди все отзывы без комментариев
```python
Review.objects.filter(comment__isnull=True)
```

### Найди все отзывы, у которых есть комментарий
```python
Review.objects.filter(comment__isnull=False)
```


## IN и Range
### Найди авторов с идентификаторами 1, 3 и 5
```python
Author.objects.filter(id__in=[1, 3, 5])
```

### Найди книги, опубликованные с 1 января по 31 декабря 2023 года
```python
Book.objects.filter(
    published_date__date__range=[
        datetime.date(2023, 1, 1),
        datetime.date(2023, 12, 31)
    ]
)
```


## Регулярные выражения
### Найди книги, название которых начинается со слова «Python»
```python
Book.objects.filter(title__regex=r'^Python')
```

### Найди авторов, чья фамилия начинается на «Mc» (игнорируя регистр)
```python
Author.objects.filter(last_name__regex=r'^Mc')
```


## Даты и время
### Найди книги, опубликованные в 2024 году
```python
Book.objects.filter(published_date__year=2024)
```

### Найди книги, опубликованные в июне
```python
Book.objects.filter(published_date__month=6)
```

### Найди отзывы, оставленные 11-го числа любого месяца
```python
Review.objects.filter(created_at__day=11)
```

### Найди книги, опубликованные на 23-й неделе года
```python
Book.objects.filter(published_date__week=23)
```

### Найди отзывы, оставленные во вторник
```python
Review.objects.filter(created_at__week_day=3)
```

### Найди книги, опубликованные во втором квартале года
```python
Book.objects.filter(published_date__quarter=2)
```

### Найди отзывы, сделанные в определённую дату
```python
Review.objects.filter(created_at__date=datetime.date(2025, 1, 1))
```

### Найди отзывы, сделанные ровно в 15:30
```python
Review.objects.filter(created_at__time=datetime.time(15, 30))
```

### Найди отзывы, сделанные в 15 часов
```python
Review.objects.filter(created_at__hour=15)
```

### Найди отзывы, сделанные в 30 минут любого часа
```python
Review.objects.filter(created_at__minute=30)
```

### Найди отзывы, созданные в момент, когда секунды были равны 0
```python
Review.objects.filter(created_at__second=0)
```


## Связанные поля
### Найди книги, написанные автором с почтой «author@example.com»
```python
Book.objects.filter(author__email='author@example.com')
```

### Найди книги авторов, чья фамилия содержит «smith» (без учёта регистра)
```python
Book.objects.filter(author__last_name__icontains='smith')
```

### Найди авторов, написавших более пяти книг
```python
Author.objects.annotate(books_count=Count('books')).filter(books_count__gt=5)
```


## JSON-поля
### Найди книги, у которых значение ключа «genre» равно «fiction»
```python
Book.objects.filter(metadata__genre='fiction') 
```

### Найди книги, где значение ключа «tags» содержит слово «bestseller» (игнорируя регистр)
```python
Book.objects.filter(metadata__tags__icontains='bestseller') 
```


## Использование выражений F и Q
### Найди книги, у которых цена равна скидке
```python
Book.objects.filter(price=F('discount')) 
```

### Найди книги, у которых цена больше скидки
```python
Book.objects.filter(price__gt=F('discount'))
```

### Найди авторов с именем «Alice» или с фамилией, не равной «Brown»
```python
Author.objects.filter(Q(first_name='Alice') | ~Q(last_name='Brown'))
```


## Задания на аннотации
### Подсчитай количество книг каждого автора
```python
Author.objects.annotate(books_count=Count('books'))
```

### Подсчитай средний рейтинг каждой книги
```python
Book.objects.annotate(avg_rating=Avg('reviews__rating'))
```

### Посчитай окончательную цену книги (цена минус скидка)
```python
Book.objects.annotate(final_price=F('price') - F('price') * F('discount') / 100)
```


## Использование select_related и prefetch_related
### Получи список книг и авторов так, чтобы выполнить всего один SQL-запрос
```python
Book.objects.select_related('author').all()
```

### Получи список авторов и всех их книг так, чтобы было выполнено ровно два SQL-запроса
```python
Author.objects.prefetch_related('books').all()
```
