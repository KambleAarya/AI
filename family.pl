% Facts
male(john).   male(paul).   male(james).   male(robert).   male(steve).
female(mary). female(linda). female(alice). female(susan). female(claire).

parent(john, paul).      parent(john, linda).
parent(mary, paul).      parent(mary, linda).
parent(paul, james).     parent(alice, james).
parent(paul, susan).     parent(alice, susan).
parent(james, robert).   parent(claire, robert).
parent(linda, steve).    parent(steve, claire).

% Rules
father(X, Y) :- male(X), parent(X, Y).
mother(X, Y) :- female(X), parent(X, Y).
sibling(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y.
grandparent(X, Y) :- parent(X, Z), parent(Z, Y).
grandmother(X, Y) :- female(X), grandparent(X, Y).
grandfather(X, Y) :- male(X), grandparent(X, Y).
ancestor(X, Y) :- parent(X, Y).
ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y).