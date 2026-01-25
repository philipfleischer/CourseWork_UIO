package no.uio.ifi.in2000.philipef.oblig2.data.alpacas

import no.uio.ifi.in2000.philipef.oblig2.data.votes.VotesRepository
import no.uio.ifi.in2000.philipef.oblig2.model.alpacas.AlpacaPartyInfo
import no.uio.ifi.in2000.philipef.oblig2.model.votes.District
import no.uio.ifi.in2000.philipef.oblig2.model.votes.DistrictVotes
import no.uio.ifi.in2000.philipef.oblig2.network.AlpacaApiService

interface AlpacaPartiesRepository {
    suspend fun getAlpacas(): List<AlpacaPartyInfo>
    suspend fun getPartyById(id: String): AlpacaPartyInfo?
    suspend fun getPartiesWithVotes(district: District): List<DistrictVotes>
}

class DefaultAlpacasRepository(
    private val alpacaApiService: AlpacaApiService,
    private val votesRepository: VotesRepository
) : AlpacaPartiesRepository {
    override suspend fun getAlpacas(): List<AlpacaPartyInfo> {
        return alpacaApiService.getAlpacas().parties
    }

    override suspend fun getPartyById(id: String): AlpacaPartyInfo? {
        return alpacaApiService.getAlpacas().parties.find { it.id == id }
    }

    override suspend fun getPartiesWithVotes(district: District): List<DistrictVotes> {
        val votes = votesRepository.getVotesForDistrict(district)
        val alpacas = getAlpacas()

        return votes.map { vote ->
            val partyName = alpacas.find { it.id == vote.alpacaPartyId }?.name ?: "PartiUkjent"
            vote.copy(
                alpacaPartyId = partyName,
                numberOfVotesForParty = vote.numberOfVotesForParty
            )
        }
    }
}


