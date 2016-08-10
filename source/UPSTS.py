from genericImportClass import *

class UPSTS:

    def __init__(self, scrapeUrl):
        self.scrapeURL = scrapeUrl


    def grabSoup(self):
       """
       grabs soup URL from config file stores in variable
while the “see more” link is visible
	click the see more link

grab all html elements with class userContent and store in array

then
for I in that array
store I.find(‘p’).text

will also grab the names of the people posting the soup usage is
findAll(“h5”) with class _5pbw


for I in (placeholder):
array store I.find(‘a’).text

will return both arrays
       """
