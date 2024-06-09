DELIMITER $$

CREATE PROCEDURE Insertar_adquisicion_libro (IN p_adqui_code int, IN p_libro_code int, IN p_prov_code int, IN p_afdqui_fecha date, IN p_adqui_costo float) 
BEGIN
    INSERT INTO adquisicion_libro (adqui_code, libro_code, prov_code, afdqui_fecha, adqui_costo) VALUES (p_adqui_code, p_libro_code, p_prov_code, p_afdqui_fecha, p_adqui_costo);
END $$

CREATE PROCEDURE ObtenerTodos_adquisicion_libro () 
BEGIN
    SELECT * FROM adquisicion_libro;
END $$

CREATE PROCEDURE Insertar_autor (IN p_autor_code int, IN p_autor_nombres varchar(255), IN p_autor_apellidos varchar(255), IN p_ciudad varchar(255), IN p_pais varchar(255)) 
BEGIN
    INSERT INTO autor (autor_code, autor_nombres, autor_apellidos, ciudad, pais) VALUES (p_autor_code, p_autor_nombres, p_autor_apellidos, p_ciudad, p_pais);
END $$

CREATE PROCEDURE ObtenerTodos_autor () 
BEGIN
    SELECT * FROM autor;
END $$

CREATE PROCEDURE Insertar_biblioteca (IN p_bilbioteca_code int, IN p_ciudad_code int, IN p_biblioteca_name varchar(255), IN p_bdireccion varchar(255)) 
BEGIN
    INSERT INTO biblioteca (bilbioteca_code, ciudad_code, biblioteca_name, bdireccion) VALUES (p_bilbioteca_code, p_ciudad_code, p_biblioteca_name, p_bdireccion);
END $$

CREATE PROCEDURE ObtenerTodos_biblioteca () 
BEGIN
    SELECT * FROM biblioteca;
END $$

CREATE PROCEDURE Insertar_bibliotecario (IN p_bibli_code int, IN p_biblioteca_code int, IN p_bilbi_nombre varchar(255), IN p_bibli_apellido varchar(255), IN p_bibli_jornada varchar(255), IN p_bibli_telefono varchar(255)) 
BEGIN
    INSERT INTO bibliotecario (bibli_code, biblioteca_code, bilbi_nombre, bibli_apellido, bibli_jornada, bibli_telefono) VALUES (p_bibli_code, p_biblioteca_code, p_bilbi_nombre, p_bibli_apellido, p_bibli_jornada, p_bibli_telefono);
END $$

CREATE PROCEDURE ObtenerTodos_bibliotecario () 
BEGIN
    SELECT * FROM bibliotecario;
END $$

CREATE PROCEDURE Insertar_centroestudio (IN p_cenestu_code int, IN p_cenestu_nombre varchar(255), IN p_cenestu_direccion varchar(255), IN p_cenestu_telef varchar(255)) 
BEGIN
    INSERT INTO centroestudio (cenestu_code, cenestu_nombre, cenestu_direccion, cenestu_telef) VALUES (p_cenestu_code, p_cenestu_nombre, p_cenestu_direccion, p_cenestu_telef);
END $$

CREATE PROCEDURE ObtenerTodos_centroestudio () 
BEGIN
    SELECT * FROM centroestudio;
END $$

CREATE PROCEDURE Insertar_ciudad (IN p_ciudad_code int, IN p_ciudad_nombre varchar(255)) 
BEGIN
    INSERT INTO ciudad (ciudad_code, ciudad_nombre) VALUES (p_ciudad_code, p_ciudad_nombre);
END $$

CREATE PROCEDURE ObtenerTodos_ciudad () 
BEGIN
    SELECT * FROM ciudad;
END $$

CREATE PROCEDURE Insertar_cliente (IN p_cliente_code int, IN p_cenestu_code int, IN p_ciudad_code int, IN p_cliente_cedula varchar(255), IN p_cliente_nombres varchar(255), IN p_cliente_apellidos varchar(255), IN p_cliente_telef varchar(255), IN p_cliente_direccion varchar(255)) 
BEGIN
    INSERT INTO cliente (cliente_code, cenestu_code, ciudad_code, cliente_cedula, cliente_nombres, cliente_apellidos, cliente_telef, cliente_direccion) VALUES (p_cliente_code, p_cenestu_code, p_ciudad_code, p_cliente_cedula, p_cliente_nombres, p_cliente_apellidos, p_cliente_telef, p_cliente_direccion);
END $$

CREATE PROCEDURE ObtenerTodos_cliente () 
BEGIN
    SELECT * FROM cliente;
END $$

CREATE PROCEDURE Insertar_detalleventa (IN p_dventa_code int, IN p_venta_code int, IN p_libro_code int, IN p_cliente_code int, IN p_cantidad int, IN p_precio float) 
BEGIN
    INSERT INTO detalleventa (dventa_code, venta_code, libro_code, cliente_code, cantidad, precio) VALUES (p_dventa_code, p_venta_code, p_libro_code, p_cliente_code, p_cantidad, p_precio);
END $$

CREATE PROCEDURE ObtenerTodos_detalleventa () 
BEGIN
    SELECT * FROM detalleventa;
END $$

CREATE PROCEDURE Insertar_edicion (IN p_edicion_code int, IN p_editorial_code int, IN p_edicion varchar(255)) 
BEGIN
    INSERT INTO edicion (edicion_code, editorial_code, edicion) VALUES (p_edicion_code, p_editorial_code, p_edicion);
