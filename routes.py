from pytonik.Router import Router

route = Router()

route.get("/")

route.any('fff', 'profileController@index:id:user')

route.any('login', 'AccountController@signin')

route.any('register', 'AccountController@signup')

route.any('recover', 'AccountController@recover')

route.get('logout', 'AccountController@signout')

route.get('first', 'AccountController@update_user_step_one')

route.any('professionals', 'indexController@professionals')

route.any('companies', 'indexController@companies')

#route.any('info', 'profileController@info')


route.get('profile/follow', route.args(
    params=['id']

))
