MyString=abcde
i=0
while (( i++ < ${#MyString} ))
do
   char=$(expr substr "$MyString" $i 1)
   echo "<$char>"
done
