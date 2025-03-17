import java.io.BufferedReader
import java.io.InputStreamReader

var maxValue = Int.MIN_VALUE
var minValue = Int.MAX_VALUE

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val N = readLine().toInt()
    val numbers = readLine().split(" ").map { it.toInt() }.toIntArray()
    val (add, sub, mul, div) = readLine().split(" ").map { it.toInt() }
    dfs(1, numbers[0], add, sub, mul, div, numbers)
    println(maxValue)
    println(minValue)
}

fun dfs(index: Int, result: Int, add: Int, sub: Int, mul: Int, div: Int, numbers: IntArray) {
    if (index == numbers.size) {
        maxValue = maxOf(maxValue, result)
        minValue = minOf(minValue, result)
        return
    }
    if (add > 0) dfs(index + 1, result + numbers[index], add - 1, sub, mul, div, numbers)
    if (sub > 0) dfs(index + 1, result - numbers[index], add, sub - 1, mul, div, numbers)
    if (mul > 0) dfs(index + 1, result * numbers[index], add, sub, mul - 1, div, numbers)
    if (div > 0) {
        val divResult = if (result < 0) -(-result / numbers[index]) else result / numbers[index]
        dfs(index + 1, divResult, add, sub, mul, div - 1, numbers)
    }
}
