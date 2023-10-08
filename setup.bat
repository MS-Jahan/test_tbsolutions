@echo off
echo "Installing latest pip..."
py get-pip.py

echo "Installing pip packages..."
py -m pip install -r requirements.txt
@pause