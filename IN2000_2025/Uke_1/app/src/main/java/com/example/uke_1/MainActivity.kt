package com.example.uke_1
// Lag en app med der du viser frem navnet ditt, en fun-fact og en liste av emner på IFI som du har tatt
import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.example.uke_1.ui.theme.Uke_1Theme

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContent {
            Uke_1Theme {
                MainScreen(context = this)
            }
        }
    }
}

@Composable
fun MainScreen(context: Context) {
    Column (
        modifier = Modifier
            .fillMaxSize()
            .padding(16.dp),
        horizontalAlignment = Alignment.CenterHorizontally,
        verticalArrangement = Arrangement.Center
    ) {
        NameTitle(name = "Philip Elias Fleischer")
        FunFact(funfact = "Fun Fact: \nI can not solve a rubix cube")
        Text(
            text = "Subjects taken:",
            fontSize = 20.sp,
            modifier = Modifier.padding(top = 16.dp),
            textAlign = TextAlign.Center
        )
        SubjectList()

        val iterSubjects = loadSubjectsFromFile(context)
        IterableSubjectList(iterSubjects)
    }
}

@Composable
fun NameTitle(name: String) {
    Text(
        text = name,
        fontSize = 40.sp,
        modifier = Modifier.padding(top = 16.dp),
        textAlign = TextAlign.Center
    )
}

@Composable
fun FunFact(funfact: String) {
    Text(
        text = funfact,
        fontSize = 20.sp,
        modifier = Modifier.padding(vertical = 30.dp),
        textAlign = TextAlign.Center
    )
}

@Composable
fun SubjectList() {
    val subjects = listOf(
        "IN1000",
        "IN1020",
        "IN1010",
        "IN1030",
        "IN2010",
        "IN2110",
        "IN2000"
    )

    Column(modifier = Modifier.padding(top = 16.dp)) {
        //Add a bulletin point list
        subjects.forEach { subject ->
            Text(
                //Bullet symbol before subject
                text = "• $subject",
                fontSize = 18.sp,
                modifier = Modifier.padding(start = 16.dp, bottom = 8.dp),
                textAlign = TextAlign.Start
            )
        }
    }
}
//Liste med emner, row og for løkke som iterer gjennom?


//Second list function with LAZY COLUMN to display the list
@Composable
fun IterableSubjectList(subjects: List<String>) {
    LazyColumn(modifier = Modifier.padding(top = 16.dp)) {
        items(subjects) { subject ->
            Text(
                text = "$subject", // Bullet symbol before the subject name
                fontSize = 18.sp,
                modifier = Modifier.padding(start = 16.dp, bottom = 8.dp),
                textAlign = TextAlign.Start
            )
        }
    }
}

//Function to load data from a file
fun loadSubjectsFromFile(context: Context): List<String> {
    val inputStream = context.resources.openRawResource(R.raw.subjects) //subjects.txt
    return inputStream.bufferedReader().readLines()
}


@Preview(showBackground = true)
@Composable
fun MainScreenPreview() {
    Uke_1Theme {
        MainScreen()
    }
}
