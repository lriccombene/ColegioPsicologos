-- Table: party_party

-- DROP TABLE party_party;

CREATE TABLE party_party
(
  id integer NOT NULL,
  code character varying, -- Code
  create_date timestamp(6) without time zone, -- Create Date
  write_uid integer,
  write_date timestamp(6) without time zone,
  active boolean, -- Active
  nombre character varying(100), -- Nombre
  apellido character varying, -- Apellido
  tipo_doc character varying(50),
  nro_doc character varying(100), -- Cuit Cuil
  CONSTRAINT party_party_pkey PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE party_party
  OWNER TO postgres;
COMMENT ON COLUMN party_party.code IS 'Code';
COMMENT ON COLUMN party_party.create_date IS 'Create Date';
COMMENT ON COLUMN party_party.active IS 'Active';
COMMENT ON COLUMN party_party.nombre IS 'Nombre';
COMMENT ON COLUMN party_party.apellido IS 'Apellido';
COMMENT ON COLUMN party_party.nro_doc IS 'Cuit Cuil';

