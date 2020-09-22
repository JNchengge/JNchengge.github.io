import numpy as np
a=np.array([4,5,6])
b=np.expand_dims(a,axis=0)
c=np.squeeze(b)
print(c)