create table developers(
    d_id serial primary key,
    name varchar(50) not null,
    country varchar(50) not null,
    founded_year int check(founded_year>1800),
    website varchar(255)
);

create table games(
    g_id serial primary key,
    title varchar(100) not null,
    genre varchar(100) not null,
    release_date date not null,
    price decimal(10,2) not null check(price>=0),
    d_id int not null,
    constraint fk_game_developer foreign key(d_id) references developers(d_id)
);

create table customers(
    c_id serial primary key,
    name varchar(100) not null,
    email varchar(100) unique not null
);

create table purchases(
    p_id serial primary key,
    c_id int not null,
    g_id int not null,
    p_date timestamp default_current_timestamp,
    p_price decimal(10,2) not null check p_price>=0,
    constraint fk_purchase_customer foreign key (c_id) references customers(c_id),
    constraint fk_purchase_game foreign key (g_id) references games(g_id)
);

create table reviews(
    review_id serial primary key,
    c_id int not null,
    g_id int not null,
    rating int not null check(rating between 1 and 5),
    comment text,
    created_at timestamp default_current_timestamp,

    CONSTRAINT fk_review_customer
        FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id),

    CONSTRAINT fk_review_game
        FOREIGN KEY (game_id)
        REFERENCES games(game_id)
)