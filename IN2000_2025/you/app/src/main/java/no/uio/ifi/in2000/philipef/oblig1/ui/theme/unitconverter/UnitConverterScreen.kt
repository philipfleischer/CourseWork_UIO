package no.uio.ifi.in2000.philipef.oblig1.ui.theme.unitconverter

import androidx.compose.foundation.border
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
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
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.ArrowDropDown
import androidx.compose.material3.Button
import androidx.compose.material3.DropdownMenu
import androidx.compose.material3.DropdownMenuItem
import androidx.compose.material3.Icon
import androidx.compose.material3.IconButton
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.material3.TextField
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.RectangleShape
import androidx.compose.ui.platform.LocalSoftwareKeyboardController
import androidx.compose.ui.text.input.ImeAction
import androidx.compose.ui.text.input.KeyboardType
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.navigation.NavController
import no.uio.ifi.in2000.philipef.oblig1.ConverterUnits
import no.uio.ifi.in2000.philipef.oblig1.converter

@Composable
fun UnitConverterScreen(
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
        UnitConverter(modifier = Modifier.fillMaxWidth())
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
        onClick = { navController.navigate("palindrome") },
        modifier = modifier
            .height(80.dp)
            .fillMaxWidth(),
        shape = RectangleShape
    ) {
        Text(text = "Go to Palindrome Checker")
    }
}


@Composable
fun UnitConverter(
    modifier: Modifier = Modifier
) {
    var amount by remember { mutableIntStateOf(0) }
    var expanded by remember { mutableStateOf(false) }
    var result by remember { mutableIntStateOf(0) }
    var selectedUnit by remember { mutableStateOf(UnitOption("Ounce", ConverterUnits.OUNCE)) }

    val keyboardController = LocalSoftwareKeyboardController.current

    LaunchedEffect(amount, selectedUnit.unit) {
        result = converter(amount, selectedUnit.unit)
    }

    Column(
        modifier = modifier.padding(MyPaddings.paddingMedium),
        horizontalAlignment = Alignment.CenterHorizontally,
        verticalArrangement = Arrangement.spacedBy(MyPaddings.spacingMedium)
    ) {
        Text(
            text = "Unit converter",
            fontSize = 30.sp
        )

        UnitDropDown(
            selectedUnit = selectedUnit,
            unitOptions = ConverterUnits.entries.map { UnitOption(it.name, it) },
            onUnitSelected = { selectedUnit = it },
            expanded = expanded,
            onExpandedChange = { expanded = it }
        )

        TextField(
            value = if (amount == 0) "" else amount.toString(),
            onValueChange = { amount = it.toIntOrNull() ?: 0 },
            label = { Text("Enter amount of ${selectedUnit.name}s you want converted to liter") },
            keyboardOptions = KeyboardOptions.Default.copy(
                keyboardType = KeyboardType.Number,
                imeAction = ImeAction.Done
            ),
            modifier = Modifier.fillMaxWidth(),
            keyboardActions = KeyboardActions(
                onDone = {
                    result = converter(amount, selectedUnit.unit)
                    keyboardController?.hide()
                }
            )
        )
        ConversionResultField(amount, selectedUnit.name, result)
    }
}

data class UnitOption(val name: String, val unit: ConverterUnits)

object MyPaddings {
    val paddingSmall = 8.dp
    val paddingMedium = 16.dp
    val paddingLarge = 30.dp
    val spacingMedium = 16.dp
}

@Composable
fun UnitDropDown(
    selectedUnit: UnitOption,
    unitOptions: List<UnitOption>,
    onUnitSelected: (UnitOption) -> Unit,
    expanded: Boolean,
    onExpandedChange: (Boolean) -> Unit,
    modifier: Modifier = Modifier
) {
    Box {
        Row(
            modifier = modifier,
            verticalAlignment = Alignment.CenterVertically,
            horizontalArrangement = Arrangement.spacedBy(MyPaddings.paddingSmall)
        ) {
            Text(
                text = selectedUnit.name,
            )
            IconButton(onClick = { onExpandedChange(!expanded) }) {
                Icon(Icons.Default.ArrowDropDown, contentDescription = "Dropdown Arrow")
            }
        }
        DropdownMenu(
            expanded = expanded,
            onDismissRequest = { onExpandedChange(false) }
        ) {
            unitOptions.forEach { unit ->
                DropdownMenuItem(
                    text = { Text(unit.name) },
                    onClick = {
                        onUnitSelected(unit)
                        onExpandedChange(false)
                    }
                )
            }
        }
    }
}


@Composable
fun ConversionResultField(amount: Int, unit: String, result: Int, modifier: Modifier = Modifier) {
    Box(
        modifier = modifier
            .padding(top = MyPaddings.paddingLarge)
            .wrapContentHeight()
            .border(2.dp, Color.Black)
            .padding(MyPaddings.paddingMedium),
        contentAlignment = Alignment.Center
    ) {
        Text(
            text = "$amount ${unit}s equals $result liters",
            style = MaterialTheme.typography.bodyLarge,
            modifier = Modifier.fillMaxWidth()
        )
    }
}
