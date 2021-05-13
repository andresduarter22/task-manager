#Check if OS is Linux, else quit
os_ver=$(uname -s)
os_needed="Linux"

if [ "$os_ver" != "$os_needed" ];then
    echo "OS Mismatch!"
    exit 1
fi

#GET the python version, only the major release number
var=$(python3 -c 'import platform; major, _, _ = platform.python_version_tuple(); print(major)')

case "$var" in
"1")
    echo "LOL, python 1!?  proceeding to install python 3.8";
    sudo apt update
    sudo apt install python3-pip
    ;;
"2")
    echo "python 2 detected,  proceeding to install python 3.8";
    sudo apt update
    sudo apt install python3-pip
    ;;
"3")
    echo "python 3 detected";
    ;;
*)
    echo "no python detected, proceeding to install python 3.8"
    sudo apt update
    sudo apt install python3-pip
    ;;
esac

# Check if in a VENV
INVENV=$(python3 -c 'import sys; print ("1" if hasattr(sys, "real_prefix") else "0")')
case "$INVENV" in
"0")
    echo "No virtual environment found.. Installing Venv Now...";
    sudo pip3 install virtualenv
    virtualenv venv
    source venv/bin/activate
    ;;
"1")
    echo "python VENV found";
    ;;
esac

#packaging and building
# creates dist/example_pkg-0.0.1-py3-none-any.whl
echo "---------------------------------"
echo "Installing packages..."
echo "---------------------------------"
pip3 install -r requirements.txt
python3 -m pip install --upgrade build
python3 -m build

echo "---------------------------------"
echo "Starting Tox..."
echo "---------------------------------"
#test
tox -vvv .
