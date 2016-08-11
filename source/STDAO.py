class STDAO:

    def __init__(self, scrapeResult, ignoreW4w, ignoreW4m, ignoreW4couple, ignoreW4t,
                 ignoreCouple4couple, ignoreCouple4m, ignoreCouple4w, ignoreCouple4t,
                 ignoreM4w, ignoreM4couple, ignoreM4t, ignoreT4t, ignoreT4couple, ignoreT4w,ignoreT4m):
        self.scrapeResult = scrapeResult
        self.ignoreW4w = ignoreW4w
        self.ignoreW4m = ignoreW4m
        self.ignoreW4couple = ignoreW4couple
        self.ignoreW4t = ignoreW4t
        self.ignoreCouple4couple = ignoreCouple4couple
        self.ignoreCouple4m = ignoreCouple4m
        self.ignoreCouple4w = ignoreCouple4w
        self.ignoreCouple4t = ignoreCouple4t
        self.ignoreM4w = ignoreM4w
        self.ignoreM4couple = ignoreM4couple
        self.ignoreM4t = ignoreM4t
        self.ignoreT4t = ignoreT4t
        self.ignoreT4couple = ignoreT4couple
        self.ignoreT4w = ignoreT4w
        self.ignoreT4m = ignoreT4m

        def dataProcess(self):
            addW4w =[]
            addW4m =[]
            addW4couple =[]
            addW4t = []
            addCouple4couple =[]
            addCouple4m =[]
            addCouple4w =[]
            addCouple4t =[]
            addM4w =[]
            addM4couple =[]
            addM4t =[]
            addT4t =[]
            addT4couple =[]
            addT4w = []
            addT4m = []


            """
            string dic scrapeResult ( memberName: [memberPosts ]) ←sent by UPS Scraper grabSoup()

string array ignore(name of tag) for each swing tag ← will contain names of people with tag already ← grabed by dataBase Get getNoTag() method

string array add(name of tag) for each tag. Empty intially and will be populated by names of people who need the tag

It goes through each scraped post of each person and if it sees a tag

checks the corresponding ignore list and if the person name is in there moves on

if the person name is not in there then append persons name to corresponding addTag array


then once its all done

call the dataBaseSet object on each of the addTags
            :param self:
            :return:
            """






