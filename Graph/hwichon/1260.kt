import java.util.LinkedList
import java.util.Queue

fun main() = with(System.`in`.bufferedReader()) {
    val (N, M, V) = readLine().split(" ").map { it.toInt() }
    val graph = Array(N + 1) { mutableListOf<Int>() }
    repeat(M) {
        val (u, v) = readLine().split(" ").map { it.toInt() }.toIntArray()
        graph[u].add(v)
        graph[v].add(u)
    }
    graph.forEach { it.sort() }

    val visitedDfs = BooleanArray(N + 1)
    fun dfs(start: Int) {
        print("$start ")
        visitedDfs[start] = true
        graph[start].forEach {
            if (!visitedDfs[it]) {
                dfs(it)
            }
        }
    }

    fun bfs(start: Int) {
        val queue: Queue<Int> = LinkedList()
        val visited = BooleanArray(N + 1)
        queue.add(start)
        visited[start] = true

        while (queue.isNotEmpty()) {
            val node = queue.poll()
            print("$node ")
            graph[node!!].forEach {
                if (!visited[it]) {
                    visited[it] = true
                    queue.add(it)
                }
            }
        }
    }
    dfs(V)
    println()
    bfs(V)
}
