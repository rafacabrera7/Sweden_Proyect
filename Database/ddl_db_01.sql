-- Database generated with pgModeler (PostgreSQL Database Modeler).
-- pgModeler  version: 0.9.2
-- PostgreSQL version: 12.0
-- Project Site: pgmodeler.io
-- Model Author: ---


-- Database creation must be done outside a multicommand file.
-- These commands were put in this file only as a convenience.
-- -- object: new_database | type: DATABASE --
-- -- DROP DATABASE IF EXISTS new_database;
-- CREATE DATABASE new_database;
-- -- ddl-end --
-- 

-- object: public.job_offer | type: TABLE --
-- DROP TABLE IF EXISTS public.job_offer CASCADE;
CREATE TABLE public.job_offer (
	id_job integer NOT NULL,
	name_job varchar(60) NOT NULL,
	description_job varchar(100),
	email_job varchar(50) NOT NULL,
	id_company_company integer NOT NULL,
	date_accesed date,
	url_job varchar(70),
	id_city_city smallint,
	id_sector_main_sector integer,
	id_subcategory_subcategory integer,
	CONSTRAINT job_offer_pk PRIMARY KEY (id_job)

);
-- ddl-end --
-- ALTER TABLE public.job_offer OWNER TO postgres;
-- ddl-end --

-- object: public.company | type: TABLE --
-- DROP TABLE IF EXISTS public.company CASCADE;
CREATE TABLE public.company (
	id_company integer NOT NULL GENERATED ALWAYS AS IDENTITY ,
	name_company varchar(80) NOT NULL,
	CONSTRAINT company_pk PRIMARY KEY (id_company)

);
-- ddl-end --
-- ALTER TABLE public.company OWNER TO postgres;
-- ddl-end --

-- object: public.main_sector | type: TABLE --
-- DROP TABLE IF EXISTS public.main_sector CASCADE;
CREATE TABLE public.main_sector (
	id_sector integer NOT NULL GENERATED ALWAYS AS IDENTITY ,
	name_sector varchar(50) NOT NULL,
	CONSTRAINT sector_pk PRIMARY KEY (id_sector)

);
-- ddl-end --
-- ALTER TABLE public.main_sector OWNER TO postgres;
-- ddl-end --

-- object: company_fk | type: CONSTRAINT --
-- ALTER TABLE public.job_offer DROP CONSTRAINT IF EXISTS company_fk CASCADE;
ALTER TABLE public.job_offer ADD CONSTRAINT company_fk FOREIGN KEY (id_company_company)
REFERENCES public.company (id_company) MATCH FULL
ON DELETE RESTRICT ON UPDATE CASCADE;
-- ddl-end --

-- object: main_sector_fk | type: CONSTRAINT --
-- ALTER TABLE public.job_offer DROP CONSTRAINT IF EXISTS main_sector_fk CASCADE;
ALTER TABLE public.job_offer ADD CONSTRAINT main_sector_fk FOREIGN KEY (id_sector_main_sector)
REFERENCES public.main_sector (id_sector) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: public.customer | type: TABLE --
-- DROP TABLE IF EXISTS public.customer CASCADE;
CREATE TABLE public.customer (
	id_customer integer NOT NULL GENERATED ALWAYS AS IDENTITY ,
	name_customer varchar(50) NOT NULL,
	customer_email varchar(50) NOT NULL,
	password_customer varchar(20) NOT NULL,
	CONSTRAINT customer_pk PRIMARY KEY (id_customer)

);
-- ddl-end --
-- ALTER TABLE public.customer OWNER TO postgres;
-- ddl-end --

-- object: public.body_message | type: TABLE --
-- DROP TABLE IF EXISTS public.body_message CASCADE;
CREATE TABLE public.body_message (
	id_customer_customer integer NOT NULL,
	body_id integer NOT NULL,
	body_message varchar(2000),
	CONSTRAINT body_message_pk PRIMARY KEY (body_id,id_customer_customer)

);
-- ddl-end --
-- ALTER TABLE public.body_message OWNER TO postgres;
-- ddl-end --

-- object: public.city | type: TABLE --
-- DROP TABLE IF EXISTS public.city CASCADE;
CREATE TABLE public.city (
	id_city smallint NOT NULL GENERATED ALWAYS AS IDENTITY ,
	name_city varchar(50) NOT NULL,
	CONSTRAINT city_pk PRIMARY KEY (id_city)

);
-- ddl-end --
-- ALTER TABLE public.city OWNER TO postgres;
-- ddl-end --

-- object: city_fk | type: CONSTRAINT --
-- ALTER TABLE public.job_offer DROP CONSTRAINT IF EXISTS city_fk CASCADE;
ALTER TABLE public.job_offer ADD CONSTRAINT city_fk FOREIGN KEY (id_city_city)
REFERENCES public.city (id_city) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: public.subcategory | type: TABLE --
-- DROP TABLE IF EXISTS public.subcategory CASCADE;
CREATE TABLE public.subcategory (
	id_subcategory integer NOT NULL GENERATED ALWAYS AS IDENTITY ,
	name_subcategory varchar(50) NOT NULL,
	CONSTRAINT subcategory_pk PRIMARY KEY (id_subcategory)

);
-- ddl-end --
-- ALTER TABLE public.subcategory OWNER TO postgres;
-- ddl-end --

-- object: subcategory_fk | type: CONSTRAINT --
-- ALTER TABLE public.job_offer DROP CONSTRAINT IF EXISTS subcategory_fk CASCADE;
ALTER TABLE public.job_offer ADD CONSTRAINT subcategory_fk FOREIGN KEY (id_subcategory_subcategory)
REFERENCES public.subcategory (id_subcategory) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: customer_fk | type: CONSTRAINT --
-- ALTER TABLE public.body_message DROP CONSTRAINT IF EXISTS customer_fk CASCADE;
ALTER TABLE public.body_message ADD CONSTRAINT customer_fk FOREIGN KEY (id_customer_customer)
REFERENCES public.customer (id_customer) MATCH FULL
ON DELETE CASCADE ON UPDATE CASCADE;
-- ddl-end --

-- object: public.application | type: TABLE --
-- DROP TABLE IF EXISTS public.application CASCADE;
CREATE TABLE public.application (
	id_customer_customer integer NOT NULL,
	id_job_job_offer integer NOT NULL,
	date_app date,
	CONSTRAINT application_pk PRIMARY KEY (id_customer_customer,id_job_job_offer)

);
-- ddl-end --
-- ALTER TABLE public.application OWNER TO postgres;
-- ddl-end --

-- object: job_offer_fk | type: CONSTRAINT --
-- ALTER TABLE public.application DROP CONSTRAINT IF EXISTS job_offer_fk CASCADE;
ALTER TABLE public.application ADD CONSTRAINT job_offer_fk FOREIGN KEY (id_job_job_offer)
REFERENCES public.job_offer (id_job) MATCH FULL
ON DELETE CASCADE ON UPDATE CASCADE;
-- ddl-end --

-- object: customer_fk | type: CONSTRAINT --
-- ALTER TABLE public.application DROP CONSTRAINT IF EXISTS customer_fk CASCADE;
ALTER TABLE public.application ADD CONSTRAINT customer_fk FOREIGN KEY (id_customer_customer)
REFERENCES public.customer (id_customer) MATCH FULL
ON DELETE CASCADE ON UPDATE CASCADE;
-- ddl-end --


