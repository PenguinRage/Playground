""" 
(         )                     (            ____ 
 )\ )   ( /(    (     *   )      )\ )  *   ) |   / 
(()/(   )\())   )\  ` )  /( (   (()/(` )  /( |  /  
 /(_)) ((_)\  (((_)  ( )(_)))\   /(_))( )(_))| /   
(_))_    ((_) )\___ (_(_())((_) (_)) (_(_()) |/    
 |   \  / _ \((/ __||_   _|| __|/ __||_   _|(      
 | |) || (_) || (__   | |  | _| \__ \  | |  )\     
 |___/  \___/  \___|  |_|  |___||___/  |_| ((_)    
                                                   
"""

def bound(minval, value, maxval):
	"""bound(number, number, number) -> number
	This function compares the min and max to the value."""
	
	"""
	>>> bound(2,3,4)
	3
	>>> bound(9,2,4)
	9
	>>> bound(1,4,3)
	4
	"""
	if minval > value:
		return minval
	elif maxval < value:
		return maxval
	else:
		return value

import doctest
doctest.testmod()