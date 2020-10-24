# setDisplayVar4WSL
Are you using WSL, X applications and are too lazy to set up our own solution to configure DISPLAY variable with IP of Windows? If the answer is yes, then use this python script or binary compiled with nuitka (Linux x86-64)
Put it in your home folder and add the following to .bashrc


python3 ~/.setupDisplay.py > ~/.disp_ip

export DISPLAY=`cat ~/.disp_ip`
