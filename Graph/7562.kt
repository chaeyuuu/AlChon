import java.util.LinkedList
import java.util.Queue

data class Pair(val x: Int, val y: Int, val count: Int)

fun main() = with(System.`in`.bufferedReader()) {
    val N = readLine().toInt()
    repeat(N) {
        val l = readLine().toInt()
        val (startX, startY) = readLine().split(" ").map { it.toInt() }
        val (endX, endY) = readLine().split(" ").map { it.toInt() }

        val visited = Array(l) { BooleanArray(l) }

        val dx = arrayOf(-1, -2, -2, -1, 1, 2, 2, 1)
        val dy = arrayOf(2, 1, -1, -2, -2, -1, 1, 2)

        fun bfs(startX: Int, startY: Int): Int {
            if (startX == endX && startY == endY) return 0

            val queue: Queue<Pair> = LinkedList()
            queue.add(Pair(startX, startY, 0))
            visited[startX][startY] = true

            while (queue.isNotEmpty()) {
                val (x, y, endCount) = queue.poll()!!
                if (x == endX && y == endY) {
                    return endCount
                }
                for (i in 0 until 8) {
                    val nx = x + dx[i]
                    val ny = y + dy[i]

                    if (nx in 0 until l && ny in 0 until l && !visited[nx][ny]) {
                        visited[nx][ny] = true
                        queue.add(Pair(nx, ny, endCount + 1))
                    }
                }
            }
            return -1
        }
        println(bfs(startX, startY))
    }
}
