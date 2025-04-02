import java.util.LinkedList
import java.util.Queue

data class Pair(val x: Int, val y: Int)

fun main() = with(System.`in`.bufferedReader()) {
    val (N, M) = readLine().split(" ").map { it.toInt() }
    val map = Array(N) { readLine().map { it.digitToInt() }.toIntArray() }
    val visited = Array(N) { BooleanArray(M) }

    val moveX = arrayOf(-1, 0, 1, 0)
    val moveY = arrayOf(0, 1, 0, -1)

    fun bfs(startX: Int, startY: Int) {
        val queue: Queue<Pair> = LinkedList()
        queue.add(Pair(startX, startY))
        visited[startX][startY] = true

        while (queue.isNotEmpty()) {
            val (x, y) = queue.poll()!!
            if (x == N - 1 && y == M - 1) {
                println(map[x][y])
                return
            }
            for (i in 0 until 4) {
                val nx = x + moveX[i]
                val ny = y + moveY[i]

                if (nx in 0 until N && ny in 0 until M && !visited[nx][ny] && map[nx][ny] == 1) {
                    queue.add(Pair(nx, ny))
                    visited[nx][ny] = true
                    map[nx][ny] = map[x][y] + 1
                }
            }
        }
    }
    bfs(0,0)
}
