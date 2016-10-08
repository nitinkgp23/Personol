#!/bin/sh

while read u b
do

    git clone --bare $u
    cd $b
    sh ~/Desktop/Projects/Personol/history-writer/script.sh 
    git push --force --tags origin 'refs/heads/*'
    cd ..
    rm -rf $b

done < url_list.txt
