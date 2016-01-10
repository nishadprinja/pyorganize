# pyorganize
## Quickly move files and folders into subdirectories so they can easily be sorted out

**Note!** - This is written for/in Mac OS X and has not yet been tested to work in Windows. At a point in the future where it will be tested, this note will be removed.

You may try this script on a Windows machine with Python installed and it may work, but as I have not tested it, I'm not accountable if it doesn't work properly.

> Comments are written in the script to help a user or developer understand how it works rather quickly.

**Procedure**

1. Open Terminal *(cmd + space, search for 'Terminal' or go to Applications/Utilities)*

2. This module uses the 'os' and 'sys' libraries that are bundled with every install of Python, so there's no need for any additional library installation for this script

3. To run the script, type into Terminal (from the directory where pyorganize.py is saved)
	
	`python pyorganize.py`

	A prompt will ask for the directory you want organized.

	A good way to get this is to find a file or folder in the directory, open inspector (cmd + i or right click and 'Get Info'), and under 'General:' locate 'Where:', copy the path after that, and paste it into terminal after the prompt.

*This script will organize your files in a directory, especially one that's very disorganized, and separate them into 'Audio', 'Docs', 'Files', 'Folders', 'Misc', 'Pics', and 'Vids' folders.*

If everything works out you should see 'Cleanup Done!' and your folders will contain files (or directories for the 'Folders' folder) that can now be moved into external hard drives, organized on the local computer, batch renamed, or deleted.

If you'd prefer a different naming scheme, want to organize things differently, or want to extend the script's functionality, feel free to fork this repo and clone its contents to do so.