from libnum import n2s,s2n
from gmpy2 import invert,gcdext,powmod
from math import pow
n=int(0x67755F890795644EC27E68892B94042C78334C34F9A6D8B6AA488D9B424D64A8B9B2DCC91B1D098A09D7AC4F9A06A4B5267F88F8968B4BAD29235D9A80330845F126B9A865F44C7A77DF72F763F553E99020745F40C8D97F0AB906154FBB1020B588F441F712B2377505B644FE36A78743EE4995B42C7B17B8DF4782EBB595097EE1BE74143261893C4EE2C140DC469E32B17F8AB30E25F07164506B4E79C6B4E3AF5BEA0268427FFB1134FB90A5122729C4EEF17B6D0B12CFBA4E7F14E27AA3C2B4F978E75163242EBD5CBD73829336F9A120E86E25D69CAE0229FDCCEB5B35DC630187B0EEF1532EEC546F4037A6EAB0D0207199B9566011A52F8E9ACD7261)
e1=117
e2=65537
f1=open('cipher1.txt','r')
f2=open('cipher2.txt','r')
c1=s2n(f1.read())
c2=s2n(f2.read())
_,s1,s2=gcdext(e1,e2)
s1=30808
s2=55
c2_=invert(c2,n)
m=(powmod(c1,s1,n)*powmod(c2_,s2,n))%n
print(n2s(m))
f1.close()
f2.close()

def common_modulus(n, e1, e2, c1, c2):
    """
    ref: https://crypto.stackexchange.com/questions/16283/how-to-use-common-modulus-attack
    ∵gcd(e1,e2)==1,∴由扩展欧几里得算法，存在e1*s1+e2*s2==1
    ∴m==m^1==m^(e1*s1+e2*s2)==((m^e1)^s1)*((m^e2)^s2)==(c1^s1)*(c2^s2)
    """
    assert (libnum.gcd(e1, e2) == 1)
    _, s1, s2 = gmpy2.gcdext(e1, e2)
    # 若s1<0，则c1^s1==(c1^-1)^(-s1)，其中c1^-1为c1模n的逆元。
    m = pow(c1, s1, n) if s1 > 0 else pow(gmpy2.invert(c1, n), -s1, n)
    m *= pow(c2, s2, n) if s2 > 0 else pow(gmpy2.invert(c2, n), -s2, n)
    return m % n