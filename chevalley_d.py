def chevalley_d(n,a,decomp):
    W=WeylGroup('D'+str(n),prefix='s')
    ref=W.reflections()
    altref = W.reflections().inverse_family()
    sim=W.simple_reflections()
    refl=list(ref)
    siml=list(sim)
    Wl=list(W)
    el=Wl[0]
    for i in range(len(decomp)):
        el=el*siml[decomp[i]-1]
    j=Wl.index(el)
    chev=[]
    for i in range(len(refl)):
        if (W[j]*refl[i]).length()==W[j].length()+1:
            chev.append(refl[i])
                             
    chevres=[]
    for i in range(len(chev)):
        chevres.append(el*chev[i])
        
    chevroots=[]
    for i in range(len(chev)):
        chevroots.append(altref[chev[i]])

    chevcoroots=[]
    for i in range(len(chev)):
        chevcoroots.append(2*chevroots[i]/(chevroots[i].dot_product(chevroots[i])))
        
    weight=W.domain().fundamental_weights()[a]
    
    chevbeta=[]
    for i in range(len(chev)):
        chevbeta.append(weight.dot_product(chevcoroots[i]))
    ans=[]
    coeff=[]
    for i in range(len(chev)):
        if chevbeta[i]!=0:
            ans.append([chevbeta[i],chevres[i]])
            coeff.append(chevbeta[i])
            

    ansp=""
    for i in range(len(ans)):
        if coeff ==1:
            ansp=ansp+"+"+str(ans[i])
        else:
            ansp=ansp+'+'+str(coeff[i])+'*'+str(ans[i])
    exp=ansp[1:]
    return ans

def multlist(m,L):
	for i in range(len(L)):
		L[i][0]=m*L[i][0]
	return L

def two_ref(n):
	finco=[]
	schub=[]
	finco=finco+chevalley(n,n-2,[n-2])[0]+multlist(2,chevalley(n,n-1,[n-1])[0])+chevalley(n,n,[n])[0]+multlist(-2,chevalley(n,n-2,[n-1])[0])+multlist(-2,chevalley(n,n-1,[n])[0])
	schub=schub+chevalley(n,n-2,[n-2])[1]+chevalley(n,n-1,[n-1])[1]+chevalley(n,n,[n])[1]+chevalley(n,n-2,[n-1])[1]+chevalley(n,n-1,[n])[1]

	unique=[]
	for i in schub:
		if i not in unique:
        		unique.append(i)
	uco=[]
	for i in range(len(unique)):
    		co=0
    		for j in range(len(finco)):
        		if schub[j]==unique[i]:
            			co=co+finco[j]
    		uco.append(co)

	finans=''

	for i in range(len(uco)):
    		if uco[i]!=0:
        		finans=finans+str(uco[i])+str(unique[i])+'+'
	return finans[:-1]


def redec(dec):
    hm=str(dec)
    redec1=[]
    i=1
    while i<len(hm):
        redec1.append(int(hm[i]))
        i=i+3
    return redec1


def finchev_d(n,red):
	schub=chevalley_d(n,red[0],[red[1]])
	j=2
	if len(red)==2:
		schub1=schub
	else:
		schub1=[]
	while j<len(red):
    		schub1=[] 

    		for i in range(len(schub)):
        		for k in range(len(chevalley_b(n,red[j],redec(schub[i][1])))):
            			schub1.append(chevalley_b(n,red[j],redec(schub[i][1]))[k])
        		for k in range(len(chevalley_b(n,red[j],redec(schub[i][1])))):
            			schub1[-k-1][0]=schub[i][0]*schub1[-k-1][0]
    		schub=schub1
    		j=j+1
	schubfin=[]
	schubert=[]
	
	for i in range(len(schub1)):
    		schubert.append(schub1[i][1])
	

	for i in range(len(schubert)):
    		like_i=[]
    		sum_i=0
    		if all(schubert[i]!=schubert[j] for j in range(i))==True:
        		for k in range(len(schubert)):
            			if schubert[k]==schubert[i]:
                			sum_i=sum_i+schub1[k][0]
        		schubfin.append([sum_i,schubert[i]])
	return schubfin

def pchev_d(n,k,red):
	not_p_schub=finchev_d(n,red)
	p_schub=[]
	for i in range(len(not_p_schub)):
		for j in range(len(mincp_d(n,k,len(red)))):
			if not_p_schub[i][1]==mincp_d(n,k,len(red))[j]:
				p_schub.append(not_p_schub[i])
	return p_schub
		
def pchev1_d(n,k,red):
	not_p_schub=finchev_d(n,red)	
	p_schub=[]
	for i in range(len(not_p_schub)):
		if not_p_schub[i][1] in mincp_d(n,k,len(red)):
			p_schub.append(not_p_schub[i])
	return p_schub