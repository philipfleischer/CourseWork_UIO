/*
film: filmid, title, prodyear
filmcharacter: partid, filmcharacter
filmcountry: filmid, country
filmgenre: filmid, genre
filmparticipation: partid, personid, filmid, parttype
filmrating: filmid, votes, distribution, rank
filmlanguage: filmid, langid, language
runningtime: filmid, timeid, time, country
person: personid, firstname, lastname, gender
*/

--Oppgave 1
SELECT p.firstname || ' ' || p.lastname AS skuespiller
FROM person AS p
INNER JOIN filmparticipation AS fp
USING (personid)
INNER JOIN film AS f
USING (filmid)
WHERE f.title = 'Star Wars' AND fp.parttype = 'cast';

--Oppgave 2
SELECT fc.country, count(fc.country) AS antall_filmer
FROM filmcountry AS fc
GROUP BY fc.country
ORDER BY count(fc.country) DESC;

--Oppgave 3
SELECT rt.country, AVG(cast(rt.time AS int)) AS gjennomsnittlig_kjoretid
FROM runningtime AS rt
WHERE rt.time ~ '^\d+$'
GROUP BY rt.country
HAVING  rt.country IS NOT NULL AND count(rt.time) >= 200
ORDER BY rt.country;

--Oppgave 4
SELECT f.title, count(fg.genre)
FROM film AS f
INNER JOIN filmgenre AS fg
USING (filmid)
GROUP BY f.title
HAVING count(fg.genre) > 10
ORDER BY count(fg.genre) DESC
LIMIT 10;

--Oppgave 5
SELECT fc.country,
  (SELECT count(fcc.country)
  FROM filmcountry AS fcc
  WHERE (fc.country = fcc.country)) AS total_filmer,
  (SELECT avg(fr.rank)
  FROM filmrating AS fr
  INNER JOIN filmcountry AS fcc
  USING (filmid)
  WHERE (fcc.country = fc.country)
) AS average_rating,
  (SELECT fg.genre AS sjanger
  FROM filmgenre AS fg
  INNER JOIN filmcountry AS fcc
  USING (filmid)
  WHERE (fcc.country = fc.country)
  GROUP BY fg.genre
  ORDER BY sjanger DESC
  LIMIT 1
  ) AS sjangeren
FROM filmcountry AS fc
GROUP BY fc.country
ORDER BY fc.country;

/*
film: filmid, title, prodyear
filmcharacter: partid, filmcharacter
filmcountry: filmid, country
filmgenre: filmid, genre
filmparticipation: partid, personid, filmid, parttype
filmrating: filmid, votes, distribution, rank
filmlanguage: filmid, langid, language
runningtime: filmid, timeid, time, country
person: personid, firstname, lastname, gender
*/
--Oppgave 6


--Oppgave 7


--Oppgave 8


--Oppgave 9


--Oppgave 10
