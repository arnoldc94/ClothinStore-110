#Backend for online store

## Corey Arnold

## Help:

### Start DB Service (WSL):
sudo service mongodb status
sudo service mongodb start
sudo service mongodb stop

### DB service (mac):
brew services start mongodb-community@4.4
brew services stop mongodb-community@4.4

### Delete all your orders
mongo
use onlinestorech20
db.order.remove({})