-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Feb 06, 2026 at 02:06 PM
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
-- Database: `django_login_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add student', 7, 'add_student'),
(26, 'Can change student', 7, 'change_student'),
(27, 'Can delete student', 7, 'delete_student'),
(28, 'Can view student', 7, 'view_student'),
(29, 'Can add teacher', 8, 'add_teacher'),
(30, 'Can change teacher', 8, 'change_teacher'),
(31, 'Can delete teacher', 8, 'delete_teacher'),
(32, 'Can view teacher', 8, 'view_teacher'),
(33, 'Can add mark', 9, 'add_mark'),
(34, 'Can change mark', 9, 'change_mark'),
(35, 'Can delete mark', 9, 'delete_mark'),
(36, 'Can view mark', 9, 'view_mark');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$600000$dLvO2IFOw8L9lXVuHXLjUe$e3snIS2GUkDPMQbKrjry/vR0K2eN+a+vPuxxH5TvWZY=', '2026-02-06 12:53:47.411079', 0, 'Admin', 'admin', '', 'admin@gmail.com', 0, 1, '2026-02-06 07:17:04.188872');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(9, 'form_register', 'mark'),
(7, 'form_register', 'student'),
(8, 'form_register', 'teacher'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2026-02-06 07:15:44.333502'),
(2, 'auth', '0001_initial', '2026-02-06 07:15:57.758571'),
(3, 'admin', '0001_initial', '2026-02-06 07:15:59.916330'),
(4, 'admin', '0002_logentry_remove_auto_add', '2026-02-06 07:15:59.982070'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2026-02-06 07:16:00.029846'),
(6, 'contenttypes', '0002_remove_content_type_name', '2026-02-06 07:16:00.951311'),
(7, 'auth', '0002_alter_permission_name_max_length', '2026-02-06 07:16:01.133037'),
(8, 'auth', '0003_alter_user_email_max_length', '2026-02-06 07:16:01.316892'),
(9, 'auth', '0004_alter_user_username_opts', '2026-02-06 07:16:01.372366'),
(10, 'auth', '0005_alter_user_last_login_null', '2026-02-06 07:16:02.059980'),
(11, 'auth', '0006_require_contenttypes_0002', '2026-02-06 07:16:02.109453'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2026-02-06 07:16:02.161464'),
(13, 'auth', '0008_alter_user_username_max_length', '2026-02-06 07:16:02.366936'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2026-02-06 07:16:02.516811'),
(15, 'auth', '0010_alter_group_name_max_length', '2026-02-06 07:16:03.166598'),
(16, 'auth', '0011_update_proxy_permissions', '2026-02-06 07:16:03.235026'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2026-02-06 07:16:03.543124'),
(18, 'form_register', '0001_initial', '2026-02-06 07:16:07.174189'),
(19, 'sessions', '0001_initial', '2026-02-06 07:16:07.893587'),
(20, 'form_register', '0002_alter_student_student_class', '2026-02-06 11:00:02.709932');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('4h2gfy5wnppo4i85jkbktko3tzfja3cp', '.eJxVjMsOgjAURP-la9O0l7ZYl-79BnK5D0FNSSisjP8uJCx0OXPOzNt0uC5Dt1aZu5HNxXhz-u16pKeUHfADy32yNJVlHnu7K_ag1d4mltf1cP8OBqzDtk7kcuNBQgQ4O2XJjWZNqATiInkGCiFASi06TQ155Taii8wgWwrm8wXXODfD:1voIS1:ohvkRoDHPCAmaLfqiGQ7U7285CaJd92HoAGke_nmt7U', '2026-02-20 09:48:33.455394'),
('7ehculp09jpgktwm2ttqfk7fi9thnq4m', '.eJxVjMsOgjAURP-la9O0l7ZYl-79BnK5D0FNSSisjP8uJCx0OXPOzNt0uC5Dt1aZu5HNxXhz-u16pKeUHfADy32yNJVlHnu7K_ag1d4mltf1cP8OBqzDtk7kcuNBQgQ4O2XJjWZNqATiInkGCiFASi06TQ155Taii8wgWwrm8wXXODfD:1voLLH:imNclwDndjZ3VTU8dIAU60KUWl-Qptnuk0TXlCUP2xc', '2026-02-20 12:53:47.664552');

-- --------------------------------------------------------

--
-- Table structure for table `form_register_mark`
--

CREATE TABLE `form_register_mark` (
  `id` bigint(20) NOT NULL,
  `subject` varchar(100) NOT NULL,
  `term` varchar(50) NOT NULL,
  `marks` double NOT NULL,
  `total_marks` double NOT NULL,
  `mark_type` varchar(10) NOT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `student_id` bigint(20) NOT NULL,
  `teacher_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `form_register_mark`
--

INSERT INTO `form_register_mark` (`id`, `subject`, `term`, `marks`, `total_marks`, `mark_type`, `created_at`, `student_id`, `teacher_id`) VALUES
(1, 'physics', 'Term 1', 40, 60, 'Quiz', '2026-02-06 11:02:55.743373', 2, 1);

