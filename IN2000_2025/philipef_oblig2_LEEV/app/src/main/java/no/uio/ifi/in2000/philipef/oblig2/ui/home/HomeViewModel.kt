package no.uio.ifi.in2000.philipef.oblig2.ui.home

import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.setValue
import androidx.lifecycle.ViewModel
import androidx.lifecycle.ViewModelProvider
import androidx.lifecycle.viewModelScope
import androidx.lifecycle.viewmodel.initializer
import androidx.lifecycle.viewmodel.viewModelFactory
import kotlinx.coroutines.launch
import no.uio.ifi.in2000.philipef.oblig2.AlpacaApplication
import no.uio.ifi.in2000.philipef.oblig2.data.alpacas.AlpacaPartiesRepository
import no.uio.ifi.in2000.philipef.oblig2.data.votes.VotesRepository
import no.uio.ifi.in2000.philipef.oblig2.model.alpacas.AlpacaPartyInfo
import no.uio.ifi.in2000.philipef.oblig2.model.votes.District

sealed interface AlpacaPartyUiState {
    data class Success(
        val alpacas: List<AlpacaPartyInfo>,
        val selectedDistrict: District = District.DISTRICT_1,
        val votes: Map<String, Int> = emptyMap()
    ) : AlpacaPartyUiState

    data object Error : AlpacaPartyUiState
    data object Loading : AlpacaPartyUiState
}

class AlpacasViewModel(
    private val alpacaPartiesRepository: AlpacaPartiesRepository,
    private val votesRepository: VotesRepository
) : ViewModel() {

    var alpacaPartyUiState: AlpacaPartyUiState by mutableStateOf(AlpacaPartyUiState.Loading)
        private set

    init {
        getAlpacas()
    }

    fun getAlpacas() {
        viewModelScope.launch {
            alpacaPartyUiState = AlpacaPartyUiState.Loading
            alpacaPartyUiState = try {
                AlpacaPartyUiState.Success(alpacaPartiesRepository.getAlpacas()).also {
                    selectDistrict(it.selectedDistrict)
                }
            } catch (e: Exception) {
                AlpacaPartyUiState.Error
            }
        }
    }

    fun selectDistrict(district: District) {
        viewModelScope.launch {
            val votes = votesRepository.getVotesForDistrict(district)
                .associate { it.alpacaPartyId to it.numberOfVotesForParty }

            (alpacaPartyUiState as AlpacaPartyUiState.Success).let {
                alpacaPartyUiState = it.copy(
                    selectedDistrict = district,
                    votes = votes
                )
            }
        }
    }

    companion object {
        val Factory: ViewModelProvider.Factory = viewModelFactory {
            initializer {
                val application =
                    (this[ViewModelProvider.AndroidViewModelFactory.APPLICATION_KEY] as AlpacaApplication)
                AlpacasViewModel(
                    alpacaPartiesRepository = application.container.alpacaPartiesRepository,
                    votesRepository = application.container.votesRepository
                )
            }
        }
    }
}

