CREATE OR REPLACE FUNCTION table_notify() RETURNS trigger AS $$
DECLARE
  id bigint;
  payload text;
  json_record JSON;
  payload_size INT;
BEGIN
  IF TG_OP = 'INSERT' THEN
    id = NEW.id;
    json_record = row_to_json(NEW);
  ELSE
    id = OLD.id;
  END IF;
  payload = json_build_object('table_name', TG_TABLE_SCHEMA || '.' || TG_TABLE_NAME, 'id', id, 'type', TG_OP, 'row', json_record)::text;
  payload_size = octet_length(payload);
  IF payload_size >= 8000 THEN
    payload = json_build_object('table_name', TG_TABLE_SCHEMA || '.' || TG_TABLE_NAME, 'id', id, 'type', TG_OP)::text;
  END IF;
  PERFORM pg_notify('notification_update', payload);
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;