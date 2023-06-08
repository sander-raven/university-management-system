SELECT DISTINCT s.full_name, s.id
FROM students AS s
INNER JOIN educational_plans AS ep ON s.group_id = ep.group_id
INNER JOIN courses AS c ON ep.course_id = c.id
WHERE c.name = 'Математика'
ORDER BY 1 ASC;
