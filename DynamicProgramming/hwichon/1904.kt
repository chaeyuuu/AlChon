fun main() = with(System.`in`.bufferedReader()){
    val N = readLine().toInt()
    val dp = IntArray(N+1)
    if (N==1 || N==2){
        println(N)
        return@with
    }
    dp[1]=1
    dp[2]=2
    for (i in 3..N){
        dp[i] = (dp[i-1]+dp[i-2]) % 15746
    }
    println(dp[N])
}
