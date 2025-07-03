% Rooms and doors
room(kitchen).
room(hall).
room(bedroom).
room(balcony).
room(dining).

door(kitchen, hall).
door(hall, kitchen).
door(hall, balcony).
door(balcony, hall).
door(hall, dining).
door(dining, hall).
door(dining, bedroom).
door(bedroom, dining).

% Contents in rooms
contents(kitchen, utensils).
contents(hall, [tv, sofa]).
contents(dining, [chair, table]).
contents(bedroom, [bed, wardrobe]).
contents(balcony, shoerack).

% Two-way connection
connect(X, Y) :- door(X, Y), door(Y, X).

% Find connected rooms and what they contain
find_connected_rooms(X, Y, Z) :- connect(X, Y), contents(Y, Z).
