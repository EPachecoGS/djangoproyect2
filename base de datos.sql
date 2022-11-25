create table usuarios(
	idusuario serial primary key not null,
	nombre varchar(20),
	contrasena varchar(20)
)

select * from usuarios

Alter table usuarios
Rename column contrasena to lastname

insert into usuarios (nombre, contrasena) values ('Epacheco', 'EP123')

insert into usuarios (nombre, contrasena) values ('Rogdrigo', 'Rodrigo123')

insert into usuarios (nombre, contrasena) values ('Andres', 'Andres123')


 