package no.uio.ifi.in2000.philipef.oblig2

import android.app.Application
import no.uio.ifi.in2000.philipef.oblig2.data.alpacas.AppContainer
import no.uio.ifi.in2000.philipef.oblig2.data.alpacas.DefaultAppContainer

class AlpacaApplication : Application() {
    lateinit var container: AppContainer
    override fun onCreate() {
        super.onCreate()
        container = DefaultAppContainer()
    }
}