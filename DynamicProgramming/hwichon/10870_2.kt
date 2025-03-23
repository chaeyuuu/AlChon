fun main() = with(System.`in`.bufferedReader()) {
    val N = readLine().toInt()

    if (N==0 || N==1){
        println(N)
        return
    }

    var a = 0
    var b =1

    for (i in 2..N){
        val temp = a+b
        a = b
        b = temp
    }
    println(b)
}
