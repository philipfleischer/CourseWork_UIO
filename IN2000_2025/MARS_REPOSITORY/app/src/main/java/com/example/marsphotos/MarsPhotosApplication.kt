package com.example.marsphotos

import android.app.Application
import com.example.marsphotos.data.AppContainer
import com.example.marsphotos.data.DefaultAppContainer

/*This class inherits from the application object
, so you need to add it to the class declaration.*/
class MarsPhotosApplication : Application() {
    /*Inside the MarsPhotosApplication class,
    declare a variable called container of the type AppContainer to
    store the DefaultAppContainer object. The variable is initialized
    during the call to onCreate(), so the variable needs to be marked
    with the lateinit modifier.*/
    lateinit var container: AppContainer
    override fun onCreate() {
        super.onCreate()
        container = DefaultAppContainer()
    }
}