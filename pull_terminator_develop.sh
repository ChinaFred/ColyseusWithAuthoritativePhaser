echo "pulling terminator sources"
git pull https://github.com/ChinaFred/terminator develop
echo "refresh over" 
echo "*******************************************************************************"
echo "starting server" 
sudo python terminator/getAlive.py