murderer(X) :- bagof(Y,contradictsPerson(X,Y),Ys), length(Ys,N), N >1.

contradictsPerson(A,B) :-
claims(A,AClaims), claims(B,BClaims), contradictsClaims(AClaims,BClaims).

contradictsClaims(Claims,[H|T]) :-
contradictsClaims1(Claims,H); contradictsClaims(Claims,T).
contradictsClaims1([H|T],C) :-
contradictsClaim(H,C); contradictsClaims1(T,C).
contradictsClaim([Claim1,Who],[Claim2,Who]) :-
contradictory(Claim1,Claim2).




