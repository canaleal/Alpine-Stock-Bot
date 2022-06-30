CREATE TABLE IF NOT EXISTS pageinfo
(
    page_id serial,
    page_name character varying(50) COLLATE pg_catalog."default" NOT NULL,
    page_code character varying(10) COLLATE pg_catalog."default" NOT NULL,
    description character varying(50) COLLATE pg_catalog."default" NOT NULL,
    created_by integer NOT NULL,
    created_on date NOT NULL,
    updated_by integer NULL,
    updated_on date NULL,
    CONSTRAINT pageinfo_pkey PRIMARY KEY (page_id),
    CONSTRAINT fk_created_by FOREIGN KEY (created_by)
        REFERENCES public.users (id) MATCH SIMPLE,
    CONSTRAINT fk_updated_by FOREIGN KEY (updated_by)
        REFERENCES public.users (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);

CREATE TABLE pageinfoelement(
    page_element_id serial,
    page_id integer NOT NULL,
    element_code char(1) NOT NULL,
    description text NULL,
    created_by integer NOT NULL,
    created_on date NOT NULL,
    updated_by integer NULL,
    updated_on date NULL,
    CONSTRAINT pageinfoelement_pkey PRIMARY KEY (page_id),
    CONSTRAINT fk_page_id FOREIGN KEY (page_id)
        REFERENCES public.pageinfo (page_id) MATCH SIMPLE,
    CONSTRAINT fk_created_by FOREIGN KEY (created_by)
        REFERENCES public.users (id) MATCH SIMPLE,
    CONSTRAINT fk_updated_by FOREIGN KEY (updated_by)
        REFERENCES public.users (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);
