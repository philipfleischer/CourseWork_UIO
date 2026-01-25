package no.uio.ifi.in2000.philipef.oblig2.ui.party

import androidx.lifecycle.LiveData
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import androidx.lifecycle.ViewModelProvider
import androidx.lifecycle.viewModelScope
import kotlinx.coroutines.launch
import no.uio.ifi.in2000.philipef.oblig2.data.alpacas.AlpacaPartiesRepository
import no.uio.ifi.in2000.philipef.oblig2.model.alpacas.AlpacaPartyInfo

class PartyViewModel(
    private val repository: AlpacaPartiesRepository
) : ViewModel() {

    private val _party = MutableLiveData<AlpacaPartyInfo?>()
    val party: LiveData<AlpacaPartyInfo?> = _party

    fun getPartyById(id: String) {
        viewModelScope.launch {
            _party.value = repository.getPartyById(id)
        }
    }

    companion object {
        fun provideFactory(repository: AlpacaPartiesRepository): ViewModelProvider.Factory {
            return object : ViewModelProvider.Factory {
                override fun <T : ViewModel> create(modelClass: Class<T>): T {
                    if (modelClass.isAssignableFrom(PartyViewModel::class.java)) {
                        @Suppress("UNCHECKED_CAST")
                        return PartyViewModel(repository) as T
                    }
                    throw IllegalArgumentException("Not right, check class gitt: ${modelClass.name}")
                }
            }
        }
    }
}
