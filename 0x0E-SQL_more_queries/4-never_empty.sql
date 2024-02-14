--  creates the table id_not_null on your MySQL server.
CREATE TABLEIF NOT EXISTS `id_not_null` (
    id INT(11) NOT NULL DEFAULT 1,
    name VARCHAR(256)
);
