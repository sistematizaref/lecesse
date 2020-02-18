/*
 Navicat PostgreSQL Data Transfer

 Source Server         : localhost_5432
 Source Server Type    : PostgreSQL
 Source Server Version : 100010
 Source Host           : localhost:5432
 Source Catalog        : lecesse
 Source Schema         : public

 Target Server Type    : PostgreSQL
 Target Server Version : 100010
 File Encoding         : 65001

 Date: 17/02/2020 20:31:41
*/


-- ----------------------------
-- Sequence structure for auth_group_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."auth_group_id_seq";
CREATE SEQUENCE "public"."auth_group_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for auth_group_permissions_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."auth_group_permissions_id_seq";
CREATE SEQUENCE "public"."auth_group_permissions_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for auth_permission_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."auth_permission_id_seq";
CREATE SEQUENCE "public"."auth_permission_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for django_content_type_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."django_content_type_id_seq";
CREATE SEQUENCE "public"."django_content_type_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for django_migrations_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."django_migrations_id_seq";
CREATE SEQUENCE "public"."django_migrations_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for phase_one_category_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."phase_one_category_id_seq";
CREATE SEQUENCE "public"."phase_one_category_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for phase_one_material_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."phase_one_material_id_seq";
CREATE SEQUENCE "public"."phase_one_material_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for phase_one_subcategory_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."phase_one_subcategory_id_seq";
CREATE SEQUENCE "public"."phase_one_subcategory_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for phase_one_subcategorytwo_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."phase_one_subcategorytwo_id_seq";
CREATE SEQUENCE "public"."phase_one_subcategorytwo_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for phase_one_typemeasure_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."phase_one_typemeasure_id_seq";
CREATE SEQUENCE "public"."phase_one_typemeasure_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for users_customuser_groups_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."users_customuser_groups_id_seq";
CREATE SEQUENCE "public"."users_customuser_groups_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for users_customuser_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."users_customuser_id_seq";
CREATE SEQUENCE "public"."users_customuser_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for users_customuser_user_permissions_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."users_customuser_user_permissions_id_seq";
CREATE SEQUENCE "public"."users_customuser_user_permissions_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS "public"."auth_group";
CREATE TABLE "public"."auth_group" (
  "id" int4 NOT NULL DEFAULT nextval('auth_group_id_seq'::regclass),
  "name" varchar(150) COLLATE "pg_catalog"."default" NOT NULL
)
;

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS "public"."auth_group_permissions";
CREATE TABLE "public"."auth_group_permissions" (
  "id" int4 NOT NULL DEFAULT nextval('auth_group_permissions_id_seq'::regclass),
  "group_id" int4 NOT NULL,
  "permission_id" int4 NOT NULL
)
;

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS "public"."auth_permission";
CREATE TABLE "public"."auth_permission" (
  "id" int4 NOT NULL DEFAULT nextval('auth_permission_id_seq'::regclass),
  "name" varchar(255) COLLATE "pg_catalog"."default" NOT NULL,
  "content_type_id" int4 NOT NULL,
  "codename" varchar(100) COLLATE "pg_catalog"."default" NOT NULL
)
;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO "public"."auth_permission" VALUES (1, 'Can add permission', 1, 'add_permission');
INSERT INTO "public"."auth_permission" VALUES (2, 'Can change permission', 1, 'change_permission');
INSERT INTO "public"."auth_permission" VALUES (3, 'Can delete permission', 1, 'delete_permission');
INSERT INTO "public"."auth_permission" VALUES (4, 'Can view permission', 1, 'view_permission');
INSERT INTO "public"."auth_permission" VALUES (5, 'Can add group', 2, 'add_group');
INSERT INTO "public"."auth_permission" VALUES (6, 'Can change group', 2, 'change_group');
INSERT INTO "public"."auth_permission" VALUES (7, 'Can delete group', 2, 'delete_group');
INSERT INTO "public"."auth_permission" VALUES (8, 'Can view group', 2, 'view_group');
INSERT INTO "public"."auth_permission" VALUES (9, 'Can add content type', 3, 'add_contenttype');
INSERT INTO "public"."auth_permission" VALUES (10, 'Can change content type', 3, 'change_contenttype');
INSERT INTO "public"."auth_permission" VALUES (11, 'Can delete content type', 3, 'delete_contenttype');
INSERT INTO "public"."auth_permission" VALUES (12, 'Can view content type', 3, 'view_contenttype');
INSERT INTO "public"."auth_permission" VALUES (13, 'Can add session', 4, 'add_session');
INSERT INTO "public"."auth_permission" VALUES (14, 'Can change session', 4, 'change_session');
INSERT INTO "public"."auth_permission" VALUES (15, 'Can delete session', 4, 'delete_session');
INSERT INTO "public"."auth_permission" VALUES (16, 'Can view session', 4, 'view_session');
INSERT INTO "public"."auth_permission" VALUES (17, 'Can add user', 5, 'add_customuser');
INSERT INTO "public"."auth_permission" VALUES (18, 'Can change user', 5, 'change_customuser');
INSERT INTO "public"."auth_permission" VALUES (19, 'Can delete user', 5, 'delete_customuser');
INSERT INTO "public"."auth_permission" VALUES (20, 'Can view user', 5, 'view_customuser');
INSERT INTO "public"."auth_permission" VALUES (21, 'Can add subcategory', 6, 'add_subcategory');
INSERT INTO "public"."auth_permission" VALUES (22, 'Can change subcategory', 6, 'change_subcategory');
INSERT INTO "public"."auth_permission" VALUES (23, 'Can delete subcategory', 6, 'delete_subcategory');
INSERT INTO "public"."auth_permission" VALUES (24, 'Can view subcategory', 6, 'view_subcategory');
INSERT INTO "public"."auth_permission" VALUES (25, 'Can add subcategory two', 7, 'add_subcategorytwo');
INSERT INTO "public"."auth_permission" VALUES (26, 'Can change subcategory two', 7, 'change_subcategorytwo');
INSERT INTO "public"."auth_permission" VALUES (27, 'Can delete subcategory two', 7, 'delete_subcategorytwo');
INSERT INTO "public"."auth_permission" VALUES (28, 'Can view subcategory two', 7, 'view_subcategorytwo');
INSERT INTO "public"."auth_permission" VALUES (29, 'Can add category', 8, 'add_category');
INSERT INTO "public"."auth_permission" VALUES (30, 'Can change category', 8, 'change_category');
INSERT INTO "public"."auth_permission" VALUES (31, 'Can delete category', 8, 'delete_category');
INSERT INTO "public"."auth_permission" VALUES (32, 'Can view category', 8, 'view_category');
INSERT INTO "public"."auth_permission" VALUES (33, 'Can add type measure', 9, 'add_typemeasure');
INSERT INTO "public"."auth_permission" VALUES (34, 'Can change type measure', 9, 'change_typemeasure');
INSERT INTO "public"."auth_permission" VALUES (35, 'Can delete type measure', 9, 'delete_typemeasure');
INSERT INTO "public"."auth_permission" VALUES (36, 'Can view type measure', 9, 'view_typemeasure');
INSERT INTO "public"."auth_permission" VALUES (37, 'Can add material', 10, 'add_material');
INSERT INTO "public"."auth_permission" VALUES (38, 'Can change material', 10, 'change_material');
INSERT INTO "public"."auth_permission" VALUES (39, 'Can delete material', 10, 'delete_material');
INSERT INTO "public"."auth_permission" VALUES (40, 'Can view material', 10, 'view_material');

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS "public"."django_content_type";
CREATE TABLE "public"."django_content_type" (
  "id" int4 NOT NULL DEFAULT nextval('django_content_type_id_seq'::regclass),
  "app_label" varchar(100) COLLATE "pg_catalog"."default" NOT NULL,
  "model" varchar(100) COLLATE "pg_catalog"."default" NOT NULL
)
;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO "public"."django_content_type" VALUES (1, 'auth', 'permission');
INSERT INTO "public"."django_content_type" VALUES (2, 'auth', 'group');
INSERT INTO "public"."django_content_type" VALUES (3, 'contenttypes', 'contenttype');
INSERT INTO "public"."django_content_type" VALUES (4, 'sessions', 'session');
INSERT INTO "public"."django_content_type" VALUES (5, 'users', 'customuser');
INSERT INTO "public"."django_content_type" VALUES (6, 'phase_one', 'subcategory');
INSERT INTO "public"."django_content_type" VALUES (7, 'phase_one', 'subcategorytwo');
INSERT INTO "public"."django_content_type" VALUES (8, 'phase_one', 'category');
INSERT INTO "public"."django_content_type" VALUES (9, 'phase_one', 'typemeasure');
INSERT INTO "public"."django_content_type" VALUES (10, 'phase_one', 'material');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS "public"."django_migrations";
CREATE TABLE "public"."django_migrations" (
  "id" int4 NOT NULL DEFAULT nextval('django_migrations_id_seq'::regclass),
  "app" varchar(255) COLLATE "pg_catalog"."default" NOT NULL,
  "name" varchar(255) COLLATE "pg_catalog"."default" NOT NULL,
  "applied" timestamptz(6) NOT NULL
)
;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO "public"."django_migrations" VALUES (1, 'contenttypes', '0001_initial', '2020-02-15 17:09:57.696267-05');
INSERT INTO "public"."django_migrations" VALUES (2, 'contenttypes', '0002_remove_content_type_name', '2020-02-15 17:09:57.723315-05');
INSERT INTO "public"."django_migrations" VALUES (3, 'auth', '0001_initial', '2020-02-15 17:09:57.986593-05');
INSERT INTO "public"."django_migrations" VALUES (4, 'auth', '0002_alter_permission_name_max_length', '2020-02-15 17:09:58.322875-05');
INSERT INTO "public"."django_migrations" VALUES (5, 'auth', '0003_alter_user_email_max_length', '2020-02-15 17:09:58.365816-05');
INSERT INTO "public"."django_migrations" VALUES (6, 'auth', '0004_alter_user_username_opts', '2020-02-15 17:09:58.389484-05');
INSERT INTO "public"."django_migrations" VALUES (7, 'auth', '0005_alter_user_last_login_null', '2020-02-15 17:09:58.411763-05');
INSERT INTO "public"."django_migrations" VALUES (8, 'auth', '0006_require_contenttypes_0002', '2020-02-15 17:09:58.423999-05');
INSERT INTO "public"."django_migrations" VALUES (9, 'auth', '0007_alter_validators_add_error_messages', '2020-02-15 17:09:58.444807-05');
INSERT INTO "public"."django_migrations" VALUES (10, 'auth', '0008_alter_user_username_max_length', '2020-02-15 17:09:58.467203-05');
INSERT INTO "public"."django_migrations" VALUES (11, 'auth', '0009_alter_user_last_name_max_length', '2020-02-15 17:09:58.486566-05');
INSERT INTO "public"."django_migrations" VALUES (12, 'auth', '0010_alter_group_name_max_length', '2020-02-15 17:09:58.51132-05');
INSERT INTO "public"."django_migrations" VALUES (13, 'auth', '0011_update_proxy_permissions', '2020-02-15 17:09:58.532586-05');
INSERT INTO "public"."django_migrations" VALUES (14, 'base', '0001_initial', '2020-02-15 17:09:58.802592-05');
INSERT INTO "public"."django_migrations" VALUES (15, 'base', '0002_delete_customuser', '2020-02-15 17:09:59.171318-05');
INSERT INTO "public"."django_migrations" VALUES (16, 'sessions', '0001_initial', '2020-02-15 17:09:59.315287-05');
INSERT INTO "public"."django_migrations" VALUES (17, 'users', '0001_initial', '2020-02-15 17:09:59.739505-05');
INSERT INTO "public"."django_migrations" VALUES (18, 'phase_one', '0001_initial', '2020-02-16 15:07:44.003284-05');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS "public"."django_session";
CREATE TABLE "public"."django_session" (
  "session_key" varchar(40) COLLATE "pg_catalog"."default" NOT NULL,
  "session_data" text COLLATE "pg_catalog"."default" NOT NULL,
  "expire_date" timestamptz(6) NOT NULL
)
;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO "public"."django_session" VALUES ('b57df6gj55707oa3iyoedvnuypk2q8rn', 'YTRkOTMzMmMwMzdiOTQzN2VlOTNhMDkxNDcxMWNlMTU4OTNlMzc0NTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI3MzQ1MGQ5YTFmYzIwYTE1NDFkZjBlNTkyMDhlNjdmMjUwNjY4ZjAxIn0=', '2020-03-01 21:12:21.021127-05');
INSERT INTO "public"."django_session" VALUES ('omia9dxyp2ow51kii8u1aqqlqt2drevf', 'YTRkOTMzMmMwMzdiOTQzN2VlOTNhMDkxNDcxMWNlMTU4OTNlMzc0NTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI3MzQ1MGQ5YTFmYzIwYTE1NDFkZjBlNTkyMDhlNjdmMjUwNjY4ZjAxIn0=', '2020-03-02 19:42:34.031817-05');

