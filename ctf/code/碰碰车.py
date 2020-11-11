from hashlib import md5
alphbet='A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 1 2 3 4 5 6 7 8 9 0 a b c d e f g h i j k l m n o p q r s t u v w x y z'
alphbet=alphbet.split(' ')
f=open('h','w')
for a in range(len(alphbet)):
    for b in range(len(alphbet)):
        for c in range(len(alphbet)):
            s='AGVSCF'+alphbet[a]+'TZV'+alphbet[b]+'WBGVHC'+alphbet[c]+'U'
            hl=md5()
            hl.update(s.encode(encoding='UTF-8'))
            h=hl.hexdigest()
            f.write(h+'\n')
            if ('a8f738' in h) and ('5ea5' in h) and ('80865' in h) and ('af' in h):
                print(s)
f.close()