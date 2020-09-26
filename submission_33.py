#!/usr/bin/env python
# coding: utf-8

# In[35]:


import random
import numpy as np
from matplotlib import pyplot as plt
I = 115
TP= 135000000
n = int(input("enter the number of days: "))
Infected = []
Death = []
Recover = []
Quarantine =[]
S = []
AS = []
IA = []
NIA = []
R1 =[]
D1=[]
CS = []
SS = []
DO1=[]
NDO1=[]
R2=[]
SS1=[]
DO2 =[]
NDO2 =[]
R3 =[]
CRS1 =[]
DO3 =[]
NDO3 =[]
R4 =[]
CRS2= []
Q = []
R5 =[]
CRS3 =[]
D2 =[]
AB =[]
CRS =[]
D3 =[]
R6 =[]
Q1=[]
Q2=[]
RC=[]
DC=[]
QC=[]
RP=[]
DP=[]
X=[]
Y=[]
Z=[]
TC=[]
day=[]
dayG=[]
test = []
IP=[]
T = 20000
GovR = [93,38,129,139,195,111,101,178,149,260,273,422,391,419,702,395,642,484,443,584,614,610,690,631,939,812,956,1072,1295,1189,1445,1111,1414,1668,1580,1871,1980,1569,2289,3966,2571,2438,3076,3113,3131,3271,2561,3307,3014,3571,3472,3171,5707,4309,4916,4902,4531,3786,4379,4783,10462,5143,5247,5070,6814,5993,7259,8095,7363,10631, 6886, 10744, 9024, 13975, 9071, 10885, 10437, 13114, 13983,10246,14229,11628,13497,12565,12060,20006,14417,14743,15829,15259,16908]
Gov = [ 573, 565, 809, 875, 846, 759, 1248, 1034, 883, 1060, 922, 2013, 1250, 924, 1541, 1290, 1669, 1408, 1836, 1607, 1561, 1873, 1738, 1801, 2394, 2442, 2806,3932, 2963, 3587, 3344, 3113, 4353, 3607, 3524, 3763, 3942, 3787, 4864, 5050, 4630, 6147, 5553, 6198,6568, 6629, 7113, 6414, 5843, 7293, 7300, 8105, 8336, 8782, 7761, 8821, 9633, 9889, 9471, 10438, 10864, 8442, 8852, 12375, 11128, 11320, 12023, 11157,10243, 11135, 13103, 13827, 14721, 15915, 15183, 13540, 15665, 16870, 18185,18276,20131,19620,18339,18256,19428,21948,22721,24015,23932,22510,23135]
GovD = [28,49,22,39,43,27,35,29,26,38,35,38,33,53,36,40,59,45,56,58,69,71,75,69,100,68,175,127,92,104,96,116,111,82,121,136,98,104,118,154,131,146,132,150,142,142,156,148,172,190,177,269,205,223,200,221,259,275,286,297,261,266,246,388,394,389,309,321,395, 2006, 341, 342, 366, 307, 426, 312, 468, 424, 401,381,414,384,417,506,438,377,444,610,421,474,479]
for a in range(len(Gov)):
    dayG.append(a+1)
for a in range(n):
    day.append(a+1)
    print("infected Persons on", a+1, "day:",I)
    A = []
    for i in range(I):
        a_list = [0,1]
        distribution = [0.16, 0.84]
        random_number = random.choices(a_list, distribution)
        A.append(random_number[0])
    AS.append(sum(A))
    S.append(len(A)-sum(A))
# Asymptomatic 
    for i in range(len(AS)):
        B = []
        for j in range(AS[i]):
            a_list = [0,1]
            distribution = [0.1, 0.9]
            random_number = random.choices(a_list, distribution)
            B.append(random_number[0])
    IA.append(sum(B))
    NIA.append(len(B)-sum(B))
# Doesn't makes others infected/ makes others infected probablity of death percentage 10
    
    for i in range(len(AS)):
        C =[]
        for j in range(AS[i]):
            a_list = [0,1,2]
            distribution = [0.02,0.9,0.08]
            random_number = random.choices(a_list, distribution)
            C.append(random_number[0])
    if a<=30:
        R1.append(0)
        D1.append(0)
        Q1.append(0)
    else:
        D1.append(C.count(0))
        R1.append(C.count(1))
        Q1.append(C.count(2))
