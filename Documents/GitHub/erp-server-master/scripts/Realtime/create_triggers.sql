DROP TRIGGER IF EXISTS notification_insert ON notifications;
CREATE TRIGGER notification_insert
AFTER INSERT ON notifications
FOR EACH ROW EXECUTE PROCEDURE table_notify();