from sage.schemes.toric.weierstrass import j_invariant
R.<x,y,z,m>=QQ[];
f_m=x^3+y^3+z^3+m*x*y*z
j=j_invariant(f_m, variables=[x,y,z])
show(j)
