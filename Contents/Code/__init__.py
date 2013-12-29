TITLE = "E-Books"
ART = 'art-default.jpg'
ICON = 'icon-default.png'

def Start():
    Plugin.AddPrefixHandler("ebooks/main", MainMenu, TITLE, ICON, ART)
    Plugin.AddViewGroup("InfoList", viewMode="InfoList", mediaType="items")

    ObjectContainer.title1 = TITLE
    ObjectContainer.view_group = 'List'
    ObjectContainer.art = R(ART)

    DirectoryObject.thumb = R(ICON)
    DirectoryObject.art = R(ART)

    EpisodeObject.thumb = R(ICON)
    EpisodeObject.art = R(ART)

    HTTP.CacheTime = CACHE_1HOUR


def MainMenu():
    oc = ObjectContainer(
            objects = [
                DirectoryObject(
                    key = Callback(LoadAuthors),
                    title = 'Authors'
                ),
                DirectoryObject(
                    key = Callback(LoadTitles),
                    title = 'E-Books'
                )
            ]
    )
    return oc

def LoadAuthors():
    oc = ObjectContainer()
    return oc

def LoadTitles():
    oc = ObjectContainer()
    return oc
