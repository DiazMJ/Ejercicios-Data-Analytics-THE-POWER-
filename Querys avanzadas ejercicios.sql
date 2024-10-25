--2.1. Ordena las películas por duración de forma ascendente

SELECT "f"."title" AS "películas",
		"f"."length" AS "duración"
FROM "film" as "f"
ORDER BY "f"."length" ASC

--2.2. Muestra los 10 clientes con mayor valor de id

SELECT CONCAT("c"."first_name", ' ' ,"c"."last_name") AS " cliente",
		"c"."customer_id" AS "id"
FROM "customer" AS "c"
ORDER BY "c"."customer_id" DESC
LIMIT 10

--2.3. Encuentra lo que costó el antepenúltimo alquiler ordenado por día.

SELECT  "p"."amount" AS "coste"
FROM "payment"	AS "p"
ORDER BY  "p"."payment_date" DESC
LIMIT 1 -- para mostrar un unico valor
OFFSET 2 --para indicar numero de filas a omitir el resutado
	
--2.4. Qué películas se alquilan por encima del precio medio. 
--Para este ejercicio tendrás que generar dos queries diferentes. 
--Una primera para calcular la media y la segunda para obtener las películas que se alquilan 
--por encima de ese valor.

SELECT  ROUND(AVG("f"."rental_rate"),0) AS "media_gasto_alquiler"
FROM "film" AS "f"

SELECT "f"."title" AS "películas",
		"f"."rental_rate" AS "media_gasto_alquiler"
FROM "film" AS "f"
WHERE "f"."rental_rate" > 3

--2.5. Encuentra la cantidad total de películas en cada clasificación de la tabla film y muestra la clasificación junto con el recuento.

SELECT COUNT(DISTINCT("f"."film_id"))AS "cantidad_pleículas",
		"f"."rating"
FROM "film" AS "f"
GROUP BY "f"."rating"

--2.6. Encuentra el promedio de duración de las películas para cada clasificación de la tabla film y muestra la clasificación junto con el promedio de duración.

SELECT "f"."rating"	AS "Clasificaciones",
	ROUND(AVG("f"."length"),0) AS "Duración"
FROM "film" AS "f"
GROUP BY "f"."rating"
ORDER BY "Duración"

--2.7. Números de alquiler por día. Ordenados por cantidad de alquiler de forma descendente.

SELECT COUNT("r"."rental_id") AS "alquileres",
	DATE ("r"."rental_date") AS "día"
FROM "rental" AS "r"
GROUP BY "día"
ORDER BY "alquileres" DESC

--2.8. Averigua el número de alquileres registrados por mes.

SELECT  COUNT("r"."rental_id") AS "alquileres",
	EXTRACT( MONTH FROM "r"."rental_date") AS "mes"  
FROM "rental" AS "r"
GROUP BY "mes"
ORDER BY "mes"

--2.9. Número de películas por categoría estrenadas en 2006

SELECT COUNT("film_id") as "numero_peliculas",
	"rating" as "categoría"
FROM "film" as "f"
WHERE "release_year" = 2006 -- usamos WHERE porque ews una condicion de los datos y no de la agrupación, por ello tb el group by va debajo,
GROUP BY "rating"
ORDER  BY "numero_peliculas"


--2.10. Muestra el id de los actores que hayan participado en más de 40 películas.

SELECT "actor_id",
	COUNT(DISTINCT "film_id")
FROM  "film_actor"
GROUP BY "actor_id"
HAVING COUNT ("film_id") >40


