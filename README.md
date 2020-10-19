# setDisplayVar
Are you using WSL, X applications and are too lazy to setup our own solution to configure DISPLAY variable with IP of Windows ?
If answer is yes then use this python script or binary compiled with nuitka (Linux x86-64)

Put it in your home folder and add following to .bashrc


~/.setupDisplay.bin > ~/.disp_ip
export DISPLAY=`cat ~/.disp_ip`
