fun main() = with(System.`in`.bufferedReader()) {
    val N = readLine().toInt()
    val Alist = readLine().split(" ").map { it.toInt() }.sorted()
    val Blist = readLine().split(" ").map { it.toInt() }.sortedDescending()

    var result = Alist.indices.sumOf { Alist[it] * Blist[it] }

    println(result)
}
