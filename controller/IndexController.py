from pytonik import Web as mvc

m = mvc.App()


def index():
    
    data = {
        'title': "pytonik MVC",
        
    }
    m.header()
    m.views('index', data)


