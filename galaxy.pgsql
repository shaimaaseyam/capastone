--
-- PostgreSQL database dump
--

-- Dumped from database version 12.2
-- Dumped by pg_dump version 12.2

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
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO postgres;

--
-- Name: planets; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.planets (
    id integer NOT NULL,
    name character varying,
    moons_number integer
);


ALTER TABLE public.planets OWNER TO postgres;

--
-- Name: planets_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.planets_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.planets_id_seq OWNER TO postgres;

--
-- Name: planets_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.planets_id_seq OWNED BY public.planets.id;


--
-- Name: stars; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.stars (
    id integer NOT NULL,
    name character varying,
    age integer
);


ALTER TABLE public.stars OWNER TO postgres;

--
-- Name: stars_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.stars_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.stars_id_seq OWNER TO postgres;

--
-- Name: stars_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.stars_id_seq OWNED BY public.stars.id;


--
-- Name: planets id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.planets ALTER COLUMN id SET DEFAULT nextval('public.planets_id_seq'::regclass);


--
-- Name: stars id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.stars ALTER COLUMN id SET DEFAULT nextval('public.stars_id_seq'::regclass);


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.alembic_version (version_num) FROM stdin;
46bea005800b
\.


--
-- Data for Name: planets; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.planets (id, name, moons_number) FROM stdin;
1	mars	3
2	oranos	1
3	earth	5
\.


--
-- Data for Name: stars; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.stars (id, name, age) FROM stdin;
1	sun	300
2	red	5
\.


--
-- Name: planets_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.planets_id_seq', 3, true);


--
-- Name: stars_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.stars_id_seq', 2, true);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: planets planets_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.planets
    ADD CONSTRAINT planets_pkey PRIMARY KEY (id);


--
-- Name: stars stars_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.stars
    ADD CONSTRAINT stars_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

