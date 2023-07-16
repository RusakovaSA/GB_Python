-- 2. Создать файл my.sql, в котором должна создаваться таблица с информацией об одногруппниках. 
-- В таблице должно быть четыре поля: id, name, age, address. Все поля в таблице обязательны для заполнения.
-- Необходимо добавить 5-10 одногруппников в данную таблицу.
-- Необходимо написать запрос на получение имен всех одногруппников (только имен, без всего остального), 
-- которые живут в Москве и их возраст находится в диапазоне [18, 30) лет.


-- create
CREATE TABLE groupmates (
  id INTEGER PRIMARY KEY AUTO_INCREMENT,
  name TEXT NOT NULL,
  age TEXT NOT NULL,
  address TEXT NOT NULL
);

-- insert
INSERT INTO groupmates (name, age, address) VALUES ('Ольга', '29', 'Москва');
INSERT INTO groupmates (name, age, address) VALUES ('Николай', '30', 'Москва');
INSERT INTO groupmates (name, age, address) VALUES ('Петр', '27', 'Москва');
INSERT INTO groupmates (name, age, address) VALUES ('Иван', '25', 'Санкт Петербург');
INSERT INTO groupmates (name, age, address) VALUES ('Татьяна', '30', 'Саратов');
INSERT INTO groupmates (name, age, address) VALUES ('Нина', '25', 'Саратов');


-- fetch 
SELECT id, name AS Имя
FROM groupmates 
WHERE address = 'Москва' AND age BETWEEN  18 AND 30-1;