-- ----------------------------
-- Table structure for phase_one_category
-- ----------------------------
DROP TABLE IF EXISTS "public"."phase_one_category";
CREATE TABLE "public"."phase_one_category" (
  "id" int4 NOT NULL DEFAULT nextval('phase_one_category_id_seq'::regclass),
  "name" varchar(100) COLLATE "pg_catalog"."default" NOT NULL,
  "created_at" timestamptz(6) NOT NULL,
  "updated_at" timestamptz(6) NOT NULL,
  "subcategory_id" int4 NOT NULL,
  "subcategory_two_id" int4
)
;

-- ----------------------------
-- Table structure for phase_one_material
-- ----------------------------
DROP TABLE IF EXISTS "public"."phase_one_material";
CREATE TABLE "public"."phase_one_material" (
  "id" int4 NOT NULL DEFAULT nextval('phase_one_material_id_seq'::regclass),
  "name" varchar(100) COLLATE "pg_catalog"."default" NOT NULL,
  "description" varchar(200) COLLATE "pg_catalog"."default" NOT NULL,
  "image" varchar(100) COLLATE "pg_catalog"."default" NOT NULL,
  "created_at" timestamptz(6) NOT NULL,
  "updated_at" timestamptz(6) NOT NULL,
  "category_id" int4 NOT NULL,
  "subcategory_id" int4 NOT NULL,
  "subcategory_two_id" int4 NOT NULL,
  "type_measure_id" int4 NOT NULL
)
;

