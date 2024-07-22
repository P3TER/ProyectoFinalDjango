-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 14-03-2024 a las 22:28:32
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `bdlibreriangv`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `autores`
--

CREATE TABLE `autores` (
  `id_autor` int(11) NOT NULL,
  `nombres` varchar(25) NOT NULL,
  `apellidos` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `autores`
--

INSERT INTO `autores` (`id_autor`, `nombres`, `apellidos`) VALUES
(1, 'Marc', 'Cerasini'),
(2, 'Julio', 'Verne'),
(3, 'Edgar', 'Allan Poe'),
(4, 'Ben', 'Mezrich'),
(5, 'Mary', 'Wollstonecraft Shelley'),
(6, 'Bram', 'Stoker'),
(7, 'Bruno', 'Nievas'),
(8, 'C sar', 'Garc a Muñoz'),
(9, 'Armando', 'Rodera'),
(10, 'Jane', 'Austen'),
(11, 'Emily', 'Bronte'),
(12, 'Alejandro', 'Dumas'),
(13, 'Gabriel', 'Garc a M rquez'),
(14, 'Nikos', 'Kazantzakis'),
(15, 'Raymond', 'Carver');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `categorias`
--

CREATE TABLE `categorias` (
  `id_categoria` int(11) NOT NULL,
  `categoria` varchar(75) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `categorias`
--

INSERT INTO `categorias` (`id_categoria`, `categoria`) VALUES
(1, 'Acción y Aventura'),
(2, 'Terror'),
(3, 'Ficción Moderna'),
(4, 'Suspenso'),
(5, 'Romance'),
(6, 'Narrativa');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `clientes`
--

CREATE TABLE `clientes` (
  `id_cliente` int(11) NOT NULL,
  `identificacion` varchar(12) NOT NULL,
  `nombres` varchar(25) NOT NULL,
  `apellidos` varchar(25) NOT NULL,
  `direccion` varchar(128) DEFAULT NULL,
  `telefono` varchar(14) NOT NULL,
  `correo` varchar(128) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `clientes`
--

INSERT INTO `clientes` (`id_cliente`, `identificacion`, `nombres`, `apellidos`, `direccion`, `telefono`, `correo`) VALUES
(1, '1011510881', 'VALERIA', 'GONZÁLEZ GÓMEZ', NULL, '1234567890', 'valgonzlez111111@soy.sena.edu.co'),
(2, '1036251918', 'JUAN JOSÉ', 'MUÑETÓN ZULUAGA', NULL, '2345678901', 'juajmueton@soy.sena.edu.co'),
(3, '1064897675', 'RICHARD REOVIS', 'RODRÍGUEZ PÉREZ', NULL, '3456789012', 'rrrodrguez@soy.sena.edu.co'),
(4, '1038262858', 'SANTIAGO', 'CHAVARRÍA MURILLO', NULL, '4567890123', 'sanchavarria@soy.sena.edu.co'),
(5, '1021805011', 'KEVIN STEVEN', 'SANMARTÍN ACOSTA', NULL, '5678901234', 'kevssanmartin@soy.sena.edu.co'),
(6, '1017941691', 'NICOLÁS', 'GIL VERGARA', NULL, '6789012345', 'nicgil11@soy.sena.edu.co'),
(7, '1021923074', 'MIGUEL ALEJANDRO', 'OSPINA GARCÍA', NULL, '7890123456', 'migaospina111111@soy.sena.edu.co'),
(8, '1015186683', 'DIEGO ALEJANDRO', 'PUERTA LOBO', NULL, '8901234567', 'dieapuerta1j@soy.sena.edu.co'),
(9, '1033487913', 'JUAN PABLO', 'SALAZAR BRICEÑO', NULL, '9012345678', 'jpsalazar11111@soy.sena.edu.co'),
(10, '1025762109', 'JOAN SEBASTIÁN', 'CASTAÑEDA QUINTERO', NULL, '1234567809', 'joascastaeda111@soy.sena.edu.co'),
(11, '1045606558', 'YAIR ALEJANDRO', 'OSORIO ALZATE', NULL, '2345678091', 'yaiaosori@soy.sena.edu.co'),
(12, '1125080170', 'SEBASTIÁN', 'PRESIGA PATIÑO', NULL, '3456780912', 'spresiga0@soy.sena.edu.co'),
(13, '1036449409', 'JUAN MANUEL', 'RUIZ GARCÍAO', NULL, '4567809123', 'juamruiz11@soy.sena.edu.co'),
(14, '1033488706', 'DAVID ANDRÉS', 'MONSALVE SÁNCHEZ', NULL, '5678091234', 'davamonsalve@soy.sena.edu.co'),
(15, '1011392569', 'EMANUEL', 'MEDINA ARANGO', NULL, '6780912345', 'emedina1111111@soy.sena.edu.co'),
(16, '1018228823', 'ANDERSON', 'RODRÍGUEZ RIVERA', NULL, '7809123456', 'anderson.rodriguez8@soy.sena.edu.co');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `libros`
--

CREATE TABLE `libros` (
  `isbn` int(11) NOT NULL,
  `titulo` varchar(128) NOT NULL,
  `fecha_pub` date NOT NULL,
  `precio` double NOT NULL,
  `id_categoria` int(11) NOT NULL,
  `cantidad_stock` int(11) NOT NULL,
  `portada` varchar(128) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `libros`
--

INSERT INTO `libros` (`isbn`, `titulo`, `fecha_pub`, `precio`, `id_categoria`, `cantidad_stock`, `portada`) VALUES
(28, 'Catedral', '2004-08-15', 25700, 6, 100, 'no_portada.png'),
(128, 'Alexis Zorba, el griego', '2010-11-25', 38500, 6, 100, 'no_portada.png'),
(328, 'Miguel Strogoff', '2001-12-10', 25000, 1, 100, 'no_portada.png'),
(372, 'Operation Hell Gate', '2005-09-27', 48000, 1, 100, 'no_portada.png'),
(385, 'Sexo en la Luna', '2011-06-01', 29500, 3, 100, 'no_portada.png'),
(415, 'Dr cula', '1999-04-10', 46800, 2, 100, 'no_portada.png'),
(428, 'Realidad aumentada', '2001-03-13', 35200, 4, 100, 'no_portada.png'),
(442, 'Juicio Final, Sangre en el cielo', '2009-05-30', 40000, 4, 100, 'no_portada.png'),
(466, 'El Enigma de los Vencidos', '2000-11-25', 38500, 4, 100, 'no_portada.png'),
(468, 'El gato negro', '1997-10-12', 44000, 2, 100, 'no_portada.png'),
(498, 'Frankenstein', '1990-03-01', 55500, 2, 100, 'no_portada.png'),
(578, 'Orgullo y Prejuicio', '2003-09-25', 36100, 5, 100, 'no_portada.png'),
(603, 'Cumbres Borrascosas', '1998-11-25', 60800, 5, 100, 'no_portada.png'),
(618, 'La Dama de las Camelias', '1995-07-28', 57600, 5, 100, 'no_portada.png'),
(729, '100 a os de soledad', '1990-04-27', 39500, 6, 100, 'no_portada.png');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `libro_x_autor`
--

CREATE TABLE `libro_x_autor` (
  `isbn` int(11) NOT NULL,
  `id_autor` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `libro_x_autor`
--

INSERT INTO `libro_x_autor` (`isbn`, `id_autor`) VALUES
(28, 15),
(128, 14),
(328, 2),
(372, 1),
(385, 4),
(415, 6),
(428, 7),
(442, 8),
(466, 9),
(468, 3),
(498, 5),
(578, 10),
(603, 11),
(618, 12),
(729, 13);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pedido_x_cliente`
--

CREATE TABLE `pedido_x_cliente` (
  `id_pedido` int(11) NOT NULL,
  `id_cliente` int(11) NOT NULL,
  `isbn` int(11) NOT NULL,
  `cantidad` int(11) NOT NULL DEFAULT 1,
  `fecha_ped` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `autores`
--
ALTER TABLE `autores`
  ADD PRIMARY KEY (`id_autor`);

--
-- Indices de la tabla `categorias`
--
ALTER TABLE `categorias`
  ADD PRIMARY KEY (`id_categoria`);

--
-- Indices de la tabla `clientes`
--
ALTER TABLE `clientes`
  ADD PRIMARY KEY (`id_cliente`);

--
-- Indices de la tabla `libros`
--
ALTER TABLE `libros`
  ADD PRIMARY KEY (`isbn`),
  ADD KEY `id_categoria` (`id_categoria`);

--
-- Indices de la tabla `libro_x_autor`
--
ALTER TABLE `libro_x_autor`
  ADD PRIMARY KEY (`isbn`,`id_autor`),
  ADD KEY `id_autor` (`id_autor`);

--
-- Indices de la tabla `pedido_x_cliente`
--
ALTER TABLE `pedido_x_cliente`
  ADD PRIMARY KEY (`id_pedido`),
  ADD KEY `id_cliente` (`id_cliente`),
  ADD KEY `isbn` (`isbn`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `autores`
--
ALTER TABLE `autores`
  MODIFY `id_autor` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT de la tabla `categorias`
--
ALTER TABLE `categorias`
  MODIFY `id_categoria` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `clientes`
--
ALTER TABLE `clientes`
  MODIFY `id_cliente` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT de la tabla `pedido_x_cliente`
--
ALTER TABLE `pedido_x_cliente`
  MODIFY `id_pedido` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `libros`
--
ALTER TABLE `libros`
  ADD CONSTRAINT `libros_ibfk_1` FOREIGN KEY (`id_categoria`) REFERENCES `categorias` (`id_categoria`);

--
-- Filtros para la tabla `libro_x_autor`
--
ALTER TABLE `libro_x_autor`
  ADD CONSTRAINT `libro_x_autor_ibfk_1` FOREIGN KEY (`isbn`) REFERENCES `libros` (`isbn`),
  ADD CONSTRAINT `libro_x_autor_ibfk_2` FOREIGN KEY (`id_autor`) REFERENCES `autores` (`id_autor`);

--
-- Filtros para la tabla `pedido_x_cliente`
--
ALTER TABLE `pedido_x_cliente`
  ADD CONSTRAINT `pedido_x_cliente_ibfk_1` FOREIGN KEY (`id_cliente`) REFERENCES `clientes` (`id_cliente`),
  ADD CONSTRAINT `pedido_x_cliente_ibfk_2` FOREIGN KEY (`isbn`) REFERENCES `libros` (`isbn`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
