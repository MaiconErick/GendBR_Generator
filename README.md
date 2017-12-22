# GendBR_Generator


This is a tool I developed to help me with the generation of GENDBR when translating Pokémon Games.

For those who don't know, GENDBR works like this:

If you're playing as a boy, there's a line like this: 
>"Forgive us, young **master**..."

And if you play as a girl: 
>"Forgive us, young **mistress**...",

These two cases are stored in the text file as:

>**"Forgive us, young _m[VAR GENDBR(00FF,0705)]asteristress_..."**

![GENDBR GENERATOR](https://i.imgur.com/mTTXKpj.png)

It has unicode support.
Python 2.7.
