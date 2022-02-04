CREATE TABLE IF NOT EXISTS  animes(
    id				BIGSERIAL		PRIMARY KEY,
    anime			VARCHAR(100)	NOT NULL UNIQUE,
    released_date	DATE			NOT NULL,
    seasons			INTEGER			NOT NULL
);

INSERT INTO 
    animes(anime, released_date, seasons)
VALUES
    ('naruto', '21/09/1999', 8),
    ('naruto shippuden', '15/02/2007', 9),
    ('hellsing', '10/10/2001', 1),
    ('death note', '03/10/2006', 1),
    ('Fullmetal Alchemist', '12/07/2001', 4);





-- {
-- 	"anime": "naruto",
-- 	"released_date": "21/09/1999",
-- 	"seasons": 8
-- }
-- {
-- 	"anime": "naruto shippuden",
-- 	"released_date": "15/02/2007",
-- 	"seasons": 9
-- }
-- {
-- 	"anime": "death note",
-- 	"released_date": "03/10/2006",
-- 	"seasons": 1
-- }
-- {
-- 	"anime": "Fullmetal Alchemist",
-- 	"released_date": "12/07/2001",
-- 	"seasons": 4
-- }
-- {
-- 	"anime": "hellsing",
-- 	"released_date": "10/10/2001",
-- 	"seasons": 1
-- }
