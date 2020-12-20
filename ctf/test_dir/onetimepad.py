from libnum import n2s
def str2num(s):
    return int(s.encode('hex'), 16)

def process(m, k):
    tmp = m ^ k
    res = 0
    for i in bin(tmp)[2:]:
        res = res << 1
        if (int(i)):
            res = res ^ tmp
        if (res >> 256):
            res = res ^ P
    return res

fake_secret1 = "I_am_not_a_secret_so_you_know_me"
fake_secret2 = "feeddeadbeefcafefeeddeadbeefcafe"
flag=0xaf3fcc28377e7e983355096fd4f635856df82bbab61d2c50892d9ee5d913a07f
ctxt2=0x630eb4dce274d29a16f86940f2f35253477665949170ed9e8c9e828794b5543c
ctxt3=0xe913db07cbe4f433c7cdeaac549757d23651ebdccf69d7fbdfd5dc2829334d1b
P = 0x10000000000000000000000000000000000000000000000000000000000000425L
key2=0
key3=0
key2=ctxt2^str2num(fake_secret1)
key3=ctxt3^str2num(fake_secret2)

k2=0x2a51d5b1bd1abdee4999363397902036332916fbce0982ebd3f5ece8e3ea3959L
k3=0x8f76be63af819557a5a88fca37f631b750348eb8ab0cb69fbdb0b94e4a522b7eL
kt=k3
for i in range(255):
    kt=process(kt,0)
seed=kt^k2


kt=k2
for i in range(255):
    kt=process(kt,0)
k1=kt^seed
print(n2s(flag^k1))