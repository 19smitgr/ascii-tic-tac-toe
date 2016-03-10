"""

	Tic-Tac-Toe: a game coded by Garrett Smith

		--See bottom for more information--

"""


#tic-tac-toe board split into an array
#extra "" added at the beginning so the iteration starts at 1
grid = ["", "    A  ", "   B   ", "  C  ", "       ", "|     ", "|     ", "1      ", "|     ", "|     ", "  _____", "|_____", "|_____", "       ", "|     ", "|     ", "2      ", "|     ", "|     ", "  _____", "|_____", "|_____", "       ", "|     ", "|     ", "3      ", "|     ", "|     ", "       ", "|     ", "|     " ]

#Grid spaces that haven't been used; gets modified at the end of script
unused_grid_spaces = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]

def turn(round_number):
	#this method is for the purpose of making a new line after every third item in the array
	#otherwise, the grid would be all in one line
	def check_if_is_divisible_by_a_certain_number(number, number_to_divide_by):
		global divisible_by_certain_number

		remainder_when_divided_by_number = number % number_to_divide_by

		if remainder_when_divided_by_number == 0:
			divisible_by_certain_number = True
		else:
			divisible_by_certain_number = False

		return divisible_by_certain_number

	#this method paints the grid, and inserts an endline every third item
	#by default, print() prints an endline.  By specifying 
	def paint_grid():
		for item in range(0,31):
			check_if_is_divisible_by_a_certain_number(item, 3)

			if divisible_by_certain_number and item != 0:
				print(grid[item])
			else:
				print(grid[item], end = "")

	#runs the print_grid() function and paints the board on first run
	if round_number == 1:
		paint_grid()

	#Takes user input of what space to play in; doesn't continue until input matches certain values
	while True:
		play_in_what_space = input("\nType the space you would like to play in:  ").upper().strip()

		#checks to see if the user input matches any of the acceptable responses
		if play_in_what_space in unused_grid_spaces:
			break
		else:
			print("\nThat answer is not valid. Are you typing the grid spot correctly?\nEx. B3\n")
			continue

	#User input -> index number in grid[]
	cases = {

		"A1": 7,
		"A2": 16,
		"A3": 25,
		"B1": 8,
		"B2": 17,
		"B3": 26,
		"C1": 9,
		"C2": 18,
		"C3": 27

	}

	#this method inserts stuff into a string
	def insert(original, new, position):
		return original[:position] + new + original[position:]


	def insert_letter_into_square_in_grid(space_in_the_grid_the_user_picked):

		if space_in_the_grid_the_user_picked == 7 or space_in_the_grid_the_user_picked == 16 or space_in_the_grid_the_user_picked == 25:

			#sets the following variable equal to the grid space the user choose with an "x" or an "o" in it
			if check_if_is_divisible_by_a_certain_number(round_number, 2):		
				box_with_letter_inserted_into_it = insert(grid[space_in_the_grid_the_user_picked], "o", 4)
			else:
				box_with_letter_inserted_into_it = insert(grid[space_in_the_grid_the_user_picked], "x", 4)

		else:

			if round_number % 2 == 0:
				box_with_letter_inserted_into_it = insert(grid[space_in_the_grid_the_user_picked], "o", 3)
			else:
				box_with_letter_inserted_into_it = insert(grid[space_in_the_grid_the_user_picked], "x", 3)

		#When the insert() function is called, the string is enlarged by one space
		#the following 3 lines take off the last space in the string
		backwards_element_in_grid_list = box_with_letter_inserted_into_it[::-1]  #Reverse the string ex. 'Example' -> 'elpmaxE'
		take_off_last_space = backwards_element_in_grid_list[1:]  #Start at the second letter: 'elpmaxE' -> 'lpmaxE'
		undo_backwards_element_in_grid_list = take_off_last_space[::-1] #Undo the reverse: 'lpmaxE' -> 'Exampl'

		#change element in grid[] to the new string with an 'x' in it
		grid[space_in_the_grid_the_user_picked] = undo_backwards_element_in_grid_list

	#calls previous function and uses the cases dictionary to find the key/pair value
	insert_letter_into_square_in_grid(cases.get(play_in_what_space))

	#remove the used grid square from the acceptable responses list
	unused_grid_spaces.remove(play_in_what_space)

	#prints newline
	print()

	#repaint grid once calculations are all done
	paint_grid()

#set default round equal to zero
round = 0

while unused_grid_spaces:
	#When the program runs, the round will become 1 and the program will start
	round = round + 1
	turn(round)

	

"""
Mini-sketch:

   A  B  C
1 __|__|__
2 __|__|__
3   |  |  



Enlarged-sketch:
    A     B     C  
       |     |     
1      |     |     
  _____|_____|_____
       |     |     
2      |     |     
  _____|_____|_____
       |     |     
3      |     |     
       |     |     

grid = ["    A  ", "   B   ", "  C  ", "       ", "|     ", "|     ", "1      ", "|     ", "|     ", "  _____", "|_____", "|_____", "       ", "|     ", "|     ", "2      ", "|     ", "|     ", " _____", "|_____", "|_____", "       ", "|     ", "|     ", "3      ", "|     ", "|     ", "       ", "|     ", "|     " ]

"""