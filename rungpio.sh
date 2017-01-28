#!/bin/bash

print_menu() {
    echo  "R P i - G P I O - M E N U"
    echo  " l) Blink LED diode"
    echo  " b) Detect button press"
    echo  " p) List running GPIO operations"
    echo  " k) Kill all GPIO operations"
    echo  " q) Exit"
}

read_choice(){
    local choice
    read -p "Enter choice [ l,b,i,q ] " choice
    case $choice in
        l) blinkled ;;
        b) pressbutton ;;
	p) checkproc ;;
	k) killproc ;;
        q) echo "     Bye !" && exit 0 ;;
        *) echo -e "${RED}Error...${STD}" && sleep 1
    esac
}


pause(){
  read -p "Press [Enter] key to continue..." fackEnterKey
}



blinkled(){
    clear
    python  /root/gpio/workshop-kit-python-code/3_blink_forever2s.py & 2>/dev/null
    echo ""
    echo " Led is blinking ..."
    pause
}

pressbutton(){
    clear
    python  /root/gpio/workshop-kit-python-code/4_button.py & 2>/dev/null
    echo ""
    echo " Button press is monitored ..."
    pause
}


checkproc(){
    clear
    ps -ef |grep "/root/gpio/workshop-kit-python-code/" |grep -v "grep"
    echo ""
    echo " List of running GPIO operations ..."
    pause
}

#checkprocverif(){
#    if [[ $running != 0 ]]; then
#        echo "someting is still running"
#    else
#        echo "No more GPIO operations running ..."
#    fi
#}

#running=(){
#	runningproc=$(ps -ef |grep '/root/gpio/workshop-kit-python-code' |grep -v 'grep' | awk '{print $2}')
#}

# This one should exclude killing of this script which is in same location
#killproc(){
#    for i in echo "$runningproc"
#	do
#		kill -9 $i
#    done
#    echo ""
#    echo " GPIO operations stopped ..."
#    pause
#}

# Run : 

while true 
do
    print_menu
    read_choice
done


