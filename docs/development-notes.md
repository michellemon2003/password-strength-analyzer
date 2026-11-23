# Development notes

- `analyze(password)` returns a rating, count and feedback. It has no input or output operations, so sample strings can exercise the rules directly.
- Lowercase, uppercase, decimal digits and non-alphanumeric non-whitespace characters each contribute one group. This count is displayed for education. Rating uses length and predictability.
- `casefold()` makes common-word and sequence checks case-insensitive. Four-character substrings detect ascending and descending patterns. Three consecutive identical characters trigger the repeat rule.
- The classification checks under eight characters and exact common entries first. Samples under fifteen characters or with simple patterns need improvement. Longer samples that clear those rules receive the highest label.
- `main()` uses `getpass()` so inputs stay off the screen. A warning becomes an error when the terminal cannot hide input.
