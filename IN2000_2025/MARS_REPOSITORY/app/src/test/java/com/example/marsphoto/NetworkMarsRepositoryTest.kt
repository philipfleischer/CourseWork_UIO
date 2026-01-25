package com.example.marsphoto

import com.example.marsphoto.fake.FakeDataSource
import com.example.marsphoto.fake.FakeMarsApiService
import com.example.marsphotos.data.NetworkMarsPhotoRepository
import kotlinx.coroutines.test.runTest
import org.junit.Assert.assertEquals
import org.junit.Test

class NetworkMarsRepositoryTest {
    @Test
    fun networkMarsPhotoRepository_getMarsPhotos_verifyPhotoList() =
        runTest {
            val repository = NetworkMarsPhotoRepository(
                marsApiService = FakeMarsApiService()
            )
            assertEquals(FakeDataSource.photosList, repository.getMarsPhotos())
            /*By passing the fake API service, any calls to the marsApiService
            property in the repository result in a call to the FakeMarsApiService. By passing
            fake classes for dependencies, you can control exactly what the dependency returns.
            This approach ensures that the code you are testing doesn't depend on untested code
            or APIs that could change or have unforeseen problems. Such situations can cause
            your test to fail, even when nothing is wrong with the code you wrote. Fakes help
            create a more consistent test environment, reduce test flakiness, and facilitate
            concise tests that test a single functionality.*/
        }
}