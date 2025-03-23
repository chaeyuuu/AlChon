import java.io.BufferedReader
import java.io.InputStreamReader

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val N = readLine().toInt()
    val numbers = readLine().split(" ").map { it.toInt() }.toIntArray()
    val dp =  IntArray(N) { numbers[it] }

    for (i in 1..N - 1) {
        for (j in 0..i - 1) {
            if (numbers[j] < numbers[i]) {
                dp[i] = maxOf(dp[i], dp[j] + numbers[i])
            }
        }
    }
    println(dp.max())
}