-- --------------------------------------------------------

--
-- Table structure for table `form_register_student`
--

CREATE TABLE `form_register_student` (
  `id` bigint(20) NOT NULL,
  `student_firstname` varchar(100) NOT NULL,
  `student_lastname` varchar(100) NOT NULL,
  `student_class` varchar(10) NOT NULL,
  `student_dob` date NOT NULL,
  `student_email` varchar(254) DEFAULT NULL,
  `student_national_id` bigint(20) NOT NULL,
  `student_phone` bigint(20) NOT NULL,
  `student_address` varchar(255) NOT NULL,
  `primary_school` varchar(150) DEFAULT NULL,
  `secondary_school` varchar(150) DEFAULT NULL,
  `father_firstname` varchar(100) NOT NULL,
  `father_lastname` varchar(100) NOT NULL,
  `father_phone` bigint(20) NOT NULL,
  `father_email` varchar(254) DEFAULT NULL,
  `father_national_id` bigint(20) DEFAULT NULL,
  `father_occupation` varchar(100) DEFAULT NULL,
  `mother_firstname` varchar(100) NOT NULL,
  `mother_lastname` varchar(100) NOT NULL,
  `mother_phone` bigint(20) NOT NULL,
  `mother_email` varchar(254) DEFAULT NULL,
  `mother_national_id` bigint(20) DEFAULT NULL,
  `mother_occupation` varchar(100) DEFAULT NULL,
  `student_code` varchar(10) NOT NULL,
  `created_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `form_register_student`
--

INSERT INTO `form_register_student` (`id`, `student_firstname`, `student_lastname`, `student_class`, `student_dob`, `student_email`, `student_national_id`, `student_phone`, `student_address`, `primary_school`, `secondary_school`, `father_firstname`, `father_lastname`, `father_phone`, `father_email`, `father_national_id`, `father_occupation`, `mother_firstname`, `mother_lastname`, `mother_phone`, `mother_email`, `mother_national_id`, `mother_occupation`, `student_code`, `created_at`) VALUES
(1, 'NIYOKWIZERWA', 'jean pacifique', 'p4', '2026-02-06', 'niyokwizerwa@gmail.com', 98765, 34567890, 'kigali', 'fha', 'esmuram', 'batege', 'pacifique', 3456789, 'batege@gmail.com', 34567890, 'carpeter', 'nikuze', 'rose', 3456789, 'nikuzerose@gmail.com', 34567890, 'other', '417567NVSE', '2026-02-06 07:21:33.876342'),
(2, 'ramadan', 'mugisha', 'l4 sod', '2026-02-06', 'ITUZETONY@GMAIL.COM', 4567890, 345678, 'rwamagana', 'kayanza', 'sanzare/ acodes mushishiro', 'kalisa', 'erenest', 34567890, 'ayabagabo@gmail.com', 3456789, 'umucuruzi', 'dushimimana', 'asia', 3456789, 'nikuzerose@gmail.com', 3456789, 'other', '770039KHEV', '2026-02-06 11:01:37.361628');

-- --------------------------------------------------------

--
-- Table structure for table `form_register_teacher`
--

CREATE TABLE `form_register_teacher` (
  `id` bigint(20) NOT NULL,
  `firstname` varchar(100) NOT NULL,
  `lastname` varchar(100) NOT NULL,
  `phone` bigint(20) NOT NULL,
  `email` varchar(254) DEFAULT NULL,
  `subject` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `form_register_teacher`
--

INSERT INTO `form_register_teacher` (`id`, `firstname`, `lastname`, `phone`, `email`, `subject`) VALUES
(1, 'bosco', 'ndatimana', 9876543, 'niyokwizerwaj786@gmail.com', 'math');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `form_register_mark`
--
ALTER TABLE `form_register_mark`
  ADD PRIMARY KEY (`id`),
  ADD KEY `form_register_mark_student_id_ff90da9a_fk_form_regi` (`student_id`),
  ADD KEY `form_register_mark_teacher_id_268d20cf_fk_form_regi` (`teacher_id`);

--
-- Indexes for table `form_register_student`
--
ALTER TABLE `form_register_student`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `student_national_id` (`student_national_id`),
  ADD UNIQUE KEY `student_code` (`student_code`);

--
-- Indexes for table `form_register_teacher`
--
ALTER TABLE `form_register_teacher`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=37;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `form_register_mark`
--
ALTER TABLE `form_register_mark`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `form_register_student`
--
ALTER TABLE `form_register_student`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `form_register_teacher`
--
ALTER TABLE `form_register_teacher`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `form_register_mark`
--
ALTER TABLE `form_register_mark`
  ADD CONSTRAINT `form_register_mark_student_id_ff90da9a_fk_form_regi` FOREIGN KEY (`student_id`) REFERENCES `form_register_student` (`id`),
  ADD CONSTRAINT `form_register_mark_teacher_id_268d20cf_fk_form_regi` FOREIGN KEY (`teacher_id`) REFERENCES `form_register_teacher` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
