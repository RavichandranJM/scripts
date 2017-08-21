#! /bin/sh

# 11. Write a shell script to take a file name on its command line, and
#     edit it with sed so that every instance of "/usr/local/bin" is
#     changed to "/usr/bin"

# This solution suffers from a number of problems.
# 1. If it is interrupted, then a temporary file may be left behind
# 2. The file permissions and ownership of the original file may be changed
# 3. The tmpfile location is known and can be used to attack the user.

prog=$(basename $0)
usage() {
    cat <<EOF
Usage: $prog file...
Edit file... so that each instance of /usr/local/bin is replaced by /usr/bin
EOF
}

[ $# -eq 0 ] && { usage; exit 1 }

for file
do
    [ ! -r $file ] && { echo "Cannot read $file"; continue; }
    # Note: the next test is not really correct, since the directory that
    # contains it must be writable; but if we don't have write permission
    # on the file itself, then perhaps we should not overwrite it.
    [ ! -w $file ] && { echo "Cannot write to $file"; continue; }
    file_base=$(basename $file)
    tmpfile=/tmp/${file_base}.$$
    sed -r 's!/usr/local/bin!/usr/bin!g' $file > $tmpfile
    mv $tmpfile $file || echo "Unable to overwrite $file"
done
