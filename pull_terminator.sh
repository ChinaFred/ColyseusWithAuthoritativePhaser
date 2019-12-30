echo "pulling terminator sources"
git pull origin master
echo "refresh over" 
echo "*******************************************************************************"
echo "starting server" 
sudo python terminator/getAlive.py