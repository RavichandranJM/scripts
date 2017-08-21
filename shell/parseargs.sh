:

if [ $# -gt 0 ]
then
    while [ $# -gt 0 ]
    do
        case $1 in
            -f)
                filename=$2
                shift
                shift
                ;;
            -a)
                echo "Option is a"
                shift
                ;;
        esac    
    done
fi
echo $filename
