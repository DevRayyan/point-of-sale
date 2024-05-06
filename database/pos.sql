-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 06, 2024 at 10:03 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pos`
--

-- --------------------------------------------------------

--
-- Table structure for table `category`
--

CREATE TABLE `category` (
  `id` char(50) NOT NULL,
  `name` varchar(100) NOT NULL,
  `status` int(11) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT current_timestamp(),
  `updated_at` datetime NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `category`
--

INSERT INTO `category` (`id`, `name`, `status`, `created_at`, `updated_at`) VALUES
('0001', 'Burgers', 1, '2024-05-05 10:58:49', '2024-05-05 10:58:49'),
('0002', 'Pizzas', 0, '2024-05-05 11:17:57', '2024-05-05 11:17:57'),
('4729ecda-0af7-11ef-abde-54ee752ae2f0', 'Burder', 1, '2024-05-05 11:51:03', '2024-05-05 11:51:03'),
('58f48bc5-0af7-11ef-abde-54ee752ae2f0', '58f48bd5-0af7-11ef-abde-54ee752ae2f0', 1, '2024-05-05 11:51:33', '2024-05-05 11:51:33'),
('5918d467-0af7-11ef-abde-54ee752ae2f0', '5918d478-0af7-11ef-abde-54ee752ae2f0', 1, '2024-05-05 11:51:33', '2024-05-05 11:51:33'),
('591bf10d-0af7-11ef-abde-54ee752ae2f0', '591bf119-0af7-11ef-abde-54ee752ae2f0', 1, '2024-05-05 11:51:33', '2024-05-05 11:51:33'),
('59229cd1-0af7-11ef-abde-54ee752ae2f0', '59229ce0-0af7-11ef-abde-54ee752ae2f0', 1, '2024-05-05 11:51:34', '2024-05-05 11:51:34'),
('59322142-0af7-11ef-abde-54ee752ae2f0', '5932216c-0af7-11ef-abde-54ee752ae2f0', 1, '2024-05-05 11:51:34', '2024-05-05 11:51:34'),
('593ed70a-0af7-11ef-abde-54ee752ae2f0', '593ed724-0af7-11ef-abde-54ee752ae2f0', 1, '2024-05-05 11:51:34', '2024-05-05 11:51:34'),
('5943593e-0af7-11ef-abde-54ee752ae2f0', '59435959-0af7-11ef-abde-54ee752ae2f0', 1, '2024-05-05 11:51:34', '2024-05-05 11:51:34'),
('5948783e-0af7-11ef-abde-54ee752ae2f0', '59487858-0af7-11ef-abde-54ee752ae2f0', 1, '2024-05-05 11:51:34', '2024-05-05 11:51:34'),
('594f4438-0af7-11ef-abde-54ee752ae2f0', '594f4453-0af7-11ef-abde-54ee752ae2f0', 1, '2024-05-05 11:51:34', '2024-05-05 11:51:34'),
('5953fca7-0af7-11ef-abde-54ee752ae2f0', '5953fcc1-0af7-11ef-abde-54ee752ae2f0', 1, '2024-05-05 11:51:34', '2024-05-05 11:51:34');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
