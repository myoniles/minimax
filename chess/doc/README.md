---
title: ReadMe: Design Doc
author: myoniles
date: \today
geometry: margin=1in
---

# Chess game design

I am currently torn over giving a list of `Piece` references to the `Player` or to the `Board` object.
For either option, or even if I give a list to both, the `possible moves` method could resemble the composite pattern.
*(Although not fully because I do not intend to implement an interface/class for one method.)*
At the moment, I am leaning towards giving this list of pointers to the player, so that a playr function does not see moves that it cannot do.
Giving the references to the board however does have its advantages: chiefly that the `Board` becomes more like an interface that players can interact with rather than trusitng that a `Player` method gave the currect possible moves.
Only time will tell which is better.

