CREATE DATABASE IF NOT EXISTS prueba;

USE prueba;

CREATE TABLE IF NOT EXISTS Cargos (
    id INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(255) NOT NULL,
    grado INT NOT NULL,
    genero VARCHAR(255) NOT NULL,
    nacionalidad VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
);


CREATE TABLE IF NOT EXISTS Rentas (
    id INT NOT NULL AUTO_INCREMENT,
    cargo_id INT,
    renta_bruta FLOAT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (cargo_id) REFERENCES Cargos(id)
);
