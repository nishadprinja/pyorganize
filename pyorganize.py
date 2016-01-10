import os, sys

### Definition of source path from user input and destination folders
if sys.version_info[0] < 3:
    sourcepath = raw_input("What is the path of the directory you want to clean up?: ")
else:
    sourcepath = input("What is the path of the directory you want to clean up?: ")
docpath = os.path.join(sourcepath, 'Docs')
filepath = os.path.join(sourcepath, 'Files')
picpath = os.path.join(sourcepath, 'Pics')
audiopath = os.path.join(sourcepath, 'Audio')
vidpath = os.path.join(sourcepath, 'Vids')
miscpath = os.path.join(sourcepath, 'Misc')
folderpath = os.path.join(sourcepath, 'Folders')

# Make list from all files and folders
source = os.listdir(sourcepath)

file_types = ['.pdf', '.txt', '.rtf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.epub', '.enex', '.mobi', '.djvu', '.php', '.js', '.html', '.css', '.sql',
			'.zip', '.rar', '.dmg', '.pkg', '.tar.gz', '.gz', '.webarchive', '.ics',
			'.jpg', '.jpeg', '.png', '.gif', '.psd',
			'.mp3', '.aac', '.flac', '.ogg', '.wav', '.aif', '.aiff', '.wma', '.m4a',
			'.mov', '.mp4', '.h264', '.avi', '.wmv', '.mkv', '.flv', '.mpg', '.mpeg']

# Contraints to stop hidden files/folders causing a program error
hidden_elements = ['.', '_']

# Constraints to prevent destination folders from being moved into 'folders' directory (or 'folders' being moved into itself [error])
folderpath_exclusions = [docpath, filepath, picpath, audiopath, vidpath, miscpath, folderpath]

## Function to move files into directories according to their type
def move_files ():
	'''

	Iterate through the list 'source' and 'each_file' is one
	instance we're isolating/moving in the following subloops

	'''
	for each_file in source:

		# Loop and check file format of each_file against first row of elements of file_types list
		for doctype in file_types[:18]:
			if each_file.endswith(doctype) or each_file.endswith(doctype.upper()):

				# Create 'Docs' folder if it doesn't exist
				if not os.path.isdir(docpath):
					os.mkdir(docpath)

				# Move each file from main directory to 'Docs' folder (rename the file path)
				os.rename(os.path.join(sourcepath, each_file), os.path.join(docpath, each_file))

		# Same as last loop but with files moved to 'Files' folder
		for filetype in file_types[18:26]:
			if each_file.endswith(filetype) or each_file.endswith(filetype.upper()):
	    		
				if not os.path.isdir(filepath):
					os.mkdir(filepath)

				os.rename(os.path.join(sourcepath, each_file), os.path.join(filepath, each_file))

		# Same loop but with pictures moved to 'Pics' folder
		for pictype in file_types[26:31]:
			if each_file.endswith(pictype) or each_file.endswith(pictype.upper()):
	    		  		
				if not os.path.isdir(picpath):
					os.mkdir(picpath)

				os.rename(os.path.join(sourcepath, each_file), os.path.join(picpath, each_file))

		# Same loop but with audio/songs moved to 'Audio' folder
		for audiotype in file_types[31:40]:
			if each_file.endswith(audiotype) or each_file.endswith(audiotype.upper()):
		   		  		
				if not os.path.isdir(audiopath):
					os.mkdir(audiopath)

				os.rename(os.path.join(sourcepath, each_file), os.path.join(audiopath, each_file))

		# Same loop but with videos/movies moved to 'Vids' folder
		for vidtype in file_types[40:]:
			if each_file.endswith(vidtype) or each_file.endswith(vidtype.upper()):
		   		  		
				if not os.path.isdir(vidpath):
					os.mkdir(vidpath)

				os.rename(os.path.join(sourcepath, each_file), os.path.join(vidpath, each_file))

		# Same loop but with files of types not in the file_types list moved to 'Misc' folder
		for anytype in file_types:
			# If the file doesn't end with any type from the file_list, is a file and not a folder, and the first character isn't a '.' or '_' (hidden system file), proceed to move it
			if not each_file.endswith(anytype) and os.path.isfile(os.path.join(sourcepath, each_file)) and each_file[0] not in hidden_elements:

				if not os.path.isdir(miscpath):
					os.mkdir(miscpath)

				os.rename(os.path.join(sourcepath, each_file), os.path.join(miscpath, each_file))

## Function to move folders into a single subdirectory named 'Folders'
def move_folders ():
	# Same principle as the initial move_files loop, but isolating folders
	for folder in source:
		# If the folder's first character isn't '.' or '_' (hidden system folder), the folder name/path doesn't match those of the directories with moved files and the 'Folders' one being created, and it is a folder, continue on
		if folder[0] not in hidden_elements and os.path.join(sourcepath, folder) not in folderpath_exclusions and os.path.isdir(os.path.join(sourcepath, folder)):

			# If the 'Folders' directory doesn't exist, create it
			if not os.path.isdir(folderpath):
				os.mkdir(folderpath)

			# Move the folder into the 'Folders' directory
			os.rename(os.path.join(sourcepath, folder), os.path.join(folderpath, folder))

# Call the functions - move all files first, then all folders
move_files()
move_folders()

# Output message
print "Cleanup Done!"