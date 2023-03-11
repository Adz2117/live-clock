#we want to make a simple game today
while True:
#we import random for system's decision
    import random as rn
#we get user movement : rock or paper or scissors
    b=input('please type r (for rock ) or p (for paper) or s (for scissors) ')
#here we determine movements for system 
    a=('r','p','s')
#with random we want from system to choice one of them
    c=(rn.choice(a))
#we print user and system choices
    print(b,'#',c)
#at the end with if and elif we find winner
    if b==('r') and c==('p'):
        print('you lose')
    elif b==('r') and c==('r'):
        print('draw')
    elif b==('r') and c==('s'):
        print('you win')
    elif b==('s') and c==('r'):
        print('you lose')
    elif b==('s') and c==('s'):
        print('draw')
    elif b==('s') and c==('p'):
        print('you win')
    elif b==('p') and c==('r'):
        print('you win')
    elif b==('p') and c==('s'):
        print('you lose')
    elif b==('p') and c==('p'):
        print('draw')
    else :
        break
