TITLE = "E-Books"
ART = 'art-default.jpg'
ICON = 'icon-default.png'

def Start():
    Plugin.AddPrefixHandler('ebooks/main', MainMenu, TITLE, ICON, ART)
    Plugin.AddViewGroup('AuthorList', viewMode='List', mediaType='items')
    Plugin.addViewGroup('BookList', viewMode='List', mediaType='items')
    ObjectContainer.title1 = TITLE
    ObjectContainer.view_group = 'BookList'
    ObjectContainer.art = R(ART)
    DirectoryObject.thumb = R(ICON)
    DirectoryObject.art = R(ART)
    EpisodeObject.thumb = R(ICON)
    EpisodeObject.art = R(ART)
    HTTP.CacheTime = CACHE_1HOUR

def MainMenu():
    oc = ObjectContainer(objects=[
        DirectoryObject(key=Callback(LoadAuthors), title='Authors'),
        DirectoryObject(key=Callback(LoadTitles), title='Books')
        ])
    #oc.header='E-Books'
    #oc.message='Whats next?'
    return oc

@route('ebooks/authors')
def LoadAuthors():
    oc = ObjectContainer(view_group='AuthorList')
    oc.add(
        EpisodeObject(
            url='http://www.google.de',
            title='Dan Brown',
            summary='Die Type ebend',
            duration=1,
            thumb=Resource.ContentsOfURLWithFallback(url='http://authors.here/?n=Brown, Dan', fallback=ICON),
            originally_available_at = Datetime.FromTimestamp(1234).date()
        )
    )
    return oc

@route('ebooks/books')
def LoadTitles():
    oc = ObjectContainer(view_group='BookList')
    return oc