-- ----------------------------
-- Table structure for phase_one_subcategory
-- ----------------------------
DROP TABLE IF EXISTS "public"."phase_one_subcategory";
CREATE TABLE "public"."phase_one_subcategory" (
  "id" int4 NOT NULL DEFAULT nextval('phase_one_subcategory_id_seq'::regclass),
  "name" varchar(100) COLLATE "pg_catalog"."default" NOT NULL,
  "created_at" timestamptz(6) NOT NULL,
  "updated_at" timestamptz(6) NOT NULL
)
;

-- ----------------------------
-- Table structure for phase_one_subcategorytwo
-- ----------------------------
DROP TABLE IF EXISTS "public"."phase_one_subcategorytwo";
CREATE TABLE "public"."phase_one_subcategorytwo" (
  "id" int4 NOT NULL DEFAULT nextval('phase_one_subcategorytwo_id_seq'::regclass),
  "name" varchar(100) COLLATE "pg_catalog"."default" NOT NULL,
  "created_at" timestamptz(6) NOT NULL,
  "updated_at" timestamptz(6) NOT NULL
)
;

-- ----------------------------
-- Table structure for phase_one_typemeasure
-- ----------------------------
DROP TABLE IF EXISTS "public"."phase_one_typemeasure";
CREATE TABLE "public"."phase_one_typemeasure" (
  "id" int4 NOT NULL DEFAULT nextval('phase_one_typemeasure_id_seq'::regclass),
  "name" varchar(100) COLLATE "pg_catalog"."default" NOT NULL
)
;

