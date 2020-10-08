1. 选取一对互素的素数p,q
2. 计算pq的乘积n
3. 计算n的欧拉函数,`φ(n)=(p-1)(q-1)`
4. 选取e，使得(e,n)=1，(e,n)作为公钥对
5. 计算私钥d，使得ed=1(mod φ(n))，(d,n)作为私钥对

# 加密
- 使用公钥e进行加密
```
m^e≡c(mod n)
```

# 解密
- 使用私钥d进行解密
```
c^d≡m(mod n)
```

