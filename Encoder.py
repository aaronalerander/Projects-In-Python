



'''This is the main function, responsible for the use interface

@params		none
@return		none'''


def main():
	alphabet = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
	list_alphabet = list(alphabet)
	lenght_of_alphabet = 26
	


	'''This is the load function, responsible loading text to the program

	@params		string of file to load
	@return		string of text in file'''
	
	def load_fun(file_to_load):
		try:
			unmod_text = open(file_to_load,"r").read()
			return (unmod_text.upper())
		except:
			print("unable to load file")
			unmod_text = ("")
			return (unmod_text)
		file_to_load.close()



	'''This is the save function, responsible for saving text that was encoded or decoded

	@params		name of file to be saved, text to be saved in file
	@return		none'''

	def save_fun(name_of_file,text):
		file = open(name_of_file,"w")
		file.write(text)
		file.close

	'''This is the encode function, responsible for encoding text

	@params		text to be encoded, alphabet to be used for encoding
	@return		encoded text'''

	def encode_fun(str_to_encode,encoded_alphabet):

		'''This is the list to string function, it takes a list and makes it into a string
	@params		list
	@return		string'''
		def list_to_string(list_name):
			length_of_list = len(list_name)
			new_string = ("")
			for x in range(length_of_list):
				new_string += list_name[x]
			return new_string

		list_encoded_alphabet = list(encoded_alphabet)
		list_encoded = []
		list_str_to_encode = list(str_to_encode)
		lenght_str_to_encode = len(list_str_to_encode)
		for x in range(lenght_str_to_encode):
			for y in range(lenght_of_alphabet ):
				if list_str_to_encode[x] == list_alphabet[y]:
					list_encoded.append(list_encoded_alphabet[y])
					break
				if y == 25:
					list_encoded.append(list_str_to_encode[x])
				
		return (list_to_string(list_encoded))
	'''This is the decode function, responsible for decoding text 
	@params		text to be decoded, alphabet to be used for decoding
	@return		decoded text'''

	def decode_fun(str_to_decode,encoded_alphabet):
		'''This is the list to string function, it takes a list and makes it into a string
		@params		list
		@return		string'''
		def list_to_string(list_name):
			length_of_list = len(list_name)
			new_string = ("")
			for x in range(length_of_list):
				new_string += list_name[x]
			return new_string
		list_encoded_alphabet = list(encoded_alphabet)
		length_encoded_alphabet = 26
		list_decoded = []
		list_str_to_decode = list(str_to_decode)
		lenght_str_to_decode = len(list_str_to_decode)
		for x in range(lenght_str_to_decode):
			for y in range(length_encoded_alphabet):
				if list_str_to_decode[x] == list_encoded_alphabet[y]:
					list_decoded.append(list_alphabet[y])
					break
				if y == 25:
					list_decoded.append(list_str_to_decode[x])

		return (list_to_string(list_decoded))



	'''This is the set alphabet function, responsible for setting the alphabet for encoding or decoding 
	@params		none
	@return		string '''



	def cryptogram_alphabet():
		normal_alphabet = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
		b = normal_alphabet
		
		error1 = ("NO")
		error2 = ("NO")
		error3 = ("NO")
		encoded_alphabet = input("enter an encoded alphabet ").upper()
		list_encoded_alphabet = list(encoded_alphabet)
		length_encoded_alphabet = len(list_encoded_alphabet)
		for x in range(length_encoded_alphabet):
			a = ord(list_encoded_alphabet[x])
			if a < 65 or a > 90:
				error1 = ("YES")
					
		for y in range(length_encoded_alphabet):
			for z in range (length_encoded_alphabet):
				if list_encoded_alphabet[y] == list_encoded_alphabet[z] and y != z:
					error2 = ("YES")
						
		if length_encoded_alphabet != 26:
			error3 = ("YES")
				
		if error1 == ("YES"):
			print("You made an error. You can only use letters. The current alphabet is set to the standard alphabet")
			return b
		elif error2 == ("YES"):
			print("You made an error. You can only use each letter once. The current alphabet is set to the standard alphabet")
			return b
		elif error3 == ("YES"):
			print("You made an error. You entered too little or too much letter. The current alphabet is set to the standard alphabet")
			return b

		
		else:
			return encoded_alphabet


























	intial_text = ("Empty")
	current_text = ("Empty")
	current_alphabet = ("Empty")
	while True:
		
		print("\nIntial Text = ",intial_text)
		print("Current Text = ",current_text)
		print("Current Alphabet = ",current_alphabet)
		print("\n1) Load Text")
		print("2) Save Text")
		print("3) Encode Text")
		print("4) Decode Text")
		print("5) Set Alphabet")
		print("6) Quit")
		user_input = input("\nWhat would you like to do? (enter number) ")
		
		if user_input == ("1"):
			file_to_load = input("What is the name of the file you would like to load? ")
			intial_text = load_fun(file_to_load)
		
		elif user_input == ("2"):
			name_given_to_file = input("What would you like to name the file you are saving? ")
			save_fun(name_given_to_file,current_text)
			
		elif user_input == ("3"):
			if intial_text != ("Empty") or current_alphabet != ("Empty"):
				current_text = encode_fun(intial_text,current_alphabet)
			else:
				print("You need to load a file and set an alphabet before you encode")


		elif user_input == ("4"):
			if intial_text != ("Empty") or current_alphabet != ("Empty"):
				current_text = decode_fun(intial_text,current_alphabet)
			else:
				print("You need to load a file and set an alphabet before you decode")


		elif user_input == ("5"):
			current_alphabet = cryptogram_alphabet()
		elif user_input == ("6"):
			break
		else:
			print("Your input was invalid")
main()

