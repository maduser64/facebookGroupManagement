from CPG import grabConfigURL
from genericImportClass import *



while True:
    programInitalized = True
    dataBaseInit = None

    CPG.grabConfigUrl()
    run = UPSTS()



    """script will call each action object at the correct timing

    -Member Names Scraper and its full LifeCycle will run once a day
        need to check database init param in configParam python folder
        to see if datbase has been popluated or not


    -Swing Tag scraper will run every 7 days

    -periodic poster will run every 7 days, if programInitalized = True wait 24 hours before running """

