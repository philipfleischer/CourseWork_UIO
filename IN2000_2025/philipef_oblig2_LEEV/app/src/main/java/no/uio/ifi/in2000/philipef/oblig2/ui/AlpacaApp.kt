package no.uio.ifi.in2000.philipef.oblig2.ui

import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.material3.TopAppBar
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.lifecycle.viewmodel.compose.viewModel
import androidx.navigation.NavHostController
import no.uio.ifi.in2000.philipef.oblig2.AlpacaNavHost
import no.uio.ifi.in2000.philipef.oblig2.ui.home.AlpacasViewModel


@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun AlpacaApp(navController: NavHostController) {
    val alpacasViewModel: AlpacasViewModel = viewModel(factory = AlpacasViewModel.Factory)
    Scaffold(
        modifier = Modifier.fillMaxSize(),
        topBar = {
            TopAppBar(
                title = {
                    Text(
                        text = "Partier",
                        style = MaterialTheme.typography.headlineLarge
                    )
                }
            )
        }
    ) { paddingValues ->
        AlpacaNavHost(
            navController = navController,
            modifier = Modifier.padding(paddingValues),
            alpacasViewModel = alpacasViewModel
        )
    }
}
