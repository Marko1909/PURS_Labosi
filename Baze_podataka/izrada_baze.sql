DROP DATABASE IF EXISTS lvj6;
CREATE DATABASE lvj6;
USE lvj6;


DROP USER IF EXISTS app;
CREATE USER app@'%' IDENTIFIED BY '1234';
GRANT SELECT, INSERT, UPDATE, DELETE ON lvj6.* TO app@'%';


CREATE TABLE temperatura (
	id INT PRIMARY KEY AUTO_INCREMENT,
    datum DATETIME,
    vrijednost INT
);

INSERT INTO temperatura (datum, vrijednost) VALUES 
	('2023-10-10 23:40:13', 23),
    ('2023-10-11 12:59:53', 20),
    ('2023-10-12 14:31:32', 22),
    ('2023-10-13 05:45:17', 18);

CREATE TABLE vlaga (
	id INT PRIMARY KEY AUTO_INCREMENT,
    datum DATETIME,
    vrijednost INT
);

INSERT INTO vlaga (datum, vrijednost) VALUES
	('2023-10-10 23:41:13', 56),
    ('2023-10-11 13:00:53', 32),
    ('2023-10-12 14:32:32', 48),
    ('2023-10-13 05:46:17', 27);

CREATE TABLE ovlasti (
	id INT PRIMARY KEY AUTO_INCREMENT,
    naziv VARCHAR(100)
);

INSERT INTO ovlasti (naziv) VALUES
	('Administrator'),
    ('Korisnik');
    
CREATE TABLE korisnik (
	id INT PRIMARY KEY AUTO_INCREMENT,
    ime CHAR(50) NOT NULL,
    prezime CHAR(50) NOT NULL,
    username VARCHAR(50) NOT NULL,
    password BINARY(32) NOT NULL,
    id_ovlasti INT,
    FOREIGN KEY (id_ovlasti) REFERENCES ovlasti(id) ON UPDATE CASCADE ON DELETE SET NULL
);

INSERT INTO korisnik (ime, prezime, username, password, id_ovlasti) VALUES
	('Purs', 'Pursić', 'PURS', UNHEX(SHA2('1234', 256)), 1),
	('Ladislav', 'Kovač', 'lkovac', UNHEX(SHA2('1234', 256)), 1),
    ('Valentina', 'Ilić', 'vilic', UNHEX(SHA2('abcd', 256)), 1),
    ('Danko', 'Kovac', 'dkovac', UNHEX(SHA2('ab12', 256)), 2),
    ('Katija', 'Kolar', 'kkolar', UNHEX(SHA2('12ab', 256)), 2),
    ('Ladislav', 'Kovač', 'lkovac', UNHEX(SHA2('1234', 256)), 1),
    ('Valentina', 'Ilić', 'vilic', UNHEX(SHA2('abcd', 256)), 1);
    
CREATE TABLE korisnikove_temperature (
	id_korisnika INT NOT NULL,
    id_temperature INT NOT NULL,
    FOREIGN KEY (id_korisnika) REFERENCES korisnik(id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (id_temperature) REFERENCES temperatura(id) ON UPDATE CASCADE ON DELETE CASCADE,
    PRIMARY KEY (id_korisnika, id_temperature)
);

INSERT INTO korisnikove_temperature (id_korisnika, id_temperature) VALUES
	(1, 1),
	(2, 1),
    (1, 2),
    (2, 2),
    (1, 3);

CREATE TABLE korisnikove_vlage (
	id_korisnika INT NOT NULL,
    id_vlage INT NOT NULL,
    FOREIGN KEY (id_korisnika) REFERENCES korisnik(id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (id_vlage) REFERENCES vlaga(id) ON UPDATE CASCADE ON DELETE CASCADE,
    PRIMARY KEY (id_korisnika, id_vlage)
);

INSERT INTO korisnikove_vlage (id_korisnika, id_vlage) VALUES
	(1, 1),
	(2, 1),
    (1, 2),
    (2, 2),
    (1, 3);
