begin;

create table district (
    id   serial              primary key,
    name varchar(100)        not null
);

create table city (
    id   serial              primary key,
    name varchar(150)        not null
);

create table address (
    id          serial       primary key,
    district_id integer      not null references district(id),
    city_id     integer      not null references city(id),
    post_code   varchar(50),
    address     varchar(150)
);

create table business_org (
    id         serial        primary key,
    name       varchar(1000) not null,
    name_short varchar(500)  not null,
    inn        char(15)      not null,
    ogm        varchar(20)   not null,
    address_id integer       not null references address(id)
);

create table business_man (
    id          serial       primary key,
    last_name   varchar(100) not null,
    first_name  varchar(100) not null,
    middle_name varchar(100) not null,
    inn         char(15)     not null,
    ogn         char(16)     not null,
    address_id  integer      not null references address(id)
);

create table owner (
    id                       serial  primary key,
    business_org_id          integer references business_org(id),
    business_man_id          integer references business_man(id)
);

create table owner_contact (
    id       serial          primary key,
    owner_id integer         not null references owner(id)
);

create type Role_Code AS enum ('default', 'admin');
create table "user" (
    id        serial         primary key,
    role_code Role_Code      not null
);

create table industry (
    id   serial              primary key,
    name varchar(150)        not null
);

create table project (
    id               serial         primary key,
    user_id          integer        not null references "user"(id),
    owner_id         integer        not null references owner(id),
    address_id       integer        not null references address(id),
    industry_id      integer        not null references industry(id),
    name             varchar(500)   not null,
    app_own_amount   real,
    app_sup_amount   real,
    work_place_count integer        not null,
    tax_amount       integer,       -- TODO: currency?
    desk             integer[1000]  -- TODO: Понять че это
);

create type Decision_Type as enum ('');
create table decision (
    id              serial          primary key,
    project_id      integer         not null references project(id),
    decision_type   Decision_Type   not null,
    decision_date   date            not null,
    protocol_number varchar(50)     not null,
    decision        varchar(1000)   not null
);

create type Support_Type_Code as enum ('');
create type Unit_Type_Code    as enum ('');
create table support (
    id                 serial       primary key,
    project_id         integer      not null references project(id),
    support_program_id integer      not null,
    support_org_id     integer      not null,
    type_code          Support_Type_Code,
    unit_code          Unit_Type_Code,
    date_start         date,
    date_end           date,
    amount             real,
    descr              varchar(500)
);

commit;