/*
 * Copyright (C) 2023 The Android Open Source Project
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     https://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.example.marsphotos.model

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/*When kotlinx serialization parses the JSON, it matches the keys by name
and fills the data objects with appropriate values.*/
@Serializable
data class MarsPhoto(
    val id: String,
    /*To use variable names in your data class that differ from the key names
in the JSON response, use the @SerialName annotation. In the following
example, the name of the variable in the data class is imgSrc. The variable
can be mapped to the JSON attribute img_src using @SerialName(value = "img_src").

Replace the line for the img_src key with the line shown below.*/
    @SerialName(value = "img_src")
    val imgSrc: String
)
