package no.uio.ifi.in2000.philipef.oblig2

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.navigation.compose.rememberNavController
import no.uio.ifi.in2000.philipef.oblig2.ui.AlpacaApp
import no.uio.ifi.in2000.philipef.oblig2.ui.theme.AlpacasTheme

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContent {
            AlpacasTheme {
                val navController = rememberNavController()
                AlpacaApp(navController = navController)

            }
        }
    }
}
