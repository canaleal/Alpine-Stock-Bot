CREATE TABLE pageinfo(
	page_id serial PRIMARY KEY,
	page_name VARCHAR ( 50 ) UNIQUE NOT NULL,
	page_code VARCHAR ( 10 ) NOT NULL,
	description varchar (50) NULL,
	created_by int not null,
	created_on TIMESTAMP NOT NULL,
    updated_by int null,
    created_BY TIMESTAMP NOT NULL,
    CONSTRAINT fk_created_by
        FOREIGN KEY(created_by ) 
        REFERENCES users(id),
    CONSTRAINT fk_updated_by
        FOREIGN KEY(updated_by ) 
        REFERENCES users(id)

);

CREATE TABLE pageinfoelement(
    page_element_id serial PRIMARY KEY,
    page_id int NOT NULL,
    element_id char(1) NOT NULL,
    description longtext NULL,
    created_by int not null,
    created_on TIMESTAMP NOT NULL,
    updated_by int null,
    created_BY TIMESTAMP NOT NULL,
    CONSTRAINT fk_created_by
        FOREIGN KEY(created_by ) 
        REFERENCES users(id),
    CONSTRAINT fk_updated_by
        FOREIGN KEY(updated_by ) 
        REFERENCES users(id)
);
