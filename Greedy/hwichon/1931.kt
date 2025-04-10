data class Pair(val start: Int, val end: Int)

fun main() = with(System.`in`.bufferedReader()) {
    val N = readLine().toInt()
    val meetingArr = mutableListOf<Pair>()
    repeat(N) {
        val (start, end) = readLine().split(" ").map { it.toInt() }
        meetingArr.add(Pair(start, end))
    }
    val sortedMeeting = meetingArr.sortedWith(compareBy({ it.end }, { it.start }))
    var count = 0
    var beforeEnd = 0;
    for (meet in sortedMeeting) {
        if (meet.start - beforeEnd >= 0) {
            count++
            beforeEnd = meet.end
        }
    }
    println(count)
}
