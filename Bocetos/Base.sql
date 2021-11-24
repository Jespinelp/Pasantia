
CREATE SEQUENCE public.tipos_id_tipo_seq;

CREATE TABLE public.tipos (
                id_tipo NUMERIC(100) NOT NULL DEFAULT nextval('public.tipos_id_tipo_seq'),
                tipo_rev VARCHAR NOT NULL,
                tipo_estandar VARCHAR NOT NULL,
                tipo_rel VARCHAR NOT NULL,
                CONSTRAINT tipos_pk PRIMARY KEY (id_tipo)
);


ALTER SEQUENCE public.tipos_id_tipo_seq OWNED BY public.tipos.id_tipo;

CREATE TABLE public.revision (
                id_rev NUMERIC(100) NOT NULL,
                estado VARCHAR NOT NULL,
                fecha DATE NOT NULL,
                mantis VARCHAR NOT NULL,
                anexos VARCHAR NOT NULL,
                observaciones_generales VARCHAR,
                CONSTRAINT revision_pk PRIMARY KEY (id_rev)
);


CREATE SEQUENCE public.detalle_cumplimiento_id_detalle_seq;

CREATE TABLE public.detalle_cumplimiento (
                id_detalle NUMERIC(100) NOT NULL DEFAULT nextval('public.detalle_cumplimiento_id_detalle_seq'),
                id_tipo NUMERIC(100) NOT NULL,
                fecha_registro DATE NOT NULL,
                tipo_revision BOOLEAN NOT NULL,
                descripcion VARCHAR NOT NULL,
                observaciones VARCHAR NOT NULL,
                tipo_estandar BOOLEAN NOT NULL,
                resultado VARCHAR NOT NULL,
                id_rev NUMERIC(100) NOT NULL,
                CONSTRAINT detalle_cumplimiento_pk PRIMARY KEY (id_detalle)
);


ALTER SEQUENCE public.detalle_cumplimiento_id_detalle_seq OWNED BY public.detalle_cumplimiento.id_detalle;

CREATE SEQUENCE public.persona_id_usuario_seq;

CREATE TABLE public.persona (
                id_usuario NUMERIC(1) NOT NULL DEFAULT nextval('public.persona_id_usuario_seq'),
                nombres VARCHAR(100) NOT NULL,
                apellidos VARCHAR(100) NOT NULL,
                usuario VARCHAR(100) NOT NULL,
                rol VARCHAR(10) NOT NULL,
                contrasenia VARCHAR(20) NOT NULL,
                CONSTRAINT persona_pk PRIMARY KEY (id_usuario)
);


ALTER SEQUENCE public.persona_id_usuario_seq OWNED BY public.persona.id_usuario;

CREATE TABLE public.rev_persona (
                id_tipo NUMERIC(100) NOT NULL,
                id_usuario NUMERIC(1) NOT NULL,
                id_rev NUMERIC(100) NOT NULL,
                Tipo_relacionperrev VARCHAR NOT NULL
);


ALTER TABLE public.detalle_cumplimiento ADD CONSTRAINT tipos_detalle_cumplimiento_fk
FOREIGN KEY (id_tipo)
REFERENCES public.tipos (id_tipo)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.rev_persona ADD CONSTRAINT tipos_rev_persona_fk
FOREIGN KEY (id_tipo)
REFERENCES public.tipos (id_tipo)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.rev_persona ADD CONSTRAINT revision_rev_persona_fk
FOREIGN KEY (id_rev)
REFERENCES public.revision (id_rev)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.detalle_cumplimiento ADD CONSTRAINT revision_detalle_cumplimiento_fk
FOREIGN KEY (id_rev)
REFERENCES public.revision (id_rev)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.rev_persona ADD CONSTRAINT persona_rev_persona_fk
FOREIGN KEY (id_usuario)
REFERENCES public.persona (id_usuario)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;
