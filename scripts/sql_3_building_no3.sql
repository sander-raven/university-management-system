SELECT DISTINCT t.full_name, t.id
FROM teachers AS t
INNER JOIN schedules AS s ON t.id = s.teacher_id
INNER JOIN audiences AS a ON s.audience_id = a.id
INNER JOIN buildings AS b ON a.building_id = b.id
WHERE b.info = 'Здание №3'
ORDER BY 1 ASC;
