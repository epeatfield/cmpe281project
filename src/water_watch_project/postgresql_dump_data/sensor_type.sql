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
-- Data for Name: sensor_type; Type: TABLE DATA; Schema: public; Owner: waterwatchadmin
--

COPY public.sensor_type (id, sensor_type_name, description, unit, usgs_sensor_type_code) FROM stdin;
1	pH, water, unfiltered, field, standard units	pH, water, unfiltered, field, standard units	std units	45810855
2	Temperature, water, degrees Celsius	Temperature, water, degrees Celsius	deg C	45807042
3	Stream flow, ft3/s	Discharge, cubic feet per second	ft3/s	45807197
4	Gage height, ft	Gage height, feet	ft	45807202
5	Specific conductance, water, unfiltered	Specific conductance, water, unfiltered, microsiemens per centimeter at 25 degrees Celcius	uS/cm @25C	45807295
6	Dissolved oxygen, water, unfiltered, mg/L	Dissolved oxygen, water, unfiltered, milligrams per liter	mg/L	45809894
7	DCP battery voltage, V	DCP battery voltage, volts	volts	52280502
\.


--
-- Name: sensor_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: waterwatchadmin
--

SELECT pg_catalog.setval('public.sensor_type_id_seq', 7, true);


--
-- PostgreSQL database dump complete
--

