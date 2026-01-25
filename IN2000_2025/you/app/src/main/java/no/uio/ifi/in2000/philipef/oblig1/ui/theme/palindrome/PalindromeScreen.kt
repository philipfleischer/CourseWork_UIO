package no.uio.ifi.in2000.philipef.oblig1.ui.theme.palindrome

import androidx.compose.foundation.border
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.wrapContentHeight
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.text.KeyboardActions
import androidx.compose.foundation.text.KeyboardOptions
import androidx.compose.foundation.verticalScroll
import androidx.compose.material3.Button
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.material3.TextField
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.RectangleShape
import androidx.compose.ui.platform.LocalSoftwareKeyboardController
import androidx.compose.ui.text.input.ImeAction
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.navigation.NavController
import no.uio.ifi.in2000.philipef.oblig1.isPalindrome
import no.uio.ifi.in2000.philipef.oblig1.ui.theme.unitconverter.MyPaddings

@Composable
fun PalindromeScreen(
    navController: NavController,
    modifier: Modifier = Modifier
) {
    val scrollState = rememberScrollState()
    Column(
        modifier = modifier
            .fillMaxSize()
            .padding(top = MyPaddings.paddingLarge)
            .verticalScroll(scrollState),
        verticalArrangement = Arrangement.SpaceBetween,
        horizontalAlignment = Alignment.CenterHorizontally
    ) {
        PalindromeChecker(modifier = Modifier.padding(MyPaddings.paddingMedium))
        Spacer(modifier = Modifier.weight(1f))
        ScreenNavButton(navController)
    }
}

@Composable
fun ScreenNavButton(
    navController: NavController,
    modifier: Modifier = Modifier
) {
    Button(
        onClick = { navController.navigate("unitconverter") },
        modifier = modifier
            .fillMaxWidth()
            .height(80.dp),
        shape = RectangleShape
    ) {
        Text(text = "Go to Unit Converter")
    }
}


@Composable
fun PalindromeChecker(
    modifier: Modifier = Modifier
) {
    var text by remember { mutableStateOf("") }
    var result by remember { mutableStateOf("") }
    val keyboardController = LocalSoftwareKeyboardController.current

    fun enterButton() {
        result = if (isPalindrome(text)) {
            "$text --> Is a palindrome"
        } else {
            "$text --> Is not a palindrome"
        }
        keyboardController?.hide()
    }

    Column(
        modifier = modifier
            .padding(MyPaddings.paddingMedium)
            .fillMaxWidth(),
        horizontalAlignment = Alignment.CenterHorizontally,
        verticalArrangement = Arrangement.Top
    ) {
        Text(
            text = "Palindrome Checker",
            fontSize = 30.sp,
            modifier = Modifier.padding(MyPaddings.paddingLarge)
        )
        TextField(
            value = text,
            onValueChange = { text = it },
            label = { Text("Is it Palindrome?") },
            keyboardOptions = KeyboardOptions.Default.copy(
                imeAction = ImeAction.Done
            ),
            modifier = Modifier,
            keyboardActions = KeyboardActions(
                onDone = {
                    enterButton()
                }
            )
        )

        Button(
            onClick = { enterButton() },
            modifier = Modifier
                .padding(MyPaddings.paddingMedium)
        )
        { Text(text = "Check") }

        if (result.isNotEmpty()) {
            Box(
                modifier = Modifier
                    .wrapContentHeight()
                    .border(2.dp, Color.Black)
                    .padding(MyPaddings.paddingMedium),
                contentAlignment = Alignment.Center
            ) {
                Text(
                    text = result,
                    style = MaterialTheme.typography.bodyLarge,
                )
            }
        }
    }
}
