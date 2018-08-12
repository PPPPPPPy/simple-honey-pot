IP=$(echo "$SSH_CLIENT" | awk '{ print $1}')

if [ $IP = '192.168.42.11' ]
then
	echo "Welcome home :)"
else
# nohup - when logout, process will not shutdown
# & background execute
	nohup python /home/pi/Public/alarm.py &
fi
