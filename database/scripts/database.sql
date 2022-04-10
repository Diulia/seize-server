create table crises (
    id serial primary key,
    descricao varchar(50) not null
);

create table fatores (
    id serial primary key,
    descricao varchar(50) not null
);

create table registros (
    id serial primary key,
    dia date not null,
    crise_id int not null references crises (id),
    fator_id int not null references fatores (id)
);