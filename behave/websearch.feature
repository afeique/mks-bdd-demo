Feature: Web search using Chrome
    
    @visit_google
    @websearch
    Scenario: User visits Google
        Given I visit "google.com"
        Then I see "Google in the Title"
        And I see "Google Search Field"
        And I see "Google Search Button"

    @google_search
    @websearch
    Scenario Outline: User searches using Google
        Given I visit "google.com"
        When I enter "<search terms>" into "Google Search Field"
        And I click "Google Search Button"
        Then "Google Result Stats" appears within "5" seconds

        Examples: Simple Searches
            | search terms                                      |
            | MKS Instruments                                   | 
            | RF Power Generator                                |
            | PECVD plasma enhanced chemical vapour deposition  |