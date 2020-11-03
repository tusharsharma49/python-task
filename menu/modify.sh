#!bin/bash
add(){
    echo Enter your File name :
    read file
    if ls | grep $file
    then
        echo Adding your new file to hadoop........
        hadoop fs -put $file /
    else
        tput setaf 1
        echo file $file not found
        tput setaf 7
    fi
}

cat(){
    echo Getting information from hadoop.....
    hadoop fs -ls /
}

if $1 == 1
then
    add
elif $1 == 2
then
    cat
elif $1 == 3
then
    hadoop dfsadmin -report
else
    tput setaf 1
    echo Enter correct number
    tput setaf 7
fi