echo "pulling terminator sources"
git pull https://github.com/ChinaFred/terminator master
echo "refresh over" 
echo "*******************************************************************************"
echo "starting server" 
sudo python terminator/getAlive.py