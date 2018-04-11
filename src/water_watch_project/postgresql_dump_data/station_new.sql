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
-- Data for Name: station; Type: TABLE DATA; Schema: public; Owner: waterwatchadmin
--

COPY public.station (id, usgs_site_code, station_name, us_state_cd, longitude, latitude, current_status) FROM stdin;
1	11044000	SANTA MARGARITA R NR TEMECULA CA	CA	-117.142000000000	33.474000000000	ACTIVE
2	11074000	SANTA ANA R BL PRADO DAM CA	CA	-117.645000000000	33.883000000000	ACTIVE
3	11125605	HILTON CYN C 0.25 MI BL BRADBURY DAM NR SANTA YNEZ	CA	-119.985000000000	34.584000000000	ACTIVE
4	11128500	SANTA YNEZ R A SOLVANG CA	CA	-120.145000000000	34.585000000000	ACTIVE
5	11133000	SANTA YNEZ R A NARROWS NR LOMPOC CA	CA	-120.425000000000	34.636000000000	ACTIVE
\.


--
-- Name: station_id_seq; Type: SEQUENCE SET; Schema: public; Owner: waterwatchadmin
--

SELECT pg_catalog.setval('public.station_id_seq', 5, true);


--
-- PostgreSQL database dump complete
--

