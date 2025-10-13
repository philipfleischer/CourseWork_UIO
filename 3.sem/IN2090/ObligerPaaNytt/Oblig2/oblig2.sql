/*
Stjerne: navn, avstand, masse
Planet: navn, masse, oppdaget, stjerne
Materie: planet, molekyl
*/

--Oppgave 2a
SELECT *
FROM planet AS p
WHERE p.stjerne = 'Proxima Centauri';

--Oppgave 2b
SELECT DISTINCT oppdaget
FROM planet
WHERE stjerne = 'TRAPPIST-1' OR stjerne = 'Kepler-154';

--Oppgave 2c
SELECT *
FROM planet AS p
WHERE p.masse IS NULL;

--Oppgave 2d
SELECT p.navn, p.oppdaget
FROM planet AS p
WHERE p.oppdaget = 2020 AND masse > (
  SELECT avg(masse) FROM planet
);

--Oppgave 2e
SELECT (MAX(p.oppdaget) - MIN(p.oppdaget)) AS differanse
FROM planet AS p;

--Oppgave 3a
SELECT *
FROM planet AS p
INNER JOIN materie AS m
ON (p.navn = m.planet)
WHERE p.masse > 3 AND p.masse < 10 AND m.molekyl = 'H2O';

--Oppgave 3b
SELECT p.navn, p.stjerne, m.molekyl
FROM stjerne AS s
INNER JOIN planet AS p
ON (p.stjerne = s.navn)
INNER JOIN materie AS m
ON (p.navn = m.planet)
WHERE (s.avstand < (s.masse * 12)) AND m.molekyl LIKE '%H%';

--Oppgave 3c
SELECT count(*)
FROM planet AS p
INNER JOIN planet AS p2
ON (p.stjerne = p2.stjerne)
INNER JOIN stjerne AS s
ON (p.stjerne = s.navn)
WHERE p.masse > 10 AND p2.masse > 10 AND s.avstand > 50;

--Oppgave 4
/*
Under er sql-spørringen som Nils har laget:
SELECT oppdaget
FROM planet
NATURAL JOIN stjerne
WHERE avstand > 8000;

Under er en sql-spørring som fungerer for Nils sitt formål:
SELECT p.navn, p.oppdaget, s.avstand
FROM planet AS p
NATURAL JOIN stjerne AS s
ON (p.stjerne = s.navn)
WHERE s.avstand > 8000;

Grunnen til at det ikke fungerer er at Nils bruker NATURAL JOIN.
Ved å bruke INNER JOIN og "joine" dem på stjernens navn, så vil sql spørringen fungere.
*/

--Oppgave 5a
INSERT INTO stjerne (navn, avstand, masse)
VALUES ('Sola', 0, 1);

--Oppgave 5b
INSERT INTO planet (navn, masse, oppdaget, stjerne)
VALUES ('Jorda', 0.003146, NULL, 'Sola');

--Oppgave 6
CREATE TABLE observasjon (
  observasjons_id int NOT NULL PRIMARY KEY,
  observasjon text,
  tidspunkt timestamp NOT NULL,
  planet text NOT NULL,
  FOREIGN KEY (planet) REFERENCES planet(navn)
);
