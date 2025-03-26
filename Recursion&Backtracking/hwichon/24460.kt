import java.io.BufferedReader
import java.io.InputStreamReader

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val N = readLine().toInt()
    val array = Array(N) { readLine().split(" ").map { it.toInt() }.toIntArray() }
    println(recall(array, 0, 0, N))
}

fun recall(array: Array<IntArray>, x: Int, y: Int, size: Int): Int {
    if (size == 1) return array[x][y]
    if (size == 2) {
        val list = listOf(
            array[x][y], array[x + 1][y],
            array[x][y + 1], array[x + 1][y + 1]
        )
        return list.sorted()[1]
    }
    val half = size / 2
    val s1 = recall(array, x, y, half)
    val s2 = recall(array, x + half, y, half)
    val s3 = recall(array, x, y + half, half)
    val s4 = recall(array, x + half, y + half, half)

    return listOf(s1, s2, s3, s4).sorted()[1]
}
