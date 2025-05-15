import java.util.PriorityQueue

fun main() = with(System.`in`.bufferedReader()) {
    val N = readLine().toInt()
    val pq = PriorityQueue<Int>()

    repeat(N) {
        val numbers = readLine().split(" ").map { it.toInt() }
        for (num in numbers) {
            pq.add(num)
            if (pq.size > N) pq.poll()
        }
    }

    println(pq.peek())
}
