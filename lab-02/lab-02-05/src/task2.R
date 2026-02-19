# Пример map_dbl
iris_num <- iris[, 1:4]
mean_vec <- map_dbl(iris_num, mean)
print(mean_vec)

# Пример map_lgl
my_numbers <- list(a = 10, b = 5, c = 20, d = 3)
is_gt_6 <- map_lgl(my_numbers, ~ .x > 6)
print(is_gt_6)

# Пример map_chr
col_types <- map_chr(iris, class)
print(col_types)

# Пример map_dfr
df_list <- list(
  group_a = data.frame(id = 1:2, val = c(10, 20)),
  group_b = data.frame(id = 3:4, val = c(30, 40))
)
combined_df <- map_dfr(df_list, identity, .id = "source_group")
print(combined_df)