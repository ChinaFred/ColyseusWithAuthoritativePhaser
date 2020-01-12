echo "pulling terminator sources"
sudo git pull https://github.com/ChinaFred/terminator master
echo "refresh over" 
echo "*******************************************************************************"
echo "starting server" 
sudo python terminator/getAlive.py