-- ----------------------------
-- Table structure for users_customuser
-- ----------------------------
DROP TABLE IF EXISTS "public"."users_customuser";
CREATE TABLE "public"."users_customuser" (
  "id" int4 NOT NULL DEFAULT nextval('users_customuser_id_seq'::regclass),
  "password" varchar(128) COLLATE "pg_catalog"."default" NOT NULL,
  "last_login" timestamptz(6),
  "is_superuser" bool NOT NULL,
  "first_name" varchar(30) COLLATE "pg_catalog"."default" NOT NULL,
  "last_name" varchar(150) COLLATE "pg_catalog"."default" NOT NULL,
  "is_staff" bool NOT NULL,
  "is_active" bool NOT NULL,
  "date_joined" timestamptz(6) NOT NULL,
  "email" varchar(254) COLLATE "pg_catalog"."default" NOT NULL,
  "document_number" varchar(150) COLLATE "pg_catalog"."default" NOT NULL,
  "phone_number" varchar(30) COLLATE "pg_catalog"."default" NOT NULL,
  "address" varchar(100) COLLATE "pg_catalog"."default" NOT NULL,
  "role" varchar(30) COLLATE "pg_catalog"."default" NOT NULL
)
;

-- ----------------------------
-- Records of users_customuser
-- ----------------------------
INSERT INTO "public"."users_customuser" VALUES (2, 'pbkdf2_sha256$150000$LcjqDAf2Hl9X$n6Whc6fdtiywouxQcMPE4ewt1884nS8OTs6w1ypQeiQ=', '2020-02-17 19:42:33.970369-05', 'f', 'Admin prueba', 'Admin prueba', 'f', 't', '2020-02-15 23:00:55.089951-05', 'adminprueba@mail.com', '12345678', '8974562', 'calle falsa 123', 'ADMINISTRATOR');

