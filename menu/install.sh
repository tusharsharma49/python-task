#!bin/bash
install(){
    pack = $(ls | grep $1)
    echo Searchig $1 package......
    if rpm -q $pack
    then
        echo $pack already installed
    elif ls | grep $1
    then
        echo Running $1 Istallation......
        rpm -i $pack --force
    else
        tput setaf 1
        echo $pack package not found
        tput setaf 7  
    fi
}
install jdk
install hadoop