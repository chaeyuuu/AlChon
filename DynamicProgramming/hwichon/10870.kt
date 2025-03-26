fun main() = with(System.`in`.bufferedReader()) {
    val N = readLine().toInt()
    val dp = IntArray(N + 2) { 0 }

    dp[0] = 0
    dp[1] = 1

    if (N > 1) {
        for (i in 2..N) {
            dp[i] = dp[i - 1] + dp[i - 2]
        }
    }
    println(dp[N])
}