-- ----------------------------
-- Table structure for users_customuser_groups
-- ----------------------------
DROP TABLE IF EXISTS "public"."users_customuser_groups";
CREATE TABLE "public"."users_customuser_groups" (
  "id" int4 NOT NULL DEFAULT nextval('users_customuser_groups_id_seq'::regclass),
  "customuser_id" int4 NOT NULL,
  "group_id" int4 NOT NULL
)
;

-- ----------------------------
-- Table structure for users_customuser_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS "public"."users_customuser_user_permissions";
CREATE TABLE "public"."users_customuser_user_permissions" (
  "id" int4 NOT NULL DEFAULT nextval('users_customuser_user_permissions_id_seq'::regclass),
  "customuser_id" int4 NOT NULL,
  "permission_id" int4 NOT NULL
)
;

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."auth_group_id_seq"
OWNED BY "public"."auth_group"."id";
SELECT setval('"public"."auth_group_id_seq"', 2, false);
ALTER SEQUENCE "public"."auth_group_permissions_id_seq"
OWNED BY "public"."auth_group_permissions"."id";
SELECT setval('"public"."auth_group_permissions_id_seq"', 2, false);
ALTER SEQUENCE "public"."auth_permission_id_seq"
OWNED BY "public"."auth_permission"."id";
SELECT setval('"public"."auth_permission_id_seq"', 41, true);
ALTER SEQUENCE "public"."django_content_type_id_seq"
OWNED BY "public"."django_content_type"."id";
SELECT setval('"public"."django_content_type_id_seq"', 11, true);
ALTER SEQUENCE "public"."django_migrations_id_seq"
OWNED BY "public"."django_migrations"."id";
SELECT setval('"public"."django_migrations_id_seq"', 19, true);
ALTER SEQUENCE "public"."phase_one_category_id_seq"
OWNED BY "public"."phase_one_category"."id";
SELECT setval('"public"."phase_one_category_id_seq"', 2, false);
ALTER SEQUENCE "public"."phase_one_material_id_seq"
OWNED BY "public"."phase_one_material"."id";
SELECT setval('"public"."phase_one_material_id_seq"', 2, false);
ALTER SEQUENCE "public"."phase_one_subcategory_id_seq"
OWNED BY "public"."phase_one_subcategory"."id";
SELECT setval('"public"."phase_one_subcategory_id_seq"', 2, false);
ALTER SEQUENCE "public"."phase_one_subcategorytwo_id_seq"
OWNED BY "public"."phase_one_subcategorytwo"."id";
SELECT setval('"public"."phase_one_subcategorytwo_id_seq"', 2, false);
ALTER SEQUENCE "public"."phase_one_typemeasure_id_seq"
OWNED BY "public"."phase_one_typemeasure"."id";
SELECT setval('"public"."phase_one_typemeasure_id_seq"', 2, false);
ALTER SEQUENCE "public"."users_customuser_groups_id_seq"
OWNED BY "public"."users_customuser_groups"."id";
SELECT setval('"public"."users_customuser_groups_id_seq"', 2, false);
ALTER SEQUENCE "public"."users_customuser_id_seq"
OWNED BY "public"."users_customuser"."id";
SELECT setval('"public"."users_customuser_id_seq"', 4, true);
ALTER SEQUENCE "public"."users_customuser_user_permissions_id_seq"
OWNED BY "public"."users_customuser_user_permissions"."id";
SELECT setval('"public"."users_customuser_user_permissions_id_seq"', 2, false);

