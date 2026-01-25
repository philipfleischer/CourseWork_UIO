package no.uio.ifi.in2000.philipef.oblig1

import kotlin.math.roundToInt

fun converter(amount: Int, converterUnit: ConverterUnits): Int {
    return when (converterUnit) {
        ConverterUnits.GALLON -> (amount * 3.78541).roundToInt()
        ConverterUnits.CUP -> (amount * 0.23659).roundToInt()
        ConverterUnits.OUNCE -> (amount * 0.02957).roundToInt()
        ConverterUnits.HOGSHEAD -> (amount * 238.481).roundToInt()
    }
}