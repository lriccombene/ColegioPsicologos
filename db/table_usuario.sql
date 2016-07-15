-- Table: usuario

-- DROP TABLE usuario;

CREATE TABLE usuario
(
  id integer,
  nombre character varying,
  active bit(1),
  password character varying,
  create_uid integer,
  email character varying,
  write_date date
)
WITH (
  OIDS=FALSE
);
ALTER TABLE usuario
  OWNER TO postgres;
