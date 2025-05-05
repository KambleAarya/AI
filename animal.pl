% Facts
has_covering(lion, hair).
has_covering(eagle, feathers).
has_covering(fish, scales).
has_covering(crocodile, scales).

lays_eggs(eagle).
lays_eggs(fish).
lays_eggs(crocodile).

gives_birth(lion).
gives_birth(human).
gives_birth(whale).

% Rules
mammal(X) :- has_covering(X, hair), gives_birth(X).
bird(X) :- has_covering(X, feathers), lays_eggs(X).
reptile(X) :- has_covering(X, scales), lays_eggs(X), \+ bird(X), \+ fish(X).
fish(X) :- has_covering(X, scales), lays_eggs(X), swims(X).

swims(fish).
swims(whale).
swims(crocodile).

% Example Query
% ?- mammal(whale). → true
% ?- bird(eagle). → true