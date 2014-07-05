################################
####account#####################
################################
def account():
    return dict(message=T('Hello World'))    


################################
####index#######################
################################
def index():
    response.flash = T("let's change banking")
    return dict()

################################
####member######################
################################
def member():
    return dict(message=T('Hello World'))

################################
####members#####################
################################
def member():
    return dict(message=T('Hello World'))

################################
####stats#######################
################################
def stats():
    return dict(message=T('Hello World'))

################################
####transparency################
################################
def transparency():
    return dict(message=T('Hello World'))



@cache.action()
def download():
    return response.download(request, db)


def call():
    return service()


@auth.requires_signature()
def data():
    return dict(form=crud())
