import random

#User enters their desired value; a random value is entered using random.choices;
#Printing both the players values;
#Main condition to check who wins;
#Results printed
def rockPaperScissor():
   print('Rock[r], Paper[p], Scissor[s]\n ')
   number_of_times = int(input('How many times you want to play ? \n'))
   times_played = 0 
   times_won_player = 0
   times_won_computer = 0
   while times_played != number_of_times:
     #taking inputs
     user_1 = input('Enter your move: ' )
     userchoice = ['r','p','s']
     user_2 = "".join(random.choices(userchoice))
     print(f'You chose \"{user_1}\"; Computer chose \"{user_2}\";')
      #condition for declaring winner
     if (user_1 == 'r' and user_2 == 's') or (user_1 == 'p' and user_2 == 'r') or (user_1 == 's' and user_2 == 'p') :
       print('Horrah!! You won')
       times_won_player +=1
     elif user_1 == user_2:
       print('Tie')
     else:
       print('Computer Wins')
       times_won_computer +=1
     times_played +=1
   print(f'Thanks for playing, your score is {times_won_player} and Computer score is {times_won_computer}')
       
      
rockPaperScissor()
