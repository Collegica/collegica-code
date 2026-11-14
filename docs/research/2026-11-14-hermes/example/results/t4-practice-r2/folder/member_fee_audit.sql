.mode csv
CREATE TABLE members (name TEXT, email TEXT, plot TEXT, joined TEXT, fee_paid_cad TEXT, note TEXT);
.import --csv --skip 1 members.csv members
.headers on
SELECT 'raw_rows' AS measure, COUNT(*) AS value FROM members;
SELECT 'normalized_unique_member_identities' AS measure, COUNT(*) AS value FROM (SELECT lower(trim(email)), lower(trim(name)), trim(plot) FROM members GROUP BY 1,2,3);
SELECT 'Bram duplicate records' AS finding, group_concat(rowid || ': ' || quote(name) || ' / ' || quote(email) || ' / fee ' || fee_paid_cad, ' | ') AS detail FROM members WHERE lower(trim(email)) = 'bram.lindqvist@example.com';
SELECT 'blank fee' AS finding, rowid || ': ' || name || ' — treated as $0 (unpaid)' AS detail FROM members WHERE trim(fee_paid_cad) = '';
SELECT 'refund / missing joined date' AS finding, rowid || ': ' || name || ' — ' || fee_paid_cad || '; ' || note AS detail FROM members WHERE CAST(fee_paid_cad AS REAL) < 0;
SELECT 'whole-dollar format' AS finding, rowid || ': ' || name || ' — ' || fee_paid_cad || '; parsed as $45.00' AS detail FROM members WHERE trim(fee_paid_cad) <> '' AND instr(fee_paid_cad, '.') = 0;
SELECT 'half-season fee' AS finding, rowid || ': ' || name || ' — ' || fee_paid_cad || COALESCE('; ' || nullif(note,''), '') AS detail FROM members WHERE fee_paid_cad = '22.50';
WITH dedup AS (
 SELECT *, ROW_NUMBER() OVER (PARTITION BY lower(trim(name)),lower(trim(email)),trim(plot),trim(joined),trim(fee_paid_cad),lower(trim(note)) ORDER BY rowid) AS copy_number FROM members
)
SELECT '2026 member rows / fee total' AS measure, COUNT(*) || ' / ' || printf('$%.2f', SUM(CAST(COALESCE(NULLIF(trim(fee_paid_cad),''),'0') AS REAL))) AS value FROM dedup WHERE copy_number=1 AND joined LIKE '2026-%';
WITH dedup AS (
 SELECT rowid AS source_line, *, ROW_NUMBER() OVER (PARTITION BY lower(trim(name)),lower(trim(email)),trim(plot),trim(joined),trim(fee_paid_cad),lower(trim(note)) ORDER BY rowid) AS copy_number FROM members
)
SELECT source_line, name, joined, printf('$%.2f', CAST(fee_paid_cad AS REAL)) AS fee_used FROM dedup WHERE copy_number=1 AND joined LIKE '2026-%';
WITH dedup AS (
 SELECT *, ROW_NUMBER() OVER (PARTITION BY lower(trim(name)),lower(trim(email)),trim(plot),trim(joined),trim(fee_paid_cad),lower(trim(note)) ORDER BY rowid) AS copy_number FROM members
)
SELECT 'all-record net after duplicate removal' AS measure, printf('$%.2f',SUM(CAST(COALESCE(NULLIF(trim(fee_paid_cad),''),'0') AS REAL))) AS value FROM dedup WHERE copy_number=1;
