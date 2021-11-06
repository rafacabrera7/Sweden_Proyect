--
-- PostgreSQL database dump
--

-- Dumped from database version 12.5
-- Dumped by pg_dump version 12.5

-- Started on 2021-11-06 15:47:54

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
-- TOC entry 214 (class 1259 OID 52153)
-- Name: application; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.application (
    id_customer_customer integer NOT NULL,
    id_job_job_offer integer NOT NULL,
    date_app date
);


ALTER TABLE public.application OWNER TO postgres;

--
-- TOC entry 209 (class 1259 OID 52116)
-- Name: body_message; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.body_message (
    id_customer_customer integer NOT NULL,
    body_id integer NOT NULL,
    body_message character varying(2000)
);


ALTER TABLE public.body_message OWNER TO postgres;

--
-- TOC entry 215 (class 1259 OID 52168)
-- Name: body_message_body_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.body_message ALTER COLUMN body_id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.body_message_body_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 211 (class 1259 OID 52126)
-- Name: city; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.city (
    id_city smallint NOT NULL,
    name_city character varying(50) NOT NULL
);


ALTER TABLE public.city OWNER TO postgres;

--
-- TOC entry 210 (class 1259 OID 52124)
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
-- TOC entry 204 (class 1259 OID 52087)
-- Name: company; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.company (
    id_company integer NOT NULL,
    name_company character varying(80) NOT NULL
);


ALTER TABLE public.company OWNER TO postgres;

--
-- TOC entry 203 (class 1259 OID 52085)
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
-- TOC entry 208 (class 1259 OID 52111)
-- Name: customer; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.customer (
    id_customer integer NOT NULL,
    name_customer character varying(50) NOT NULL,
    email_customer character varying(50) NOT NULL,
    password_customer character varying(20) NOT NULL,
    date_inserted date
);


ALTER TABLE public.customer OWNER TO postgres;

--
-- TOC entry 207 (class 1259 OID 52109)
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
-- TOC entry 202 (class 1259 OID 52080)
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
-- TOC entry 206 (class 1259 OID 52094)
-- Name: main_sector; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.main_sector (
    id_sector integer NOT NULL,
    name_sector character varying(50) NOT NULL
);


ALTER TABLE public.main_sector OWNER TO postgres;

--
-- TOC entry 205 (class 1259 OID 52092)
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
-- TOC entry 213 (class 1259 OID 52138)
-- Name: subcategory; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.subcategory (
    id_subcategory integer NOT NULL,
    name_subcategory character varying(50) NOT NULL
);


ALTER TABLE public.subcategory OWNER TO postgres;

--
-- TOC entry 212 (class 1259 OID 52136)
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
-- TOC entry 2741 (class 2606 OID 52157)
-- Name: application application_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.application
    ADD CONSTRAINT application_pk PRIMARY KEY (id_customer_customer, id_job_job_offer);


--
-- TOC entry 2735 (class 2606 OID 52123)
-- Name: body_message body_message_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.body_message
    ADD CONSTRAINT body_message_pk PRIMARY KEY (body_id, id_customer_customer);


--
-- TOC entry 2737 (class 2606 OID 52130)
-- Name: city city_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.city
    ADD CONSTRAINT city_pk PRIMARY KEY (id_city);


--
-- TOC entry 2729 (class 2606 OID 52091)
-- Name: company company_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.company
    ADD CONSTRAINT company_pk PRIMARY KEY (id_company);


--
-- TOC entry 2733 (class 2606 OID 52115)
-- Name: customer customer_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.customer
    ADD CONSTRAINT customer_pk PRIMARY KEY (id_customer);


--
-- TOC entry 2727 (class 2606 OID 52084)
-- Name: job_offer job_offer_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.job_offer
    ADD CONSTRAINT job_offer_pk PRIMARY KEY (id_job);


--
-- TOC entry 2731 (class 2606 OID 52098)
-- Name: main_sector sector_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.main_sector
    ADD CONSTRAINT sector_pk PRIMARY KEY (id_sector);


--
-- TOC entry 2739 (class 2606 OID 52142)
-- Name: subcategory subcategory_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.subcategory
    ADD CONSTRAINT subcategory_pk PRIMARY KEY (id_subcategory);


--
-- TOC entry 2744 (class 2606 OID 52131)
-- Name: job_offer city_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.job_offer
    ADD CONSTRAINT city_fk FOREIGN KEY (id_city_city) REFERENCES public.city(id_city) MATCH FULL ON UPDATE CASCADE ON DELETE SET NULL;


--
-- TOC entry 2742 (class 2606 OID 52099)
-- Name: job_offer company_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.job_offer
    ADD CONSTRAINT company_fk FOREIGN KEY (id_company_company) REFERENCES public.company(id_company) MATCH FULL ON UPDATE CASCADE ON DELETE RESTRICT;


--
-- TOC entry 2746 (class 2606 OID 52148)
-- Name: body_message customer_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.body_message
    ADD CONSTRAINT customer_fk FOREIGN KEY (id_customer_customer) REFERENCES public.customer(id_customer) MATCH FULL ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 2748 (class 2606 OID 52163)
-- Name: application customer_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.application
    ADD CONSTRAINT customer_fk FOREIGN KEY (id_customer_customer) REFERENCES public.customer(id_customer) MATCH FULL ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 2747 (class 2606 OID 52158)
-- Name: application job_offer_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.application
    ADD CONSTRAINT job_offer_fk FOREIGN KEY (id_job_job_offer) REFERENCES public.job_offer(id_job) MATCH FULL ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 2743 (class 2606 OID 52104)
-- Name: job_offer main_sector_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.job_offer
    ADD CONSTRAINT main_sector_fk FOREIGN KEY (id_sector_main_sector) REFERENCES public.main_sector(id_sector) MATCH FULL ON UPDATE CASCADE ON DELETE SET NULL;


--
-- TOC entry 2745 (class 2606 OID 52143)
-- Name: job_offer subcategory_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.job_offer
    ADD CONSTRAINT subcategory_fk FOREIGN KEY (id_subcategory_subcategory) REFERENCES public.subcategory(id_subcategory) MATCH FULL ON UPDATE CASCADE ON DELETE SET NULL;


-- Completed on 2021-11-06 15:47:54

--
-- PostgreSQL database dump complete
--

