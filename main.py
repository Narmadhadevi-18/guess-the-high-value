import random
from data import datas
from game_art import rt,  vs
#print logo
print(rt)
def game(s):
#random question generation
    q1=random.choice(datas)
    q2=random.choice(datas)
    if q1==q2:
        q2=random.choice(datas)
    #check the answer is correct or not
    def check(option,a_count,b_count,s):
        if a_count>b_count and option=='a':
            s+=1
            print(s)
            return True,s
            
        elif a_count<b_count and option=='b':
            s+=1
            return True,s
        return False,s

    def format(act):
        act_name=act["name"]
        act_film_count=act["films_count"]
        return f"{act_name}"
    
    print(f"a.{format(q1)}")
    print(vs)
    print(f"b.{format(q2)}")
    option=input("who has done more fims:").lower()
    a_count=q1["films_count"]
    b_count=q2["films_count"]
    iscorrect,s =check(option,a_count,b_count,s)
    if iscorrect==True:
        print(f"correct{s}")
        return s,True
        
    else:
        print("wrong"+str(s))
        return s,False
        
def main():
        s=0
        while True:
            s, iscorrect = game(s)
            if not iscorrect:
                break 
                
main()