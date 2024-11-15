//to change the given number into palindrome
bool isPalindrome(int x) {
    if (x < 0) {
        return false;  // Negative numbers are not palindromes
    }
    int y = x;
    int remainder;
    unsigned int reversedNumber = 0;
    while(x != 0)
    {
        remainder = x % 10;
        reversedNumber = reversedNumber * 10 + remainder;
        x /= 10;
    }

    return y == reversedNumber;

}
