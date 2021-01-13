Feature: knowledge checker for roman numerals
    
    @roman
    Scenario: user inputs 1 and "I", result is True
        Given user inputs the number and his guess
        """
        1,I
        """
        When we run the converter
        Then the result is True

    @roman
    Scenario: user inputs 2 and "III", result is False
        Given user inputs the number and his guess
        """
        2,III
        """
        When we run the converter
        Then the result is False

    @roman
    Scenario: user inputs 2 and 2, he gets an error
        Given user inputs the number and his guess with wrong type
        """
        2,2
        """
        When we run the converter
        Then the app raises an error

    @roman
    Scenario: user inputs 1972 and "MCMLXXII", result is True
        Given user inputs the number and his guess
        """
        1972,MCMLXXII
        """
        When we run the converter
        Then the result is True

    @roman 
    Scenario: user inputs 2137 and "MMCXXXVI", result is False
        Given user inputs the number and his guess
        """
        2137,MMCXXXVII
        """
        When we run the converter
        Then the result is True

    @roman 
    Scenario: user inputs mixes up the sequence of number, guess
        Given user inputs the number with wrong type and his guess with wrong type
        """
        V,5
        """
        When we run the converter
        Then the app raises an error

    @roman
    Scenario: user inputs 55 and "fifty-five", result is False
        Given user inputs the number and his guess
        """
        55,fifty-five
        """
        When we run the converter
        Then the result is False

    @roman
    Scenario: user inputs 200 and "zweihundert", result is False
        Given user inputs the number and his guess
        """
        200,zweihundert
        """
        When we run the converter
        Then the result is False