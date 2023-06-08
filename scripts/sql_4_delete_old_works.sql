DELETE FROM selfstudy_works
WHERE protection_date < current_date - interval '1 year';
