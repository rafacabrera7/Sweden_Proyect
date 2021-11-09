--
-- PostgreSQL database dump
--

-- Dumped from database version 12.8 (Ubuntu 12.8-1.pgdg20.04+1)
-- Dumped by pg_dump version 14.0 (Ubuntu 14.0-1.pgdg20.04+1)

-- Started on 2021-11-09 14:05:32 -05

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 202 (class 1259 OID 16385)
-- Name: application; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.application (
    id_customer_customer integer NOT NULL,
    id_job_job_offer integer NOT NULL,
    date_app date
);


ALTER TABLE public.application OWNER TO postgres;

--
-- TOC entry 203 (class 1259 OID 16388)
-- Name: body_message; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.body_message (
    id_customer_customer integer NOT NULL,
    id_body integer NOT NULL,
    body_message character varying(2000)
);


ALTER TABLE public.body_message OWNER TO postgres;

--
-- TOC entry 204 (class 1259 OID 16394)
-- Name: body_message_body_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.body_message ALTER COLUMN id_body ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.body_message_body_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 205 (class 1259 OID 16396)
-- Name: city; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.city (
    id_city smallint NOT NULL,
    name_city character varying(50) NOT NULL
);


ALTER TABLE public.city OWNER TO postgres;

--
-- TOC entry 206 (class 1259 OID 16399)
-- Name: city_id_city_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.city ALTER COLUMN id_city ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.city_id_city_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 207 (class 1259 OID 16401)
-- Name: company; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.company (
    id_company integer NOT NULL,
    name_company character varying(80) NOT NULL
);


ALTER TABLE public.company OWNER TO postgres;

--
-- TOC entry 208 (class 1259 OID 16404)
-- Name: company_id_company_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.company ALTER COLUMN id_company ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.company_id_company_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 209 (class 1259 OID 16406)
-- Name: customer; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.customer (
    id_customer integer NOT NULL,
    name_customer character varying(50) NOT NULL,
    email_customer character varying(50) NOT NULL,
    password_customer character varying(20) NOT NULL,
    date_inserted date,
    user_smtp character varying(30),
    password_smtp character varying(60)
);


ALTER TABLE public.customer OWNER TO postgres;

--
-- TOC entry 210 (class 1259 OID 16409)
-- Name: customer_id_customer_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.customer ALTER COLUMN id_customer ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.customer_id_customer_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 211 (class 1259 OID 16411)
-- Name: job_offer; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.job_offer (
    id_job integer NOT NULL,
    name_job character varying(60) NOT NULL,
    description_job character varying(100),
    email_job character varying(50) NOT NULL,
    id_company_company integer NOT NULL,
    date_accesed date,
    url_job character varying(70),
    id_city_city smallint,
    id_sector_main_sector integer,
    id_subcategory_subcategory integer
);


ALTER TABLE public.job_offer OWNER TO postgres;

--
-- TOC entry 212 (class 1259 OID 16414)
-- Name: main_sector; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.main_sector (
    id_sector integer NOT NULL,
    name_sector character varying(50) NOT NULL
);


ALTER TABLE public.main_sector OWNER TO postgres;

--
-- TOC entry 213 (class 1259 OID 16417)
-- Name: main_sector_id_sector_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.main_sector ALTER COLUMN id_sector ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.main_sector_id_sector_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 216 (class 1259 OID 24577)
-- Name: resume; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.resume (
    id_customer_customer integer NOT NULL,
    id_cv integer NOT NULL,
    name_cv character varying(40) NOT NULL,
    path_cv character varying(150)
);


ALTER TABLE public.resume OWNER TO postgres;

--
-- TOC entry 217 (class 1259 OID 24587)
-- Name: resume_id_cv_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.resume ALTER COLUMN id_cv ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.resume_id_cv_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 214 (class 1259 OID 16419)
-- Name: subcategory; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.subcategory (
    id_subcategory integer NOT NULL,
    name_subcategory character varying(50) NOT NULL
);


ALTER TABLE public.subcategory OWNER TO postgres;

