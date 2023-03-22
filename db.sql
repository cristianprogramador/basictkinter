CREATE TABLE students(id serial, name text, address text, age int);

INSERT INTO students(name, address, age) VALUES
    ('John', '123 Main St', 30);
INSERT INTO students(name, address, age) VALUES
    ('ryan', 'San francisco', 23);

select * from students;