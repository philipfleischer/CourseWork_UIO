package no.uio.ifi.in2000.philipef.oblig1

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.compose.runtime.Composable
import androidx.navigation.NavHostController
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.compose.rememberNavController
import no.uio.ifi.in2000.philipef.oblig1.ui.theme.palindrome.PalindromeScreen
import no.uio.ifi.in2000.philipef.oblig1.ui.theme.theme.Philipef_oblig1Theme
import no.uio.ifi.in2000.philipef.oblig1.ui.theme.unitconverter.UnitConverterScreen

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContent {
            Philipef_oblig1Theme {
                val navController = rememberNavController()
                NavGraph(navController = navController)
            }
        }
    }
}

object Routes {
    const val PALINDROME = "palindrome"
    const val UNIT_CONVERTER = "unitconverter"
}

@Composable
fun NavGraph(navController: NavHostController) {
    NavHost(navController = navController, startDestination = Routes.PALINDROME) {
        composable(Routes.PALINDROME) {
            PalindromeScreen(navController)
        }
        composable(Routes.UNIT_CONVERTER) {
            UnitConverterScreen(navController)
        }
    }
}