# Sympomatic
    
    for i in range(len(S)):
        D=[]
        for j in range(S[i]):
            a_list = [0,1]
            distribution = [0.8, 0.2] 
            random_number = random.choices(a_list, distribution)
            D.append(random_number[0])
    CS.append(sum(D))
    SS.append(len(D)-sum(D))
            
# Common Symptoms probability of visiting a doctor 47
   
    for i in range(len(CS)):
        E = []
        for  j in range(CS[i]):
            a_list = [0,1]
            distribution = [0.3, 0.7]
            random_number = random.choices(a_list, distribution)
            E.append(random_number[0])
    if a <= 30:
        DO1.append(0)
        NDO1.append(len(E))
    else:
        DO1.append(sum(E))
        NDO1.append(len(E)-sum(E))
# Common Symptoms probability of not visiting a doctor
    
    for i in range(len(NDO1)):
        F=[]
        for j in range(NDO1[i]):
            a_list = [0,1]
            distribution = [0.3, 0.7]
            random_number = random.choices(a_list, distribution)
            F.append(random_number[0])
    
    if a<=50:
        R2.append(0)
        SS1.append(len(F))
    else:
        R2.append(sum(F))
        SS1.append(len(F)-sum(F))
# Serious Symptoms
    
    for i in range(len(SS1)):
        G = []
        for j in range(SS1[i]):
            a_list = [0,1]
            distribution = [0.2, 0.8]
            random_number = random.choices(a_list, distribution)
            G.append(random_number[0])
    if a<= 95:
        DO2.append(0)
        NDO2.append(len(G))
    else:
        DO2.append(sum(G))
        NDO2.append(len(G)-sum(G))

# Serious Symptoms doesn't visit a Doctor
    
    for i in range(len(NDO2)):
        H =[]
        for j in range(NDO2[i]):
            a_list = [0,1]
            distribution = [0.6, 0.4]
            random_number = random.choices(a_list, distribution)
            H.append(random_number[0])
    if a<=70:
        R3.append(0)
        CRS1.append(len(H))
    else:
        R3.append(len(H)-sum(H))
        CRS1.append(sum(H))
# Serious Symptoms
    
    for i in range(len(SS)):
        J =[]
        for j in range(SS[i]):
            a_list = [0,1]
            distribution = [0.2, 0.8]
            random_number = random.choices(a_list, distribution)
            J.append(random_number[0])
    if a<= 95:
        DO3.append(0)
        NDO3.append(len(J))
    else:
        DO3.append(sum(J))
        NDO3.append(len(J)-sum(J))

# Serious Symptoms doesn't visits a Doctor
    for i in range(len(NDO3)):
        K =[]
        for j in range(NDO3[i]):
            a_list = [0,1]
            distribution = [0.6, 0.4]
            random_number = random.choices(a_list, distribution)
            K.append(random_number[0])
    if a<=70:
        R4.append(0)
        CRS2.append(len(K))
    else:
        R4.append(sum(K))
        CRS2.append(len(K)-sum(K))
# Quarantine      
    
    number = DO1[a] + DO2[a] + DO3[a]
    Q.append(number)
       
    for i in range(len(Q)):
        L=[]
        for j in range(Q[i]):
            a_list = [0,1]
            distribution = [0.6, 0.4]
            random_number = random.choices(a_list, distribution)
            K.append(random_number[0])
    if a<=14:
        R5.append(0)
        CRS3.append(len(L))
    else:
        R5.append(sum(L))
        CRS3.append(len(L)-sum(L))
    
 # Critical Symptoms
    
    CRS.append(CRS1[a]+CRS2[a]+CRS3[a])
    for i in range(len(CRS)):
        N=[]
        for j in range(CRS[i]):
            a_list = [0,1]
            distribution = [0.98, 0.02]
            random_number = random.choices(a_list, distribution)
            N.append(random_number[0])
    if a<=15:
        D2.append(0)
        AB.append(len(N))
    else:
        D2.append(sum(N))
        AB.append(len(N)-sum(N))
    
