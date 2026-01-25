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
package com.example.racetracker

import com.example.racetracker.ui.RaceParticipant
import junit.framework.TestCase.assertEquals
import kotlinx.coroutines.launch
import kotlinx.coroutines.test.advanceTimeBy
import kotlinx.coroutines.test.runCurrent
import kotlinx.coroutines.test.runTest
import org.junit.Test

class RaceParticipantTest {
    private val raceParticipant = RaceParticipant(
        name = "Test",
        maxProgress = 100,
        progressDelayMillis = 500L,
        initialProgress = 0,
        progressIncrement = 1
    )

    //Since the test block needs to be placed in the runTest builder,
    // use the expression
    // syntax to return the runTest() block as a test result.
    @Test
    fun raceParticipant_RaceStarted_ProgressUpdated() = runTest {
        val expectedProgress = 1
        launch { raceParticipant.run() }
        //Use the advanceTimeBy() helper function to advance the time
        // by the value of raceParticipant.progressDelayMillis. The
        // advanceTimeBy() function helps to reduce the test execution time.
        advanceTimeBy(raceParticipant.progressDelayMillis)
        //Since advanceTimeBy() doesn't run the task scheduled at the given duration,
        // you need to call the runCurrent() function. This function executes any
        // pending tasks at the current time.
        runCurrent()
        //To ensure the progress updates, add a call to the assertEquals() function
        // to check if the value of the raceParticipant.currentProgress property
        // matches the value of the expectedProgress variable.
        assertEquals(expectedProgress, raceParticipant.currentProgress)
    }

    @Test
    fun raceParticipant_RaceFinished_ProgressUpdated() = runTest {
        //Use launch builder to launch a new coroutine and add a call
        // to the raceParticipant.run() function in it.
        launch { raceParticipant.run() }
        //To simulate the race finish, use the advanceTimeBy() function to
        // advance the dispatcher's time by
        // raceParticipant.maxProgress * raceParticipant.progressDelayMillis:
        advanceTimeBy(raceParticipant.maxProgress * raceParticipant.progressDelayMillis)
        runCurrent()
        //To ensure the progress updates correctly, add a call to the assertEquals()
        // function to check if the value of the raceParticipant.currentProgress
        // property is equal to 100.
        assertEquals(100, raceParticipant.currentProgress)
    }
}









