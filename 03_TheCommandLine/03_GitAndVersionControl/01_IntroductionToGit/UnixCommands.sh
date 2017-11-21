# Introduction to Version Control Systems
mkdir random_numbers
git init

# The .git Folder
ls -al

# Creating Files in the Repository
echo "Random number generator" > README.md
echo -e 'if __name__ == "__main__":\n    print("10")' > script.py

# Checking File Status & adding them to the staging area
git status
git add script.py
git add README.md

# Configuring Identity in Git
git config --global user.email "kenneth.kite@gmail.com"
git congig --global user.name "Ken Kite"

# Committing Changes
git commit -m "Initial commit. Added script.py and README.md"

# Viewing File Differences
echo -e "import random\n\nprint(random.randint(0,10))" >> script.py
git diff
git status

# Making a Second Commit
git add script.py
git commit
git commit -m "Appended, returns random integer between 0 & 10" #Note, commit message should be very detailed 
# with file names as they do not seem to be included in the log output.

# Reviewing the Commit History
git log

# Viewing Commit Differences
git log --stat
