
import pygame


#instructions
print("This is the ghost maker")

instructions_answer = input("Would you like instructions? ").upper()

if instructions_answer == ("YES"):
	#write instructions here 
	print("\nThis program takes a background image and a foreground image, then makes the foreground image transparent and placeses it on the background at the desired coordinates")
	print("\nThese are the instructions")
	print("First enter the name of the background bmp, then the name of the foreground bmp, then enter the x-coordinate and y-coordinate of where you want the center of the transparent foreground image to be (The coordinates must be within the background image)")
	print("\nIf you follow the prompts corectly you should be ok\n")

#loads images and gets dimensions
background_image = pygame.image.load(input("What is the name of the background file? "))
(width_of_background, height_of_background) = background_image.get_rect().size


ghost_image = pygame.image.load(input("What is the name of the foreground file? "))
(width_of_ghost, height_of_ghost) = ghost_image.get_rect().size

#sets window and out bacground image in it
main_window = pygame.display.set_mode((width_of_background, height_of_background))


main_window.blit( background_image, (0, 0) )
pygame.display.update()

#while loop to get valid coordinates
while True:
	x_coordinate = int(input("What do you want the x-coordinate of the ghost it to be? "))
	y_coordinate = int(input("What do you want the y-coordinate of the ghost it to be? "))
	
	x_coordinate_adjust = x_coordinate//2
	y_coordinate_adjust = y_coordinate//2


	if x_coordinate >= 0 and x_coordinate <= width_of_background and y_coordinate >= 0 and y_coordinate <= height_of_background:
		break
	else:
		print("Invalid coordinates, coordinates were outstide background image")


#searches to foreground image for pixels that are not green, if the pixel is not green it find the corelating pixel on the background and averages the rgb values and sets it on the main window (window/image)
for row_of_ghost in range(height_of_ghost):
	for columns_of_ghost in range(width_of_ghost):
		(ghost_red_number, ghost_green_number, ghost_blue_number, ghost_na) = ghost_image.get_at((columns_of_ghost, row_of_ghost))
		if not ghost_green_number == 255:

			(background_red_number, background_green_number, background_blue_number, background_na) = background_image.get_at( ( (x_coordinate - x_coordinate_adjust + columns_of_ghost), (y_coordinate - y_coordinate_adjust + row_of_ghost) ) )
			
			main_window.set_at( (x_coordinate - x_coordinate_adjust + columns_of_ghost, y_coordinate - y_coordinate_adjust + row_of_ghost), ((ghost_red_number + background_red_number)//2, (ghost_green_number + background_green_number)//2, (ghost_blue_number + background_blue_number)//2) )

#updates screen
pygame.display.update()
			
#keeps the main window open till the user wants to close the window
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
	pygame.display.update()





