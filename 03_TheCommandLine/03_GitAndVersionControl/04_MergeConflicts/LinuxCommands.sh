# 1 Introduction (Create two seperate branches and then cause a merge conflict)
cd /home/dq
git clone /dataquest/user/git/chatbot chatbot
cd chatbot
git checkout -b feature/king-bot
# Edit bot.py and add an appropriately kingly print statement at the end of the file.
git add .
git commit -m "Kingly Print Statement"

git checkout master
git checkout -b feature/queen-bot
# Edit bot.py and add an appropriately queenly print statement at the end at the end of the file
git add .
git commit -m "Queenly Print Statement"

git checkout master
git merge feature/king-bot
git merge feature/queen-bot 



# 2 Aborting a Merge
git merge --abort



# 3 Resolving conflicts
git checkout master
git merge feature/queen-bot
# Manually fix the merge markup so the lines from feature/queen-bot are the ones Git retains
git add .
git commit -m "Fixed conflicts"
git push origin master



# 4 Resolving Mulit-Line Merge Conflicts
cd /home/dq/chatbot
git checkout master
git checkout -b feature/random-printing
# Edit bot.py to add a block that prints one of three random messages at the end.
git add .
git commit -m "Random message feature"

git checkout master
git checkout -b feature/dice-roller
# Edit bot.py to add a block that generates and displays two random numbers at the end
git add .
git commit -m "Dice rolloer feature"

git checkout master
git merge feature/random-printing
git merge feature/dice-roller # creats a multi-line merge conflict
# Manually edit the bot.py file and correct the merge conflict keeping what ever lines I choose
git add .
git commit -m "Resolved multi-line conflict"
git push origin master


# 5 Resolving Mulit-Line Merge Conflicts
cd /home/dq/chatbot
git checkout master
git checkout -b feature/more-printing
# Edit bot.py and add multiple lines that print some text (whatever you'd like)
git add .
git commit -m "more-printing"

git checkout master
git checkout -b feature/more-printing-2
# Edit bot.py and add different print statements to the same lines you edited in feature/more-printing
git add .
git commit -m "more-printing-2"

git checkout master
git merge feature/more-printing
git merge feature/more-printing-2 # creates merge conflict

# Manually edit the Head to resolve the merge conflict keeping the lines I choose
git commit -m "Resolved multi-line conflict"
git push origin master


# 6 Accepting Changes From Only One Branch
cd /home/dq/chatbot
checkout master
checkout -b feature/remove-bot
git rm bot.py
git commit -m "remove-bot"

git checkout master
git checkout -b feature/keep-bot
printf '\n\nprint("Another Print Statement")' >> bot.py
git add .
git commit -m "keep-bot"

git branch master
git merge feature/remove-bot
git merge feature/keep-bot
git checkout --theirs .

git add .
git commit -m "Keeping bot.py"
git push origin master


# 7 Ignoring Files
cd /home/dq/chatbot
git branch master
printf ".DS_Store\n*.pyc\n" > .gitignore
git add .
git commit -m "Added gitignore"
git push origin master


# 8 Removing Cashed Files
cd /home/dq/chatbot
git branch master
git rm --cached bot.py
# Do not use git add here, because that would add bot.py back in!
git commit -m "Removed bot.py"
git push origin master