fun main() = with(System.`in`.bufferedReader()) {
    val N = readLine().toInt()
    val (A, B) = readLine().split(" ").map { it.toInt() }
    val points = HashMap<Int, MutableSet<Int>>()

    repeat(N) {
        val (x, y) = readLine().split(" ").map { it.toInt() }
        points.computeIfAbsent(x) { mutableSetOf() }.add(y)
    }

    var total = 0
    for ((x, yList) in points) {
        for (y in yList) {
            val x1 = x + A
            val y1 = y + B
            if (points[x1]?.contains(y) == true &&
                points[x]?.contains(y1) == true &&
                points[x1]?.contains(y1) == true
            ) {
                total++
            }
        }
    }
    println(total)
}
