# Stone Paper Scissor
import random
dict = {"st":1, "p":0, "s":-1}
rev_dict = {1:"st", 0:"p", -1:"s"}
computer = random.choice([-1,0,1])
youin = input("""Options -
1.stone (st)
2.paper (p)
              
3.scissor (s)
Enter your choice here : """)
you = dict[youin]  
comp = rev_dict[computer]    
print(f"Computer's choice {comp}")
print(f"Your choice {youin}")
if (computer == you):
    print("It's Tie !!!")
elif (computer==1 and you==0):
    print("You Win !!!")
elif (computer==1 and you==-1):
    print("Computer Win !!!")
elif (computer==0 and you==1):
    print("Computer Win !!!")
elif (computer==0 and you==-1):
    print("You Win !!!")
elif (computer==-1 and you==1):
    print("You Win !!!")
elif (computer==-1 and you==0):
    print("Computer Win !!!")
else:
    print("Something went wrong !!!")    
