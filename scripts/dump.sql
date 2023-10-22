--
-- PostgreSQL database dump
--

-- Dumped from database version 15.1 (Debian 15.1-1.pgdg110+1)
-- Dumped by pg_dump version 15.1

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
-- Name: order; Type: TABLE; Schema: public; Owner: tech_user
--

CREATE TABLE public."order" (
    order_id integer NOT NULL,
    order_time timestamp with time zone NOT NULL,
    "_Order__finish_time" timestamp with time zone NOT NULL,
    user_id bigint,
    order_status text
);


ALTER TABLE public."order" OWNER TO tech_user;

--
-- Name: order_order_id_seq; Type: SEQUENCE; Schema: public; Owner: tech_user
--

CREATE SEQUENCE public.order_order_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.order_order_id_seq OWNER TO tech_user;

--
-- Name: order_order_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: tech_user
--

ALTER SEQUENCE public.order_order_id_seq OWNED BY public."order".order_id;


--
-- Name: plate; Type: TABLE; Schema: public; Owner: tech_user
--

CREATE TABLE public.plate (
    plate_id integer NOT NULL,
    plate_name text NOT NULL,
    price double precision NOT NULL,
    picture text
);


ALTER TABLE public.plate OWNER TO tech_user;

--
-- Name: plate_order; Type: TABLE; Schema: public; Owner: tech_user
--

CREATE TABLE public.plate_order (
    plate_id integer NOT NULL,
    order_id integer NOT NULL,
    quantity integer NOT NULL
);


ALTER TABLE public.plate_order OWNER TO tech_user;

--
-- Name: plate_plate_id_seq; Type: SEQUENCE; Schema: public; Owner: tech_user
--

CREATE SEQUENCE public.plate_plate_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.plate_plate_id_seq OWNER TO tech_user;

--
-- Name: plate_plate_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: tech_user
--

ALTER SEQUENCE public.plate_plate_id_seq OWNED BY public.plate.plate_id;


--
-- Name: review; Type: TABLE; Schema: public; Owner: tech_user
--

CREATE TABLE public.review (
    review_id integer NOT NULL,
    user_id integer NOT NULL,
    plate_id integer NOT NULL,
    comment text,
    rating integer NOT NULL
);


ALTER TABLE public.review OWNER TO tech_user;

--
-- Name: review_review_id_seq; Type: SEQUENCE; Schema: public; Owner: tech_user
--

CREATE SEQUENCE public.review_review_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.review_review_id_seq OWNER TO tech_user;

--
-- Name: review_review_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: tech_user
--

ALTER SEQUENCE public.review_review_id_seq OWNED BY public.review.review_id;


--
-- Name: user; Type: TABLE; Schema: public; Owner: tech_user
--

CREATE TABLE public."user" (
    user_id integer NOT NULL,
    username text NOT NULL,
    hashed_password text NOT NULL
);


ALTER TABLE public."user" OWNER TO tech_user;

--
-- Name: user_user_id_seq; Type: SEQUENCE; Schema: public; Owner: tech_user
--

CREATE SEQUENCE public.user_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.user_user_id_seq OWNER TO tech_user;

--
-- Name: user_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: tech_user
--

ALTER SEQUENCE public.user_user_id_seq OWNED BY public."user".user_id;


--
-- Name: order order_id; Type: DEFAULT; Schema: public; Owner: tech_user
--

ALTER TABLE ONLY public."order" ALTER COLUMN order_id SET DEFAULT nextval('public.order_order_id_seq'::regclass);


--
-- Name: plate plate_id; Type: DEFAULT; Schema: public; Owner: tech_user
--

ALTER TABLE ONLY public.plate ALTER COLUMN plate_id SET DEFAULT nextval('public.plate_plate_id_seq'::regclass);


--
-- Name: review review_id; Type: DEFAULT; Schema: public; Owner: tech_user
--

ALTER TABLE ONLY public.review ALTER COLUMN review_id SET DEFAULT nextval('public.review_review_id_seq'::regclass);


--
-- Name: user user_id; Type: DEFAULT; Schema: public; Owner: tech_user
--

ALTER TABLE ONLY public."user" ALTER COLUMN user_id SET DEFAULT nextval('public.user_user_id_seq'::regclass);


--
-- Data for Name: order; Type: TABLE DATA; Schema: public; Owner: tech_user
--

COPY public."order" (order_id, order_time, "_Order__finish_time", user_id, order_status) FROM stdin;
1	2023-10-22 15:54:38.81897+00	2023-10-22 15:59:45.81905+00	2	Delivered
2	2023-10-22 15:55:56.079727+00	2023-10-22 16:08:08.079744+00	2	Delivered
3	2023-10-22 16:07:15.178462+00	2023-10-22 16:12:08.178479+00	1	Delivered
4	2023-10-22 16:08:26.445165+00	2023-10-22 16:17:10.445185+00	1	Delivered
5	2023-10-22 16:10:32.982914+00	2023-10-22 16:15:54.982948+00	1	Approved
6	2023-10-22 16:17:33.19812+00	2023-10-22 16:20:44.198152+00	1	Submitted
7	2023-10-22 16:34:59.066862+00	2023-10-22 16:43:00.066908+00	3	Delivered
8	2023-10-22 16:36:03.755828+00	2023-10-22 16:49:12.755862+00	3	Delivered
\.


--
-- Data for Name: plate; Type: TABLE DATA; Schema: public; Owner: tech_user
--

