# Порівняння функцій пошуку мінімальної кількості монет використовуючи динамічне програмування та жадібний алгоритм.

## Відповідні алгоритми описані у функціях:

find_coins_greedy - Жадібний алгоритм пошуку мінімальної кількості монет  
find_min_coins - Пошук мінімальної кількості монет використовуючи метод динамічного програмування

# Тести алгоритмів

Тест витраченого часу на виконання пошуку проводився на 3 випадках:

1. **small_amount** - невелика сума, що потребує малу кількість ітерацій
2. **medium_amount** - сума, що потребує більшої кількості ітерацій
3. **big_amount** - сума, що потребує великої кількості ітерацій

Час виконання замірявся бібліотекою timeit.

## Тест

**Алгоритм: find_min_coins**  
`small_amount`: 5.254102870821953e-05 seconds  
`medium_amount`: 0.00030170800164341927 seconds  
`big_amount`: 0.3065566250588745 seconds

**Алгоритм: find_coins_greedy**  
`small_amount`: 3.583962097764015e-06 seconds  
`medium_amount`: 4.62518073618412e-06 seconds  
`big_amount`: 0.0014608330093324184 seconds

# Висновок

Порівнюючи результати тесту, якщо відсортувати алгоритми за часом виконання, то ми отримаємо наступну таблицю:

| Кейс              |             Алгоритм              |
| ----------------- | :-------------------------------: |
| **small_amount**  | find_coins_greedy, find_min_coins |
| **medium_amount** | find_coins_greedy, find_min_coins |
| **big_amount**    | find_coins_greedy, find_min_coins |

Згідно з таблицею вище, можна зробити висновок, що жадібний алгоритм пошуку працює найшвидше для всіх кейсів, представлених у даному дослідженні. Наступною за швидкістю виконання є функція що написана використовуючи метод динамічного програмування.

У середньому, порівнюючи дані алгоритми, можна сказати що жадібний алгоритм працює набагато швидше ніж динамічний підхід – приблизно в 96 разів швидше.

Отже, згідно з цим дослідженням, емпірично було доведено, що жадібний алгоритм є найкращим варіантом для вирішення поставленої задачі в даному випадку, адже робить локально оптимальний вибір на кожному кроці, тоді як динамічне програмування обчислює оптимальні рішення для всіх проміжних сум, що потребує більше обчислень (створення та заповнення таблиці).
