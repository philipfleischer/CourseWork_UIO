package no.uio.ifi.in2000.philipef.oblig2.ui.party

import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.automirrored.filled.ArrowBack
import androidx.compose.material3.Card
import androidx.compose.material3.CenterAlignedTopAppBar
import androidx.compose.material3.CircularProgressIndicator
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.Icon
import androidx.compose.material3.IconButton
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.getValue
import androidx.compose.runtime.livedata.observeAsState
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.layout.ContentScale
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.res.dimensionResource
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import androidx.navigation.NavController
import coil.compose.AsyncImage
import coil.request.ImageRequest
import no.uio.ifi.in2000.philipef.oblig2.R
import no.uio.ifi.in2000.philipef.oblig2.model.alpacas.AlpacaPartyInfo


@Composable
fun PartyScreen(
    partyID: String,
    navController: NavController,
    viewModel: PartyViewModel
) {
    LaunchedEffect(partyID) {
        viewModel.getPartyById(partyID)
    }

    val partyState by viewModel.party.observeAsState()

    when (partyState) {
        null -> {
            Box(
                modifier = Modifier.fillMaxSize(),
                contentAlignment = Alignment.Center
            ) {
                CircularProgressIndicator()
            }
        }

        else -> {
            AlpacaPartySpecific(alpaca = partyState!!, navController = navController)
        }
    }
}

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun AlpacaPartySpecific(
    alpaca: AlpacaPartyInfo,
    navController: NavController,
    modifier: Modifier = Modifier
) {
    Column(
        modifier = modifier
            .fillMaxSize()
            .padding(dimensionResource(R.dimen.padding_medium))
    ) {
        CenterAlignedTopAppBar(
            title = { Text(text = alpaca.name) },
            navigationIcon = {
                IconButton(onClick = { navController.popBackStack() }) {
                    Icon(
                        imageVector = Icons.AutoMirrored.Filled.ArrowBack,
                        contentDescription = "Back"
                    )
                }
            }
        )

        Card(
            modifier = Modifier
                .fillMaxWidth()
                .padding(top = 8.dp)
        ) {
            Column(
                modifier = Modifier
                    .fillMaxSize()
                    .padding(dimensionResource(R.dimen.padding_medium)),
                verticalArrangement = Arrangement.SpaceBetween,
                horizontalAlignment = Alignment.CenterHorizontally
            ) {
                Column(
                    modifier = Modifier.weight(1f),
                    horizontalAlignment = Alignment.CenterHorizontally
                ) {
                    Text(
                        text = alpaca.name,
                        modifier = Modifier
                            .fillMaxWidth()
                            .padding(dimensionResource(R.dimen.padding_small)),
                        style = MaterialTheme.typography.titleLarge,
                        fontWeight = FontWeight.Bold,
                        textAlign = TextAlign.Start
                    )
                    AsyncImage(
                        modifier = Modifier
                            .fillMaxWidth()
                            .height(140.dp)
                            .clip(CircleShape)
                            .padding(8.dp),
                        model = ImageRequest.Builder(LocalContext.current)
                            .data(alpaca.img)
                            .crossfade(true)
                            .build(),
                        contentDescription = null,
                        contentScale = ContentScale.Crop,
                        error = painterResource(id = R.drawable.ic_broken_image),
                        placeholder = painterResource(id = R.drawable.loading_img)
                    )
                    Text(
                        text = "Leder: ${alpaca.leader}",
                        modifier = Modifier
                            .fillMaxWidth()
                            .padding(dimensionResource(R.dimen.padding_medium)),
                        style = MaterialTheme.typography.titleLarge,
                        fontWeight = FontWeight.Bold,
                        textAlign = TextAlign.Start
                    )
                }

                Box(
                    modifier = Modifier
                        .fillMaxWidth()
                        .height(20.dp)
                        .background(Color(android.graphics.Color.parseColor(alpaca.color)))
                )

                Text(
                    text = alpaca.description,
                    modifier = Modifier
                        .fillMaxWidth()
                        .padding(dimensionResource(R.dimen.padding_medium)),
                    style = MaterialTheme.typography.bodyMedium,
                    fontWeight = FontWeight.Normal,
                    textAlign = TextAlign.Start
                )
            }
        }
    }
}


@Preview
@Composable
fun PreviewAlpacaPartySpecific() {
    val sampleAlpaca = AlpacaPartyInfo(
        id = "1",
        name = "AlpacaNorth",
        leader = "Chewpaca",
        img = "https://in2000-proxy.ifi.uio.no/alpacaapi/v2/assets/18788507266",
        color = "#edb879",
        description = "Chewpaca, med sin saftige, brune pels og navn inspirert av den berÃ¸mte Star Wars-karakteren Chewbacca, er en uimotstÃ¥elig alpakka fÃ¸dt under de klare stjernehimmelen pÃ¥ et dyreelskende smÃ¥bruk i Oregon.\\n\\nHan kom til verden med en bemerkelsesverdig hÃ¸y statur og et ansikt sÃ¥ uttrykksfullt at det straks minnet gÃ¥rdseierne om den kjÃ¦re Wookiee krigeren. Chewpaca viste seg tidlig som en naturlig beskytter av de yngre og mindre alpakkaene pÃ¥ gÃ¥rden, og hans dype, nysgerrige brumming la til personligheten som allerede var like stor som hans filmiske motpart.\\n\\nKjÃ¦rlig og leken, har han blitt lokalberÃ¸mthet for sitt gode humÃ¸r og for sin rolle i Ã¥ gjÃ¸re gÃ¥rdbesÃ¸k til et intergalaktisk eventyr for fans og familier som kommer for Ã¥ mÃ¸te denne stjernen fra alpakkaverdenen."
    )
    AlpacaPartySpecific(
        alpaca = sampleAlpaca,
        navController = NavController(LocalContext.current)
    )
}