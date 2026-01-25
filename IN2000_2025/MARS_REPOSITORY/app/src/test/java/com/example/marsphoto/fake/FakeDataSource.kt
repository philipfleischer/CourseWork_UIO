package com.example.marsphoto.fake

import com.example.marsphotos.model.MarsPhoto

/*In this object, create a property
set to a list of MarsPhoto objects. The list
does not have to be long, but it should contain at least two objects.*/
object FakeDataSource {
    const val idOne = "img1"
    const val idTwo = "img2"
    const val imgOne = "url.1"
    const val imgTwo = "url.2"

    val photosList = listOf(
        MarsPhoto(
            id = idOne,
            imgSrc = imgOne
        ),
        MarsPhoto(
            id = idTwo,
            imgSrc = imgTwo
        )
    )

}