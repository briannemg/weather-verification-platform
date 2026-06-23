DROP TABLE IF EXISTS verification_results;
DROP TABLE IF EXISTS observations;
DROP TABLE IF EXISTS forecasts;
DROP TABLE IF EXISTS locations;

CREATE TABLE locations (
    location_id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    latitude REAL NOT NULL,
    longitude REAL NOT NULL,
    timezone TEXT NOT NULL
);

CREATE TABLE forecasts (
    forecast_id INTEGER PRIMARY KEY AUTOINCREMENT,
    location_id TEXT NOT NULL,
    valid_time TEXT NOT NULL,
    temperature_f REAL,
    retrieved_at TEXT NOT NULL,
    FOREIGN KEY (location_id) REFERENCES locations(location_id)
);

CREATE TABLE observations (
    observation_id INTEGER PRIMARY KEY AUTOINCREMENT,
    location_id TEXT NOT NULL,
    valid_time TEXT NOT NULL,
    temperature_f REAL,
    retrieved_at TEXT NOT NULL,
    FOREIGN KEY (location_id) REFERENCES locations(location_id)
);

CREATE TABLE verification_results (
    verification_id INTEGER PRIMARY KEY AUTOINCREMENT,
    location_id TEXT NOT NULL,
    valid_time TEXT NOT NULL,
    forecast_temperature_f REAL,
    observed_temperature_f REAL,
    error_f REAL,
    absolute_error_f REAL,
    squared_error_f REAL,
    FOREIGN KEY (location_id) REFERENCES locations(location_id)
);