-- list only tv shows without genre id
SELECT title, genre_id
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
WHERE genre_id is NULL
ORDER BY title, genre_id ASC;
