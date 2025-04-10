fun main() = with(System.`in`.bufferedReader()) {
    val (N, K) = readLine().split(" ").map { it.toInt() }
    val coinList = List(N) { readLine().toInt() }.reversed()

    var cost = K
    var count = 0

    for (coin in coinList) {
        if (cost >= coin) {
            count += cost / coin
            cost %= coin
        }
    }

    println(count)
}
