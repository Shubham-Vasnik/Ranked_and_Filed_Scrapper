echo "Installing Requirements"
echo "Installing Python3"
sudo apt-get install python3
echo "Installing pip"
sudo apt-get install python3-pip
echo "Installing Packages"
pip3 install requests
pip3 install tqdm
clear
echo "Requirements Installed"
echo "Running The Scrapper"
python3 scrapper.py

