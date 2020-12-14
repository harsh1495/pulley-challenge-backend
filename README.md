# Pulley Shakesearch Challenge

## API Endpoints

### GET ```"/search"```

- Fetches a list of dictionary of all the search results (shows the first 10 search results by default)
- Request query arguments: <q>, <start>, <size>
- Returns: A list of dictionaries of search results containing the name of the Shakespeare play and the raw content which matches the search query

#### Sample Response

```
{
    "data":
        [
            {
                "book": "THE MERCHANT OF VENICE",
                "raw_content": "PORTIA.\nFor the intent and purpose of the law\nHath full relation
                    to the penalty,\nWhich here appeareth due upon the bond.\n\nSHYLOCK.\n\u2019Tis very true. O wise and upright
                    judge,\nHow much more elder art thou than thy looks!\n\nPORTIA.\nTherefore lay bare your bosom.\n\nSHYLOCK.\nAy, his
                    breast\n..."
            },
            .
            .
            .
        ]
}
```