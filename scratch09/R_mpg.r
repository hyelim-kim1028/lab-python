library(ggplot2)
library(dplyr)

mpg <- ggplot2::mpg


linear_model <- lm(formula = cty ~ displ, data = mpg)
print(linear_model)

mpg %>% 
  ggplot(mapping = aes(displ, cty)) + 
  geom_point()+
  stat_smooth(method = lm, level = 0.95)

print(head(mpg))
write.csv(x = mpg,
          row.names = F,
          file = 'C:/dev/lab-python/scratch08/mpg.csv' )
  # row names = F, row names seem unnecessary -> 쓰지 않겠다 