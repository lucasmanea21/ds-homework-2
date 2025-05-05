class Nod:
    def __init__(self,valoare):
        self.val=valoare
        self.stanga=None
        self.dreapta=None

class SplayTree:
    def __init__(self):
        self.radacina=None

    def rotire_stanga(self,x):
        y=x.dreapta
        x.dreapta=y.stanga
        y.stanga=x
        return y

    def rotire_dreapta(self,x):
        y=x.stanga
        x.stanga=y.dreapta
        y.dreapta=x
        return y

    def splay(self,root,val):
        if not root:return None
        tmp=Nod(None)
        left=right=tmp
        while True:
            if val==root.val:break
            if val<root.val:
                if not root.stanga:break
                if val<root.stanga.val:
                    root=self.rotire_dreapta(root)
                    if not root.stanga:break
                right.stanga=root
                right=root
                root=root.stanga
            else:
                if not root.dreapta:break
                if val>root.dreapta.val:
                    root=self.rotire_stanga(root)
                    if not root.dreapta:break
                left.dreapta=root
                left=root
                root=root.dreapta
        left.dreapta=root.stanga
        right.stanga=root.dreapta
        root.stanga=tmp.dreapta
        root.dreapta=tmp.stanga
        return root

    def insert(self,val):
        if self.radacina is None:
            self.radacina=Nod(val)
            return
        self.radacina=self.splay(self.radacina,val)
        if self.radacina.val==val:return
        nou=Nod(val)
        if val<self.radacina.val:
            nou.dreapta=self.radacina
            nou.stanga=self.radacina.stanga
            self.radacina.stanga=None
        else:
            nou.stanga=self.radacina
            nou.dreapta=self.radacina.dreapta
            self.radacina.dreapta=None
        self.radacina=nou

    def delete(self,val):
        if self.radacina is None:return
        self.radacina=self.splay(self.radacina,val)
        if self.radacina.val!=val:return
        if self.radacina.stanga is None:
            self.radacina=self.radacina.dreapta
        else:
            temp=self.radacina.dreapta
            self.radacina=self.splay(self.radacina.stanga,val)
            self.radacina.dreapta=temp

    def search(self,val):
        if self.radacina is None:return False
        self.radacina=self.splay(self.radacina,val)
        return self.radacina.val==val

    def floor(self,val):
        if not self.radacina:return None
        self.radacina=self.splay(self.radacina,val)
        if self.radacina.val<=val:return self.radacina.val
        nod=self.radacina.stanga
        rez=None
        while nod:
            if nod.val<=val:
                rez=nod.val
                nod=nod.dreapta
            else:
                nod=nod.stanga
        return rez

    def ceil(self,val):
        nod=self.radacina
        rez=None
        while nod:
            if nod.val>=val:
                rez=nod.val
                nod=nod.stanga
            else:
                nod=nod.dreapta
        return rez

    def range_query(self,a,b):
        rez=[]
        if not self.radacina:return rez
        self.radacina=self.splay(self.radacina,a)
        stack=[]
        nod=self.radacina
        while stack or nod:
            while nod:
                stack.append(nod)
                nod=nod.stanga if nod.val>a else None
            nod=stack.pop()
            if a<=nod.val<=b:rez.append(nod.val)
            if nod.val>b:break
            nod=nod.dreapta
        return rez

    def __len__(self):
        count=0
        stack=[self.radacina]
        while stack:
            nod=stack.pop()
            if nod:
                count+=1
                stack.append(nod.stanga)
                stack.append(nod.dreapta)
        return count
