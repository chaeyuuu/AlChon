fun main() = with(System.`in`.bufferedReader()) {
    val formulaList = readLine().split("-")
    val first = formulaList.first().split("+").sumOf { it.toInt() }

    val rest = formulaList.drop(1).sumOf { part ->
        part.split("+").sumOf { it.toInt() }
    }
    println(first - rest)
}
