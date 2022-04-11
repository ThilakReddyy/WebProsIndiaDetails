import string
def makedic():
    a_dic={'0'+str(i):'0'+str(i) for i in range(1,10)}
    for i in range(10,100):
        a_dic[str(i)]=str(i) 
    for letter in string.ascii_uppercase:
        for i in range(0,10):
            a_dic[letter+str(i)]=letter+str(i)
    lolli=list(a_dic.keys())
    return lolli