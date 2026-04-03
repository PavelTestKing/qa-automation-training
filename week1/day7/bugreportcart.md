BugCart 01 - SCRUM-19
Summary: Кнопка Checkout активна при пустой корзине.
Severity: S2
Priority: Medium
Steps to Reproduce:
1. Залогиниться на странице https://www.saucedemo.com/ standard_user / secret_sauce
2. Нажать на кнопку "Корзина" (cart) в верхнем правом углу экрана
3. Убедиться что корзина пуста (нет товаров).
4. Нажать кнопку "Checkout"
Actual Result: Переход на страницу введения данных (оформление заказа).
Expected Result: Кнопка не активна без товаров в корзине.
Environment: (Win 11, Firefox 149.0, 64-разрядный)


BugCart 02 - SCRUM-20
Summary: Поле First name, при оформлении заказа допускает введение цифр
Severity: S2
Priority: Medium
Steps to Reproduce:
1. Залогиниться на странице https://www.saucedemo.com/ standard_user / secret_sauce
2. Добавить товар "Sauce Labs Bike Light" в корзину
3. Нажать на корзину (cart) в верхней левой части экрана.
4. Нажать кнопку "Checkout"
5. Ввести в поле "First name" цифры
6. Ввести в поле "Last name" Kukuev
7. Ввести цифровой ZIP 612000
6. Нажать кнопку Continue
Actual Result: Данные приняты, перенаправлен на страницу https://www.saucedemo.com/checkout-step-two.html для завершения заказа.
Expected Result: Ошибка "First Name может содержать только буквы"
Environment: (Win 11, Firefox 149.0, 64-разрядный)