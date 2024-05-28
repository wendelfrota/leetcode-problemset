package easy.kotlin.`3110-score-of-a-string`

import kotlin.math.abs

class Solution {
    fun scoreOfString(s: String): Int {
        var sum = 0;

        for (i in 1 until s.length)
            sum += abs(s[i] - s[i-1])

        return sum;
    }
}

//fun main(){
//    println(Solution().scoreOfString("hello"))
//}