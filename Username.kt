// Read the number of test cases from the standard input
val t = readLine()!!.toInt()
// Loop through all the test cases
repeat(t) {
  // Read the ID from the standard input
  val s = readLine()!!
  // Initialize a variable to store the username
  var username = ""
  // Loop through the ID from the end to the start
  for (i in s.length - 1 downTo 0) {
    // Get the current character
    val c = s[i]
    // If the character is a digit, append it to the username
    if (c.isDigit()) {
      username = c + username
    } else {
      // Else, check if the username is not empty and contains at least one letter
      if (username.isNotEmpty() && username.any { it.isLetter() }) {
        // If so, append the character to the username and break the loop
        username = c + username
        break
      } else {
        // Else, clear the username and append the character
        username = c.toString()
      }
    }
  }
  // Print the username to the standard output
  println(username)
}