--
-- TOC entry 215 (class 1259 OID 16422)
-- Name: subcategory_id_subcategory_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.subcategory ALTER COLUMN id_subcategory ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.subcategory_id_subcategory_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 2878 (class 2606 OID 16425)
-- Name: application application_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.application
    ADD CONSTRAINT application_pk PRIMARY KEY (id_customer_customer, id_job_job_offer);


--
-- TOC entry 2880 (class 2606 OID 16427)
-- Name: body_message body_message_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.body_message
    ADD CONSTRAINT body_message_pk PRIMARY KEY (id_body, id_customer_customer);


--
-- TOC entry 2882 (class 2606 OID 16429)
-- Name: city city_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.city
    ADD CONSTRAINT city_pk PRIMARY KEY (id_city);


--
-- TOC entry 2884 (class 2606 OID 16431)
-- Name: company company_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.company
    ADD CONSTRAINT company_pk PRIMARY KEY (id_company);


--
-- TOC entry 2886 (class 2606 OID 16433)
-- Name: customer customer_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.customer
    ADD CONSTRAINT customer_pk PRIMARY KEY (id_customer);


--
-- TOC entry 2888 (class 2606 OID 16435)
-- Name: job_offer job_offer_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.job_offer
    ADD CONSTRAINT job_offer_pk PRIMARY KEY (id_job);


--
-- TOC entry 2894 (class 2606 OID 24586)
-- Name: resume resume_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.resume
    ADD CONSTRAINT resume_pk PRIMARY KEY (id_customer_customer, id_cv);


--
-- TOC entry 2890 (class 2606 OID 16437)
-- Name: main_sector sector_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.main_sector
    ADD CONSTRAINT sector_pk PRIMARY KEY (id_sector);


--
-- TOC entry 2892 (class 2606 OID 16439)
-- Name: subcategory subcategory_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.subcategory
    ADD CONSTRAINT subcategory_pk PRIMARY KEY (id_subcategory);


--
-- TOC entry 2898 (class 2606 OID 16440)
-- Name: job_offer city_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.job_offer
    ADD CONSTRAINT city_fk FOREIGN KEY (id_city_city) REFERENCES public.city(id_city) MATCH FULL ON UPDATE CASCADE ON DELETE SET NULL;


--
-- TOC entry 2899 (class 2606 OID 16445)
-- Name: job_offer company_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.job_offer
    ADD CONSTRAINT company_fk FOREIGN KEY (id_company_company) REFERENCES public.company(id_company) MATCH FULL ON UPDATE CASCADE ON DELETE RESTRICT;


--
-- TOC entry 2897 (class 2606 OID 16450)
-- Name: body_message customer_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.body_message
    ADD CONSTRAINT customer_fk FOREIGN KEY (id_customer_customer) REFERENCES public.customer(id_customer) MATCH FULL ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 2895 (class 2606 OID 16455)
-- Name: application customer_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.application
    ADD CONSTRAINT customer_fk FOREIGN KEY (id_customer_customer) REFERENCES public.customer(id_customer) MATCH FULL ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 2902 (class 2606 OID 24580)
-- Name: resume customer_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.resume
    ADD CONSTRAINT customer_fk FOREIGN KEY (id_customer_customer) REFERENCES public.customer(id_customer) MATCH FULL ON UPDATE CASCADE ON DELETE RESTRICT;


--
-- TOC entry 2896 (class 2606 OID 16460)
-- Name: application job_offer_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.application
    ADD CONSTRAINT job_offer_fk FOREIGN KEY (id_job_job_offer) REFERENCES public.job_offer(id_job) MATCH FULL ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 2900 (class 2606 OID 16465)
-- Name: job_offer main_sector_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.job_offer
    ADD CONSTRAINT main_sector_fk FOREIGN KEY (id_sector_main_sector) REFERENCES public.main_sector(id_sector) MATCH FULL ON UPDATE CASCADE ON DELETE SET NULL;


--
-- TOC entry 2901 (class 2606 OID 16470)
-- Name: job_offer subcategory_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.job_offer
    ADD CONSTRAINT subcategory_fk FOREIGN KEY (id_subcategory_subcategory) REFERENCES public.subcategory(id_subcategory) MATCH FULL ON UPDATE CASCADE ON DELETE SET NULL;


-- Completed on 2021-11-09 14:05:32 -05

--
-- PostgreSQL database dump complete
--

