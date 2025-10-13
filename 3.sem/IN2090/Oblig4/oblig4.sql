/*
Skriv derfor en spørring som finner navn på alle skuespillere og rollen
de spiller i filmen med tittelen 'Star Wars'. (108 rader)
*/

--Oppgave 1)
SELECT p.firstname, p.lastname, k.filmcharacter, f.title
FROM filmparticipation AS fp
JOIN film AS f
ON (fp.filmid = f.filmid)
JOIN person AS p
ON (fp.personid = p.personid)
JOIN filmcharacter AS k
ON (fp.partid = k.partid)
WHERE (fp.parttype = 'cast') AND (f.title = 'Star Wars');


/*
Skriv derfor en spørring som finner antall filmer som er laget i hver
land. Sorter resultatet fra høyest til lavest antall. (190 rader)
*/
--Oppgave 2)
SELECT fc.country, count(fc.country) AS antall_filmer
FROM filmcountry AS fc
GROUP BY fc.country
ORDER BY antall_filmer DESC;


/*
Skriv en spørring som finner gjennomsnittlig kjøretid for filmer per
land (hvor country ikke er NULL), men hvor vi kun ønsker å ta med de
landene hvor vi har minst 200 kjøretider (i minutter som beskrevet over).
(44 rader)
*/
--Oppgave 3)
SELECT rt.country, avg(cast(rt.time AS int))
FROM runningtime AS rt
WHERE (rt.time ~ '^\d+$')
GROUP BY rt.country
HAVING count(rt.time) >= 200 AND (rt.country IS NOT NULL);



/*
Så skriv en SQL-spørring som finner de 10 kinofilmene med flest sjan- gre.
Dersom det er filmer med like mange sjangre, velg dem som kommer alfabetisk
først. (10 rader)
*/
--Oppgave 4
WITH ant_sjangere AS (
  SELECT f.title, count(fg.genre) AS antall_sjangre
  FROM filmgenre AS fg
  INNER JOIN film AS f
  USING (filmid)
  GROUP BY f.title
  ORDER BY count(fg.genre) DESC
)
SELECT *
FROM ant_sjangere
LIMIT 10;

/*
Skriv en spørring som for hvert land finner totalt antall filmer laget
i det landet, gjennomsnittlig rating for disse filmene,
og sjangeren som er vanligst for landets filmer. (190 eller 172 rader)
*/
--Oppgave 5
SELECT fc.country,
  (SELECT count(fcc.filmid)
  FROM filmcountry AS fcc
  WHERE (fc.country = fcc.country)
) AS ant_filmer,
  (SELECT avg(fr.rank)
  FROM filmrating AS fr
  INNER JOIN filmcountry AS fccf
  USING (filmid)
  WHERE (fccf.country = fc.country)
) AS avg_rating,
  (SELECT fg.genre AS vanligste_sjangeren
  FROM filmgenre AS fg
  INNER JOIN filmcountry AS fccff
  USING (filmid)
  WHERE (fccff.country = fc.country)
  GROUP BY fg.genre
  ORDER BY vanligste_sjangeren DESC
  LIMIT 1
) AS favoritt_sjanger
FROM filmcountry AS fc
GROUP BY fc.country
ORDER BY fc.country;


/*
Skriv derfor en SQL-spørring som finner navnene (fornavn og etternavn) på
alle par av personer som har jobber i mer enn 40 norske
kinofilmer sam- men. Merk: Hvert par skal bare forekomme én gang
i resultatet. (2 rader)
*/
--Oppgave 6)
WITH filmer AS (
  SELECT concat (p.firstname, ' ', p.lastname) AS navnet, f.filmid --filmid
  FROM film as f
  INNER JOIN filmcountry AS fc
  USING (filmid)
  INNER JOIN filmitem AS fi
  USING (filmid)
  INNER JOIN filmparticipation AS fp
  USING (filmid)
  INNER JOIN person AS p
  USING (personid)
  WHERE (fc.country = 'Norway') AND (fi.filmtype = 'C')
)
SELECT DISTINCT f1.navnet AS skuespiller_1, f2.navnet AS skuespiller_2, count(*) AS ant_filmer
FROM filmer AS f1
INNER JOIN filmer AS f2
ON (f1.filmid = f2.filmid) AND (f1.navnet > f2.navnet) AND (f1.navnet != f2.navnet)
GROUP BY f1.navnet, f2.navnet
HAVING (count(*) >= 40)
ORDER BY ant_filmer DESC;


/*
Skriv derfor en spørring som finner navn og produksjonsår på alle
filmer som har en tittel som inneholder minst ett av ordene 'Dark' og 'Night',
og som er grøsser (har sjanger horror) eller er fra
Romaina (eller evt. begge). Resultatet skal ikke inneholde duplikater. (457 rader)
*/
--Oppgave 7)
SELECT f.title, f.prodyear, fg.genre, fc.country
FROM film AS f
INNER JOIN filmgenre AS fg
USING (filmid)
INNER JOIN filmcountry AS fc
USING (filmid)
WHERE (f.title LIKE '%Dark%' OR f.title LIKE '%Night%') AND (fg.genre = 'Horror' OR fc.country = 'Romania');


/*
Skriv derfor en spørring som finner tittel og antall deltakere til alle
filmer laget i 2010 eller senere, og som kun har 2 eller
færre deltakere (i henhold til filmparticipation-tabellen, uansett rolle).
(28 rader).
*/
--Oppgave 8)
SELECT f.title, f.prodyear, count(fp.personid) AS antall
FROM film AS f
LEFT JOIN filmparticipation AS fp
USING (filmid)
WHERE (f.prodyear >= 2010)
GROUP BY f.title, f.prodyear
HAVING count(fp.personid) < 3;


/*
Skriv derfor en spørring som finner antall
filmer som hverken har sjanger 'Sci-Fi' eller 'Horror'. (1 rad)
*/
--Oppgave 9)
SELECT count(*) AS ant_filmer
FROM film AS f
INNER JOIN filmgenre AS fg
USING (filmid)
WHERE (NOT fg.genre = 'Sci-Fi') AND (NOT fg.genre = 'Horror');


/*
• De 10 som har høyest rank og votes (altså om de har lik rank,
  så velg de som har høyest votes).
• De filmene som Harrison Ford er skuespiller i.
• De filmene som har sjanger 'Comedy' eller 'Romance'.
Du får derfor i oppgave å lage en spørring som finner tittel og
antall språk det snakkes i filmen (også dersom det ikke snakkes noen språk)
for de utvalgte filmene beskrevet over. (170 rader)

*/
--Oppgave 10)
WITH tabell1 AS (
  SELECT filmid, fr.rank, fr.votes
  FROM filmrating AS fr
  JOIN filmitem AS fi USING (filmid)
  WHERE fr.rank >= 8 AND fr.votes >= 1000 AND fi.filmtype = 'C'
),
utvalg AS (
  (
    SELECT i.filmid
    FROM tabell1 AS i
    ORDER BY i.rank DESC, i.votes DESC
    LIMIT 10
  )
  UNION
  (
    SELECT filmid
    FROM tabell1 AS i
    JOIN filmgenre USING (filmid)
    WHERE (genre = 'Romance') OR (genre = 'Comedy')
  )
),
tale AS (
  SELECT count(fl.language) AS spraak, filmid
  FROM utvalg
  LEFT OUTER JOIN filmlanguage AS fl USING (filmid)
  GROUP BY filmid
)
SELECT f.title AS tittel, t.spraak AS språk
FROM tale AS t
JOIN film AS f
USING (filmid);
