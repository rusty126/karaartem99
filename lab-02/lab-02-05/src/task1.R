library(repurrrsive)
library(purrr)

films <- map(sw_films, ~ .x$title)
named_films <- set_names(sw_films, films)
print(named_films)