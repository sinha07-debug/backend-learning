INSERT INTO developers (name, country, founded_year, website)
VALUES
('Mojang Studios', 'Sweden', 2009, 'https://www.minecraft.net'),
('Rockstar Games', 'USA', 1998, 'https://www.rockstargames.com'),
('CD Projekt Red', 'Poland', 2002, 'https://www.cdprojektred.com'),
('Valve', 'USA', 1996, 'https://www.valvesoftware.com');

INSERT INTO games (title, genre, release_date, price, developer_id)
VALUES
('Minecraft', 'Sandbox', '2011-11-18', 29.99, 1),
('Grand Theft Auto V', 'Action', '2013-09-17', 59.99, 2),
('Cyberpunk 2077', 'RPG', '2020-12-10', 49.99, 3),
('Half-Life 2', 'FPS', '2004-11-16', 9.99, 4);

INSERT INTO customers (first_name, last_name, email, country)
VALUES
('Sagar', 'sgr@example.com', 'USA'),
('Dheeman', 'demon@example.com', 'India'),
('Jayati', 'jaggu@example.com', 'Japan'),
('Suraj', 'suraj@example.com', 'Australia');

INSERT INTO purchases (customer_id, game_id, purchase_price)
VALUES
(1, 1, 29.99),
(1, 2, 59.99),
(2, 1, 19.99),
(3, 4, 9.99),
(4, 3, 49.99);

INSERT INTO reviews
(customer_id, game_id, rating, comment)
VALUES
(1, 1, 5, 'One of the best games ever made.'),
(1, 2, 4, 'Really fun open world experience.'),
(2, 1, 5, 'Love the creativity.'),
(3, 4, 5, 'A timeless classic.'),
(4, 3, 3, 'Good game but had bugs at launch.');