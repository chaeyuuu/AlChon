import java.util.LinkedList
import java.util.Queue

data class Point(val x: Int, val y: Int)

fun main() = with(System.`in`.bufferedReader()) {
    while (true) {
        val (w, h) = readLine().split(" ").map { it.toInt() }
        if (w == 0 && h == 0) break

        val map = Array(h) { readLine().split(" ").map { it.toInt() }.toIntArray() }
        val visited = Array(h) { BooleanArray(w) }

        val dx = arrayOf(-1, -1, -1, 0, 1, 1, 1, 0)
        val dy = arrayOf(1, 0, -1, -1, -1, 0, 1, 1)

        var landCount = 0

        fun bfs(startX: Int, startY: Int) {
            val queue: Queue<Point> = LinkedList()
            queue.add(Point(startX, startY))
            visited[startX][startY] = true

            while (queue.isNotEmpty()) {
                val (x, y) = queue.poll()!!

                for (i in 0 until 8) {
                    val nx = x + dx[i]
                    val ny = y + dy[i]
                    if (nx in 0 until h && ny in 0 until w && !visited[nx][ny] && map[nx][ny] == 1) {
                        visited[nx][ny] = true
                        queue.add(Point(nx, ny))
                    }
                }
            }
        }

        for (i in 0 until h) {
            for (j in 0 until w) {
                if (map[i][j] == 1 && !visited[i][j]) {
                    bfs(i, j)
                    landCount++
                }
            }
        }
        println(landCount)
    }
}
