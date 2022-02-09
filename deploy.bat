del .\static\arzamas-16.zip
"c:\Program Files\7-Zip\7z.exe" a arzamas-16.zip . -mx9 -xr!public
move arzamas-16.zip ./static
hugo
firebase deploy
del .\static\arzamas-16.zip
pause