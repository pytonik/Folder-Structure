from pytonik import Web

m = Web.App()

def index():
  
   data = {'title': 'pytonik MVC Error Page'}
   m.header(0)
   m.views('404', data)

def page():
   
   data = {'title': 'pytonik MVC Error Page'}
   m.header(0)
   m.views('404', data)
