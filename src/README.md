Конструкция with ... as используется для оборачивания выполнения блока инструкций менеджером контекста. Иногда это более удобная конструкция, чем try...except...finally.

Синтаксис конструкции with ... as:

"with" expression ["as" target] ("," expression ["as" target])* ":"
    suite

по порядку о том, что происходит при выполнении данного блока:

- Выполняется выражение в конструкции with ... as.
- Загружается специальный метод __exit__ для дальнейшего использования.
- Выполняется метод __enter__. Если конструкция with включает в себя слово as, то возвращаемое методом __enter__ значение записывается в переменную.
- Выполняется suite.
- Вызывается метод __exit__, причём неважно, выполнилось ли suite или произошло исключение. В этот метод передаются параметры исключения, если оно произошло, или во всех аргументах значение None, если исключения не было.