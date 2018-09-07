bored=[[" "," "," "],[" "," "," "],[" "," "," "]],[[" "," "," "],[" "," "," "],[" "," "," "]],[[" "," "," "],[" "," "," "],[" "," "," "]]
global place 
place = 0
turns = 0
global winner 
winner = ""
def victory():
	global winner 
	winner = check
	global place 
	place = 28
while place != 28:
	place =  int(input("where do you want to place your token, 1 - 27 ")) -1
	if turns % 2 == 0:
		bored[int(place/9)][int((place%9)/3)][int((place%9)%3)] = "x"
	else:
		bored[int(place/9)][int((place%9)/3)][int((place%9)%3)] = "o"
	turns+=1
	print(str(bored[0][0]) + "/" + str(bored[1][0]) + "/" + str(bored[2][0]))
	print(str(bored[0][1]) + "/" + str(bored[1][1]) + "/" + str(bored[2][1]))
	print(str(bored[0][2]) + "/" + str(bored[1][2]) + "/" + str(bored[2][2]))
	i=0
	k=0
	check = ""
	while i < 3:
		j = 0
		while j<3:
			for q in range(2):
				if q == 0:
					check = "x"
				else:
					check = "o"
				if bored[i][j] == [check,check,check]:
					victory()
				elif bored[i][0][j] == bored[i][1][j] == bored[i][2][j] == check:
					victory()
				elif bored[i][0][0] == bored[i][1][1] == bored[i][2][2] == check:
					victory()
				elif bored[i][0][2] == bored[i][1][1] == bored[i][2][0] == check:
					victory()
				elif bored[0][0][0] == bored[1][1][1] == bored[2][2][2] == check:
					victory()
				elif bored[0][0][2] == bored[1][1][1] == bored[2][2][0] == check:
					victory()
				elif bored[0][2][2] == bored[1][1][1] == bored[2][0][0] == check:
					victory()
				elif bored[0][2][0] == bored[1][1][1] == bored[2][0][2] == check:
					victory()
				elif bored[0][i][0] == bored[1][i][1] == bored[2][i][2] == check:
					victory()
				elif bored[0][0][i] == bored[1][1][i] == bored[2][2][i] == check:
					victory()
				elif bored[0][2][i] == bored[1][1][i] == bored[2][0][i] == check:
					victory()
				elif bored[0][j][i] == bored[1][j][i] == bored[2][j][i] == check:
					victory()
			j+=1
		i+=1
print(str(winner) +" wins")

