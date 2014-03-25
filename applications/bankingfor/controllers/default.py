def index():
    response.flash = T("let's change banking")
    return dict()



@cache.action()
def download():
    return response.download(request, db)


def call():
    return service()


@auth.requires_signature()
def data():
    return dict(form=crud())
