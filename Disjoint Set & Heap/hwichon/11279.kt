import java.util.PriorityQueue

fun main() = with(System.`in`.bufferedReader()) {
    val N = readLine().toInt()
    val list = PriorityQueue<Int>(compareByDescending { it })
    val answer = mutableListOf<Int>()

    repeat(N) {
        val x = readLine().toInt()
        if (x == 0) {
            if (list.isEmpty()) {
                answer.add(0)
                return@repeat
            } else {
                answer.add(list.poll())
            }
        } else {
            list.add(x)
        }
    }
    answer.forEach { println(it) }
}
