/*
Navn på alle planeter som går i bane rundt stjernen med navn Proxima
Centauri.
*/
/*

*/
--Oppgave 2a
SELECT navn
  FROM planet
  WHERE stjerne = 'Proxima Centauri';

/*
Hvilke årstall (uten duplikater) det ble oppdaget planeter i bane rundt
stjernene med navn TRAPPIST-1 og Kepler-154.
*/
--Oppgave 2b
SELECT DISTINCT oppdaget, stjerne
  FROM planet
  WHERE (stjerne = 'TRAPPIST-1') OR (stjerne = 'Kepler-154');

/*
Antall planeter det er som ikke har oppgitt en masse (altså hvor masse
er NULL).
*/
--Oppgave 2c
SELECT count(*)
  FROM planet
  WHERE masse IS NULL;

/*
Navn og masse på alle planeter oppdaget i 2020 med masse høyere enn
gjennomsnittet av massen til alle planeter.
*/
--Oppgave 2d
SELECT navn, avg(masse) AS gjennomsnitt
  FROM planet
  GROUP BY navn
  HAVING avg(masse) > (SELECT avg(masse) FROM planet);

/*
Antall år mellom første og siste oppdagede planet i planet-tabellen.
*/
--Oppgave 2e
SELECT max(oppdaget) - min(oppdaget)AS differanse FROM planet;

/*
at de må komme fra en planet med masse mellom 3 og 10. Videre vet de at
romvesnene inneholder vann (altså H2O), så planeten må inneholde dette molekylet.
Skriv derfor en spørring som finner navn på alle planeter som passer denne informasjonen.
*/
--Oppgave 3a
SELECT DISTINCT m.molekyl, p.navn, p.masse
  FROM materie AS m, planet AS p
  WHERE (m.molekyl = 'H2O') AND (p.masse > 3) AND (p.masse < 10);

/*
romskipet høyst kan ha reist en avstand lik stjernens masse ganger 12,
altså må planeten gå i bane rundt en stjerne som har en avstand mindre enn
12 ganger dens masse. Motoren bruker hydrogen som drivstoff, så planeten de reiser fra
må ha molekyler som inneholder hydrogen (altså molekyler som inneholder bokstaven ’H’).
Skriv derfor en SQL- spørring som finner navn på planeter som passer informasjonen over.
*/
--Oppgave 3b
  SELECT DISTINCT p.navn, s.masse, s.avstand
    FROM planet AS p
    INNER JOIN stjerne AS s
    ON (p.stjerne = s.navn)
    INNER JOIN materie AS m
    ON (m.planet = p.navn)
    WHERE ((s.masse * 12) > s.avstand) AND (m.molekyl = 'H');

/*
Et alternativ til å bruke en massiv stjerne er å bruke to massive planeter for
akselerasjon. Romvesnene kan ha reist fra en av to planeter fra samme solsystem,
begge med masse større enn 10, gitt at avstanden til deres solsystem er mindre enn 50.
Skriv en SQL-spørring som finner navn på alle planeter som passer med informasjonen over.
*/
--Oppgave 3c
SELECT DISTINCT p.navn
  FROM planet AS p
  INNER JOIN stjerne AS s
  ON (p.stjerne = s.navn)
  WHERE (p.masse > 10) AND (s.avstand < 50);


/*
Nils, en av de ansatte på HUFF, ble svært imponert over hva du får til med SQL,
og forsøkte seg derfor på å skrive en spørring selv. Nils ønsket å finne ut når
planeter som går i bane rundt en stjerne med avstand større enn 8000 ble oppdaget,
og skrev derfor denne spørringen:
    SELECT oppdaget
    FROM planet NATURAL JOIN stjerne
    WHERE avstand > 8000;
Forklar Nils hvorfor spørringen hans ikke finner det
han er ute etter og hvorfor den ikke gir noen rader i resultatet.
*/
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


/*
Setter inn Sola i stjerne-tabellen, med navn lik Sola, avstand lik 0 og masse lik 1.
*/
--Oppgave 5a
INSERT INTO stjerne VALUES('Sola', 0, 1);

/*
Setter inn Jorda i planet-tabellen, med navn lik Jorda, masse lik 0.003146,
oppdaget lik NULL, og stjerne lik Sola.
*/
--Oppgave 5b
INSERT INTO planet VALUES('Jorda', 0.003146, NULL, 'Sola');

/*

*/
--Oppgave 6
CREATE TABLE observasjon(
  observasjons_id int PRIMARY KEY, -- PK
  tidspunkt timestamp,
  planet text REFERENCES planet(navn), --FK -> planet(navn)
  observasjon text
);
