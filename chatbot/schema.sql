DROP TABLE IF EXISTS order;
DROP TABLE IF EXISTS query;
DROP TABLE IF EXISTS inventory;
CREATE TABLE query (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  queryText TEXT NOT NULL,
  queryAction TEXT NOT NULL,
  params TEXT,
  fulfillmentText TEXT,
  intentMatched TEXT
);

CREATE TABLE order (
  order_id INTEGER PRIMARY KEY AUTOINCREMENt,
  ordername TEXT
);

CREATE TABLE inventory (
  product_id INTEGER PRIMARY KEY AUTOINCREMENT,
  product_name INTEGER NOT NULL,
  product_price INTEGER NOT NULL,
  quantity INTEGER
);

