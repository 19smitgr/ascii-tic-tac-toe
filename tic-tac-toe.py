"""

	Tic-Tac-Toe: a game coded by Garrett Smith

		--See bottom for more information--

"""

#tic-tac-toe board split into an array
#extra "" added at the beginning so the iteration starts at 1
grid = ["", "    A  ", "   B   ", "  C  ", "       ", "|     ", "|     ", "1      ", "|     ", "|     ", "  _____", "|_____", "|_____", "       ", "|     ", "|     ", "2      ", "|     ", "|     ", "  _____", "|_____", "|_____", "       ", "|     ", "|     ", "3      ", "|     ", "|     ", "       ", "|     ", "|     " ]

#Grid spaces that haven't been used; gets modified at the end of script
unused_grid_spaces = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]

#arrays for recording which spaces have been played in from each letter: 'x' and 'o'
spaces_that_x_has_played_in = []
spaces_that_o_has_played_in = []

cleared_grid = list(grid)
cleared_unused_grid_spaces = list(unused_grid_spaces)
cleared_spaces_that_x_has_played_in = list(spaces_that_x_has_played_in)
cleared_spaces_that_o_has_played_in = list(spaces_that_o_has_played_in)

def clear_arrays_from_previous_game():
	grid = cleared_grid[:]
	unused_grid_spaces = cleared_unused_grid_spaces[:]
	spaces_that_x_has_played_in = cleared_spaces_that_x_has_played_in[:]
	spaces_that_o_has_played_in = cleared_spaces_that_o_has_played_in[:]

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

#set default round equal to zero
round_number_increment = 0

#set default to not winning
win = False


def winning_rules(winning_combination):
	if set(winning_combinations[winning_combination]).issubset(spaces_that_o_has_played_in):
		print("\n'o' wins!")
		return True
	elif set(winning_combinations[winning_combination]).issubset(spaces_that_x_has_played_in):
		print("\n'x' wins!")
		return True
	else:
		return False

while unused_grid_spaces:
	
	#When the program runs, the round will become 1 and the program will start
	round_number_increment += 1

	#Actually goes from 0 to 7 since it counts from zero
	for one_through_eight in range(0,7):
		win_or_not = winning_rules(one_through_eight)

		if win_or_not:
			win = True

		while win:
			want_to_play_again = input("\nWould you like to play again?  Y/N:  ").upper().strip()

			#checks to see if the user input matches any of the acceptable responses
			if want_to_play_again == "Y":
				round_number_increment = 0

				round_number_increment += 1
				grid, unused_grid_spaces, spaces_that_x_has_played_in, spaces_that_o_has_played_in = clear_arrays_from_previous_game()

				#prints newline
				print()

				win = False

				turn(round_number_increment)
			elif want_to_play_again == "N":
				#Nest line is so that the while loop doesn't persist
				win = False

				break
			else:
				print("\nYour answer isn't valid.  Please type either Y or N.")
				continue
			

	if win:
		break
	elif win == False:
		turn(round_number_increment)



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