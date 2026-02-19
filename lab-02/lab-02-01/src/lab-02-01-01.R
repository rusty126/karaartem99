calculate_payments <- function() {
  if (interactive()) {
    cat("Введите расходы на Продукты: ")
    cost1 <- as.numeric(readline())
    cat("Введите расходы на Коммунальные услуги: ")
    cost2 <- as.numeric(readline())
    cat("Введите расходы на Транспорт: ")
    cost3 <- as.numeric(readline())
  } else {
    cost1 <- 12500
    cost2 <- 6000
    cost3 <- 2000
  }
  
  if (is.na(cost1) || is.na(cost2) || is.na(cost3)) {
    cat("Ошибка: Введены некорректные данные.\n")
    return(NULL)
  }
  
  max_payment <- max(cost1, cost2, cost3)
  total_sum <- cost1 + cost2 + cost3
  
  payment_names <- c("Продукты", "Коммунальные услуги", "Транспорт")
  payment_values <- c(cost1, cost2, cost3)
  max_category <- payment_names[which.max(payment_values)]
  
  cat("Отчёт о расходах\n")
  cat(sprintf("Суммарные расходы за месяц: %.2f\n", total_sum))
  cat(sprintf("Максимальная статья расходов: %.2f (%s)\n", max_payment, max_category))
}

calculate_payments()