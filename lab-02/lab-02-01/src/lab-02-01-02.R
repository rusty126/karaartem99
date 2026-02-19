foo <- function(n) {
  if (n > 0) {
    return(n * foo(n - 1))
  } else {
    return(1)
  }
}

result <- foo(7)
cat("Результат вызова foo(7):", result, "\n")  # Выведет 5040