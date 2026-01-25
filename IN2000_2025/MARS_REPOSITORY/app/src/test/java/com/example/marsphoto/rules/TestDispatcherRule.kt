package com.example.marsphoto.rules

import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.test.TestDispatcher
import kotlinx.coroutines.test.UnconfinedTestDispatcher
import kotlinx.coroutines.test.resetMain
import kotlinx.coroutines.test.setMain
import org.junit.rules.TestWatcher
import org.junit.runner.Description

/*The TestWatcher class enables you to take actions on
different execution phases of a test.*/
class TestDispatcherRule(
    //Create a TestDispatcher constructor parameter for the TestDispatcherRule
    val testDispatcher: TestDispatcher = UnconfinedTestDispatcher(),
) : TestWatcher() {
    /*The primary goal of this test rule is to
    replace the Main dispatcher with a test dispatcher before a test begins
    to execute. The starting() function of the TestWatcher class executes before
    a given test executes. Override the starting() function.*/
    override fun starting(description: Description) {
        Dispatchers.setMain(testDispatcher)
    }

    /*After test execution is finished,
    reset the Main dispatcher by overriding the finished() method.
    Call the Dispatchers.resetMain() function.*/
    override fun finished(description: Description) {
        Dispatchers.resetMain()
    }
}