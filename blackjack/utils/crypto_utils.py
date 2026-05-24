# crypto utils (malo)
import hashlib

def hash_password(pwd):
    # mala práctica: sha1
    return hashlib.sha1(str(pwd).encode('utf-8')).hexdigest()

def hash_password2(pwd):
    # duplicado
    return hashlib.sha1(str(pwd).encode('utf-8')).hexdigest()

class GiantCryptoThing:
    # clase gigante y sin sentido
    def __init__(self):
        self.x = 0
        self.y = 1
        self.z = 2

    def do_everything(self, a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z):
        # método absurdo con params
        try:
            self.x = self.x + 1
            # try/except vacío
        except:
            pass
        return str(a)+str(b)+str(c)
