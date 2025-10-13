--Oppgave 2a
SELECT navn
  FROM planet
  WHERE stjerne = 'Proxima Centauri';

--Oppgave 2b
SELECT DISTINCT oppdaget, stjerne
  FROM planet
  WHERE (stjerne = 'TRAPPIST-1') OR (stjerne = 'Kepler-154');

--Oppgave 2c
SELECT count(*)
  FROM planet
  WHERE masse IS NULL;

--Oppgave 2d
SELECT navn, avg(masse) AS gjennomsnitt
  FROM planet
  GROUP BY navn
  HAVING avg(masse) > (SELECT avg(masse) FROM planet);

--Oppgave 2e
SELECT max(oppdaget) - min(oppdaget)AS differanse FROM planet;


--Oppgave 3a
SELECT DISTINCT m.molekyl, p.navn, p.masse
  FROM materie AS m, planet AS p
  WHERE (m.molekyl = 'H2O') AND (p.masse > 3) AND (p.masse < 10);

--Oppgave 3b
  SELECT DISTINCT p.navn, s.masse, s.avstand
    FROM planet AS p
    INNER JOIN stjerne AS s
    ON (p.stjerne = s.navn)
    INNER JOIN materie AS m
    ON (m.planet = p.navn)
    WHERE ((s.masse * 12) > s.avstand) AND (m.molekyl = 'H');

--Oppgave 3c
SELECT DISTINCT p.navn
  FROM planet AS p
  INNER JOIN stjerne AS s
  ON (p.stjerne = s.navn)
  WHERE (p.masse > 10) AND (s.avstand < 50);


--Oppgave 4
/*
Grunnen til at Nils sin sql-spørring ikke finner det
han er ute etter og at ingen rader dukker opp, er at
han bruker NATURAL JOIN. NATURAL JOIN legger sammen
to tabeller basert på samme attributt navn og datatype,
men det blir kun lagret en kopi av den samme kolonnen.
På grunn av dette får ikke Nils riktig resultat og
ingen rader utskrevet.
*/


--Oppgave 5a
INSERT INTO stjerne VALUES('Sola', 0, 1);

--Oppgave 5b
INSERT INTO planet VALUES('Jorda', 0.003146, NULL, 'Sola');


--Oppgave 6
CREATE TABLE observasjon(
  observasjons_id int PRIMARY KEY, -- PK
  tidspunkt timestamp,
  planet text REFERENCES planet(navn), --FK -> planet(navn)
  observasjon text
);
