# Web Search

Tags: websearch

    | search_terms                                      |
    | MKS Instruments                                   | 
    | RF Power Generator                                |
    | PECVD plasma enhanced chemical vapour deposition  |

This is a demo specification for puppeting a Google Chrome instance which is used to search the web.

The following context or "setup" step is executed before every scenario:

* Visit "google.com"


## User visits google.com

Tags: visit google

In this scenario, the user visits google.com and sees: the google logo (img), a search box (input), and a search button (input).

* Look for "Google in Title"
* Look for "Google Search Field"
* Look for "Google Search Button"


## User searches using google.com

Tags: google search

In this scenario, the user navigates to google.com and performs a few searches.

* Enter <search_terms> into "Google Search Field"
* Click "Google Search Icon Button"
* "Google Result Stats" appears within "5" seconds
