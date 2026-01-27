-- Añadir tipos de usuario
INSERT INTO tb_usuarios_tipos (nombre) VALUES ('administrador');
INSERT INTO tb_usuarios_tipos (nombre) VALUES ('cliente');

-- Añadir usuarios
-- Supongamos que los IDs de los tipos son 1 para 'administrador' y 2 para 'cliente'
INSERT INTO tb_usuarios (tipo_usuario_id, nombre, email, contraseña) VALUES (1, 'Juan Admin', 'juan.admin@example.com', 'pass123');
INSERT INTO tb_usuarios (tipo_usuario_id, nombre, email, contraseña) VALUES (2, 'Ana Cliente', 'ana.cliente@example.com', 'pass456');
INSERT INTO tb_usuarios (tipo_usuario_id, nombre, email, contraseña) VALUES (2, 'Luis Cliente', 'luis.cliente@example.com', 'pass789');
INSERT INTO tb_usuarios (tipo_usuario_id, nombre, email, contraseña) VALUES (2, 'María Cliente', 'maria.cliente@example.com', 'pass101');
INSERT INTO tb_usuarios (tipo_usuario_id, nombre, email, contraseña) VALUES (2, 'Carlos Cliente', 'carlos.cliente@example.com', 'pass112');