a=5
b=3
c=7

rhs_result=(a+b)+c
lhs_result=a+(b+c)

assosiative_law_holds=rhs_result==lhs_result
print("rhs result({}+{})+{}={}",rhs_result)
print("lhs result{}+({}+{})={}",lhs_result)

if assosiative_law_holds:
    print("Assosiative law hods addition")
else:
    print("Assosiative law not hold addition")

#Assosiative law multiplication
'''a=5
b=3
c=7
rhs_result=(a*b)*c
lhs_result=a*(b*c)

assosiative_law_holds=rhs_result==lhs_result
print("rhs result({}*{})*{}={}".format(a,b,c,rhs_result))
print("lhs result{}*({}*{})={}".format(a,b,c,lhs_result))

if assosiative_law_holds:
    print("assosiative law holds multiplication")
else:
    print("assosiative law doe not holds multiplication")'''

#distributive law

'''a=2
b=3
c=4
rhs=a*(b+c)
lhs=(a*b)+(a*c)
distributive_law=rhs==lhs
print("rhs a*(b+c)",rhs)
print("lhs(a*b)+(a*c)",lhs)

if distributive_law:
    print("distributive law holds for addition over multipliction")
else:
    print("distributive law does not holds for addition over multiplication")'''
