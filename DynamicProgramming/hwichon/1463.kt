import kotlin.math.min

fun main() = with(System.`in`.bufferedReader()) {
    val N = readLine().toInt()
    val dp = IntArray(N + 1) { 0 }
    for (i in 2..N) {
        dp[i] = dp[i - 1] + 1
        if (i % 2 == 0) {
            dp[i] = min(dp[i / 2] + 1, dp[i])
        }
        if (i % 3 == 0) {
            dp[i] = min(dp[i / 3] + 1, dp[i])
        }
    }
    println(dp[N])
}