COPY public.plate (plate_id, plate_name, price, picture) FROM stdin;
1	Pizza Margherita	12.99	https://upload.wikimedia.org/wikipedia/commons/thumb/a/a3/Eq_it-na_pizza-margherita_sep2005_sml.jpg/440px-Eq_it-na_pizza-margherita_sep2005_sml.jpg
2	Rösti	15.99	https://upload.wikimedia.org/wikipedia/commons/thumb/3/3d/Roesti.jpg/500px-Roesti.jpg
3	Fondue	13.99	https://upload.wikimedia.org/wikipedia/commons/thumb/d/d8/Swiss_fondue.jpg/500px-Swiss_fondue.jpg
4	Raclette	18.99	https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Raclette_20040817_140816.jpg/440px-Raclette_20040817_140816.jpg
5	Carpaccio	23.99	https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/Carpaccio_with_cheese_in_Warsaw.jpg/500px-Carpaccio_with_cheese_in_Warsaw.jpg
6	BBQ Chicken Burger & Sweet Potato Fries	12.99	https://www.howsweeteats.com/wp-content/uploads/2011/04/bbqburgers-7.jpg
7	Spaghetti Carbonara	11.99	https://upload.wikimedia.org/wikipedia/commons/thumb/3/33/Espaguetis_carbonara.jpg/500px-Espaguetis_carbonara.jpg
8	Risotto	15.99	https://upload.wikimedia.org/wikipedia/commons/4/40/Italian_Risotto.png
\.


--
-- Data for Name: plate_order; Type: TABLE DATA; Schema: public; Owner: tech_user
--

COPY public.plate_order (plate_id, order_id, quantity) FROM stdin;
7	1	3
4	1	16
5	1	1
5	2	2
7	2	2
4	3	2
8	3	1
1	4	3
6	5	3
8	6	3
8	7	2
6	7	1
2	7	1
7	8	1
\.


--
-- Data for Name: review; Type: TABLE DATA; Schema: public; Owner: tech_user
--

COPY public.review (review_id, user_id, plate_id, comment, rating) FROM stdin;
1	2	7	The pasta was overcooked.	2
2	2	5	Could be better.	3
3	1	1	Very good pizza.	5
4	3	2	Not fresh.	2
5	3	8	Very good risotto, my wife loved it.	4
6	3	7	Pretty good, but I could do better at home.	3
\.


--
-- Data for Name: user; Type: TABLE DATA; Schema: public; Owner: tech_user
--

COPY public."user" (user_id, username, hashed_password) FROM stdin;
1	ines	1a05f59fc22e9a5e5cbcb25d5c0723e558166728e6e118289ce83795c51a9f59
2	meli	ebdf496f67651cddf6aaa1f0b130f1b99ce9e2e93dc2503d926edcff15aee668
3	john	bfbfe08edb20e274563cd69250f4e1be3c17bbb919a68082b7fb82802e10ffe0
\.


--
-- Name: order_order_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tech_user
--

SELECT pg_catalog.setval('public.order_order_id_seq', 8, true);


--
-- Name: plate_plate_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tech_user
--

SELECT pg_catalog.setval('public.plate_plate_id_seq', 1, false);


--
-- Name: review_review_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tech_user
--

SELECT pg_catalog.setval('public.review_review_id_seq', 6, true);


--
-- Name: user_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tech_user
--

SELECT pg_catalog.setval('public.user_user_id_seq', 3, true);


--
-- Name: order order_pkey; Type: CONSTRAINT; Schema: public; Owner: tech_user
--

ALTER TABLE ONLY public."order"
    ADD CONSTRAINT order_pkey PRIMARY KEY (order_id);


--
-- Name: plate_order plate_order_pkey; Type: CONSTRAINT; Schema: public; Owner: tech_user
--

ALTER TABLE ONLY public.plate_order
    ADD CONSTRAINT plate_order_pkey PRIMARY KEY (plate_id, order_id);


--
-- Name: plate plate_pkey; Type: CONSTRAINT; Schema: public; Owner: tech_user
--

ALTER TABLE ONLY public.plate
    ADD CONSTRAINT plate_pkey PRIMARY KEY (plate_id);


--
-- Name: review review_pkey; Type: CONSTRAINT; Schema: public; Owner: tech_user
--

ALTER TABLE ONLY public.review
    ADD CONSTRAINT review_pkey PRIMARY KEY (review_id);


--
-- Name: user user_pkey; Type: CONSTRAINT; Schema: public; Owner: tech_user
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (user_id);


--
-- Name: order order_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: tech_user
--

ALTER TABLE ONLY public."order"
    ADD CONSTRAINT order_user_id_fkey FOREIGN KEY (user_id) REFERENCES public."user"(user_id) NOT VALID;


--
-- Name: plate_order plate_order_order_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: tech_user
--

ALTER TABLE ONLY public.plate_order
    ADD CONSTRAINT plate_order_order_id_fkey FOREIGN KEY (order_id) REFERENCES public."order"(order_id);


--
-- Name: plate_order plate_order_plate_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: tech_user
--

ALTER TABLE ONLY public.plate_order
    ADD CONSTRAINT plate_order_plate_id_fkey FOREIGN KEY (plate_id) REFERENCES public.plate(plate_id);


--
-- Name: review review_plate_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: tech_user
--

ALTER TABLE ONLY public.review
    ADD CONSTRAINT review_plate_id_fkey FOREIGN KEY (plate_id) REFERENCES public.plate(plate_id) NOT VALID;


--
-- Name: review review_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: tech_user
--

ALTER TABLE ONLY public.review
    ADD CONSTRAINT review_user_id_fkey FOREIGN KEY (user_id) REFERENCES public."user"(user_id) NOT VALID;


--
-- PostgreSQL database dump complete
--

