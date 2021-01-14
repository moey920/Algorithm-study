lst =  [input() for _ in range(8)]


trapped1 =  [lst[i][j] for i in range(8) for j in range(8) if i % 2 ==0 and  j % 2 == 0 and lst[i][j] =='H' ]
trapped2 =  [lst[i][j] for i in range(8) for j in range(8) if i % 2 ==1 and  j % 2 == 1 and lst[i][j] =='H' ]


print(len(trapped1 + trapped2))