public class StrongVsWeakTyping {
    public static void main(String[] args) {
        String x = "10"; // x is a string
        int y = 5;       // y is an integer

        // This will cause an error if we try to add directly (incompatible types)
        // System.out.println(x + y); // Uncommenting works in Java because + means concatenation with string

        // To make it clear, we show explicit conversion
        System.out.println(x + String.valueOf(y)); // Output: 105
    }
}