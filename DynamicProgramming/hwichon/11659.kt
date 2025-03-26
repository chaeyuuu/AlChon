fun main() = with(System.`in`.bufferedReader()) {
    val (N, M) = readLine().split(" ").map { it.toInt() }
    val array = readLine().split(" ").map { it.toInt() }

    val prefixSum = IntArray(N+1){0}

    for (i in 1..N){
        prefixSum[i] = prefixSum[i-1]+array[i-1]
    }

    val result = StringBuilder()
    for (k in 1..M){
        val (i, j) = readLine().split(" ").map { it.toInt() }
        result.append("${prefixSum[j] - prefixSum[i - 1]}\n")
    }
    println(result)
}
