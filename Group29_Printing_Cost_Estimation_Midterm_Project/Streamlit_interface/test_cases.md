# System Test Cases

| Test | Example | Result |
|---|---|---|
| Normal | 150 pages, 50 color, 25 copies | Positive estimate displayed |
| Missing | Required numeric input omitted | Interface prevents incomplete input |
| Boundary | 1 page, 0 color, 1 copy | Minimum inputs accepted; manual quotation warning displayed because the prediction is negative |
| Invalid | Color pages greater than pages | Error message displayed |
| Uncertain | 500 pages or 100 copies | Reliability warning displayed |
| Negative prediction | 40 pages, 10 color, 2 copies | Manual quotation warning displayed |