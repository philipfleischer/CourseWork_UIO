package no.uio.ifi.in2000.philipef.oblig2

import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext
import androidx.lifecycle.viewmodel.compose.viewModel
import androidx.navigation.NavHostController
import androidx.navigation.NavType
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.navArgument
import no.uio.ifi.in2000.philipef.oblig2.ui.home.AlpacasViewModel
import no.uio.ifi.in2000.philipef.oblig2.ui.home.HomeScreen
import no.uio.ifi.in2000.philipef.oblig2.ui.party.PartyScreen
import no.uio.ifi.in2000.philipef.oblig2.ui.party.PartyViewModel

@Composable
fun AlpacaNavHost(
    navController: NavHostController,
    modifier: Modifier = Modifier,
    alpacasViewModel: AlpacasViewModel = viewModel(factory = AlpacasViewModel.Factory)
) {
    NavHost(
        navController = navController,
        startDestination = "home",
        modifier = modifier
    ) {
        composable("home") {
            HomeScreen(
                navController = navController,
                alpacaPartyUiState = alpacasViewModel.alpacaPartyUiState,
                retryAction = alpacasViewModel::getAlpacas,
                selectDistrict = alpacasViewModel::selectDistrict
            )
        }

        composable(
            route = "party/{partyID}",
            arguments = listOf(navArgument("partyID") { type = NavType.StringType })
        ) { backStackEntry ->
            val partyID = backStackEntry.arguments?.getString("partyID") ?: ""
            val partyViewModel: PartyViewModel = viewModel(
                factory = PartyViewModel.provideFactory((LocalContext.current.applicationContext as AlpacaApplication).container.alpacaPartiesRepository)
            )
            PartyScreen(
                partyID = partyID,
                navController = navController,
                viewModel = partyViewModel
            )
        }
    }
}
