-- ----------------------------
--  Table structure for customers
-- ----------------------------
DROP TABLE IF EXISTS "public"."customers";
CREATE TABLE "public"."customers" (
	"first_name" varchar(100) COLLATE "default",
	"id" int4 NOT NULL,
	"last_name" varchar(255) COLLATE "default"
)
WITH (OIDS=FALSE);

-- ----------------------------
--  Records of customers
-- ----------------------------
BEGIN;
INSERT INTO "public"."customers" VALUES ('Rolf', '1', 'Smith');
INSERT INTO "public"."customers" VALUES ('Jose', '2', 'Salvatierra');
INSERT INTO "public"."customers" VALUES ('Anne', '3', 'Watson');
INSERT INTO "public"."customers" VALUES ('Craig', '4', 'Scott');
INSERT INTO "public"."customers" VALUES ('Michael', '5', 'Adam');
COMMIT;

-- ----------------------------
--  Primary key structure for table customers
-- ----------------------------
ALTER TABLE "public"."customers" ADD PRIMARY KEY ("id") NOT DEFERRABLE INITIALLY IMMEDIATE;


--SELECT * from CUSTOMERS WHERE last_name LIKE '%t%';

--SELECT * from items INNER JOIN purchases on items.id = purchases.item_id
--INNER JOIN customers on purchases.customer_id = customers.id;

--SELECT customers.first_name, customers.last_name, COUNT(purchases.id)
--FROM customers LEFT JOIN purchases
--ON customers.id = purchases.customer_id
--GROUP BY customers.id;

--SELECT customers.first_name, customers.last_name, SUM(items.price) from items
--JOIN purchases on items.id = purchases.item_id
--JOIN customers on purchases.customer_id = customers.id
--GROUP BY customers.id;

--SELECT customers.first_name, customers.last_name, items.name, items.price FROM CUSTOMERS
--JOIN purchases on customers.id = purchases.customer_id
--JOIN items on purchases.item_id = items.id
--ORDER BY items.price;

--SELECT SUM(items.price) from purchases
--JOIN items ON purchases.item_id = items.id;

--SELECT customers.first_name, customers.last_name, SUM(items.price) AS "total spent" FROM items
--JOIN purchases on purchases.item_id = items.id
--JOIN customers on purchases.customer_id = customers.id
--GROUP BY customers.id
--ORDER BY "total spent" DESC
--LIMIT 3;

--CREATE sequence users_id_seq START 3; --Sequence Starter (Auto-Increment of sorts for MySql, Start details first postiion to start)

--ALTER table public.users
--ALTER column id
--SET default nextval('users_id_seq'); --Alter Table set sequence to column after setting table

-- ALTER SEQUENCE users_id_seq OWNED BY public.users.id; --Set sequent to a particular table

--CREATE INDEX users_name_index ON public.users(name); add index for search method

