SELECT * FROM temperatura;
SELECT * FROM temperatura ORDER BY id DESC LIMIT 1;

SELECT ime, prezime, naziv AS naziv_ovlasti FROM korisnik
INNER JOIN ovlasti ON korisnik.id_ovlasti = ovlasti.id;

SELECT * FROM korisnik WHERE username = 'kkolar' AND password = '12ab';

SELECT ime, prezime, vrijednost AS vrijednost_temprature FROM korisnikove_temperature
LEFT JOIN korisnik ON korisnikove_temperature.id_korisnika = korisnik.id
LEFT JOIN temperatura ON korisnikove_temperature.id_temperature = temperatura.id
WHERE korisnik.id = 1;


SELECT * FROM mysql.user;