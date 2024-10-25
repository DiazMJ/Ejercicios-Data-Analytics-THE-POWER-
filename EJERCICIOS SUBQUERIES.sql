--2.1. Hay algún actor o actriz que no apareca en ninguna película en la tabla film_actor.

SELECT CONCAT("a"."first_name",' ', "a"."last_name") AS "actores"
FROM "actor" AS "a"
WHERE "a"."actor_id" NOT IN(SELECT "fa"."actor_id" AS "id_actor" FROM "film_actor" AS "fa")

--2.2. Qué películas se alquilan por encima del precio medio. (Este ejercicio ya lo resolvimos en el segundo reto guiado de SQL)

SELECT "f"."title" as "peliculas",
		"f"."rental_rate" as "coste_alquiler"
FROM  "film" as "f"
WHERE "f"."rental_rate" >
	(SELECT AVG("rental_rate")
	FROM "film")
ORDER BY "coste_alquiler" ASC

--2.3. Encuentra los nombres de las películas que tienen la misma duración que la película con el título "Dancing Fever" Ordena los resultados alfabéticamente por título de película.

SELECT "f"."title" as "peliculas",
		"length" as "duración"
FROM "film" as "f"
WHERE "length" = (SELECT "length" FROM "film" WHERE "title" ILIKE 'DANCING FEVER')
ORDER BY "length"
	
--2.4. Encuentra los nombres de los clientes que han alquilado al menos 7 películas distintas.
--Ordena los resultados alfabéticamente por apellido.
SELECT CONCAT("c"."first_name", ' ', "c"."last_name") AS "Clientes"
FROM "customer" as "c"
WHERE  "c"."customer_id"  IN ( SELECT  "r"."customer_id"-- relacionamos la consulta con la tabla rental atraves del customer_id
	FROM "rental" as "r" 
	GROUP BY "r"."rental_id"-- acuerdate que hy q agrfupar antes de aplicar una cndicion a un grup0o con fx de agregacion
	HAVING COUNT(DISTINCT "r"."inventory_id") >= 7)
ORDER BY "last_name"

--2.5. Encuentra el nombre y apellido de los actores que aparecen en la película con título"Egg Igby".

SELECT CONCAT("a"."first_name", ' ', "a"."last_name") AS "actores"
FROM "actor" as "a"
WHERE  "a"."actor_id" IN(
	SELECT "fa"."actor_id" --relaciono consulta con film actor tabla
	FROM "film_actor" as "fa"
		WHERE "fa"."film_id" IN ( 
			SELECT "f"."film_id"
			FROM "film" as "f"
				WHERE "f"."title" ILIKE 'Egg Igby'))

-- 2.6. Encuentra el título de todas las películas que son de la misma categoría que "Animation".
	
SELECT "f"."title" as "título"
FROM "film" as "f"
WHERE "f"."film_id" IN(-- RELACIONO CON FILM CATEGORY A TRAVES DEL FILM ID
	SELECT "fc"."film_id"
	FROM "film_category" as "fc"
		WHERE "fc"."category_id" IN(
		SELECT "c"."category_id"
		FROM "category" as "c"
			WHERE "c"."name" = 'Animation')
		)

--2.7. Encuentra el título de todas las películas que fueron alquiladas por más de 8 días.

SELECT "f"."title" as "título",
		"f"."rental_duration" 
FROM "film" as "f" 
WHERE "f"."rental_duration" >8 	-- SI VEMOS LOS DATOS NO HAY ALQUILERES SUPERIORES A 7 DIAS

--2.8. Encuentra el nombre y apellido de los actores que no han actuado en ninguna película de la categoría "Music".

SELECT CONCAT("a"."first_name", ' ', "a"."last_name") AS "actores"
FROM "actor" as "a"
WHERE "a"."actor_id" NOT IN(-- NOS SOLICITAN LOS QUE NOOOO HAN ACTUADO POR ESO PONEMOS NOT IN
	SELECT "fa"."film_id"
	FROM "film_actor" as "fa"
	WHERE "fa"."film_id" IN (
		SELECT "fc"."category_id" FROM "film_category" as "fc"
		WHERE "fc"."category_id" IN (
			SELECT "c"."category_id" FROM "category" as "c"
			WHERE "c"."name" = 'Muisc')))
	
		
	