-- ----------------------------
-- Indexes structure for table auth_group
-- ----------------------------
CREATE INDEX "auth_group_name_a6ea08ec_like" ON "public"."auth_group" USING btree (
  "name" COLLATE "pg_catalog"."default" "pg_catalog"."varchar_pattern_ops" ASC NULLS LAST
);

-- ----------------------------
-- Uniques structure for table auth_group
-- ----------------------------
ALTER TABLE "public"."auth_group" ADD CONSTRAINT "auth_group_name_key" UNIQUE ("name");

-- ----------------------------
-- Primary Key structure for table auth_group
-- ----------------------------
ALTER TABLE "public"."auth_group" ADD CONSTRAINT "auth_group_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Indexes structure for table auth_group_permissions
-- ----------------------------
CREATE INDEX "auth_group_permissions_group_id_b120cbf9" ON "public"."auth_group_permissions" USING btree (
  "group_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);
CREATE INDEX "auth_group_permissions_permission_id_84c5c92e" ON "public"."auth_group_permissions" USING btree (
  "permission_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);

-- ----------------------------
-- Uniques structure for table auth_group_permissions
-- ----------------------------
ALTER TABLE "public"."auth_group_permissions" ADD CONSTRAINT "auth_group_permissions_group_id_permission_id_0cd325b0_uniq" UNIQUE ("group_id", "permission_id");

-- ----------------------------
-- Primary Key structure for table auth_group_permissions
-- ----------------------------
ALTER TABLE "public"."auth_group_permissions" ADD CONSTRAINT "auth_group_permissions_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Indexes structure for table auth_permission
-- ----------------------------
CREATE INDEX "auth_permission_content_type_id_2f476e4b" ON "public"."auth_permission" USING btree (
  "content_type_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);

-- ----------------------------
-- Uniques structure for table auth_permission
-- ----------------------------
ALTER TABLE "public"."auth_permission" ADD CONSTRAINT "auth_permission_content_type_id_codename_01ab375a_uniq" UNIQUE ("content_type_id", "codename");

-- ----------------------------
-- Primary Key structure for table auth_permission
-- ----------------------------
ALTER TABLE "public"."auth_permission" ADD CONSTRAINT "auth_permission_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Uniques structure for table django_content_type
-- ----------------------------
ALTER TABLE "public"."django_content_type" ADD CONSTRAINT "django_content_type_app_label_model_76bd3d3b_uniq" UNIQUE ("app_label", "model");

-- ----------------------------
-- Primary Key structure for table django_content_type
-- ----------------------------
ALTER TABLE "public"."django_content_type" ADD CONSTRAINT "django_content_type_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table django_migrations
-- ----------------------------
ALTER TABLE "public"."django_migrations" ADD CONSTRAINT "django_migrations_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Indexes structure for table django_session
-- ----------------------------
CREATE INDEX "django_session_expire_date_a5c62663" ON "public"."django_session" USING btree (
  "expire_date" "pg_catalog"."timestamptz_ops" ASC NULLS LAST
);
CREATE INDEX "django_session_session_key_c0390e0f_like" ON "public"."django_session" USING btree (
  "session_key" COLLATE "pg_catalog"."default" "pg_catalog"."varchar_pattern_ops" ASC NULLS LAST
);

-- ----------------------------
-- Primary Key structure for table django_session
-- ----------------------------
ALTER TABLE "public"."django_session" ADD CONSTRAINT "django_session_pkey" PRIMARY KEY ("session_key");

-- ----------------------------
-- Indexes structure for table phase_one_category
-- ----------------------------
CREATE INDEX "phase_one_category_subcategory_id_7060c826" ON "public"."phase_one_category" USING btree (
  "subcategory_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);
CREATE INDEX "phase_one_category_subcategory_two_id_55d308a5" ON "public"."phase_one_category" USING btree (
  "subcategory_two_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);

-- ----------------------------
-- Primary Key structure for table phase_one_category
-- ----------------------------
ALTER TABLE "public"."phase_one_category" ADD CONSTRAINT "phase_one_category_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Indexes structure for table phase_one_material
-- ----------------------------
CREATE INDEX "phase_one_material_category_id_1c36da6f" ON "public"."phase_one_material" USING btree (
  "category_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);
CREATE INDEX "phase_one_material_subcategory_id_9944cc96" ON "public"."phase_one_material" USING btree (
  "subcategory_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);
CREATE INDEX "phase_one_material_subcategory_two_id_806c62f5" ON "public"."phase_one_material" USING btree (
  "subcategory_two_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);
CREATE INDEX "phase_one_material_type_measure_id_0d263e2e" ON "public"."phase_one_material" USING btree (
  "type_measure_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);

-- ----------------------------
-- Primary Key structure for table phase_one_material
-- ----------------------------
ALTER TABLE "public"."phase_one_material" ADD CONSTRAINT "phase_one_material_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table phase_one_subcategory
-- ----------------------------
ALTER TABLE "public"."phase_one_subcategory" ADD CONSTRAINT "phase_one_subcategory_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table phase_one_subcategorytwo
-- ----------------------------
ALTER TABLE "public"."phase_one_subcategorytwo" ADD CONSTRAINT "phase_one_subcategorytwo_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table phase_one_typemeasure
-- ----------------------------
ALTER TABLE "public"."phase_one_typemeasure" ADD CONSTRAINT "phase_one_typemeasure_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Indexes structure for table users_customuser
-- ----------------------------
CREATE INDEX "users_customuser_email_6445acef_like" ON "public"."users_customuser" USING btree (
  "email" COLLATE "pg_catalog"."default" "pg_catalog"."varchar_pattern_ops" ASC NULLS LAST
);

-- ----------------------------
-- Uniques structure for table users_customuser
-- ----------------------------
ALTER TABLE "public"."users_customuser" ADD CONSTRAINT "users_customuser_email_key" UNIQUE ("email");

-- ----------------------------
-- Primary Key structure for table users_customuser
-- ----------------------------
ALTER TABLE "public"."users_customuser" ADD CONSTRAINT "users_customuser_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Indexes structure for table users_customuser_groups
-- ----------------------------
CREATE INDEX "users_customuser_groups_customuser_id_958147bf" ON "public"."users_customuser_groups" USING btree (
  "customuser_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);
CREATE INDEX "users_customuser_groups_group_id_01390b14" ON "public"."users_customuser_groups" USING btree (
  "group_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);

-- ----------------------------
-- Uniques structure for table users_customuser_groups
-- ----------------------------
ALTER TABLE "public"."users_customuser_groups" ADD CONSTRAINT "users_customuser_groups_customuser_id_group_id_76b619e3_uniq" UNIQUE ("customuser_id", "group_id");

-- ----------------------------
-- Primary Key structure for table users_customuser_groups
-- ----------------------------
ALTER TABLE "public"."users_customuser_groups" ADD CONSTRAINT "users_customuser_groups_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Indexes structure for table users_customuser_user_permissions
-- ----------------------------
CREATE INDEX "users_customuser_user_permissions_customuser_id_5771478b" ON "public"."users_customuser_user_permissions" USING btree (
  "customuser_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);
CREATE INDEX "users_customuser_user_permissions_permission_id_baaa2f74" ON "public"."users_customuser_user_permissions" USING btree (
  "permission_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);

-- ----------------------------
-- Uniques structure for table users_customuser_user_permissions
-- ----------------------------
ALTER TABLE "public"."users_customuser_user_permissions" ADD CONSTRAINT "users_customuser_user_pe_customuser_id_permission_7a7debf6_uniq" UNIQUE ("customuser_id", "permission_id");

-- ----------------------------
-- Primary Key structure for table users_customuser_user_permissions
-- ----------------------------
ALTER TABLE "public"."users_customuser_user_permissions" ADD CONSTRAINT "users_customuser_user_permissions_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Foreign Keys structure for table auth_group_permissions
-- ----------------------------
ALTER TABLE "public"."auth_group_permissions" ADD CONSTRAINT "auth_group_permissio_permission_id_84c5c92e_fk_auth_perm" FOREIGN KEY ("permission_id") REFERENCES "public"."auth_permission" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "public"."auth_group_permissions" ADD CONSTRAINT "auth_group_permissions_group_id_b120cbf9_fk_auth_group_id" FOREIGN KEY ("group_id") REFERENCES "public"."auth_group" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED;

-- ----------------------------
-- Foreign Keys structure for table auth_permission
-- ----------------------------
ALTER TABLE "public"."auth_permission" ADD CONSTRAINT "auth_permission_content_type_id_2f476e4b_fk_django_co" FOREIGN KEY ("content_type_id") REFERENCES "public"."django_content_type" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED;

-- ----------------------------
-- Foreign Keys structure for table phase_one_category
-- ----------------------------
ALTER TABLE "public"."phase_one_category" ADD CONSTRAINT "phase_one_category_subcategory_id_7060c826_fk_phase_one" FOREIGN KEY ("subcategory_id") REFERENCES "public"."phase_one_subcategory" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "public"."phase_one_category" ADD CONSTRAINT "phase_one_category_subcategory_two_id_55d308a5_fk_phase_one" FOREIGN KEY ("subcategory_two_id") REFERENCES "public"."phase_one_subcategorytwo" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED;

-- ----------------------------
-- Foreign Keys structure for table phase_one_material
-- ----------------------------
ALTER TABLE "public"."phase_one_material" ADD CONSTRAINT "phase_one_material_category_id_1c36da6f_fk_phase_one" FOREIGN KEY ("category_id") REFERENCES "public"."phase_one_category" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "public"."phase_one_material" ADD CONSTRAINT "phase_one_material_subcategory_id_9944cc96_fk_phase_one" FOREIGN KEY ("subcategory_id") REFERENCES "public"."phase_one_subcategory" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "public"."phase_one_material" ADD CONSTRAINT "phase_one_material_subcategory_two_id_806c62f5_fk_phase_one" FOREIGN KEY ("subcategory_two_id") REFERENCES "public"."phase_one_subcategorytwo" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "public"."phase_one_material" ADD CONSTRAINT "phase_one_material_type_measure_id_0d263e2e_fk_phase_one" FOREIGN KEY ("type_measure_id") REFERENCES "public"."phase_one_typemeasure" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED;

-- ----------------------------
-- Foreign Keys structure for table users_customuser_groups
-- ----------------------------
ALTER TABLE "public"."users_customuser_groups" ADD CONSTRAINT "users_customuser_gro_customuser_id_958147bf_fk_users_cus" FOREIGN KEY ("customuser_id") REFERENCES "public"."users_customuser" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "public"."users_customuser_groups" ADD CONSTRAINT "users_customuser_groups_group_id_01390b14_fk_auth_group_id" FOREIGN KEY ("group_id") REFERENCES "public"."auth_group" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED;

-- ----------------------------
-- Foreign Keys structure for table users_customuser_user_permissions
-- ----------------------------
ALTER TABLE "public"."users_customuser_user_permissions" ADD CONSTRAINT "users_customuser_use_customuser_id_5771478b_fk_users_cus" FOREIGN KEY ("customuser_id") REFERENCES "public"."users_customuser" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "public"."users_customuser_user_permissions" ADD CONSTRAINT "users_customuser_use_permission_id_baaa2f74_fk_auth_perm" FOREIGN KEY ("permission_id") REFERENCES "public"."auth_permission" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED;
