BEGIN;

COPY zip_codes FROM '/path/to/csv/ZIP_CODES.txt' WITH (FORMAT csv);

COMMIT;