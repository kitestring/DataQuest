# Induction to Remote Repositories
# DataQuest Instructions
git clone /dataquest/user/git/chatbot
# Personal Instructions
git clone https://github.com/kitestring/hello-world


# Making Changes to Cloned Repositories
# DataQuest Instructions
cd /chatbot
printf "This project needs no installation" >> README.md
git add .
git commit -m "Updated README.md"
git status
# Personal Instructions
cd hello-world
nano README.md # Makes some minor proof reading edits.
git add README.md
git commit -m "Fix a bit of punctuation in the second paragraph."
git status


# Overview of the Master Branch
# DataQuest Instructions
git branch
# Personal Instructions
git branch


# Pushing Changes to the Remote
# DataQuest Instructions
git push origin master
# Personal Instructions
git push origin master


# Viewing Individual Commits
# DataQuest Instructions
git log
git show 742098bf15b8732001712d2b66e9f9df994626fe
# Personal Instruction
git log
git show 684e34c75760d7a6b901a2ab72f828ae9f4bd47c



# Commits and the Working Directory
#  DataQuest Instructions
git diff 33 74
# Personal Instruction
git log
git diff fd028 90b41



# Switching to a Specific Commit
# DataQuest Instructions
git log
git reset --hard 2201d
# Personal Instruction
git log
git reset --hard eb7a



# Pulling From a REmote Repo
# DataQuest Instructions
git pull
# Personal Instructions
git pull



# Referring to the Most Recent Commit
# DataQuestion Instructions
git reset --hard HEAD~1
# Personal Instructions
git reset --hard HEAD