# Artificial Breadthing

    for i in range(len(AB)):
        M=[]
        for j in range(AB[i]):
            a_list = [0,1,2]
            distribution = [0.17, 0.34, 0.49]
            random_number = random.choices(a_list, distribution)
            M.append(random_number[0])
    if a<=25:
        D3.append(0)
        R6.append(0)
        Q2.append(0)
    else:
        D3.append(M.count(0))
        R6.append(M.count(1))
        Q2.append(M.count(2))
    test.append(T)
    Death.append(D1[a]+D2[a]+D3[a])
    if a< 20:
        Recover.append(R1[a]+R2[a]+R3[a]+R4[a]+R5[a]+R6[a])
    else:
        Recover.append(abs(round(R1[a]+R2[a]+R3[a]+R4[a]+R5[a]+R6[a]+0.4*Quarantine[abs(n-a-219)]+0.35*Quarantine[abs(n-a-220)])))
    
    Infected.append(I)
    RC.append(sum(Recover))
    DC.append(sum(Death))
    TC.append(sum(Infected))
    RP.append(sum(Recover)/sum(Infected))
    DP.append(sum(Death)/sum(Infected))
    IP.append((1.5*sum(Infected))/sum(test))
    Quarantine.append(Infected[a]-Recover[a]-Death[a])
    QC.append(sum(Quarantine))
    
    I = round((I-Q[a])*1.077) 
    T = round(abs((Quarantine[a])*150))
i = TC[0];
while i < TC[n-1]:
        X.append(i)
        i= i*2
for j in range(len(X)):
    res = next(x for x, val in enumerate(TC) 
                                  if val >= X[j]) 
    Y.append(res+1)
    
for i in range(len(Y)-1):
    res = Y[i+1]-Y[i]
    Z.append(res)  
print("Tested",sum(test))
print('Total infected person',TC[n-1])
print('Recover',sum(Recover))
print("Death",sum(Death))
print("Quarantined",sum(Quarantine))


# In[36]:


plt.figure(figsize=(20,10))
plt.plot(dayG,GovR, label = 'Estimated Data')

plt.plot(day,Recover, label = 'Actual Data')
plt.xlabel("Days")
plt.ylabel("Number of people")
plt.title("Estimited Vs Actual- Recovery")
plt.legend()
plt.show()


# In[37]:


plt.figure(figsize=(20,10))
plt.plot(day,Infected, label = 'Infection')
plt.plot(day,Death, label = 'Death')
plt.plot(day,Recover, label = 'Recover')
plt.xlabel("Days")
plt.ylabel("Number of people")
plt.title("Plot of Infection, Recovery and Death")
plt.legend()
plt.show()


# In[38]:


plt.figure(figsize=(20,10))
plt.plot(dayG,Gov, label = 'Estimated Data')
plt.plot(day,Infected, label = 'Actual Data')
plt.xlabel("Days")
plt.ylabel("Number of people")
plt.title("Estimited Vs Actual - Infection")
plt.legend()
plt.show()


# In[39]:


plt.figure(figsize=(20,10))
plt.plot(dayG,GovD, label = 'Estimated Data')
plt.plot(day,Death, label = 'Actual Data')
plt.xlabel("Days")
plt.ylabel("Number of people")
plt.title("Estimited Vs Actual- Death")
plt.legend()
plt.show()


# In[40]:


plt.figure(figsize=(20,10))
plt.xlabel('Number of days')
plt.ylabel('Percent Recovery')
plt.title('Percentage Recovery')
plt.plot(RP)


# In[41]:



plt.figure(figsize=(20,10))
plt.xlabel('Number of days')
plt.ylabel('Percent Death')
plt.title('Percentage Death')
plt.plot(DP)




# In[42]:


plt.figure(figsize=(20,10))
print(Z)
y = Z
positions = (1, 2, 3,4,5,6,7,8,9,10,11,12,13,14)
labels = ("2", "4", "8","16","32","64","128","256","512","1024","2048","4096","8192","16384")
plt.xticks(positions, labels)
plt.xlabel("Number of times")
plt.ylabel("Days")
plt.title("Cases Doubling Rate")
plt.plot(y) 


# In[43]:



plt.figure(figsize=(20,10))
plt.plot(day,TC, label = 'Total Infection')
plt.plot(day,DC, label = 'Total Death')
plt.plot(day,RC, label = 'Total Recover')
plt.xlabel("Days")
plt.ylabel("Number of people")
plt.title("Plot of cumulative Infection, Recovery and Death")
plt.legend()
plt.show()


# In[44]:



plt.figure(figsize=(20,10))
plt.plot(day,RC, label = 'Recover')
plt.plot(day,QC, label = 'Quarantine')
plt.xlabel("Days")
plt.ylabel("Number of people")
plt.title("Recovered vs Quarantined- cumulative")
plt.legend()
plt.show()