--2.9. Encuentra el título de las películas que han sido alquiladas por el cliente con el nombre "Tammy Sanders" y que aún no se han devuelto. Ordena los resultados alfabéticamente por título de película.

SELECT "f"."title" as "título"
FROM "film" as "f" 
WHERE "f"."film_id" IN(
	SELECT "i"."film_id" FROM "inventory" as "i" -- cogemos I. Film-ID xq es lo que nos relaciona con el f.film_id
	WHERE "i"."inventory_id" IN (
		SELECT "r"."inventory_id"  FROM "rental" as "r"
		WHERE "r"."customer_id" IN (  
			SELECT "customer_id" FROM "customer" as "c"
			 WHERE "c"."first_name" ILIKE 'Tammy' AND  "c"."last_name" ILIKE 'Sanders') 
		AND "r"."return_date" IS NULL )) -- indexamos el AND junto a la consulta que contiene la tabla r
ORDER BY "f"."title"-- indexamos al primcipio porque vamos a ordenar alfabetocamente la primera seleccion		

--2.10. Encuentra los nombres de los actores que han actuado en al menos una película que pertenece a la categoría "Sci-Fi." Ordena los resultados alfabéticamente por apellido.	

SELECT CONCAT("a"."first_name", ' ', "a"."last_name") AS "actores"
FROM "actor" as "a"
WHERE "a"."actor_id" IN(
	SELECT "fa"."actor_id"
	FROM "film_actor" as "fa"
	WHERE "fa"."film_id" IN (
		SELECT "fc"."film_id" FROM "film_category" as "fc"
		WHERE "fc"."category_id" IN (
			SELECT "c"."category_id" FROM "category" as "c"
			WHERE "c"."name" = 'Sci-Fi')))
ORDER BY "a"."last_name"

-- 2.11. Encuentra la cantidad total de películas alquiladas por categoría y muestra el nombre de la categoría junto con el recuento de alquileres.

SELECT  "c"."name" as "categoría",
		COUNT(DISTINCT "fc"."film_id") as "total_pelis_alquiladas"
FROM "category" as "c" 
INNER JOIN "film_category" AS "fc" ON "c"."category_id" = "fc"."category_id" 
WHERE "fc"."film_id" IN ( SELECT "i"."film_id" FROM "inventory" as "i"
		WHERE "i"."inventory_id" IN (SELECT "r"."inventory_id" FROM  "rental" as "r"))
GROUP BY "c"."name"	

-- 2.12. Encuentra el nombre y apellido de los actores que han actuado en películas que se alquilaron después de que la película "Spartacus Cheaper" se alquilara por primera vez.
--Ordena los resultados alfabéticamente por apellido.

SELECT CONCAT("a"."first_name", ' ', "a"."last_name") AS "actores"
FROM "actor" as "a"
WHERE "a"."actor_id" IN (
	SELECT "fa"."actor_id" FROM "film_actor" as "fa"
	WHERE "fa"."film_id" IN(
	SELECT "i"."film_id" FROM "inventory" as "i"
		WHERE  "i"."inventory_id" IN (
		SELECT "r"."inventory_id" FROM "rental" as "r"
		 	WHERE "r"."inventory_id" IN(
			SELECT "i"."inventory_id" FROM "inventory" as "i"
				WHERE "i"."film_id" IN (
				SELECT "f"."film_id" FROM "film" as "f"
					WHERE "f"."title" ILIKE 'Spartacus Cheaper'))
			ORDER BY "r"."rental_date"
			LIMIT 1))) -- LO LIMITO A UNO PORQUE ME PIDEN EL 1 DIA , Y ESTA ORDENADO ALFABETICAMENTE
ORDER BY "a"."last_name"									
				)
			)
		
		)
	)

