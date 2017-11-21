# Introduction to Git Branches
git clone /dataquest/user/git/chatbot
cd chatbot
git checkout -b more-speech
python bot.py


# Switching Branches
git checkout more-speech
printf "print('More Stuff to say')" >> bot.py
git add bot.py
git commit -m "Added more output"


# Pushing a Branch to a Remote
git push origin more-speech
git branch -r


# Merging Branches
git checkout master
git merge more-speech
git push origin master


# Deleting Branches
git branch -d more-speech


# Checking Out Branches From the Remote
# Simulate a second collaborator working on the remote
cd /home/dq
git clone /dataquest/user/git/chatbot chatbot2
cd chatbot2
git checkout -b happy-bot
printf "\nprint('Happiness level:: 120')"
git add .
git commit -m "Made the bot 20% happier!"


# Finding Differences Across Branches
git diff master happy-bot


# Branch Naming Conventions
git signout -b feature/random-messages
# Edit bot.py to output one of several possible messages, based on a random number generator.
git add .
git commit -m "Random message generator"
git push origin feature/random-messages


# Branch History
git branch feature/spam-messages
git diff feature/random-messages feature/spam-messages
git diff master feature/random-messages