END $$

CREATE PROCEDURE ObtenerTodos_edicion () 
BEGIN
    SELECT * FROM edicion;
END $$

CREATE PROCEDURE Insertar_editorial (IN p_editorial_code int, IN p_editorial_nombre varchar(255)) 
BEGIN
    INSERT INTO editorial (editorial_code, editorial_nombre) VALUES (p_editorial_code, p_editorial_nombre);
END $$

CREATE PROCEDURE ObtenerTodos_editorial () 
BEGIN
    SELECT * FROM editorial;
END $$

CREATE PROCEDURE Insertar_estadoprestamo (IN p_estado_code int, IN p_estado varchar(255)) 
BEGIN
    INSERT INTO estadoprestamo (estado_code, estado) VALUES (p_estado_code, p_estado);
END $$

CREATE PROCEDURE ObtenerTodos_estadoprestamo () 
BEGIN
    SELECT * FROM estadoprestamo;
END $$

CREATE PROCEDURE Insertar_genero (IN p_genero_code int, IN p_genero_nombre varchar(255)) 
BEGIN
    INSERT INTO genero (genero_code, genero_nombre) VALUES (p_genero_code, p_genero_nombre);
END $$

CREATE PROCEDURE ObtenerTodos_genero () 
BEGIN
    SELECT * FROM genero;
END $$

CREATE PROCEDURE Insertar_libro (IN p_libro_code int, IN p_genero_code int, IN p_editorial_code int, IN p_biblioteca_code int, IN p_edicion_code int, IN p_isbn varchar(255), IN p_libro_nombre varchar(255), IN p_libro_fecha_publi date, IN p_libro_descrip varchar(255), IN p_versiondigital varchar(255)) 
BEGIN
    INSERT INTO libro (libro_code, genero_code, editorial_code, biblioteca_code, edicion_code, isbn, libro_nombre, libro_fecha_publi, libro_descrip, versiondigital) VALUES (p_libro_code, p_genero_code, p_editorial_code, p_biblioteca_code, p_edicion_code, p_isbn, p_libro_nombre, p_libro_fecha_publi, p_libro_descrip, p_versiondigital);
END $$

CREATE PROCEDURE ObtenerTodos_libro () 
BEGIN
    SELECT * FROM libro;
END $$

CREATE PROCEDURE Insertar_libro_autor (IN p_libaut int, IN p_libro_code int, IN p_autor_code int) 
BEGIN
    INSERT INTO libro_autor (libaut, libro_code, autor_code) VALUES (p_libaut, p_libro_code, p_autor_code);
END $$

CREATE PROCEDURE ObtenerTodos_libro_autor () 
BEGIN
    SELECT * FROM libro_autor;
END $$

CREATE PROCEDURE Insertar_multas (IN p_multa_code int, IN p_prestamo_code int, IN p_multa_descripcion varchar(255), IN p_multa_valor float, IN p_multa_fecha date) 
BEGIN
    INSERT INTO multas (multa_code, prestamo_code, multa_descripcion, multa_valor, multa_fecha) VALUES (p_multa_code, p_prestamo_code, p_multa_descripcion, p_multa_valor, p_multa_fecha);
END $$

CREATE PROCEDURE ObtenerTodos_multas () 
BEGIN
    SELECT * FROM multas;
END $$

CREATE PROCEDURE Insertar_prestamo (IN p_prestamo_code int, IN p_cliente_code int, IN p_libro_code int, IN p_bibli_code int, IN p_estado_code int, IN p_fecha_prestamo date, IN p_fecha_max_devolucion date, IN p_fecha_real_devolucion date, IN p_precio_prestamo float) 
BEGIN
    INSERT INTO prestamo (prestamo_code, cliente_code, libro_code, bibli_code, estado_code, fecha_prestamo, fecha_max_devolucion, fecha_real_devolucion, precio_prestamo) VALUES (p_prestamo_code, p_cliente_code, p_libro_code, p_bibli_code, p_estado_code, p_fecha_prestamo, p_fecha_max_devolucion, p_fecha_real_devolucion, p_precio_prestamo);
END $$

CREATE PROCEDURE ObtenerTodos_prestamo () 
BEGIN
    SELECT * FROM prestamo;
END $$

CREATE PROCEDURE Insertar_proveedor (IN p_prov_code int, IN p_prov_nombre varchar(255), IN p_prov_direccion varchar(255), IN p_prov_telefono varchar(255), IN p_prov_email varchar(255)) 
BEGIN
    INSERT INTO proveedor (prov_code, prov_nombre, prov_direccion, prov_telefono, prov_email) VALUES (p_prov_code, p_prov_nombre, p_prov_direccion, p_prov_telefono, p_prov_email);
END $$

CREATE PROCEDURE ObtenerTodos_proveedor () 
BEGIN
    SELECT * FROM proveedor;
END $$

CREATE PROCEDURE Insertar_venta (IN p_venda_code int, IN p_bibli_code int, IN p_venta_fecha date) 
BEGIN
    INSERT INTO venta (venda_code, bibli_code, venta_fecha) VALUES (p_venda_code, p_bibli_code, p_venta_fecha);
END $$

CREATE PROCEDURE ObtenerTodos_venta () 
BEGIN
    SELECT * FROM venta;
END $$

DELIMITER ;
