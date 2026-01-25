package com.example.marsphotos.data

import com.example.marsphotos.model.MarsPhoto
import com.example.marsphotos.network.MarsApiService

interface MarsPhotosRepository {
    /*Inside the MarsPhotosRepository interface,
    add an abstract function called getMarsPhotos(),
    which returns a list of MarsPhoto objects. It is called from a coroutine,
    so declare it with suspend.*/
    suspend fun getMarsPhotos(): List<MarsPhoto>
}

/*Inside the NetworkMarsPhotosRepository class,
override the abstract function getMarsPhotos(). This function returns the
data from calling MarsApi.retrofitService.getPhotos().*/
class NetworkMarsPhotoRepository(
    private val marsApiService: MarsApiService
) : MarsPhotosRepository {
    /*In the NetworkMarsPhotosRepository class, in the getMarsPhotos()
    function, change the return statement to retrieve data from marsApiService.*/
    override suspend fun getMarsPhotos(): List<MarsPhoto> = marsApiService.getPhotos()
}