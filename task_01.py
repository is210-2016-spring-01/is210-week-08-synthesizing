#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week-08 Synthesizing Tasks"""

col= {
	'Seattle Gray':('Accent',['Ceramic Glaze','Cumulus Nimbus']),	
	'Manatee':('Accent',['Platinum Mist','Spartan Sage']),
	'Ceramic Glaze':('Highlight',['Basically White','White']),	        
	'Cumulus Nimbus':('Highlight',['Off-White','Paper White']),	
	'Platinum Mist':('Highlight',['Bone White','Just White']),	
	'Spartan Sage':('Highlight',['Fractal White','Not White'])
     }

c1 = 'Seattle Gray'
c2 = 'Manatee'
type = 'Base'
res = 'Your selected colors are'

while 1:
    inputc = raw_input("Which {0} color, \"{1}\" or \"{2}\"?:"
                       .format(type,c1,c2))
    if col.has_key(inputc):
        c1 = col[inputc][1][0]
        c2 = col[inputc][1][1]
    type = col[inputc][0]
    res = res + ", " + inputc

    else:
    res = res + ", and "+inputc
    break

print res
	
