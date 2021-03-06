"""
	Tic-Tac-Toe: a game coded by Garrett Smith
		--See bottom for more information--
"""

print("\n\nTic-Tac-Toe: a game coded by Garrett Smith\n\n")

def set_up_board():
	#tic-tac-toe board split into an array
	#extra "" added at the beginning so the iteration starts at 1
	grid = ["", "    A  ", "   B   ", "  C  ", "       ", "|     ", "|     ", "1      ", "|     ", "|     ", "  _____", "|_____", "|_____", "       ", "|     ", "|     ", "2      ", "|     ", "|     ", "  _____", "|_____", "|_____", "       ", "|     ", "|     ", "3      ", "|     ", "|     ", "       ", "|     ", "|     " ]

	#Grid spaces that haven't been used; gets modified at the end of script
	unused_grid_spaces = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]

	#arrays for recording which spaces have been played in from each letter: 'x' and 'o'
	spaces_that_x_has_played_in = []
	spaces_that_o_has_played_in = []

	return grid, unused_grid_spaces, spaces_that_x_has_played_in, spaces_that_o_has_played_in


#3D array of all winning combinations
winning_combinations = [["A1", "B2", "C3"], ["A3", "B2", "C1"], ["A1", "A2", "A3"], ["B1", "B2", "B3"], ["C1", "C2", "C3"], ["A1", "B1", "C1"], ["A2", "B2", "C2"], ["A3", "B3", "C3"]]

def turn(round_number):

	#this method is for the purpose of making a new line after every third item in the array
	#otherwise, the grid would be all in one line
	def check_if_is_divisible_by_a_certain_number(number, number_to_divide_by):
		global divisible_by_certain_number

		remainder_when_divided_by_number = number % number_to_divide_by

		#sets to either True or False
		divisible_by_certain_number = remainder_when_divided_by_number == 0


		return divisible_by_certain_number

	#this method paints the grid, and inserts an endline every third item
	def paint_grid():
		for item in range(0,31):
			check_if_is_divisible_by_a_certain_number(item, 3)

			if divisible_by_certain_number and item != 0:
				print(grid[item])
			else:
				#by default, print() prints an endline.  By specifying end = "", no newline is created
				print(grid[item], end = "")

	#runs the print_grid() function and paints the board on first run
	if round_number == 1:
		paint_grid()

	#Takes user input of what space to play in; doesn't continue until input matches certain values
	while True:
		play_in_what_space = input("\nType the space you would like to play in:  ").upper().strip()

		#checks to see if the user input matches any of the acceptable responses
		if play_in_what_space in unused_grid_spaces:

			#Records which spaces x and o have played in
			if check_if_is_divisible_by_a_certain_number(round_number, 2):
				spaces_that_o_has_played_in.append(play_in_what_space)
			else:
				spaces_that_x_has_played_in.append(play_in_what_space)
			
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

		#spaces 7,16, and 25 are the squares on the left column;
		#They have a different number of spaces in the grid than the other 2 columns and have to be inserted differently
		if space_in_the_grid_the_user_picked == 7 or space_in_the_grid_the_user_picked == 16 or space_in_the_grid_the_user_picked == 25:

			#sets the following variable equal to the grid space the user choose with an "x" or an "o" in it
			#switches x and o every turn
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
		take_off_last_space = box_with_letter_inserted_into_it[:len(box_with_letter_inserted_into_it)-1]

		#change element in grid[] to the new string with an 'x' in it
		grid[space_in_the_grid_the_user_picked] = take_off_last_space

	#calls previous function and uses the cases dictionary to find the key/pair value
	insert_letter_into_square_in_grid(cases.get(play_in_what_space))

	#remove the used grid square from the acceptable responses list
	unused_grid_spaces.remove(play_in_what_space)

	#prints newline
	print()

	#repaint grid once calculations are all done
	paint_grid()


def winning_rules(winning_combination):
	if set(winning_combinations[winning_combination]).issubset(spaces_that_o_has_played_in):
		print("\n'o' wins!")
		return True
	elif set(winning_combinations[winning_combination]).issubset(spaces_that_x_has_played_in):
		print("\n'x' wins!")
		return True
	else:
		return False

def do_you_want_to_play_again():
	while True:
		does_user_want_to_play_again = input("\nDo you want to play again?  Y/N:  ").upper().strip()

		if does_user_want_to_play_again == "Y":
			run_game()
		elif does_user_want_to_play_again == "N":
			print("\nThanks for playing!")
			exit()
		else:
			print("\nThat doesn't make sense.  Please type in either \"Y\" or \"N.\"\n")
			continue

def run_game():
	#set default round equal to zero
	round_number_increment = 0

	#set default to not winning
	win = False

	global grid, unused_grid_spaces, spaces_that_x_has_played_in, spaces_that_o_has_played_in
	grid, unused_grid_spaces, spaces_that_x_has_played_in, spaces_that_o_has_played_in = set_up_board()

	while unused_grid_spaces:

		#When the program runs, the round will become 1 and the program will start
		round_number_increment += 1

		#checks all 8 winning positions to see if user has won
		for one_through_eight in range(0,7):
			win = winning_rules(one_through_eight)

			if win:
				do_you_want_to_play_again()

		turn(round_number_increment)

run_game()

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

the enlarged-sketch is ["    A  ", "   B   ", "  C  ", "       ", "|     ", "|     ", "1      ", "|     ", "|     ", "  _____", "|_____", "|_____", "       ", "|     ", "|     ", "2      ", "|     ", "|     ", " _____", "|_____", "|_____", "       ", "|     ", "|     ", "3      ", "|     ", "|     ", "       ", "|     ", "|     " ]
"""