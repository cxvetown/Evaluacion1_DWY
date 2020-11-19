-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 18-11-2020 a las 23:50:16
-- Versión del servidor: 10.4.14-MariaDB
-- Versión de PHP: 7.2.34

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `tienda_masitas`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `carrito_compra`
--

CREATE TABLE `carrito_compra` (
  `id_compra` int(4) NOT NULL,
  `producto` varchar(50) NOT NULL,
  `descripcion` varchar(100) NOT NULL,
  `valor` int(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `lista_deseos`
--

CREATE TABLE `lista_deseos` (
  `codigo_lista_deseo` varchar(4) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `valor` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `peluche`
--

CREATE TABLE `peluche` (
  `codigo_peluche` int(4) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `descripcion` int(100) NOT NULL,
  `valor` int(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `peluche_nuevo`
--

CREATE TABLE `peluche_nuevo` (
  `id_peluche` int(4) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `descripcion` varchar(100) NOT NULL,
  `valor` int(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `peluche_nuevo_descuento`
--

CREATE TABLE `peluche_nuevo_descuento` (
  `id_peluche_desc` int(4) NOT NULL,
  `nombre` varchar(40) NOT NULL,
  `descripcion` varchar(100) NOT NULL,
  `valor` int(8) NOT NULL,
  `descuento` int(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `rut` varchar(10) NOT NULL,
  `nombre` varchar(40) NOT NULL,
  `apellido` varchar(40) NOT NULL,
  `telefono` int(10) NOT NULL,
  `correo` varchar(50) NOT NULL,
  `contraseña` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`rut`, `nombre`, `apellido`, `telefono`, `correo`, `contraseña`) VALUES
('204188823', 'carlos', 'pardo', 1, '1', '123');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `carrito_compra`
--
ALTER TABLE `carrito_compra`
  ADD PRIMARY KEY (`id_compra`);

--
-- Indices de la tabla `lista_deseos`
--
ALTER TABLE `lista_deseos`
  ADD PRIMARY KEY (`codigo_lista_deseo`);

--
-- Indices de la tabla `peluche`
--
ALTER TABLE `peluche`
  ADD PRIMARY KEY (`codigo_peluche`);

--
-- Indices de la tabla `peluche_nuevo`
--
ALTER TABLE `peluche_nuevo`
  ADD PRIMARY KEY (`id_peluche`);

--
-- Indices de la tabla `peluche_nuevo_descuento`
--
ALTER TABLE `peluche_nuevo_descuento`
  ADD PRIMARY KEY (`id_peluche_desc`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`rut`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
