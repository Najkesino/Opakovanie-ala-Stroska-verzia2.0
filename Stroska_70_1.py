from random import *

def nahodna_veta():
    kto = choice(('Kamarát','Spolužiak','Andrej','Roman', 'Marek', 'Dano', 'Pele'))
    corobil = choice(('videl','prezradil','povedal','napísal','zistil','nakreslil', 'urobil', 'pokazil', 'opravil'))
    ake = choice(('veľké','malé','obrovské','drobné','smutné','veselé', 'zábavné', 'hlúpe', 'podivné'))
    co = choice(('tajomstvo','prekvapenie','predsavzatie', 'nezmysli', 'klamstvá'))
    spojene = kto +' '+corobil+' '+ake+' '+co+'.'
    print(spojene)

for i in range(1,21):
    nahodna_veta()
