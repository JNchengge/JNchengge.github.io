from libnum import n2s,s2n
ctxt1=0xaf3fcc28377e7e983355096fd4f635856df82bbab61d2c50892d9ee5d913a07f
ctxt2=0x630eb4dce274d29a16f86940f2f35253477665949170ed9e8c9e828794b5543c
ctxt3=0xe913db07cbe4f433c7cdeaac549757d23651ebdccf69d7fbdfd5dc2829334d1b
fake_secret1 = "I_am_not_a_secret_so_you_know_me"
fake_secret2 = "feeddeadbeefcafefeeddeadbeefcafe"
P = 0x10000000000000000000000000000000000000000000000000000000000000425
key2=ctxt2^s2n(fake_secret1)
key3=ctxt3^s2n(fake_secret2)