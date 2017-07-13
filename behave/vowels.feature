Feature: Vowels
    
    @single_word
    Scenario: Vowel counts in a single word
        Given the word "gauge"
        Then there are 3 vowels

    @multiple_words
    Scenario Outline: Vowel counts in multiple words
        Given the word "<Word>"
        Then there are <Vowel Count> vowels

        Examples: Words with Vowels
            |Word      |Vowel Count|
            |Heading   |3          |
            |Gauge     |3          |
            |Mingle    |2          |
            |Snap      |1          |
            |GoCD      |1          |
            |Rhythm    |0          |
