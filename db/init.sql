create database links;
use links;
CREATE TABLE images (
  title VARCHAR(150),
  link VARCHAR(150),
  image_description VARCHAR(150)
);
INSERT INTO images
  (title, link, image_description)
VALUES
  ('Klein bottle', 'https://upload.wikimedia.org/wikipedia/commons/2/2d/Wikistress4D_all_v1_zh.png', 'A picture of a Klein bottle'),
  ('Road', 'https://commons.wikimedia.org/wiki/File:New_Road,_Armitage_-_geograph.org.uk_-_2087075.jpg', 'A picture of a road'),
  ('Caddis fly', 'https://upload.wikimedia.org/wikipedia/commons/f/fe/Caddis_fly_%28NH266%29_%2811134645134%29.jpg', 'A picture of a caddis fly');