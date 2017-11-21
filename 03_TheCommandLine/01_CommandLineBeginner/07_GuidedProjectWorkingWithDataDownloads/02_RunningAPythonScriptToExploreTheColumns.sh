echo -e 'if __name__ == "__main__":\n    print("Program executed successfully!")' > read.py
virtualenv -p ~/anaconda3/bin/python ~/Documents/Python3CondaVirtualenv
source ~/Documents/Python3CondaVirtualenv/bin/activate
python -V
pip freeze
nano read.py
echo “edit read.py and add a pandas important and read CRDC2013_14_LEA_content.csv”
python read.py