# In[45]:


plt.figure(figsize=(20,10))
plt.plot(day,IP, label = 'Percent Infection')
plt.plot(day,DP, label = 'Percent Death')
plt.plot(day,RP, label = 'Percent Recover')
plt.xlabel("Days")
plt.ylabel("Number of people")
plt.title("Plot of Percent Infection, Recovery and Death")
plt.legend()
plt.show()


# In[46]:


import math
DR=[]
SDR = []
for j in range(len(GovR)):
    DR.append(GovR[j]-Recover[j])
    
#print(DR)
print("Average gap",sum(DR)/len(GovR))
for j in range(len(GovR)):
    SDR.append( ( Recover[j]-(sum(DR)/len(GovR) ) )*( Recover[j]-(sum(DR)/len(GovR) )) )
#print(SDR)
print("Standard Deviation",math.sqrt(sum(SDR)/(len(GovR)-1)))
print('Max Gap',max(DR))
print('Min Gap',min(DR))
if n%2 == 0:
    RQ2 = (Recover[round((n/2)-1)]+Recover[round(n/2)])/2
    if n%4 == 0:
        RQ1 = (Recover[round((n/4)-1)]+Recover[round(n/4)])/2
        RQ3 = (Recover[round((3*n/4)-1)]+Recover[round(3*n/4)])/2
    else:
        RQ1 = Recover[round((n-2)/4)]
        RQ3 = Recover[round((3*n-2)/4)]
        
        
else:
    RQ2 = Recover[(n-1)/2]
    RQ1 = Recover[(n-3)/4]
    RQ3 = Recover[(3*n-1)/4]
print('Quartile1',RQ1)
print('Quartile2',RQ2)
print('Quartile3',RQ3)  


# In[34]:


DI=[]
SDI=[]
for j in range(len(Gov)):
    DI.append(Gov[j]-Infected[j])
    
#print(DI)
print(sum(DI)/len(Gov))
for j in range(len(GovR)):
    SDI.append( ( Infected[j]-( sum(DI)/len(Gov) ) )*( Infected[j]-(sum(DI)/len(Gov) )) )
#print(SDI)
print(math.sqrt(sum(SDI)/(len(Gov)-1)))
print(max(DI))
print(min(DI))
if n%2 == 0:
    IQ2 = (Infected[round((n/2)-1)]+Infected[round(n/2)])/2
    if n%4 == 0:
        IQ1 = (Infected[round((n/4)-1)]+Infected[round(n/4)])/2
        IQ3 = (Infected[round((3*n/4)-1)]+Infected[round(3*n/4)])/2
    else:
        IQ1 = Infected[round((n-2)/4)]
        IQ3 = Infected[round((3*n-2)/4)]
        
        
else:
    IQ2 = Infected[(n-1)/2]
    IQ1 = Infected[(n-3)/4]
    IQ3 = Infected[(3*n-1)/4]
print('Quartile1',IQ1)
print('Quartile2',IQ2)
print('Quartile3',IQ3)


# In[33]:


DD=[]
SDD =[]
for j in range(len(GovD)):
    DD.append((GovD[j]-Death[j]))
    
#print(DD)
print(sum(DD)/len(GovD))
for j in range(len(GovD)):
    SDD.append( ( Death[j]-( sum(DD)/len(GovD) ) )*( Death[j]-(sum(DD)/len(GovD) )) )
#print(SDD)
print(math.sqrt(sum(SDD)/(len(GovD)-1)))
print(max(DD))
print(min(DD))
if n%2 == 0:
    DQ2 = (Death[round((n/2)-1)]+Death[round(n/2)])/2
    if n%4 == 0:
        DQ1 = (Death[round((n/4)-1)]+Death[round(n/4)])/2
        DQ3 = (Death[round((3*n/4)-1)]+Death[round(3*n/4)])/2
    else:
        DQ1 = Death[round((n-2)/4)]
        DQ3 = Death[round((3*n-2)/4)]
        
        
else:
    DQ2 = Death[(n-1)/2]
    DQ1 = Death[(n-3)/4]
    DQ3 = Death[(3*n-1)/4]
print('Quartile1',DQ1)
print('Quartile2',DQ2)
print('Quartile3',DQ3)
                


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




