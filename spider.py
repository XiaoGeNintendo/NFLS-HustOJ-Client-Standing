import urllib.request as urllib2
import re

def confirm():
    input("[[[Press Enter to Confirm and Continue]]]")

token="4npohov2uja9rg55npa7pgqq26"
probs=["10302"]
url="http://192.168.188.77/judge/status.php?&problem_id=%s&top=%s"

try:
    with open("problemset.txt",mode="r",encoding="utf-8") as f:
        token=f.readline().strip()
        probs=f.readline().strip().split(",")
        url=f.readline().strip()
        print(f"THIS IS PROBLEMSET VERSION!!!!\nParameters: \ntoken={token}\nprobs={probs}\nurl={url}\nPlease confirm by pressing Enter")
        confirm()
except:
    print("Cannot read problemset.txt! Place your ID on the first line, problem id on the second and base url on the third")
    exit(1)

def get(url):
    header={
        "cookie":"PHPSESSID="+token
        }
    req=urllib2.Request(url,headers=header)
    resp=urllib2.urlopen(req).read().decode("utf-8")
    return resp

def parseScore(s):
    if len(s)>=3 and s[-3].isdigit():
        return int(s[-3:])
    elif len(s)>=2 and s[-2].isdigit():
        return int(s[-2:])
    elif len(s)>=1 and s[-1].isdigit():
        return int(s[-1])
    else:
        return 0

#final standing
score=list()

def appendScore(user,prob,sc,status):
    isc=f'{prob}_score'
    ist=f'{prob}_status'
    
    for i in score:
        if i['user']==user:
            if isc not in i:
                i[isc]=sc
                i[ist]=status
                i['tot_score']+=sc
            elif i[isc]<=sc:
                i["tot_score"]-=i[isc]
                i[isc]=sc
                i[ist]=status
                i['tot_score']+=sc
            return
        
    score.append({
        'user':user,
        'tot_score':sc,
        isc:sc,
        ist:status
    })


#fetch single problem
def addScore(prob):
    print("Checking problem",prob)
    top="99999999999"
    while True:
        print(url%(prob,top))
        # confirm()
        
        res=get(url%(prob,top))
        # print(res)

        index=res.find("tbody")
        end=res.find("/tbody")
        
        par=1
        last=""
        tot=[]
        for i in range(index,end):
            if res[i]=='<':
                par+=1
            elif res[i]=='>':
                par-=1
            if par==0 and res[i] not in "<>":
                last+=res[i]
            else:
                last=last.strip()
                if last!="":
                    tot.append(last)
                last=""

        # print(tot)

        if len(tot)==0:
            break
        index=1
        while index+2<len(tot):
            top=tot[index-1]
            # print(tot[index],tot[index+2],parseScore(tot[index+2]))

            appendScore(tot[index],prob,parseScore(tot[index+2]),tot[index+2])
            index+=12

        top=str(int(top)-1)

        # print(top)
        # confirm()

def cmp(val):
    return -val["tot_score"]

for i in probs:
    addScore(i)
    
score.sort(key=cmp)


out="<table border=\"1\"><tr><th>Rank</th><th>User</th>"
for i in probs:
    out+="<th>"+i+"</th>"
out+="<th>Total</th></tr>"

rk=1
lastsc=0
rlrk=0

for i in score:
    if lastsc!=i['tot_score']:
        rlrk=rk
        lastsc=i['tot_score']
    out+="<tr><td>"+str(rlrk)+"</td><td>"+i['user']+"</td>"
    for j in probs:
        if j+"_score" in i:
            out+="<td title=\""+i[j+"_status"]+"\">"+str(i[j+"_score"])+"</td>"
        else:
            out+="<td>-</td>"
    out+="<td>"+str(i['tot_score'])+"</td></tr>"
    rk+=1
out+="</table>"

with open("out_ps.html",mode="w",encoding="utf-8") as f:
    f.write(out)
print("Done! Please visit out.html!")
# print(score)
