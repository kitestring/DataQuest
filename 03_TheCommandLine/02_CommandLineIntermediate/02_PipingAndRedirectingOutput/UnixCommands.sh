echo "99 bottles of beer on the wall..." > beer.txt
echo "Take one down, pass it around, 98 bottles of beer on the wall..." >> beer.txt
sort -r < beer.txt
nano coffee.txt # add this text:
# Coffee is almost as good as beer,
# But I could never drink 99 bottles of it
grep "bottles of" beer.txt coffee.txt  
touch beer1.txt
touch beer2.txt
grep "beer" beer?.txt
grep "beer" *.txt
echo -e "import random\nfor i in range(10000):\n    print(random.randint(1,10))\n" > rand.py
python3 rand.py | grep 9
echo "All the beers are gone" >> beer.txt && cat beer.txt
echo "\"Here are some double quotes\" bitch" > newfile.txt && cat newfile.txt
