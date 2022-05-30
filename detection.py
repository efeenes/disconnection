from scipy.spatial import distance
from sklearn import preprocessing

def g_w(n, Mt, olap):
    ists = []
    ieds = []

    ist = 0
    while True:
        ied = ist + Mt
        if ied > n:
            break
        ists.append(ist)
        ieds.append(ied)
        ist += int(Mt * (1 - olap/100))
    return ists, ieds


data= preprocessing.normalize(data)
i1=0
i2=0
cc=[]

for i1 in range(len(data)):
    n = 3840
    x = data[i1]
    ists, ieds = g_w(n, Mt=64, olap=0)
    X = np.array([x[ist:ied] for ist, ied in zip(ists, ieds)]) 
    ss=len(X)
    for i2 in range(ss):
        eye=max(X[i2])
        A=X[i2]
        A = [eye for n in range(len(X[i2]))]
        if distance.euclidean(A,X[i2])<0.001:
            cc.append(i1)
            plt.plot(d1[i1])
            plt.show() 
            break
print("epochs with disconnection or non-contacts",cc)
print("Total number",len(cc))
            
# PAPER : "EYE: A New Method for Detection of Electrode Disconnection in Sleep Signals"
