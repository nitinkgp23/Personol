#!/bin/sh

git clone --bare https://github.com/nitinkgp23/oct12.git
cd oct12.git
sh ~/Desktop/Projects/Personol/history-writer/script.sh 
git push --force --tags origin 'refs/heads/*'
cd ..
rm -rf oct12.git
