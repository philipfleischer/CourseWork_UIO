package no.uio.ifi.in2000.philipef.oblig2.data.alpacas

import com.jakewharton.retrofit2.converter.kotlinx.serialization.asConverterFactory
import kotlinx.serialization.json.Json
import no.uio.ifi.in2000.philipef.oblig2.data.votes.AggregatedVotesDataSource
import no.uio.ifi.in2000.philipef.oblig2.data.votes.IndividualVotesDataSource
import no.uio.ifi.in2000.philipef.oblig2.data.votes.VotesRepository
import no.uio.ifi.in2000.philipef.oblig2.network.AlpacaApiService
import okhttp3.MediaType.Companion.toMediaType
import retrofit2.Retrofit

interface AppContainer {
    val alpacaPartiesRepository: AlpacaPartiesRepository
    val votesRepository: VotesRepository
}

class DefaultAppContainer : AppContainer {

    private val baseUrl = "https://in2000-proxy.ifi.uio.no/alpacaapi/v2/"

    private val json = Json {
        ignoreUnknownKeys = true
        isLenient = true
    }

    private val retrofit: Retrofit = Retrofit.Builder()
        .baseUrl(baseUrl)
        .addConverterFactory(json.asConverterFactory("application/json".toMediaType()))
        .build()

    private val alpacaApiService: AlpacaApiService by lazy {
        retrofit.create(AlpacaApiService::class.java)
    }

    override val votesRepository: VotesRepository by lazy {
        VotesRepository(
            IndividualVotesDataSource(alpacaApiService),
            AggregatedVotesDataSource(alpacaApiService)
        )
    }

    override val alpacaPartiesRepository: AlpacaPartiesRepository by lazy {
        DefaultAlpacasRepository(alpacaApiService, votesRepository)
    }
}

