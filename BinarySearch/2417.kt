import java.io.BufferedReader
import java.io.InputStreamReader

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val n = readLine().toLong()

    var left = 0L
    var right = n
    var result = 0L

    while (left <= right) {
        val mid = (left + right) / 2
        if (mid.toDouble() * mid.toDouble() >= n) {
            result = mid
            right = mid - 1
        } else {
            left = mid+1
        }
    }
    println(result)
}
