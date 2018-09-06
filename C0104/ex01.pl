nota(joao,5.0).
nota(maria,6.0).
nota(joana,8.0).
nota(mariana,9.0).
nota(cleuza,8.5).
nota(jose,6.5).
nota(jaoquim,4.5).
nota(mara,4.0).
nota(mary,10.0).

aprovado(X):-
	nota(X,Y),Y>=7.

reprovado(X):-
	nota(X,Y),Y=<4.9.

recuperação(X):-
	nota(X,Y),Y>=5,Y<7.