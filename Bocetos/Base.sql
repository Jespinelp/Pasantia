
CREATE SEQUENCE public.doc_temp_id_doc_temp_seq_1;

CREATE TABLE public.Doc_temp (
                ID_doc_temp NUMERIC(100) NOT NULL DEFAULT nextval('public.doc_temp_id_doc_temp_seq_1'),
                Codigo VARCHAR(100) NOT NULL,
                CONSTRAINT doc_temp_pk PRIMARY KEY (ID_doc_temp)
);


ALTER SEQUENCE public.doc_temp_id_doc_temp_seq_1 OWNED BY public.Doc_temp.ID_doc_temp;

CREATE SEQUENCE public.usuarios_id_usuario_seq_1;

CREATE TABLE public.Usuarios (
                ID_usuario NUMERIC(1) NOT NULL DEFAULT nextval('public.usuarios_id_usuario_seq_1'),
                Nombres VARCHAR(100) NOT NULL,
                Apellidos VARCHAR(100) NOT NULL,
                Usuario VARCHAR(100) NOT NULL,
                Rol VARCHAR(10) NOT NULL,
                Contrasenia VARCHAR(20) NOT NULL,
                CONSTRAINT usuarios_pk PRIMARY KEY (ID_usuario)
);


ALTER SEQUENCE public.usuarios_id_usuario_seq_1 OWNED BY public.Usuarios.ID_usuario;

CREATE SEQUENCE public.documentos_id_documentos_seq;

CREATE TABLE public.Documentos (
                ID_documentos NUMERIC(100) NOT NULL DEFAULT nextval('public.documentos_id_documentos_seq'),
                ID_doc_temp NUMERIC(100) NOT NULL,
                ID_usuario NUMERIC(1) NOT NULL,
                Mantis VARCHAR NOT NULL,
                CONSTRAINT documentos_pk PRIMARY KEY (ID_documentos)
);


ALTER SEQUENCE public.documentos_id_documentos_seq OWNED BY public.Documentos.ID_documentos;

ALTER TABLE public.Documentos ADD CONSTRAINT doc_temp_documentos_fk
FOREIGN KEY (ID_doc_temp)
REFERENCES public.Doc_temp (ID_doc_temp)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.Documentos ADD CONSTRAINT usuarios_documentos_fk
FOREIGN KEY (ID_usuario)
REFERENCES public.Usuarios (ID_usuario)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;
