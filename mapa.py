import userAlive


txt_user = userAlive.giveUser()
link = "file:///map_"+ txt_user +".html" # plus nick jak bedzie generator
targetFile = link
userAlive.goTodo("StreetHackerBrowser.py -a " + targetFile)