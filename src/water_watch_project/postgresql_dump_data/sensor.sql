--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.12
-- Dumped by pg_dump version 9.5.12

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: sensor; Type: TABLE DATA; Schema: public; Owner: waterwatchadmin
--

COPY public.sensor (id, current_status, sensor_type_id, station_id) FROM stdin;
1	ACTIVE	3	4
2	ACTIVE	4	4
3	ACTIVE	5	4
4	ACTIVE	6	4
5	ACTIVE	2	4
6	ACTIVE	4	5
7	ACTIVE	5	5
8	ACTIVE	7	5
9	ACTIVE	2	5
10	ACTIVE	3	5
11	ACTIVE	4	3
12	ACTIVE	5	3
13	ACTIVE	2	3
14	ACTIVE	3	3
15	ACTIVE	5	2
16	ACTIVE	2	2
17	ACTIVE	3	2
18	ACTIVE	4	2
19	ACTIVE	6	1
20	ACTIVE	1	1
21	ACTIVE	2	1
22	ACTIVE	3	1
23	ACTIVE	4	1
24	ACTIVE	5	1
\.


--
-- Name: sensor_id_seq; Type: SEQUENCE SET; Schema: public; Owner: waterwatchadmin
--

SELECT pg_catalog.setval('public.sensor_id_seq', 24, true);


--
-- PostgreSQL database dump complete
--

