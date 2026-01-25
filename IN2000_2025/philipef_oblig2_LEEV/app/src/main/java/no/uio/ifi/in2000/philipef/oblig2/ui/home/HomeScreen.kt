package no.uio.ifi.in2000.philipef.oblig2.ui.home

import androidx.compose.foundation.Image
import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.lazy.grid.GridCells
import androidx.compose.foundation.lazy.grid.LazyVerticalGrid
import androidx.compose.foundation.lazy.grid.items
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.material3.Button
import androidx.compose.material3.Card
import androidx.compose.material3.DropdownMenu
import androidx.compose.material3.DropdownMenuItem
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.material3.TextButton
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
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
import androidx.navigation.compose.rememberNavController
import coil.compose.AsyncImage
import coil.request.ImageRequest
import no.uio.ifi.in2000.philipef.oblig2.R
import no.uio.ifi.in2000.philipef.oblig2.model.alpacas.AlpacaPartyInfo
import no.uio.ifi.in2000.philipef.oblig2.model.votes.District
import no.uio.ifi.in2000.philipef.oblig2.ui.theme.AlpacasTheme


@Composable
fun HomeScreen(
    navController: NavController,
    alpacaPartyUiState: AlpacaPartyUiState,
    retryAction: () -> Unit,
    selectDistrict: (District) -> Unit,
    modifier: Modifier = Modifier
) {
    when (alpacaPartyUiState) {
        is AlpacaPartyUiState.Loading -> LoadingScreen(modifier.size(200.dp))

        is AlpacaPartyUiState.Success -> {
            val partyInfoMap =
                alpacaPartyUiState.alpacas.associate { alpaca -> alpaca.id to alpaca.name }
            Column(modifier = modifier.padding(16.dp)) {
                DistrictDropdown(
                    selectedDistrict = alpacaPartyUiState.selectedDistrict,
                    onDistrictSelected = selectDistrict
                )
                Spacer(modifier = Modifier.height(16.dp))
                VoteList(
                    votes = alpacaPartyUiState.votes,
                    partyInfo = partyInfoMap
                )
                Spacer(modifier = Modifier.height(16.dp))
                AlpacaCardGrid(
                    alpacas = alpacaPartyUiState.alpacas,
                    navController = navController,
                    modifier = modifier.padding(
                        start = dimensionResource(R.dimen.padding_medium),
                        end = dimensionResource(R.dimen.padding_medium)
                    )
                )
            }
        }

        is AlpacaPartyUiState.Error -> ErrorScreen(retryAction, modifier)
    }
}

@Composable
fun DistrictDropdown(
    selectedDistrict: District,
    onDistrictSelected: (District) -> Unit
) {
    var expanded by remember { mutableStateOf(false) }

    Box(modifier = Modifier.fillMaxWidth()) {
        TextButton(onClick = { expanded = true }) {
            Text(text = "Valgt distrikt: ${selectedDistrict.name.replace('_', ' ')}")
        }

        DropdownMenu(
            expanded = expanded,
            onDismissRequest = { expanded = false }
        ) {
            District.entries.forEach { district ->
                DropdownMenuItem(
                    text = { Text(district.name.replace('_', ' ')) },
                    onClick = {
                        onDistrictSelected(district)
                        expanded = false
                    }
                )
            }
        }
    }
}


@Composable
fun LoadingScreen(modifier: Modifier = Modifier) {
    Image(
        painter = painterResource(R.drawable.loading_img),
        contentDescription = "Loading",
        modifier = modifier
    )
}

@Composable
fun ErrorScreen(retryAction: () -> Unit, modifier: Modifier = Modifier) {
    Column(
        modifier = modifier,
        verticalArrangement = Arrangement.Center,
        horizontalAlignment = Alignment.CenterHorizontally
    ) {
        Text("Failed to load")
        Button(onClick = retryAction) {
            Text("Retry")
        }
    }
}

@Composable
fun AlpacaCard(
    alpaca: AlpacaPartyInfo,
    onClick: (String) -> Unit,
    modifier: Modifier = Modifier
) {
    Card(
        modifier = modifier
            .clickable { onClick(alpaca.id) }
            .fillMaxWidth()
            .height(360.dp)
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
                    model = ImageRequest.Builder(context = LocalContext.current)
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
                    .padding(horizontal = 1.dp),
            )
        }

    }
}


@Composable
fun AlpacaCardGrid(
    alpacas: List<AlpacaPartyInfo>,
    navController: NavController,
    modifier: Modifier = Modifier,
) {
    LazyVerticalGrid(
        columns = GridCells.Fixed(2),
        modifier = modifier.fillMaxSize(),
    ) {
        items(alpacas) { alpaca ->
            AlpacaCard(
                alpaca = alpaca,
                onClick = {
                    val partyID = alpaca.id
                    navController.navigate("party/$partyID")
                }
            )
        }
    }
}


@Preview(showBackground = true)
@Composable
fun LoadingScreenPreview() {
    AlpacasTheme {
        LoadingScreen(
            Modifier
                .fillMaxSize()
                .size(200.dp)
        )
    }
}

@Preview(showBackground = true)
@Composable
fun ErrorScreenPreview() {
    AlpacasTheme {
        ErrorScreen({}, Modifier.fillMaxSize())
    }
}


@Preview(showBackground = true)
@Composable
fun AlpacaCardGridPreview() {
    AlpacasTheme {
        val mockData = List(10) {
            AlpacaPartyInfo(
                "5",
                "DESIR",
                "Chewbacca",
                "https://in2000-proxy.ifi.uio.no/alpacaapi/v2/assets/18788507266",
                "#edb879",
                "Chewbacca, med."
            )
        }
        AlpacaCardGrid(
            mockData,
            navController = rememberNavController(),
            modifier = Modifier.fillMaxSize()
        )
    }
}

/*
@Preview
@Composable
fun PreviewAlpacaCard() {
    val sampleAlpaca = AlpacaPartyInfo(
        id = "1",
        name = "AlpacaNorth",
        leader = "Chewpaca",
        img = "https://in2000-proxy.ifi.uio.no/alpacaapi/v2/assets/18788507266",
        color = "#edb879",
        description = "Chewpaca is a courageous alpaca from Oregon!"
    )
    AlpacaCard(
        alpaca = sampleAlpaca,
        onClick = TODO(),
        modifier = TODO()
    )
}
*/